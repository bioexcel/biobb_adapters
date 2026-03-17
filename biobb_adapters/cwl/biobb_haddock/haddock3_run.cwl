#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Wrapper class for the HADDOCK3 Run module.

doc: |-
  The HADDOCK3 run module launches the HADDOCK3 execution for docking.

baseCommand: haddock3_run

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_haddock:5.2.1--pyh106432d_0

inputs:
  input_haddock_wf_data:
    label: Input folder containing all the files defined in the config
    doc: |-
      Input folder containing all the files defined in the config
      Type: dir
      File type: input
      Accepted formats: directory, zip
      Example file: https://github.com/bioexcel/biobb_haddock/tree/master/biobb_haddock/test/data/haddock/haddock_wf_data_run.zip
    type: File
    format:
    - edam:format_1915
    - edam:format_3987
    inputBinding:
      position: 1
      prefix: --input_haddock_wf_data

  output_haddock_wf_data:
    label: Path to the output zipball containing all the current Haddock workflow
      data
    doc: |-
      Path to the output zipball containing all the current Haddock workflow data
      Type: dir
      File type: output
      Accepted formats: directory, zip
      Example file: null
    type: string
    format:
    - edam:format_1915
    - edam:format_3987
    inputBinding:
      position: 2
      prefix: --output_haddock_wf_data
    default: system.directory

  haddock_config_path:
    label: Haddock configuration CFG file path
    doc: |-
      Haddock configuration CFG file path
      Type: string
      File type: input
      Accepted formats: cfg
      Example file: https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock/run.cfg
    type: File?
    format:
    - edam:format_1476
    inputBinding:
      prefix: --haddock_config_path

  config:
    label: Advanced configuration options for biobb_haddock Haddock3Run
    doc: |-
      Advanced configuration options for biobb_haddock Haddock3Run. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_haddock Haddock3Run documentation: https://biobb-haddock.readthedocs.io/en/latest/haddock.html#module-haddock.haddock3_run
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
    format: edam:format_1915

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
