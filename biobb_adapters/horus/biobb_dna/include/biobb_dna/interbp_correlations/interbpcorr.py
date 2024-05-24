# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_filename_shift = PluginVariable(
    id="input_filename_shift",  # ID of the variable, will allow us to identify the value
    name="input_filename_shift",  # The name that will appear in the frontend
    description="Path to .ser file with data for helical parameter 'shift'",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['ser']
)

input_filename_slide = PluginVariable(
    id="input_filename_slide",  # ID of the variable, will allow us to identify the value
    name="input_filename_slide",  # The name that will appear in the frontend
    description="Path to .ser file with data for helical parameter 'slide'",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['ser']
)

input_filename_rise = PluginVariable(
    id="input_filename_rise",  # ID of the variable, will allow us to identify the value
    name="input_filename_rise",  # The name that will appear in the frontend
    description="Path to .ser file with data for helical parameter 'rise'",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['ser']
)

input_filename_tilt = PluginVariable(
    id="input_filename_tilt",  # ID of the variable, will allow us to identify the value
    name="input_filename_tilt",  # The name that will appear in the frontend
    description="Path to .ser file with data for helical parameter 'tilt'",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['ser']
)

input_filename_roll = PluginVariable(
    id="input_filename_roll",  # ID of the variable, will allow us to identify the value
    name="input_filename_roll",  # The name that will appear in the frontend
    description="Path to .ser file with data for helical parameter 'roll'",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['ser']
)

input_filename_twist = PluginVariable(
    id="input_filename_twist",  # ID of the variable, will allow us to identify the value
    name="input_filename_twist",  # The name that will appear in the frontend
    description="Path to .ser file with data for helical parameter 'twist'",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['ser']
)


output_csv_path = PluginVariable(
    id="output_csv_path",  # ID of the variable, will allow us to identify the value
    name="output_csv_path",  # The name that will appear in the frontend
    description="Path to directory where output is saved",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['csv']
)

output_jpg_path = PluginVariable(
    id="output_jpg_path",  # ID of the variable, will allow us to identify the value
    name="output_jpg_path",  # The name that will appear in the frontend
    description="Path to .jpg file where output is saved",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['jpg']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

sequence = PluginVariable(
    id="sequence",
    name="sequence",
    description="Nucleic acid sequence for the input .ser file. Length of sequence is expected to be the same as the total number of columns in the .ser file, minus the index column (even if later on a subset of columns is selected with the *seqpos* option).",
    type=VariableTypes.STRING
)

seqpos = PluginVariable(
    id="seqpos",
    name="seqpos",
    description="list of sequence positions (columns indices starting by 0) to analyze.  If not specified it will analyse the complete sequence.",
    type=VariableTypes.STRING
)

remove_tmp = PluginVariable(
    id="remove_tmp",
    name="remove_tmp",
    description="Remove temporal files.",
    type=VariableTypes.BOOLEAN
)

restart = PluginVariable(
    id="restart",
    name="restart",
    description="Do not execute if output files exist.",
    type=VariableTypes.BOOLEAN
)

# Define the action that the block will perform
def interbpcorr_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_filename_shift_value = biobb_block.inputs["input_filename_shift"]
    
    input_filename_slide_value = biobb_block.inputs["input_filename_slide"]
    
    input_filename_rise_value = biobb_block.inputs["input_filename_rise"]
    
    input_filename_tilt_value = biobb_block.inputs["input_filename_tilt"]
    
    input_filename_roll_value = biobb_block.inputs["input_filename_roll"]
    
    input_filename_twist_value = biobb_block.inputs["input_filename_twist"]
    
    
    output_csv_path_value = biobb_block.inputs["output_csv_path"]
    
    output_jpg_path_value = biobb_block.inputs["output_jpg_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["sequence"] = biobb_block.variables["sequence"]
    
    properties_values["seqpos"] = biobb_block.variables["seqpos"]
    
    properties_values["remove_tmp"] = biobb_block.variables["remove_tmp"]
    
    properties_values["restart"] = biobb_block.variables["restart"]
    
    for key in list(properties_values.keys()):
        if properties_values[key] is None:
            del properties_values[key]
    properties = {"properties": properties_values}


    with open("interbpcorr.json", "w", encoding="utf-8") as f:
        json.dump(properties, f)

    # Get the executable and engine form the config
    executable = biobb_block.config["executable_path"]

    # Copy inputs to the tmp folder
    for key, value in biobb_block.inputs.items():
        if value is not None:
            if Path(value).exists():
                abs_path_out = Path(value).absolute()
                abs_path_name = Path(Path(value).name).absolute()
                if not abs_path_name.samefile(abs_path_out):
                    shutil.copy(value, f"{Path(value).name}")

    # Call the docker biobb tool
    with subprocess.Popen(
        [
            executable,
            "run",
            "-v",
            ".:/tmp",
            "quay.io/biocontainers/biobb_dna:4.1.0--pyhdfd78af_0",
            "interbpcorr",
            "--config",
            "/tmp/interbpcorr.json",
            
            "--input_filename_shift",
            f"/tmp/{Path(input_filename_shift_value).name}",
            
            "--input_filename_slide",
            f"/tmp/{Path(input_filename_slide_value).name}",
            
            "--input_filename_rise",
            f"/tmp/{Path(input_filename_rise_value).name}",
            
            "--input_filename_tilt",
            f"/tmp/{Path(input_filename_tilt_value).name}",
            
            "--input_filename_roll",
            f"/tmp/{Path(input_filename_roll_value).name}",
            
            "--input_filename_twist",
            f"/tmp/{Path(input_filename_twist_value).name}",
            
            
            "--output_csv_path",
            f"/tmp/{Path(output_csv_path_value).name}",
            
            "--output_jpg_path",
            f"/tmp/{Path(output_jpg_path_value).name}",
            
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    ) as process:
        if process.stdout is not None:
            for line in process.stdout:
                # printing anything inside the block action will
                # redirect the output to the Horus integrated terminal
                print(line)

        if process.stderr is not None:
            for line in process.stderr:
                print(line)

        process.wait()

        if process.returncode != 0:
            # Raising an exception inside the block action will display the block as with an error,
            # and will display the error inside the block
            raise Exception(
                process.stderr
                if process.stderr
                else "An error ocurred while running the flow"
            )


        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_csv_path_value).absolute()
        abs_path_name = Path(Path(output_csv_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_csv_path_value).name}", output_csv_path_value)
        biobb_block.setOutput("output_csv_path", output_csv_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_jpg_path_value).absolute()
        abs_path_name = Path(Path(output_jpg_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_jpg_path_value).name}", output_jpg_path_value)
        biobb_block.setOutput("output_jpg_path", output_jpg_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_filename_shift)

inputs_list.append(input_filename_slide)

inputs_list.append(input_filename_rise)

inputs_list.append(input_filename_tilt)

inputs_list.append(input_filename_roll)

inputs_list.append(input_filename_twist)


outputs_list.append(output_csv_path)

outputs_list.append(output_jpg_path)


variables_list.append(sequence)

variables_list.append(seqpos)

variables_list.append(remove_tmp)

variables_list.append(restart)


interbpcorr_block = PluginBlock(
    # The name which will appear on the frontend
    name="interbpcorr",
    # Its description
    description="Calculate correlation between all base pairs of a single sequence and for a single helical parameter.",
    # The action
    action=interbpcorr_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)