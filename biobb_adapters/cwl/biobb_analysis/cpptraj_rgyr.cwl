#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Wrapper of the Ambertools Cpptraj module for computing the radius of gyration
  (Rgyr) from a given cpptraj compatible trajectory.

doc: |-
  Cpptraj (the successor to ptraj) is the main program in Ambertools for processing coordinate trajectories and data files. The parameter names and defaults are the same as the ones in the official Cpptraj manual.

baseCommand: cpptraj_rgyr

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_analysis:5.0.0--pyhdfd78af_0

inputs:
  input_top_path:
    label: Path to the input structure or topology file
    doc: |-
      Path to the input structure or topology file
      Type: string
      File type: input
      Accepted formats: top, pdb, prmtop, parmtop, zip
      Example file: https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.parm.top
    type: File
    format:
    - edam:format_3881
    - edam:format_1476
    - edam:format_3881
    - edam:format_3881
    - edam:format_3987
    inputBinding:
      position: 1
      prefix: --input_top_path

  input_traj_path:
    label: Path to the input trajectory to be processed
    doc: |-
      Path to the input trajectory to be processed
      Type: string
      File type: input
      Accepted formats: mdcrd, crd, cdf, netcdf, nc, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib
      Example file: https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/ambertools/cpptraj.traj.dcd
    type: File
    format:
    - edam:format_3878
    - edam:format_3878
    - edam:format_3650
    - edam:format_3650
    - edam:format_3650
    - edam:format_3886
    - edam:format_3886
    - edam:format_3886
    - edam:format_3878
    - edam:format_3887
    - edam:format_2033
    - edam:format_1476
    - edam:format_3816
    - edam:format_3910
    - edam:format_2033
    - edam:format_3885
    - edam:format_3875
    - edam:format_1477
    - edam:format_2333
    - edam:format_2033
    - edam:format_3814
    - edam:format_2033
    inputBinding:
      position: 2
      prefix: --input_traj_path

  output_cpptraj_path:
    label: Path to the output analysis
    doc: |-
      Path to the output analysis
      Type: string
      File type: output
      Accepted formats: dat, agr, xmgr, gnu
      Example file: https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/ambertools/ref_cpptraj.rgyr.dat
    type: string
    format:
    - edam:format_1637
    - edam:format_2033
    - edam:format_2033
    - edam:format_2033
    inputBinding:
      position: 3
      prefix: --output_cpptraj_path
    default: system.dat

  config:
    label: Advanced configuration options for biobb_analysis CpptrajRgyr
    doc: |-
      Advanced configuration options for biobb_analysis CpptrajRgyr. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_analysis CpptrajRgyr documentation: https://biobb-analysis.readthedocs.io/en/latest/ambertools.html#module-ambertools.cpptraj_rgyr
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_cpptraj_path:
    label: Path to the output analysis
    doc: |-
      Path to the output analysis
    type: File
    outputBinding:
      glob: $(inputs.output_cpptraj_path)
    format: edam:format_1637

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
