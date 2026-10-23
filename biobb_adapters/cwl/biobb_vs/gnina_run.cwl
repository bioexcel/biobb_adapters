#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Wrapper of the gnina software.

doc: |-
  This class performs docking of a ligand to a receptor, optionally rescoring the poses with a convolutional neural network, via the gnina software.

baseCommand: gnina_run

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_vs:5.3.0--pyhdfd78af_0

inputs:
  input_ligand_path:
    label: Path to the input ligand. It may hold several ligands and it must hold
      genuine 3D coordinates, as gnina samples torsions but never bond lengths, bond
      angles or ring conformations
    doc: |-
      Path to the input ligand. It may hold several ligands and it must hold genuine 3D coordinates, as gnina samples torsions but never bond lengths, bond angles or ring conformations
      Type: string
      File type: input
      Accepted formats: sdf, mol2, pdb, pdbqt
      Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/gnina/gnina_ligand.sdf
    type: File
    format:
    - edam:format_3814
    - edam:format_3816
    - edam:format_1476
    - edam:format_1476
    inputBinding:
      position: 1
      prefix: --input_ligand_path

  input_receptor_path:
    label: Path to the input receptor. Every atom of this file is treated as rigid
      receptor, so any crystal ligand must be removed beforehand. Provide a PDBQT
      file for full control over protonation, as PDBQT input is passed to gnina unmodified.
      Charges are not taken into account, just hydrogen donor/acceptor character which
      depends on the protonation state
    doc: |-
      Path to the input receptor. Every atom of this file is treated as rigid receptor, so any crystal ligand must be removed beforehand. Provide a PDBQT file for full control over protonation, as PDBQT input is passed to gnina unmodified. Charges are not taken into account, just hydrogen donor/acceptor character which depends on the protonation state
      Type: string
      File type: input
      Accepted formats: pdb, pdbqt
      Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/vina/vina_receptor.pdbqt
    type: File
    format:
    - edam:format_1476
    - edam:format_1476
    inputBinding:
      position: 2
      prefix: --input_receptor_path

  output_sdf_path:
    label: Path to the output file with the docked poses and their scores as SD data
      fields. Use a .sdf.gz extension to obtain gzip compressed output
    doc: |-
      Path to the output file with the docked poses and their scores as SD data fields. Use a .sdf.gz extension to obtain gzip compressed output
      Type: string
      File type: output
      Accepted formats: sdf, gz
      Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/reference/gnina/ref_output_gnina.sdf
    type: string
    format:
    - edam:format_3814
    - edam:format_3989
    inputBinding:
      position: 3
      prefix: --output_sdf_path
    default: system.sdf

  input_box_path:
    label: Path to the PDB file with the box center and size annotated as a REMARK,
      as written by the box and box_residues building blocks. Mutually exclusive with
      input_autobox_path
    doc: |-
      Path to the PDB file with the box center and size annotated as a REMARK, as written by the box and box_residues building blocks. Mutually exclusive with input_autobox_path
      Type: string
      File type: input
      Accepted formats: pdb
      Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/vina/vina_box.pdb
    type: File?
    format:
    - edam:format_1476
    inputBinding:
      prefix: --input_box_path

  input_autobox_path:
    label: Path to a reference structure whose bounding coordinates define the docking
      box, for example a crystal ligand, an fpocket pocket or the whole receptor.
      It only needs atoms with Cartesian coordinates, it does not need to be a real
      molecule. Mutually exclusive with input_box_path
    doc: |-
      Path to a reference structure whose bounding coordinates define the docking box, for example a crystal ligand, an fpocket pocket or the whole receptor. It only needs atoms with Cartesian coordinates, it does not need to be a real molecule. Mutually exclusive with input_box_path
      Type: string
      File type: input
      Accepted formats: sdf, mol2, pdb, pdbqt, pqr
      Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/gnina/gnina_autobox.pdb
    type: File?
    format:
    - edam:format_3814
    - edam:format_3816
    - edam:format_1476
    - edam:format_1476
    - edam:format_1476
    inputBinding:
      prefix: --input_autobox_path

  output_summary_path:
    label: Path to the JSON summary file, holding one entry per output pose with the
      ligand it belongs to and every score gnina assigned to it
    doc: |-
      Path to the JSON summary file, holding one entry per output pose with the ligand it belongs to and every score gnina assigned to it
      Type: string
      File type: output
      Accepted formats: json
      Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/reference/gnina/ref_output_summary.json
    type: string
    format:
    - edam:format_3464
    inputBinding:
      prefix: --output_summary_path
    default: system.json

  output_log_path:
    label: Path to the log file written by gnina
    doc: |-
      Path to the log file written by gnina
      Type: string
      File type: output
      Accepted formats: log
      Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/reference/gnina/ref_output_gnina.log
    type: string
    format:
    - edam:format_2330
    inputBinding:
      prefix: --output_log_path
    default: system.log

  config:
    label: Advanced configuration options for biobb_vs GninaRun
    doc: |-
      Advanced configuration options for biobb_vs GninaRun. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_vs GninaRun documentation: https://biobb-vs.readthedocs.io/en/latest/gnina.html#module-gnina.gnina_run
    type: File?
    inputBinding:
      prefix: --config

outputs:
  output_sdf_path:
    label: Path to the output file with the docked poses and their scores as SD data
      fields. Use a .sdf.gz extension to obtain gzip compressed output
    doc: |-
      Path to the output file with the docked poses and their scores as SD data fields. Use a .sdf.gz extension to obtain gzip compressed output
    type: File
    outputBinding:
      glob: $(inputs.output_sdf_path)
    format: edam:format_3814

  output_summary_path:
    label: Path to the JSON summary file, holding one entry per output pose with the
      ligand it belongs to and every score gnina assigned to it
    doc: |-
      Path to the JSON summary file, holding one entry per output pose with the ligand it belongs to and every score gnina assigned to it
    type: File?
    outputBinding:
      glob: $(inputs.output_summary_path)
    format: edam:format_3464

  output_log_path:
    label: Path to the log file written by gnina
    doc: |-
      Path to the log file written by gnina
    type: File?
    outputBinding:
      glob: $(inputs.output_log_path)
    format: edam:format_2330

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
