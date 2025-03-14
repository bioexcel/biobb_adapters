#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Class to search closest residues from a 3D structure using Biopython.

doc: |-
  Return all residues that have at least one atom within radius of center from a list of given residues.

baseCommand: closest_residues

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_structure_utils:4.2.0--pyhdfd78af_0

inputs:
  input_structure_path:
    label: Input structure file path
    doc: |-
      Input structure file path
      Type: string
      File type: input
      Accepted formats: pdb, pdbqt
      Example file: https://github.com/bioexcel/biobb_structure_utils/raw/master/biobb_structure_utils/test/data/utils/2vgb.pdb
    type: File
    format:
    - edam:format_1476
    - edam:format_1476
    inputBinding:
      position: 1
      prefix: --input_structure_path

  output_residues_path:
    label: Output molcules file path
    doc: |-
      Output molcules file path
      Type: string
      File type: output
      Accepted formats: pdb, pdbqt
      Example file: https://github.com/bioexcel/biobb_structure_utils/raw/master/biobb_structure_utils/test/reference/utils/ref_closest_residues.pdb
    type: string
    format:
    - edam:format_1476
    - edam:format_1476
    inputBinding:
      position: 2
      prefix: --output_residues_path
    default: system.pdb

  config:
    label: Advanced configuration options for biobb_structure_utils ClosestResidues
    doc: |-
      Advanced configuration options for biobb_structure_utils ClosestResidues. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_structure_utils ClosestResidues documentation: https://biobb-structure-utils.readthedocs.io/en/latest/utils.html#module-utils.closest_residues
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_residues_path:
    label: Output molcules file path
    doc: |-
      Output molcules file path
    type: File
    outputBinding:
      glob: $(inputs.output_residues_path)
    format: edam:format_1476

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
