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
from biobb_pmx.pmxbiobb.pmxcreate_top import Pmxcreate_top  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(input_topology1_path=FILE_IN, input_topology2_path=FILE_IN, output_topology_path=FILE_OUT, 
      on_failure="IGNORE", time_out=task_time_out)
def _pmxcreate_top(input_topology1_path, input_topology2_path, output_topology_path,  properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        Pmxcreate_top(input_topology1_path=input_topology1_path, input_topology2_path=input_topology2_path, output_topology_path=output_topology_path, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def pmxcreate_top(input_topology1_path, input_topology2_path, output_topology_path, properties=None, **kwargs):

    if (output_topology_path is None or (os.path.exists(output_topology_path) and os.stat(output_topology_path).st_size > 0)) and \
       True:
        print("WARN: Task Pmxcreate_top already executed.")
    else:
        _pmxcreate_top( input_topology1_path,  input_topology2_path,  output_topology_path,  properties, **kwargs)