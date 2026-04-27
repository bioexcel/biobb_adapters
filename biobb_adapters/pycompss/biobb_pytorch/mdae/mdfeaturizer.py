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
from biobb_pytorch.mdae.mdfeaturizer import mdfeaturizer  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(input_topology_path=FILE_IN, output_dataset_pt_path=FILE_OUT, output_stats_pt_path=FILE_OUT, input_trajectory_path=FILE_IN, 
      on_failure="IGNORE", time_out=task_time_out)
def _mdfeaturizer(input_topology_path, output_dataset_pt_path, output_stats_pt_path, input_trajectory_path, properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        mdfeaturizer(input_topology_path=input_topology_path, output_dataset_pt_path=output_dataset_pt_path, output_stats_pt_path=output_stats_pt_path, input_trajectory_path=input_trajectory_path, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def mdfeaturizer(input_topology_path, output_dataset_pt_path, output_stats_pt_path, input_trajectory_path=None, properties=None, **kwargs):

    if (output_dataset_pt_path is None or (os.path.exists(output_dataset_pt_path) and os.stat(output_dataset_pt_path).st_size > 0)) and \
       (output_stats_pt_path is None or (os.path.exists(output_stats_pt_path) and os.stat(output_stats_pt_path).st_size > 0)) and \
       True:
        print("WARN: Task mdfeaturizer already executed.")
    else:
        _mdfeaturizer(input_topology_path, output_dataset_pt_path, output_stats_pt_path, input_trajectory_path, properties, **kwargs)
