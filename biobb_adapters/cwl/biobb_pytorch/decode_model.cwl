#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Evaluates a PyTorch autoencoder from the given properties.

doc: |-
  Evaluates a PyTorch autoencoder from the given properties.

baseCommand: decode_model

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_pytorch:5.2.3--pyha658751_0

inputs:
  input_model_pth_path:
    label: Path to the trained model file whose decoder will be used
    doc: |-
      Path to the trained model file whose decoder will be used
      Type: string
      File type: input
      Accepted formats: pth
      Example file: https://github.com/bioexcel/biobb_pytorch/raw/master/biobb_pytorch/test/reference/mdae/output_model.pth
    type: File
    format:
    - edam:format_2333
    inputBinding:
      position: 1
      prefix: --input_model_pth_path

  input_dataset_npy_path:
    label: Path to the input latent variables file in NumPy format (e.g. encoded 'z')
    doc: |-
      Path to the input latent variables file in NumPy format (e.g. encoded 'z')
      Type: string
      File type: input
      Accepted formats: npy
      Example file: https://github.com/bioexcel/biobb_pytorch/raw/master/biobb_pytorch/test/reference/mdae/output_model.npy
    type: File
    format:
    - edam:format_2333
    inputBinding:
      position: 2
      prefix: --input_dataset_npy_path

  output_results_npz_path:
    label: Path to the output reconstructed data file (compressed NumPy archive, typically
      containing 'xhat')
    doc: |-
      Path to the output reconstructed data file (compressed NumPy archive, typically containing 'xhat')
      Type: string
      File type: output
      Accepted formats: npz
      Example file: https://github.com/bioexcel/biobb_pytorch/raw/master/biobb_pytorch/test/reference/mdae/output_results.npz
    type: string
    format:
    - edam:format_2333
    inputBinding:
      position: 3
      prefix: --output_results_npz_path
    default: system.npz

  config:
    label: Advanced configuration options for biobb_pytorch decode_model
    doc: |-
      Advanced configuration options for biobb_pytorch decode_model. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_pytorch decode_model documentation: https://biobb-pytorch.readthedocs.io/en/latest/mdae.html#module-biobb_pytorch.mdae.decode_model
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_results_npz_path:
    label: Path to the output reconstructed data file (compressed NumPy archive, typically
      containing 'xhat')
    doc: |-
      Path to the output reconstructed data file (compressed NumPy archive, typically containing 'xhat')
    type: File
    outputBinding:
      glob: $(inputs.output_results_npz_path)
    format: edam:format_2333

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
