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
from biobb_pytorch.mdae.build_model import BuildModel  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(input_stats_pt_path=FILE_IN, output_model_pth_path=FILE_OUT, 
      on_failure="IGNORE", time_out=task_time_out)
def _buildmodel(input_stats_pt_path, output_model_pth_path, properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        BuildModel(input_stats_pt_path=input_stats_pt_path, output_model_pth_path=output_model_pth_path, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def build_model(input_stats_pt_path, output_model_pth_path=None, properties=None, **kwargs):

    if (output_model_pth_path is None or (os.path.exists(output_model_pth_path) and os.stat(output_model_pth_path).st_size > 0)) and \
       True:
        print("WARN: Task BuildModel already executed.")
    else:
        _buildmodel(input_stats_pt_path, output_model_pth_path, properties, **kwargs)
