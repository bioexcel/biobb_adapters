""" Utility to generate Galaxy tool definitions (XML) from biobb json_schemas """

import sys
import json
import argparse
import os
import re
from jinja2 import Environment, FileSystemLoader, select_autoescape
from jinja2.exceptions import TemplateSyntaxError

TEMPL = "biobb_galaxy_template.xml"
CONTAINERS = "biobb_galaxy_containers.json"

def main():
    
    parser = argparse.ArgumentParser(description='Build galaxy adapters.')
    parser.add_argument("--template", default=TEMPL, help="Template for XML galaxy adapter")
    parser.add_argument("--containers", default=CONTAINERS, help="Biobb Containers and versions (json)")
    parser.add_argument("--id", help="tool id for Galaxy")
    parser.add_argument("--display_name", help="Tool name to display in Galaxy")
    parser.add_argument(dest="schema", help="Json schema from guilding block")
    
    args = parser.parse_args()
    
    if args.template == TEMPL:
        template_dir = os.path.dirname(__file__)
    else:
        template_dir = os.path.dirname(args.template)
    
    try:
        with open(args.schema, "r") as schema_file:
            schema_data = json.load(schema_file)
    except IOError as err:
        sys.exit(err)
    
    if args.containers == CONTAINERS:
        args.containers = os.path.dirname(__file__) + "/" + args.containers
        
    try:
        with open (args.containers, "r") as containers_lst:
            cont_lst = json.load(containers_lst)
    except IOError as err:
        sys.exit(err)
    
    data = {}
    
    if args.display_name:
        data['name'] = args.display_name
    else:
        data['name'] = os.path.basename(schema_data['$id'])
    
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
    
    data['files'] = {'input':{}, 'output':{}}
    
    for f in schema_data['properties']:
        if f == 'properties':
            continue
        tool_data = {'name': f, 'file_types':[]}
        for v in schema_data['properties'][f]['enum']:
            m = re.search(r"\w+", v)
            tool_data['file_types'].append(m.group(0))
        
        tool_data['label'] = schema_data['properties'][f]['filetype'] + ' ' +  ','.join(tool_data['file_types']).upper()
        data['files'][schema_data['properties'][f]['filetype']][f] = tool_data
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['xml'])
    )
    templ = env.get_template(args.template)
    with open(data['name'] + ".xml", "w") as xml_file:
        xml_file.write(templ.render(data))
        
if __name__ == '__main__':
    main()
