#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Wrapper class for the CMIP cmip module.

doc: |-
  The CMIP cmip module. CMIP cmip module compute classical molecular interaction potentials.

baseCommand: cmip

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_cmip:3.6.0--pyhdfd78af_0

inputs:
  input_pdb_path:
    label: Path to the input PDB file
    doc: |-
      Path to the input PDB file
      Type: string
      File type: input
      Accepted formats: pdb
      Example file: https://raw.githubusercontent.com/bioexcel/biobb_cmip/master/biobb_cmip/test/data/cmip/1kim_h.pdb
    type: File
    format:
    - edam:format_1476
    inputBinding:
      position: 1
      prefix: --input_pdb_path

  input_probe_pdb_path:
    label: Path to the input probe file in PDB format
    doc: |-
      Path to the input probe file in PDB format
      Type: string
      File type: input
      Accepted formats: pdb
      Example file: null
    type: File?
    format:
    - edam:format_1476
    inputBinding:
      prefix: --input_probe_pdb_path

  output_pdb_path:
    label: Path to the output PDB file
    doc: |-
      Path to the output PDB file
      Type: string
      File type: output
      Accepted formats: pdb
      Example file: https://raw.githubusercontent.com/bioexcel/biobb_cmip/master/biobb_cmip/test/reference/cmip/1kim_neutral.pdb
    type: string
    format:
    - edam:format_1476
    inputBinding:
      prefix: --output_pdb_path
    default: system.pdb

  output_grd_path:
    label: Path to the output grid file in GRD format
    doc: |-
      Path to the output grid file in GRD format
      Type: string
      File type: output
      Accepted formats: grd
      Example file: null
    type: string
    format:
    - edam:format_2330
    inputBinding:
      prefix: --output_grd_path
    default: system.grd

  output_cube_path:
    label: Path to the output grid file in cube format
    doc: |-
      Path to the output grid file in cube format
      Type: string
      File type: output
      Accepted formats: cube
      Example file: null
    type: string
    format:
    - edam:format_2330
    inputBinding:
      prefix: --output_cube_path
    default: system.cube

  output_rst_path:
    label: Path to the output restart file
    doc: |-
      Path to the output restart file
      Type: string
      File type: output
      Accepted formats: txt
      Example file: null
    type: string
    format:
    - edam:format_2330
    inputBinding:
      prefix: --output_rst_path
    default: system.txt

  output_byat_path:
    label: Path to the output atom by atom energy file
    doc: |-
      Path to the output atom by atom energy file
      Type: string
      File type: output
      Accepted formats: txt
      Example file: null
    type: string
    format:
    - edam:format_2330
    inputBinding:
      prefix: --output_byat_path
    default: system.txt

  input_vdw_params_path:
    label: Path to the CMIP input Van der Waals force parameters, if not provided
      the CMIP conda installation one is used ("$CONDA_PREFIX/share/cmip/dat/vdwprm")
    doc: |-
      Path to the CMIP input Van der Waals force parameters, if not provided the CMIP conda installation one is used ("$CONDA_PREFIX/share/cmip/dat/vdwprm")
      Type: string
      File type: input
      Accepted formats: txt
      Example file: null
    type: File?
    format:
    - edam:format_2330
    inputBinding:
      prefix: --input_vdw_params_path

  input_params_path:
    label: Path to the CMIP input parameters file
    doc: |-
      Path to the CMIP input parameters file
      Type: string
      File type: input
      Accepted formats: txt
      Example file: null
    type: File?
    format:
    - edam:format_2330
    inputBinding:
      prefix: --input_params_path

  config:
    label: Advanced configuration options for biobb_cmip Titration
    doc: |-
      Advanced configuration options for biobb_cmip Titration. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_cmip Titration documentation: https://biobb-cmip.readthedocs.io/en/latest/cmip.html#module-cmip.cmip
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_pdb_path:
    label: Path to the output PDB file
    doc: |-
      Path to the output PDB file
    type: File?
    outputBinding:
      glob: $(inputs.output_pdb_path)
    format: edam:format_1476

  output_grd_path:
    label: Path to the output grid file in GRD format
    doc: |-
      Path to the output grid file in GRD format
    type: File?
    outputBinding:
      glob: $(inputs.output_grd_path)
    format: edam:format_2330

  output_cube_path:
    label: Path to the output grid file in cube format
    doc: |-
      Path to the output grid file in cube format
    type: File?
    outputBinding:
      glob: $(inputs.output_cube_path)
    format: edam:format_2330

  output_rst_path:
    label: Path to the output restart file
    doc: |-
      Path to the output restart file
    type: File?
    outputBinding:
      glob: $(inputs.output_rst_path)
    format: edam:format_2330

  output_byat_path:
    label: Path to the output atom by atom energy file
    doc: |-
      Path to the output atom by atom energy file
    type: File?
    outputBinding:
      glob: $(inputs.output_byat_path)
    format: edam:format_2330

$namespaces:
  edam: http://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
