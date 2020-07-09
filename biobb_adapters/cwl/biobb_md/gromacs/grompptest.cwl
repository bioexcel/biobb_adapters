#!/usr/bin/env cwl-runner
cwlVersion: v1.1
class: CommandLineTool

baseCommand: echo

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_md:0.1.5--py_0

requirements:
  InlineJavascriptRequirement: {}
  InitialWorkDirRequirement:
    listing:
      - entryname: "grompp-config.json"
        entry: $(inputs.config_rec || {}) # empty JSON by default

inputs:
  config_rec:
    doc: ""
    type:
      - "null"
      - $import: grompp-config.cwl # GromppConfig record
    inputBinding:
      #prefix: --config
      # "grompp-config.json" from InitialWorkDirRequirement
      valueFrom: "grompp-config.json"
      # This does not actually work because the inner "default" fields 
      # are not allowed, but cwltool fills in lots of nulls for the optionals:
#{
#  "container_image":null,
#  "container_path":null,
#  "container_shell_path":null,
#  "container_user_id":null,
#  "container_volume_path":null,
#  "container_working_dir":null,
#  "gmx_path":null,
#  "input_mdp_path":"hello",
#  "maxwarn":100,
#  "mdp":{
#    "define":null,
#    "include":null,
#    "integrator":"steep"
#  },
#  "output_mdp_path":"soup",
#  "output_top_path":null,
#  "remove_tmp":null,
#  "restart":true,
#  "type":"nvt"
#}
  config:
    type: 
      - "null"
      - string
      - File
    inputBinding:
      prefix: --config

outputs:
  concatination:
    type: stdout

$namespaces:
  edam: http://edamontology.org/
$schemas:
  - https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
