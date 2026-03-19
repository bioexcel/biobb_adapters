#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Wrapper of the GROMACS check module for comparing and validating GROMACS files.

doc: |-
  GROMACS check reads, analyzes and compares run input, trajectory and energy files reporting potential differences and inconsistencies.

baseCommand: gmx_check

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_analysis:5.2.1--gmx2026_2

inputs:
  output_log_path:
    label: Path to the text file storing the gmx check console output
    doc: |-
      Path to the text file storing the gmx check console output
      Type: string
      File type: output
      Accepted formats: txt, log, out
      Example file: https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_check.log
    type: string
    format:
    - edam:format_2330
    - edam:format_2330
    - edam:format_2330
    inputBinding:
      position: 1
      prefix: --output_log_path
    default: system.txt

  input_structure_path:
    label: Path to the first GROMACS run input file
    doc: |-
      Path to the first GROMACS run input file
      Type: string
      File type: input
      Accepted formats: tpr, gro, g96, pdb, brk, ent
      Example file: https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr
    type: File?
    format:
    - edam:format_2333
    - edam:format_2033
    - edam:format_2033
    - edam:format_1476
    - edam:format_2033
    - edam:format_1476
    inputBinding:
      prefix: --input_structure_path

  input_structure_2_path:
    label: Path to the second GROMACS run input file
    doc: |-
      Path to the second GROMACS run input file
      Type: string
      File type: input
      Accepted formats: tpr, gro, g96, pdb, brk, ent
      Example file: https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr
    type: File?
    format:
    - edam:format_2333
    - edam:format_2033
    - edam:format_2033
    - edam:format_1476
    - edam:format_2033
    - edam:format_1476
    inputBinding:
      prefix: --input_structure_2_path

  input_traj_path:
    label: Path to the first GROMACS trajectory file
    doc: |-
      Path to the first GROMACS trajectory file
      Type: string
      File type: input
      Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng
      Example file: https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr
    type: File?
    format:
    - edam:format_3875
    - edam:format_3910
    - edam:format_2333
    - edam:format_2033
    - edam:format_2033
    - edam:format_1476
    - edam:format_3876
    inputBinding:
      prefix: --input_traj_path

  input_traj_2_path:
    label: Path to the second GROMACS trajectory file
    doc: |-
      Path to the second GROMACS trajectory file
      Type: string
      File type: input
      Accepted formats: xtc, trr, cpt, gro, g96, pdb, tng
      Example file: https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/trajectory.trr
    type: File?
    format:
    - edam:format_3875
    - edam:format_3910
    - edam:format_2333
    - edam:format_2033
    - edam:format_2033
    - edam:format_1476
    - edam:format_3876
    inputBinding:
      prefix: --input_traj_2_path

  input_energy_path:
    label: Path to the first GROMACS energy file
    doc: |-
      Path to the first GROMACS energy file
      Type: string
      File type: input
      Accepted formats: edr
      Example file: https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/energy.edr
    type: File?
    format:
    - edam:format_2330
    inputBinding:
      prefix: --input_energy_path

  input_energy_2_path:
    label: Path to the second GROMACS energy file
    doc: |-
      Path to the second GROMACS energy file
      Type: string
      File type: input
      Accepted formats: edr
      Example file: https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/energy.edr
    type: File?
    format:
    - edam:format_2330
    inputBinding:
      prefix: --input_energy_2_path

  structure_check_path:
    label: Path to the structure file to analyze for internal consistency
    doc: |-
      Path to the structure file to analyze for internal consistency
      Type: string
      File type: input
      Accepted formats: tpr, gro, g96, pdb, brk, ent
      Example file: https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/topology.tpr
    type: File?
    format:
    - edam:format_2333
    - edam:format_2033
    - edam:format_2033
    - edam:format_1476
    - edam:format_2033
    - edam:format_1476
    inputBinding:
      prefix: --structure_check_path

  input_index_path:
    label: Path to the GROMACS index file
    doc: |-
      Path to the GROMACS index file
      Type: string
      File type: input
      Accepted formats: ndx
      Example file: https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/index.ndx
    type: File?
    format:
    - edam:format_2033
    inputBinding:
      prefix: --input_index_path

  config:
    label: Advanced configuration options for biobb_analysis GMXCheck
    doc: |-
      Advanced configuration options for biobb_analysis GMXCheck. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_analysis GMXCheck documentation: https://biobb-analysis.readthedocs.io/en/latest/gromacs.html#module-gromacs.gmx_check
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_log_path:
    label: Path to the text file storing the gmx check console output
    doc: |-
      Path to the text file storing the gmx check console output
    type: File
    outputBinding:
      glob: $(inputs.output_log_path)
    format: edam:format_2330

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
