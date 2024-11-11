import os


def setup_library_management_system():
    # Step 1: Change the directory to C:\
    os.chdir("C:\\")

    # Step 2: Check if 'library-management-system' folder exists
    if os.path.exists("library-management-system"):
        print("The folder 'library-management-system' already exists. If reinstalling, please delete this directory.")
        return

    # Step 3: Clone the repository
    clone_command = "git clone https://github.com/mursalatul/library-management-system.git"
    if os.system(clone_command) != 0:
        print("Failed to clone the repository.")
        return

    # Step 4: Change directory to 'library-management-system'
    os.chdir("library-management-system")

    # Step 5: Create a Python environment with conda and Python 3.9
    env_command = "conda create -y -n library-env python=3.9"
    if os.system(env_command) != 0:
        print("Failed to create the conda environment.")
        return

    # Step 6: Activate the environment and install requirements
    activate_env_command = "conda activate library-env"
    install_requirements_command = "pip install -r requirements.txt"
    if os.system(f"{activate_env_command} && {install_requirements_command}") != 0:
        print("Failed to install requirements.")
        return

    print("Library Management System setup completed successfully.")


# Run the setup function
setup_library_management_system()
