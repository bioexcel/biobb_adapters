#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Wrapper class for the HADDOCK3 extend module.

doc: |-
  The HADDOCK3 extend. module continues the HADDOCK3 execution for docking of an already started run.

baseCommand: haddock3_extend

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_haddock:5.2.1--pyh106432d_0

inputs:
  input_haddock_wf_data:
    label: Path to the input zipball containing all the current Haddock workflow data
    doc: |-
      Path to the input zipball containing all the current Haddock workflow data
      Type: dir
      File type: input
      Accepted formats: zip
      Example file: https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/data/haddock/haddock_wf_data_caprieval.zip
    type: File
    format:
    - edam:format_3987
    inputBinding:
      position: 1
      prefix: --input_haddock_wf_data

  haddock_config_path:
    label: Haddock configuration CFG file path
    doc: |-
      Haddock configuration CFG file path
      Type: string
      File type: input
      Accepted formats: cfg
      Example file: https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg
    type: File
    format:
    - edam:format_1476
    inputBinding:
      position: 2
      prefix: --haddock_config_path

  output_haddock_wf_data:
    label: Path to the output zipball containing all the current Haddock workflow
      data
    doc: |-
      Path to the output zipball containing all the current Haddock workflow data
      Type: dir
      File type: output
      Accepted formats: zip
      Example file: https://github.com/bioexcel/biobb_haddock/raw/master/biobb_haddock/test/reference/haddock/ref_haddock3_extend.zip
    type: string
    format:
    - edam:format_3987
    inputBinding:
      position: 3
      prefix: --output_haddock_wf_data
    default: system.zip

  config:
    label: Advanced configuration options for biobb_haddock Haddock3Extend
    doc: |-
      Advanced configuration options for biobb_haddock Haddock3Extend. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_haddock Haddock3Extend documentation: https://biobb-haddock.readthedocs.io/en/latest/haddock.html#module-haddock.haddock3_extend
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_haddock_wf_data:
    label: Path to the output zipball containing all the current Haddock workflow
      data
    doc: |-
      Path to the output zipball containing all the current Haddock workflow data
    type: File
    outputBinding:
      glob: $(inputs.output_haddock_wf_data)
    format: edam:format_3987

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
