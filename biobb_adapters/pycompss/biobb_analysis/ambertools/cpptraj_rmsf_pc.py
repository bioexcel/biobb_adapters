import traceback
from pycompss.api.task import task
from pycompss.api.constraint import constraint
from pycompss.api.parameter import FILE_IN, FILE_OUT
from biobb_common.tools import file_utils as fu
from biobb_analysis.ambertools import cpptraj_rmsf

@task(input_top_path=FILE_IN, input_traj_path=FILE_IN, output_cpptraj_path=FILE_OUT, input_exp_path=FILE_IN)
def cpptraj_rmsf_pc(input_top_path, input_traj_path, output_cpptraj_path, input_exp_path, properties, **kwargs):
    try:
        cpptraj_rmsf.Rmsf(input_top_path=input_top_path, input_traj_path=input_traj_path, output_cpptraj_path=output_cpptraj_path, input_exp_path=input_exp_path, properties=properties, **kwargs).launch()
    except Exception:
        traceback.print_exc()
        fu.write_failed_output(output_cpptraj_path)
