#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Selects a single pose in the output of the gnina_run building block.

doc: |-
  Extracts one pose out of the multi record SDF file written by the gnina_run building block, copying the record verbatim.

baseCommand: gnina_select_pose

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_vs:5.3.0--pyhdfd78af_0

inputs:
  input_sdf_path:
    label: Path to the SDF file with the docked poses written by the gnina_run building
      block
    doc: |-
      Path to the SDF file with the docked poses written by the gnina_run building block
      Type: string
      File type: input
      Accepted formats: sdf, gz
      Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/gnina/gnina_poses.sdf
    type: File
    format:
    - edam:format_3814
    - edam:format_3989
    inputBinding:
      position: 1
      prefix: --input_sdf_path

  output_sdf_path:
    label: Path to the output SDF file with the selected pose
    doc: |-
      Path to the output SDF file with the selected pose
      Type: string
      File type: output
      Accepted formats: sdf, gz
      Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/reference/gnina/ref_output_pose.sdf
    type: string
    format:
    - edam:format_3814
    - edam:format_3989
    inputBinding:
      position: 2
      prefix: --output_sdf_path
    default: system.sdf

  config:
    label: Advanced configuration options for biobb_vs GninaSelectPose
    doc: |-
      Advanced configuration options for biobb_vs GninaSelectPose. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_vs GninaSelectPose documentation: https://biobb-vs.readthedocs.io/en/latest/gnina.html#module-gnina.gnina_select_pose
    type: File?
    inputBinding:
      prefix: --config

outputs:
  output_sdf_path:
    label: Path to the output SDF file with the selected pose
    doc: |-
      Path to the output SDF file with the selected pose
    type: File
    outputBinding:
      glob: $(inputs.output_sdf_path)
    format: edam:format_3814

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
