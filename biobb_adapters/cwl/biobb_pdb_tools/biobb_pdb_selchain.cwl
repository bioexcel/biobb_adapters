#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Extracts one or more chains from a PDB file.

doc: |-
  This tool extracts a specific chain or list of chains from a PDB file, discarding all others.

baseCommand: biobb_pdb_selchain

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
      Example file: https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/data/pdb_tools/input_pdb_selchain.pdb
    type: File
    format:
    - edam:format_1476
    inputBinding:
      position: 1
      prefix: --input_file_path

  output_file_path:
    label: PDB file with selected chains
    doc: |-
      PDB file with selected chains
      Type: string
      File type: output
      Accepted formats: pdb
      Example file: https://raw.githubusercontent.com/bioexcel/biobb_pdb_tools/master/biobb_pdb_tools/test/reference/pdb_tools/ref_pdb_selchain.pdb
    type: string
    format:
    - edam:format_1476
    inputBinding:
      position: 2
      prefix: --output_file_path
    default: system.pdb

  config:
    label: Advanced configuration options for biobb_pdb_tools Pdbselchain
    doc: |-
      Advanced configuration options for biobb_pdb_tools Pdbselchain. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_pdb_tools Pdbselchain documentation: https://biobb-pdb-tools.readthedocs.io/en/latest/pdb_tools.html#module-pdb_tools.biobb_pdb_selchain
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_file_path:
    label: PDB file with selected chains
    doc: |-
      PDB file with selected chains
    type: File
    outputBinding:
      glob: $(inputs.output_file_path)
    format: edam:format_1476

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
