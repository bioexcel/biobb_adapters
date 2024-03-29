# Python
import os
import sys
import traceback
# Pycompss
from pycompss.api.task import task
from pycompss.api.parameter import FILE_IN, FILE_OUT
# Adapters commons pycompss
from biobb_adapters.pycompss.biobb_commons import task_config
# Wrapped Biobb
from biobb_ml.utils.scale_columns import ScaleColumns  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(input_dataset_path=FILE_IN, output_dataset_path=FILE_OUT, 
      on_failure="IGNORE", time_out=task_time_out)
def _scalecolumns(input_dataset_path, output_dataset_path,  properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        ScaleColumns(input_dataset_path=input_dataset_path, output_dataset_path=output_dataset_path, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def scale_columns(input_dataset_path, output_dataset_path, properties=None, **kwargs):

    if (output_dataset_path is None or (os.path.exists(output_dataset_path) and os.stat(output_dataset_path).st_size > 0)) and \
       True:
        print("WARN: Task ScaleColumns already executed.")
    else:
        _scalecolumns( input_dataset_path,  output_dataset_path,  properties, **kwargs)