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
