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
from biobb_model.model.checking_log import CheckingLog  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(input_pdb_path=FILE_IN, output_log_path=FILE_OUT, 
      on_failure="IGNORE", time_out=task_time_out)
def _checkinglog(input_pdb_path, output_log_path,  properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        CheckingLog(input_pdb_path=input_pdb_path, output_log_path=output_log_path, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def checking_log(input_pdb_path, output_log_path, properties=None, **kwargs):

    if (output_log_path is None or (os.path.exists(output_log_path) and os.stat(output_log_path).st_size > 0)) and \
       True:
        print("WARN: Task CheckingLog already executed.")
    else:
        _checkinglog( input_pdb_path,  output_log_path,  properties, **kwargs)