#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Wrapper of the GROMACS convert-tpr module.

doc: |-
  The GROMACS convert-tpr module can edit run input files (.tpr): modify the run length (extend/until/nsteps) or trim the tpr file to a subset of atoms defined in an index file (input_ndx_path). Note that GROMACS does not allow both operations in a single call, so when an index file is provided the extend/until/nsteps properties are ignored.

baseCommand: convert_tpr

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_gromacs:5.3.2--pyhdfd78af_0

inputs:
  input_tpr_path:
    label: Path to the input portable binary run file TPR
    doc: |-
      Path to the input portable binary run file TPR
      Type: string
      File type: input
      Accepted formats: tpr
      Example file: https://github.com/bioexcel/biobb_gromacs/raw/master/biobb_gromacs/test/reference/gromacs/ref_grompp.tpr
    type: File
    format:
    - edam:format_2333
    inputBinding:
      position: 1
      prefix: --input_tpr_path

  output_tpr_path:
    label: Path to the output portable binary run file TPR
    doc: |-
      Path to the output portable binary run file TPR
      Type: string
      File type: output
      Accepted formats: tpr
      Example file: https://github.com/bioexcel/biobb_gromacs/raw/master/biobb_gromacs/test/reference/gromacs/ref_grompp.tpr
    type: string
    format:
    - edam:format_2333
    inputBinding:
      position: 2
      prefix: --output_tpr_path
    default: system.tpr

  input_ndx_path:
    label: Path to the input index NDX file, used to trim the tpr file to a subset
      of atoms
    doc: |-
      Path to the input index NDX file, used to trim the tpr file to a subset of atoms
      Type: string
      File type: input
      Accepted formats: ndx
      Example file: null
    type: File?
    format:
    - edam:format_2033
    inputBinding:
      prefix: --input_ndx_path

  config:
    label: Advanced configuration options for biobb_gromacs ConvertTpr
    doc: |-
      Advanced configuration options for biobb_gromacs ConvertTpr. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_gromacs ConvertTpr documentation: https://biobb-gromacs.readthedocs.io/en/latest/gromacs.html#module-gromacs.convert_tpr
    type: File?
    inputBinding:
      prefix: --config

outputs:
  output_tpr_path:
    label: Path to the output portable binary run file TPR
    doc: |-
      Path to the output portable binary run file TPR
    type: File
    outputBinding:
      glob: $(inputs.output_tpr_path)
    format: edam:format_2333

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
