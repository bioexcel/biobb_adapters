#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: This class is a wrapper for downloading a PDB structure from the Protein Data
  Bank.

doc: |-
  Wrapper for the Protein Data Bank in Europe, the Protein Data Bank and the MMB PDB mirror for downloading a single PDB structure.

baseCommand: pdb

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_io:4.2.0--pyhdfd78af_0

inputs:
  output_pdb_path:
    label: Path to the output PDB file
    doc: |-
      Path to the output PDB file
      Type: string
      File type: output
      Accepted formats: pdb
      Example file: https://github.com/bioexcel/biobb_io/raw/master/biobb_io/test/reference/api/output_pdb.pdb
    type: string
    format:
    - edam:format_1476
    inputBinding:
      position: 1
      prefix: --output_pdb_path
    default: system.pdb

  config:
    label: Advanced configuration options for biobb_io Pdb
    doc: |-
      Advanced configuration options for biobb_io Pdb. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_io Pdb documentation: https://biobb-io.readthedocs.io/en/latest/api.html#module-api.pdb
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_pdb_path:
    label: Path to the output PDB file
    doc: |-
      Path to the output PDB file
    type: File
    outputBinding:
      glob: $(inputs.output_pdb_path)
    format: edam:format_1476

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
