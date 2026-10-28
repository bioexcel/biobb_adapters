#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Wrapper class for the ANARCII antibody numbering tool.

doc: |-
  ANARCII numbers antibody, TCR, and other immune receptor sequences. Given an input PDB structure it renumbers it (IMGT scheme by default) and writes the renumbered PDB structure.

baseCommand: anarcii

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_haddock:5.3.1--pyh106432d_0

inputs:
  input_pdb_path:
    label: Path to the input PDB structure file
    doc: |-
      Path to the input PDB structure file
      Type: string
      File type: input
      Accepted formats: pdb
      Example file: https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/haddock_restraints/4G6K_clean.pdb
    type: File
    format:
    - edam:format_1476
    inputBinding:
      position: 1
      prefix: --input_pdb_path

  output_pdb_path:
    label: Path to the output renumbered PDB structure file
    doc: |-
      Path to the output renumbered PDB structure file
      Type: string
      File type: output
      Accepted formats: pdb
      Example file: https://raw.githubusercontent.com/bioexcel/biobb_haddock/master/biobb_haddock/test/data/utils/4G6K_anarcii_imgt.pdb
    type: string
    format:
    - edam:format_1476
    inputBinding:
      position: 2
      prefix: --output_pdb_path
    default: system.pdb

  config:
    label: Advanced configuration options for biobb_haddock Anarcii
    doc: |-
      Advanced configuration options for biobb_haddock Anarcii. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_haddock Anarcii documentation: https://biobb-haddock.readthedocs.io/en/latest/utils.html#module-utils.anarcii
    type: File?
    inputBinding:
      prefix: --config

outputs:
  output_pdb_path:
    label: Path to the output renumbered PDB structure file
    doc: |-
      Path to the output renumbered PDB structure file
    type: File
    outputBinding:
      glob: $(inputs.output_pdb_path)
    format: edam:format_1476

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
