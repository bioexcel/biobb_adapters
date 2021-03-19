#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Wrapper of most of the imblearn.over_sampling methods.

doc: |-
  Involves supplementing the training data with multiple copies of some of the minority classes of a given dataset. If regression is specified as type, the data will be resampled to classes in order to apply the oversampling model. Visit the imbalanced-learn official website for the different methods accepted in this wrapper: RandomOverSampler, SMOTE, BorderlineSMOTE, SVMSMOTE, ADASYN

baseCommand: oversampling

hints:
  DockerRequirement:
    dockerPull: https://quay.io/biocontainers/biobb_ml:3.5.0--py_2

inputs:
  input_dataset_path:
    label: Path to the input dataset
    doc: |-
      Path to the input dataset
      Type: string
      File type: input
      Accepted formats: csv
      Example file: https://github.com/bioexcel/biobb_ml/raw/master/biobb_ml/test/data/resampling/dataset_resampling.csv
    type: File
    format:
    - edam:format_3752
    inputBinding:
      position: 1
      prefix: --input_dataset_path

  output_dataset_path:
    label: Path to the output dataset
    doc: |-
      Path to the output dataset
      Type: string
      File type: output
      Accepted formats: csv
      Example file: https://github.com/bioexcel/biobb_ml/raw/master/biobb_ml/test/reference/resampling/ref_output_oversampling.csv
    type: string
    format:
    - edam:format_3752
    inputBinding:
      position: 2
      prefix: --output_dataset_path
    default: system.csv

  config:
    label: Advanced configuration options for biobb_ml Oversampling
    doc: |-
      Advanced configuration options for biobb_ml Oversampling. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_ml Oversampling documentation: https://biobb-ml.readthedocs.io/en/latest/resampling.html#module-resampling.oversampling
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_dataset_path:
    label: Path to the output dataset
    doc: |-
      Path to the output dataset
    type: File
    outputBinding:
      glob: $(inputs.output_dataset_path)
    format: edam:format_3752

$namespaces:
  edam: http://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl