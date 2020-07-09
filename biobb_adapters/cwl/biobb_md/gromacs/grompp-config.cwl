#cwlVersion: v1.0
type: record
name: GromppConfig
doc: "JSON configuration for invoking Grompp building block"
fields:
    input_mdp_path:
        type: string?
        doc: "Path of the input MDP file."
    mdp:
        doc: "MDP options specification. (Used if *input_mdp_path* is null)"
        s:url: "http://manual.gromacs.org/2020-current/user-guide/mdp-options.html"
        type:
            type: record
            name: MDPOptions
            fields:
                include:
                    type: string?
                    doc: "directories to include in your topology. Format: -I/home/john/mylib -I../otherlib"
                define:
                    type: string?
                    doc: |-
                      defines to pass to the preprocessor, default is no defines. 
                      You can use any defines to control options in your 
                      customized topology files. Options that act on 
                      existing top file mechanisms include:
                
                      -DFLEXIBLE will use flexible water instead of rigid 
                      water into your topology, this can be useful for normal mode analysis.
                
                      -DPOSRES will trigger the inclusion of posre.itp into 
                      your topology, used for implementing position restraints.
                integrator:
                    type: 
                        type: enum
                        name: GrompIntegrator
                        symbols: [md, md-vv, md-vv-avek, sd, bd, steep, cg, l-bfgs, nm, tpi, tpic, mimic]
                        doc: |-
                            Despite the name, this list includes algorithms that are not 
                            actually integrators over time. integrator=steep and all 
                            entries following it are in this category
                #.. 
            ## TODO: Document all of the fields of mdp file 
            ## http://manual.gromacs.org/2020-current/user-guide/mdp-options.html
            ## but as they are expected by biobb in JSON variant:
    type:
        doc: "Default options for the mdp file. Valid values: minimization, nvt, npt, free, index"
        #default: "minimization"
        type:
          - "null"
          - type: enum
            symbols: [minimization, nvt, npt, free, index]
    output_mdp_path:
        type: string?
        #default: "grompp.mdp"
        doc: "Path of the output MDP file."
    output_top_path:
        type: string?
        #default: "grompp.top"
        doc: "Path the output topology TOP file."
    maxwarn:
        type: int?
        #default: 10
        doc: "Maximum number of allowed warnings."
    gmx_path:
        type: string?
        #default: "gmx"
        doc: "Path to the GROMACS executable binary"
    remove_tmp:
        type: boolean?
        #default: true
        doc: "[WF property] Remove temporal files."
    restart:
        type: boolean?
        #default: false
        doc: "[WF property] Do not execute if output files exist."
    container_path:
        type: string?
        doc: "Path to the binary executable of your container."
    container_image:
        type: string?
        #default: "gromacs/gromacs:latest"
        doc: "Container Image identifier to execute gromacs from"
    container_volume_path:
        type: string?        
        #default: "/data"
        doc: "Path to an internal directory in the container."
    container_working_dir:
        type: string?
        doc: "Path to the internal CWD in the container."
    container_user_id:
        type: string?
        doc: "User number id to be mapped inside the container."
    container_shell_path:
        type: string?
        #default: "/bin/bash"
        doc: "Path to the binary executable of the container shell."

s:url: "https://biobb-md.readthedocs.io/en/latest/gromacs.html#module-gromacs.grompp"

$namespaces:
  s: http://schema.org/

$schemas:
- http://schema.org/version/latest/schema.rdf
