#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Performs Layer-wise Relevance Propagation on a trained autoencoder encoder.

doc: |-
  Performs Layer-wise Relevance Propagation on a trained autoencoder encoder.

baseCommand: LRP

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_pytorch:5.2.3--pyha658751_0

inputs:
  input_model_pth_path:
    label: Path to the trained model file whose encoder is analyzed
    doc: |-
      Path to the trained model file whose encoder is analyzed
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

  input_dataset_pt_path:
    label: Path to the input dataset file (.pt) used for computing relevance scores
    doc: |-
      Path to the input dataset file (.pt) used for computing relevance scores
      Type: string
      File type: input
      Accepted formats: pt
      Example file: https://github.com/bioexcel/biobb_pytorch/raw/master/biobb_pytorch/test/reference/mdae/output_model.pt
    type: File
    format:
    - edam:format_2333
    inputBinding:
      position: 2
      prefix: --input_dataset_pt_path

  output_results_npz_path:
    label: Path to the output results file containing relevance scores (compressed
      NumPy archive)
    doc: |-
      Path to the output results file containing relevance scores (compressed NumPy archive)
      Type: string
      File type: output
      Accepted formats: npz
      Example file: https://github.com/bioexcel/biobb_pytorch/raw/master/biobb_pytorch/test/reference/mdae/output_results.npz
    type: string
    format:
    - edam:format_2333
    inputBinding:
      prefix: --output_results_npz_path
    default: system.npz

  config:
    label: Advanced configuration options for biobb_pytorch LRP
    doc: |-
      Advanced configuration options for biobb_pytorch LRP. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_pytorch LRP documentation: https://biobb-pytorch.readthedocs.io/en/latest/mdae.html#module-biobb_pytorch.mdae.explainability.LRP
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_results_npz_path:
    label: Path to the output results file containing relevance scores (compressed
      NumPy archive)
    doc: |-
      Path to the output results file containing relevance scores (compressed NumPy archive)
    type: File?
    outputBinding:
      glob: $(inputs.output_results_npz_path)
    format: edam:format_2333

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
