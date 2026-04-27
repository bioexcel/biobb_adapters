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
from biobb_analysis.gromacs.gmx_check import GMXCheck  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(output_log_path=FILE_OUT, input_structure_path=FILE_IN, input_structure_2_path=FILE_IN, input_traj_path=FILE_IN, input_traj_2_path=FILE_IN, input_energy_path=FILE_IN, input_energy_2_path=FILE_IN, structure_check_path=FILE_IN, input_index_path=FILE_IN, 
      on_failure="IGNORE", time_out=task_time_out)
def _gmxcheck(output_log_path, input_structure_path, input_structure_2_path, input_traj_path, input_traj_2_path, input_energy_path, input_energy_2_path, structure_check_path, input_index_path, properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        GMXCheck(output_log_path=output_log_path, input_structure_path=input_structure_path, input_structure_2_path=input_structure_2_path, input_traj_path=input_traj_path, input_traj_2_path=input_traj_2_path, input_energy_path=input_energy_path, input_energy_2_path=input_energy_2_path, structure_check_path=structure_check_path, input_index_path=input_index_path, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def gmx_check(output_log_path, input_structure_path=None, input_structure_2_path=None, input_traj_path=None, input_traj_2_path=None, input_energy_path=None, input_energy_2_path=None, structure_check_path=None, input_index_path=None, properties=None, **kwargs):

    if (output_log_path is None or (os.path.exists(output_log_path) and os.stat(output_log_path).st_size > 0)) and \
       True:
        print("WARN: Task GMXCheck already executed.")
    else:
        _gmxcheck(output_log_path, input_structure_path, input_structure_2_path, input_traj_path, input_traj_2_path, input_energy_path, input_energy_2_path, structure_check_path, input_index_path, properties, **kwargs)
