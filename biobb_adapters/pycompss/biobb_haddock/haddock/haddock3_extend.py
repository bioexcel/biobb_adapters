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
from biobb_haddock.haddock.haddock3_extend import Haddock3Extend  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(input_haddock_wf_data=DIRECTORY_IN, haddock_config_path=FILE_IN, output_haddock_wf_data=DIRECTORY_OUT, 
      on_failure="IGNORE", time_out=task_time_out)
def _haddock3extend(input_haddock_wf_data, haddock_config_path, output_haddock_wf_data, properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        Haddock3Extend(input_haddock_wf_data=input_haddock_wf_data, haddock_config_path=haddock_config_path, output_haddock_wf_data=output_haddock_wf_data, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def haddock3_extend(input_haddock_wf_data, haddock_config_path, output_haddock_wf_data, properties=None, **kwargs):

    if (output_haddock_wf_data is None or (os.path.exists(output_haddock_wf_data) and os.stat(output_haddock_wf_data).st_size > 0)) and \
       True:
        print("WARN: Task Haddock3Extend already executed.")
    else:
        _haddock3extend(input_haddock_wf_data, haddock_config_path, output_haddock_wf_data, properties, **kwargs)
