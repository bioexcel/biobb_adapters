#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Wrapper of the GROMACS make_ndx module.

doc: |-
  The GROMACS make_ndx module, generates an index file using the atoms of the selection.

baseCommand: make_ndx

hints:
  DockerRequirement:
    dockerPull: https://quay.io/biocontainers/biobb_md:3.5.1--py_0

inputs:
  input_structure_path:
    label: Path to the input GRO/PDB/TPR file
    doc: |-
      Path to the input GRO/PDB/TPR file
      Type: string
      File type: input
      Accepted formats: gro, pdb, tpr
      Example file: https://github.com/bioexcel/biobb_md/raw/master/biobb_md/test/data/gromacs/make_ndx.tpr
    type: File
    format:
    - edam:format_2033
    - edam:format_1476
    - edam:format_2333
    inputBinding:
      position: 1
      prefix: --input_structure_path

  output_ndx_path:
    label: Path to the output index NDX file
    doc: |-
      Path to the output index NDX file
      Type: string
      File type: output
      Accepted formats: ndx
      Example file: https://github.com/bioexcel/biobb_md/raw/master/biobb_md/test/reference/gromacs/ref_make_ndx.ndx
    type: string
    format:
    - edam:format_2330
    inputBinding:
      position: 2
      prefix: --output_ndx_path
    default: system.ndx

  input_ndx_path:
    label: Path to the input index NDX file
    doc: |-
      Path to the input index NDX file
      Type: string
      File type: input
      Accepted formats: ndx
      Example file: null
    type: File?
    format:
    - edam:format_2330
    inputBinding:
      prefix: --input_ndx_path

  config:
    label: Advanced configuration options for biobb_md MakeNdx
    doc: |-
      Advanced configuration options for biobb_md MakeNdx. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_md MakeNdx documentation: https://biobb-md.readthedocs.io/en/latest/gromacs.html#module-gromacs.make_ndx
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_ndx_path:
    label: Path to the output index NDX file
    doc: |-
      Path to the output index NDX file
    type: File
    outputBinding:
      glob: $(inputs.output_ndx_path)
    format: edam:format_2330

$namespaces:
  edam: http://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl