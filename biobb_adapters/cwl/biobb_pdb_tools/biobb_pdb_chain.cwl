#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Modifies the chain identifier column of a PDB file.

doc: |-
  This tool modifies the chain identifier column of a PDB file. It can be used to change the chain identifier of a PDB file or to remove the chain identifier from a PDB file.

baseCommand: biobb_pdb_chain

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_pdb_tools:5.2.1--pyhdfd78af_0

inputs:
  input_file_path:
    label: Input PDB file
    doc: |-
      Input PDB file
      Type: string
      File type: input
      Accepted formats: pdb
      Example file: https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/1AKI.pdb
    type: File
    format:
    - edam:format_1476
    inputBinding:
      position: 1
      prefix: --input_file_path

  output_file_path:
    label: PDB file with selected modified chain
    doc: |-
      PDB file with selected modified chain
      Type: string
      File type: output
      Accepted formats: pdb
      Example file: https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_chain.pdb
    type: string
    format:
    - edam:format_1476
    inputBinding:
      position: 2
      prefix: --output_file_path
    default: system.pdb

  config:
    label: Advanced configuration options for biobb_pdb_tools Pdbchain
    doc: |-
      Advanced configuration options for biobb_pdb_tools Pdbchain. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_pdb_tools Pdbchain documentation: https://biobb-pdb-tools.readthedocs.io/en/latest/pdb_tools.html#module-pdb_tools.biobb_pdb_chain
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_file_path:
    label: PDB file with selected modified chain
    doc: |-
      PDB file with selected modified chain
    type: File
    outputBinding:
      glob: $(inputs.output_file_path)
    format: edam:format_1476

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
