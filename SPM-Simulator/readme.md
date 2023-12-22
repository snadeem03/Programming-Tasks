## Problem Statement : Simple Package Manager Simulator

### Background:
 You are tasked with creating a Simple Package Manager (SPM) simulator. This simulator allows users to install, uninstall, and list available packages.

### Requirements:
 1. Initialization :
  * Create a class named SimplePackageManager.
  * Initialize the class with two attributes:
   * available_packages: A dictionary containing available packages with their descriptions.
   * installed_packages: A list to store installed packages.
 
 2. Functionalities :
  * get_packages(): Display available and installed packages.
  * install_package(package_name): Install a specified package. Display appropriate messages based on the installation status.
  * uninstall_package(package_name): Uninstall a specified package. Display appropriate messages based on the uninstallation status.

 3. User Interface :
  * Implement a start method to interact with users.
  * Display available commands to the user: install <package_name>, uninstall <package_name>, list, and exit.
  * Process user commands and execute corresponding methods.

 4. Command Handling:
  * Handle incorrect commands gracefully by displaying appropriate messages.
  * Validate package names entered by the user before performing installation or uninstallation.

 5. Simulate Installation/Uninstallation:
  * Use time delays (simulated with time.sleep()) to mimic package installation and uninstallation processes.


### Instructions :
 1. Create a Python class named SimplePackageManager.
 2. Implement methods to display available and installed packages, install packages, and uninstall packages.
 3. Develop a user interface to accept commands and interact with the package manager.
 4. Ensure that the simulator can handle incorrect commands and validate package names.
 5. Use time delays to simulate the installation and uninstallation processes.
 6. Test the simulator by running it and executing various commands like installing packages, uninstalling packages, listing packages, and exiting the simulator.

 