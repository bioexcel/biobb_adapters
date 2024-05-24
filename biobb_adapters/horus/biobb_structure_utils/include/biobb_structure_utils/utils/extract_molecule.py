# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_structure_path = PluginVariable(
    id="input_structure_path",  # ID of the variable, will allow us to identify the value
    name="input_structure_path",  # The name that will appear in the frontend
    description="Input structure file path",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb', 'pdbqt']
)


output_molecule_path = PluginVariable(
    id="output_molecule_path",  # ID of the variable, will allow us to identify the value
    name="output_molecule_path",  # The name that will appear in the frontend
    description="Output molecule file path",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb', 'pdbqt']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

molecule_type = PluginVariable(
    id="molecule_type",
    name="molecule_type",
    description="type of molecule to be extracted. If all, only waters and ligands will be removed from the original structure. ",
    type=VariableTypes.STRING
)

chains = PluginVariable(
    id="chains",
    name="chains",
    description="if chains selected in **molecule_type**, specify them here, e.g: ['A', 'C', 'N'].",
    type=VariableTypes.STRING
)

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description="path to the check_structure application",
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
def extract_molecule_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_structure_path_value = biobb_block.inputs["input_structure_path"]
    
    
    output_molecule_path_value = biobb_block.inputs["output_molecule_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["molecule_type"] = biobb_block.variables["molecule_type"]
    
    properties_values["chains"] = biobb_block.variables["chains"]
    
    properties_values["binary_path"] = biobb_block.variables["binary_path"]
    
    properties_values["remove_tmp"] = biobb_block.variables["remove_tmp"]
    
    properties_values["restart"] = biobb_block.variables["restart"]
    
    for key in list(properties_values.keys()):
        if properties_values[key] is None:
            del properties_values[key]
    properties = {"properties": properties_values}


    with open("extract_molecule.json", "w", encoding="utf-8") as f:
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
            "quay.io/biocontainers/biobb_structure_utils:4.1.0--pyhdfd78af_0",
            "extract_molecule",
            "--config",
            "/tmp/extract_molecule.json",
            
            "--input_structure_path",
            f"/tmp/{Path(input_structure_path_value).name}",
            
            
            "--output_molecule_path",
            f"/tmp/{Path(output_molecule_path_value).name}",
            
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
        abs_path_out = Path(output_molecule_path_value).absolute()
        abs_path_name = Path(Path(output_molecule_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_molecule_path_value).name}", output_molecule_path_value)
        biobb_block.setOutput("output_molecule_path", output_molecule_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_structure_path)


outputs_list.append(output_molecule_path)


variables_list.append(molecule_type)

variables_list.append(chains)

variables_list.append(binary_path)

variables_list.append(remove_tmp)

variables_list.append(restart)


extract_molecule_block = PluginBlock(
    # The name which will appear on the frontend
    name="extract_molecule",
    # Its description
    description="This class is a wrapper of the Structure Checking tool to extract a molecule from a 3D structure.",
    # The action
    action=extract_molecule_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)