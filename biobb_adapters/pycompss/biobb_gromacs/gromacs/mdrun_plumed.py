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
from biobb_gromacs.gromacs.mdrun_plumed import MdrunPlumed  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(input_tpr_path=FILE_IN, output_gro_path=FILE_OUT, output_edr_path=FILE_OUT, output_log_path=FILE_OUT, output_trr_path=FILE_OUT, input_cpt_path=FILE_IN, output_xtc_path=FILE_OUT, output_cpt_path=FILE_OUT, output_dhdl_path=FILE_OUT, input_plumed_path=FILE_IN, input_plumed_folder=DIRECTORY_IN, output_plumed_folder=DIRECTORY_OUT, 
      on_failure="IGNORE", time_out=task_time_out)
def _mdrunplumed(input_tpr_path, output_gro_path, output_edr_path, output_log_path, output_trr_path, input_cpt_path, output_xtc_path, output_cpt_path, output_dhdl_path, input_plumed_path, input_plumed_folder, output_plumed_folder, properties, **kwargs):
    
    task_config.config_multinode(properties)
    
    try:
        MdrunPlumed(input_tpr_path=input_tpr_path, output_gro_path=output_gro_path, output_edr_path=output_edr_path, output_log_path=output_log_path, output_trr_path=output_trr_path, input_cpt_path=input_cpt_path, output_xtc_path=output_xtc_path, output_cpt_path=output_cpt_path, output_dhdl_path=output_dhdl_path, input_plumed_path=input_plumed_path, input_plumed_folder=input_plumed_folder, output_plumed_folder=output_plumed_folder, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def mdrun_plumed(input_tpr_path, output_gro_path, output_edr_path, output_log_path, output_trr_path=None, input_cpt_path=None, output_xtc_path=None, output_cpt_path=None, output_dhdl_path=None, input_plumed_path=None, input_plumed_folder=None, output_plumed_folder=None, properties=None, **kwargs):

    if (output_gro_path is None or (os.path.exists(output_gro_path) and os.stat(output_gro_path).st_size > 0)) and \
       (output_edr_path is None or (os.path.exists(output_edr_path) and os.stat(output_edr_path).st_size > 0)) and \
       (output_log_path is None or (os.path.exists(output_log_path) and os.stat(output_log_path).st_size > 0)) and \
       (output_trr_path is None or (os.path.exists(output_trr_path) and os.stat(output_trr_path).st_size > 0)) and \
       (output_xtc_path is None or (os.path.exists(output_xtc_path) and os.stat(output_xtc_path).st_size > 0)) and \
       (output_cpt_path is None or (os.path.exists(output_cpt_path) and os.stat(output_cpt_path).st_size > 0)) and \
       (output_dhdl_path is None or (os.path.exists(output_dhdl_path) and os.stat(output_dhdl_path).st_size > 0)) and \
       (output_plumed_folder is None or (os.path.exists(output_plumed_folder) and os.stat(output_plumed_folder).st_size > 0)) and \
       True:
        print("WARN: Task MdrunPlumed already executed.")
    else:
        _mdrunplumed(input_tpr_path, output_gro_path, output_edr_path, output_log_path, output_trr_path, input_cpt_path, output_xtc_path, output_cpt_path, output_dhdl_path, input_plumed_path, input_plumed_folder, output_plumed_folder, properties, **kwargs)
