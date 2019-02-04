#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: solvate.py
hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_md:0.1.4--py_0
inputs:
  input_solute_gro_path:
    type: File
    inputBinding:
      position: 1
      prefix: --input_solute_gro_path

  output_gro_path:
    type: string
    inputBinding:
      position: 2
      prefix: --output_gro_path
    default: "structure_solvated.gro"

  input_top_zip_path:
    type: File
    inputBinding:
      position: 3
      prefix: --input_top_zip_path

  output_top_zip_path:
    type: string
    inputBinding:
      position: 4
      prefix: --output_top_zip_path
    default: "topology_solvated.gro"

  config:
    type: string?
    inputBinding:
      position: 5
      prefix: --config

outputs:
  output_gro_file:
    type: File
    outputBinding:
      glob: $(inputs.output_gro_path)
  output_top_zip_file:
    type: File
    outputBinding:
      glob: $(inputs.output_top_zip_path)
