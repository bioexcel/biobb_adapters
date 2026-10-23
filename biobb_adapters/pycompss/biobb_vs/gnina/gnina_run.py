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
from biobb_vs.gnina.gnina_run import GninaRun  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(input_ligand_path=FILE_IN, input_receptor_path=FILE_IN, output_sdf_path=FILE_OUT, input_box_path=FILE_IN, input_autobox_path=FILE_IN, output_summary_path=FILE_OUT, output_log_path=FILE_OUT, 
      on_failure="IGNORE", time_out=task_time_out)
def _gninarun(input_ligand_path, input_receptor_path, output_sdf_path, input_box_path, input_autobox_path, output_summary_path, output_log_path, properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        GninaRun(input_ligand_path=input_ligand_path, input_receptor_path=input_receptor_path, output_sdf_path=output_sdf_path, input_box_path=input_box_path, input_autobox_path=input_autobox_path, output_summary_path=output_summary_path, output_log_path=output_log_path, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def gnina_run(input_ligand_path, input_receptor_path, output_sdf_path, input_box_path=None, input_autobox_path=None, output_summary_path=None, output_log_path=None, properties=None, **kwargs):

    if (output_sdf_path is None or (os.path.exists(output_sdf_path) and os.stat(output_sdf_path).st_size > 0)) and \
       (output_summary_path is None or (os.path.exists(output_summary_path) and os.stat(output_summary_path).st_size > 0)) and \
       (output_log_path is None or (os.path.exists(output_log_path) and os.stat(output_log_path).st_size > 0)) and \
       True:
        print("WARN: Task GninaRun already executed.")
    else:
        _gninarun(input_ligand_path, input_receptor_path, output_sdf_path, input_box_path, input_autobox_path, output_summary_path, output_log_path, properties, **kwargs)
