#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand:
  - genion
inputs:
  system:
    type: string
    inputBinding:
      position: 1
      prefix: --system
    default: ""
  step:
    type: string
    inputBinding:
      position: 2
      prefix: --step
    default: "genion"
  conf_file:
    type: File
    inputBinding:
      position: 3
      prefix: --conf_file
#BB specific
  input_tpr_path:
    type: File
    inputBinding:
      position: 4
      prefix: --input_tpr_path
  output_gro_path:
    type: string
    inputBinding:
      position: 5
      prefix: --output_gro_path
  input_top_zip_path:
    type: File
    inputBinding:
      position: 6
      prefix: --input_top_zip_path
  output_top_zip_path:
    type: string
    inputBinding:
      position: 7
      prefix: --output_top_zip_path
outputs:
  output_gro_file:
    type: File
    outputBinding:
      glob: $(inputs.output_gro_path)
  output_top_zip_file:
    type: File
    outputBinding:
      glob: $(inputs.output_top_zip_path)
