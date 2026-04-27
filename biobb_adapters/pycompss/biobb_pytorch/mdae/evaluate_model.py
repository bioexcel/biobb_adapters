# Python
import os
import sys
import traceback
# Pycompss
from pycompss.api.task import task
from pycompss.api.parameter import FILE_IN, FILE_OUT, DIRECTORY_IN, DIRECTORY_OUT
# Adapters commons pycompss
from biobb_adapters.pycompss.biobb_commons import task_config
# Wrapped Biobb
from biobb_pytorch.mdae.evaluate_model import EvaluateModel  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(input_model_pth_path=FILE_IN, input_dataset_pt_path=FILE_IN, output_results_npz_path=FILE_OUT, 
      on_failure="IGNORE", time_out=task_time_out)
def _evaluatemodel(input_model_pth_path, input_dataset_pt_path, output_results_npz_path, properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        EvaluateModel(input_model_pth_path=input_model_pth_path, input_dataset_pt_path=input_dataset_pt_path, output_results_npz_path=output_results_npz_path, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def evaluate_model(input_model_pth_path, input_dataset_pt_path, output_results_npz_path, properties=None, **kwargs):

    if (output_results_npz_path is None or (os.path.exists(output_results_npz_path) and os.stat(output_results_npz_path).st_size > 0)) and \
       True:
        print("WARN: Task EvaluateModel already executed.")
    else:
        _evaluatemodel(input_model_pth_path, input_dataset_pt_path, output_results_npz_path, properties, **kwargs)
