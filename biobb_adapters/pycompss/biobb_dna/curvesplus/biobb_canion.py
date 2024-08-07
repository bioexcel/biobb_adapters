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
from biobb_dna.curvesplus.biobb_canion import Canion  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(input_cdi_path=FILE_IN, input_afr_path=FILE_IN, input_avg_struc_path=FILE_IN, output_zip_path=FILE_OUT, 
      on_failure="IGNORE", time_out=task_time_out)
def _canion(input_cdi_path, input_afr_path, input_avg_struc_path, output_zip_path,  properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        Canion(input_cdi_path=input_cdi_path, input_afr_path=input_afr_path, input_avg_struc_path=input_avg_struc_path, output_zip_path=output_zip_path, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def biobb_canion(input_cdi_path, input_afr_path, input_avg_struc_path, output_zip_path, properties=None, **kwargs):

    if (output_zip_path is None or (os.path.exists(output_zip_path) and os.stat(output_zip_path).st_size > 0)) and \
       True:
        print("WARN: Task Canion already executed.")
    else:
        _canion( input_cdi_path,  input_afr_path,  input_avg_struc_path,  output_zip_path,  properties, **kwargs)