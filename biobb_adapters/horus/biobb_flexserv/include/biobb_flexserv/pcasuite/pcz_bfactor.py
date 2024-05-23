# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_pcz_path = PluginVariable(
    id="input_pcz_path",  # ID of the variable, will allow us to identify the value
    name="input_pcz_path",  # The name that will appear in the frontend
    description='Input compressed trajectory file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pcz']
)


output_dat_path = PluginVariable(
    id="output_dat_path",  # ID of the variable, will allow us to identify the value
    name="output_dat_path",  # The name that will appear in the frontend
    description='Output Bfactor x residue x PCA mode file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['dat', 'txt', 'csv']
)

output_pdb_path = PluginVariable(
    id="output_pdb_path",  # ID of the variable, will allow us to identify the value
    name="output_pdb_path",  # The name that will appear in the frontend
    description='Output PDB with Bfactor x residue x PCA mode file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description='pczdump binary path to be used.',
    type=VariableTypes.STRING
)

eigenvector = PluginVariable(
    id="eigenvector",
    name="eigenvector",
    description='PCA mode (eigenvector) from which to extract bfactor values per residue (0 means average over all modes).',
    type=VariableTypes.INTEGER
)

pdb = PluginVariable(
    id="pdb",
    name="pdb",
    description='Generate a PDB file with the computed bfactors (to be easily represented with colour scale)',
    type=VariableTypes.BOOLEAN
)

remove_tmp = PluginVariable(
    id="remove_tmp",
    name="remove_tmp",
    description='Remove temporal files.',
    type=VariableTypes.BOOLEAN
)

restart = PluginVariable(
    id="restart",
    name="restart",
    description='Do not execute if output files exist.',
    type=VariableTypes.BOOLEAN
)

# Define the action that the block will perform
def pcz_bfactor_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_pcz_path_value = biobb_block.inputs["input_pcz_path"]
    
    
    output_dat_path_value = biobb_block.inputs["output_dat_path"]
    
    output_pdb_path_value = biobb_block.inputs["output_pdb_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["binary_path"] = biobb_block.variables["binary_path"]
    
    properties_values["eigenvector"] = biobb_block.variables["eigenvector"]
    
    properties_values["pdb"] = biobb_block.variables["pdb"]
    
    properties_values["remove_tmp"] = biobb_block.variables["remove_tmp"]
    
    properties_values["restart"] = biobb_block.variables["restart"]
    
    for key in list(properties_values.keys()):
        if properties_values[key] is None:
            del properties_values[key]
    properties = {"properties": properties_values}


    with open("pcz_bfactor.json", "w", encoding="utf-8") as f:
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
            "quay.io/biocontainers/biobb_flexserv:4.1.0--pypl5321hdfd78af_0",
            "pcz_bfactor",
            "--config",
            "/tmp/pcz_bfactor.json",
            
            "--input_pcz_path",
            f"/tmp/{Path(input_pcz_path_value).name}",
            
            
            "--output_dat_path",
            f"/tmp/{Path(output_dat_path_value).name}",
            
            "--output_pdb_path",
            f"/tmp/{Path(output_pdb_path_value).name}",
            
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
        abs_path_out = Path(output_dat_path_value).absolute()
        abs_path_name = Path(Path(output_dat_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_dat_path_value).name}", output_dat_path_value)
        biobb_block.setOutput("output_dat_path", output_dat_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_pdb_path_value).absolute()
        abs_path_name = Path(Path(output_pdb_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_pdb_path_value).name}", output_pdb_path_value)
        biobb_block.setOutput("output_pdb_path", output_pdb_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_pcz_path)


outputs_list.append(output_dat_path)

outputs_list.append(output_pdb_path)


variables_list.append(binary_path)

variables_list.append(eigenvector)

variables_list.append(pdb)

variables_list.append(remove_tmp)

variables_list.append(restart)


pcz_bfactor_block = PluginBlock(
    # The name which will appear on the frontend
    name="pcz_bfactor",
    # Its description
    description='Extract residue bfactors x PCA mode from a compressed PCZ file.',
    # The action
    action=pcz_bfactor_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)