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
from biobb_haddock.haddock.flex_ref import FlexRef  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(input_haddock_wf_data=DIRECTORY_IN, output_haddock_wf_data=DIRECTORY_OUT, refinement_output_zip_path=FILE_OUT, ambig_restraints_table_path=FILE_IN, unambig_restraints_table_path=FILE_IN, hb_restraints_table_path=FILE_IN, haddock_config_path=FILE_IN, 
      on_failure="IGNORE", time_out=task_time_out)
def _flexref(input_haddock_wf_data, output_haddock_wf_data, refinement_output_zip_path, ambig_restraints_table_path, unambig_restraints_table_path, hb_restraints_table_path, haddock_config_path, properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        FlexRef(input_haddock_wf_data=input_haddock_wf_data, output_haddock_wf_data=output_haddock_wf_data, refinement_output_zip_path=refinement_output_zip_path, ambig_restraints_table_path=ambig_restraints_table_path, unambig_restraints_table_path=unambig_restraints_table_path, hb_restraints_table_path=hb_restraints_table_path, haddock_config_path=haddock_config_path, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def flex_ref(input_haddock_wf_data, output_haddock_wf_data, refinement_output_zip_path=None, ambig_restraints_table_path=None, unambig_restraints_table_path=None, hb_restraints_table_path=None, haddock_config_path=None, properties=None, **kwargs):

    if (output_haddock_wf_data is None or (os.path.exists(output_haddock_wf_data) and os.stat(output_haddock_wf_data).st_size > 0)) and \
       (refinement_output_zip_path is None or (os.path.exists(refinement_output_zip_path) and os.stat(refinement_output_zip_path).st_size > 0)) and \
       True:
        print("WARN: Task FlexRef already executed.")
    else:
        _flexref(input_haddock_wf_data, output_haddock_wf_data, refinement_output_zip_path, ambig_restraints_table_path, unambig_restraints_table_path, hb_restraints_table_path, haddock_config_path, properties, **kwargs)
