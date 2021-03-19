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
from biobb_io.api.memprotmd_sim_list import MemProtMDSimList  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(output_simulations=FILE_OUT, 
      on_failure="IGNORE", time_out=task_time_out)
def _memprotmdsimlist(output_simulations,  properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        MemProtMDSimList(output_simulations=output_simulations, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def memprotmdsimlist(output_simulations, properties=None, **kwargs):

    if (output_simulations is None or os.path.exists(output_simulations)) and \
       True:
        print("WARN: Task MemProtMDSimList already executed.")
    else:
        _memprotmdsimlist( output_simulations,  properties, **kwargs)