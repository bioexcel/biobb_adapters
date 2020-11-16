""" Utility to generate Galaxy automated tool definitions (XML) from biobb json_schemas """

import sys
import json
import argparse
import os
import re
from jinja2 import Environment, FileSystemLoader, select_autoescape
from jinja2.exceptions import TemplateSyntaxError

TEMPL = "biobb_galaxy_template.xml"
CONTAINERS = "biobb_galaxy_containers.json"
XML_DIR = "./xml_files"

def tool_name(orig):
    data = re.split('_', orig)
    return ''.join([a.capitalize() for a in data])

def main():
    """ Usage: json2galaxy.py [-h] [--template TEMPLATE] [--containers CONTAINERS]
                      [--id ID] [--display_name DISPLAY_NAME] [--create_dir]
                      [--extended]
                      schema
        positional arguments:                                                                    
            * schema (**str**)      Path to Json schema from building block                                  
        optional arguments:
            * --template (**str**)  Path to Template for XML galaxy adapter (xml) (default: biobb_galaxy_template.xml)
            * --containers (**str**)Biobb Containers and versions (json) (default: biobb_galaxy_containers.json)
            * --id (**str**)        tool id for Galaxy (default biobb_tool name)
            * --display_name (**str**) Tool name to display in Galaxy (default tool_name)
            * --create_dir (**bool**)  Create biobb group adapter directory (default False)
            * --extended (**bool**)    Create detailed from for properties (default False)
    """
    parser = argparse.ArgumentParser(description='Build galaxy adapters.')
    parser.add_argument("--template", default=TEMPL, help="Template for XML galaxy adapter")
    parser.add_argument("--containers", default=CONTAINERS, help="Biobb Containers and versions (json)")
    parser.add_argument("--id", help="tool id for Galaxy")
    parser.add_argument("--display_name", help="Tool name to display in Galaxy")
    parser.add_argument("--create_dir", action="store_true", help="Create biobb directory")
    parser.add_argument("--extended", action="store_true", help="Create detailed properties form")
    parser.add_argument(dest="schema", help="Json schema from building block")
    
    args = parser.parse_args()
    
    # Extracting data directory 
    if args.template == TEMPL:
        template_dir = os.path.dirname(__file__)
    else:
        template_dir = os.path.dirname(args.template)
    
    if not template_dir:
        template_dir='.'
    
    # Parsing containers data    
    
    if args.containers == CONTAINERS:
        args.containers = template_dir + "/" + args.containers
        
    try:
        with open (args.containers, "r") as containers_lst:
            cont_lst = json.load(containers_lst)
    except IOError as err:
        sys.exit(err)
    
    # Parsing json schema
    
    try:
        with open(args.schema, "r") as schema_file:
            schema_data = json.load(schema_file)
    except IOError as err:
        sys.exit(err)
    
    if '$id' not in schema_data:
        sys.exit(args.schema + " not parseable")
    
    #Getting data components from schema
    
    data = {'files':{'input':{}, 'output':{}}, 'props':{}}
    
    # Extracting tool name and group from schema $id to generate defaults
    if args.display_name:
        data['name'] = args.display_name
    else:
        data['name'] = os.path.basename(schema_data['$id'])
        
    data['display_name'] = tool_name(data['name'])

    m = re.search(r'(biobb_[^/]*)', schema_data['$id'])
    
    data['biobb_group'] = m.group(0)
    
    if args.id:
        data['tool_id'] = args.id
    else:
        data['tool_id'] = data['biobb_group'] + "_" + data['name']
    
    data['container_id'] = "{}:{}--py_0".format(
        cont_lst[data['biobb_group']]['docker_image'],
        cont_lst[data['biobb_group']]['version']
    )
    
    if 'version' in schema_data:
        data['version'] = schema_data['version']
    else:
        data['version'] = cont_lst[data['biobb_group']]['version']
        
    data['description'] = schema_data['title']
    
    for f in schema_data['properties']:
        if f != 'properties':
            # Parsing input and output files
            tool_data = {
                'name': f, 
                'file_types':[],
                'description': schema_data['properties'][f]['description'],
                'optional': f not in schema_data['required']
                }
            
            if enum in schema_data['properties'][f]:
                for v in schema_data['properties'][f]['enum']:
                    m = re.search(r"\w+", v)
                    tool_data['file_types'].append(m.group(0))
        
            tool_data['format'] = ','.join(tool_data['file_types'])
            
            if len(tool_data['file_types']) > 1:
                tool_data['help_format'] = '[format]'
            else:
                tool_data['help_format'] = tool_data['format']
            
            tool_data['label'] = schema_data['properties'][f]['filetype'] + ' ' +  tool_data['format'].upper()
            
            data['files'][schema_data['properties'][f]['filetype']][f] = tool_data
        
        elif args.extended:
            # Parsing properties
            # TODO include more structured information in json schema to avoid re

            props_str=[]
            for k,v in schema_data['properties'][f]['properties'].items():
                if re.match('container', k) or\
                    ('description' in v and re.search('wf property', v['description'])) or\
                    ('wf_prop' in v and v['wf_prop']):
                    continue
                if 'description' in v:
                    m = re.search('(.*) Valid values: (.*)', v['description'])
                    if m:
                        v['values'] = re.split(', *', m.group(2).replace('.',''))
                        v['description'] = m.group(1)
                        v['type'] = 'select'
                if 'enum' in v:
                    v['values'] = v['enum']
                    v['type'] = 'select'
                data['props'][k] = v
                
                # Generating "galaxyfied" Json string for config parameter
                props_str.append("__dq__" +  k + "__dq__:__dq__${config." + k + "}__dq__")
            
            data['config4str'] = "__oc__" + ",".join(props_str) + "__cc__"

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['xml'])
    )
    templ = env.get_template(args.template)
    
    if args.create_dir:
        if not os.path.isdir(XML_DIR + "/" + data['biobb_group']):
            os.mkdir(XML_DIR + "/" + data['biobb_group'])

    with open(XML_DIR + "/" + data['biobb_group'] + "/biobb_" + data['name'] + ".xml", "w") as xml_file:
        xml_file.write(templ.render(data))
        
if __name__ == '__main__':
    main()
