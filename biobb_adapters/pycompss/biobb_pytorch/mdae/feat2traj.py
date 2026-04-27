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
from biobb_pytorch.mdae.feat2traj import Feat2Traj  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(input_results_npz_path=FILE_IN, input_stats_pt_path=FILE_IN, output_traj_path=FILE_OUT, input_topology_path=FILE_IN, output_top_path=FILE_OUT, 
      on_failure="IGNORE", time_out=task_time_out)
def _feat2traj(input_results_npz_path, input_stats_pt_path, output_traj_path, input_topology_path, output_top_path, properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        Feat2Traj(input_results_npz_path=input_results_npz_path, input_stats_pt_path=input_stats_pt_path, output_traj_path=output_traj_path, input_topology_path=input_topology_path, output_top_path=output_top_path, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def feat2traj(input_results_npz_path, input_stats_pt_path, output_traj_path, input_topology_path=None, output_top_path=None, properties=None, **kwargs):

    if (output_traj_path is None or (os.path.exists(output_traj_path) and os.stat(output_traj_path).st_size > 0)) and \
       (output_top_path is None or (os.path.exists(output_top_path) and os.stat(output_top_path).st_size > 0)) and \
       True:
        print("WARN: Task Feat2Traj already executed.")
    else:
        _feat2traj(input_results_npz_path, input_stats_pt_path, output_traj_path, input_topology_path, output_top_path, properties, **kwargs)
