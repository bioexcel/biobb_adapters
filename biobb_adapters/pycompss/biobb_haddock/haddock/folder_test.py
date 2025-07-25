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
from biobb_haddock.haddock.folder_test import FolderTest  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(output_folder=FILE_OUT, 
      on_failure="IGNORE", time_out=task_time_out)
def _foldertest(output_folder,  properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        FolderTest(output_folder=output_folder, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def folder_test(output_folder, properties=None, **kwargs):

    if (output_folder is None or (os.path.exists(output_folder) and os.stat(output_folder).st_size > 0)) and \
       True:
        print("WARN: Task FolderTest already executed.")
    else:
        _foldertest( output_folder,  properties, **kwargs)