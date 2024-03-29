import traceback
from pycompss.api.task import task
from pycompss.api.constraint import constraint
from pycompss.api.parameter import FILE_IN, FILE_OUT
from biobb_common.tools import file_utils as fu
from biobb_chemistry.acpype import acpype_params_cns

@task(input_path=FILE_IN, output_path_par=FILE_OUT, output_path_inp=FILE_OUT, output_path_top=FILE_OUT)
def acpype_params_cns_pc(input_path, output_path_par, output_path_inp, output_path_top, properties, **kwargs):
    try:
        acpype_params_cns.AcpypeParamsCNS(input_path=input_path, output_path_par=output_path_par, output_path_inp=output_path_inp, output_path_top=output_path_top, properties=properties, **kwargs).launch()
    except Exception:
        traceback.print_exc()
        fu.write_failed_output(output_path_par)
        fu.write_failed_output(output_path_inp)
        fu.write_failed_output(output_path_top)
