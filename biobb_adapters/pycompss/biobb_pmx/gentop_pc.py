import traceback
from pycompss.api.task import task
from pycompss.api.constraint import constraint
from pycompss.api.multinode import multinode
from pycompss.api.parameter import FILE_IN, FILE_OUT
from biobb_common.tools import file_utils as fu
from biobb_pmx.pmx import gentop
import os
import sys


# Is constraint decorator needed in this case?
# @constraint(computingUnits=)
@task(input_top_zip_path=FILE_IN, output_top_zip_path=FILE_OUT, output_log_path=FILE_OUT, on_failure="IGNORE")
def gentop_pc(input_top_zip_path, output_top_zip_path, output_log_path, properties, **kwargs):
    try:
        gentop.Gentop(input_top_zip_path=input_top_zip_path, output_top_zip_path=output_top_zip_path, output_log_path=output_log_path, properties=properties, **kwargs).launch()
        if not os.path.exists(output_top_zip_path):
            fu.write_failed_output(output_top_zip_path)
        if not os.path.exists(output_log_path):
            fu.write_failed_output(output_log_path)
    except Exception:
        traceback.print_exc()
        fu.write_failed_output(output_top_zip_path)
        fu.write_failed_output(output_log_path)
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
