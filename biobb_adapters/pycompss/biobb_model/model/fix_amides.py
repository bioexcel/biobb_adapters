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
from biobb_model.model.fix_amides import FixAmides  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(input_pdb_path=FILE_IN, output_pdb_path=FILE_OUT, 
      on_failure="IGNORE", time_out=task_time_out)
def _fixamides(input_pdb_path, output_pdb_path,  properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        FixAmides(input_pdb_path=input_pdb_path, output_pdb_path=output_pdb_path, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def fixamides(input_pdb_path, output_pdb_path, properties=None, **kwargs):

    if (output_pdb_path is None or os.path.exists(output_pdb_path)) and \
       True:
        print("WARN: Task FixAmides already executed.")
    else:
        _fixamides( input_pdb_path,  output_pdb_path,  properties, **kwargs)