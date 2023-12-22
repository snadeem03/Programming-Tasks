import time as t


class SimplePackageManager:
    
    # initilaizes the variables 
    def __init__(self):
        
        # these are the packages that can be installed using SPM , contains name and description
        self.available_packages={
            "Git" : "A version control system",
            "Nano" : "A simple text editor",
            "whatsapp": "A chatting app"
        }
        
        # these are the installed packages # storing in a list 
        self.installed_packages=[]
        
    # fetching the installed packages and the available packages
    def get_packages(self):
        print("\n Available Packages : \n")
        
        for id,(name,description) in enumerate(self.available_packages.items(),start=1):
            print(f"{id} - {name} - {description}")
            
            
        print("\n Installed Packages : \n")
        
        if len(self.installed_packages)==0:
            print("- None")
            
        else :
            for package in self.installed_packages:
                print(f" - {package}")
                
    def install_package(self,package_name):
        
        print("Checking the availability of the package.....")
        t.sleep(2)
        
        
        if package_name in self.installed_packages:
            print(f"package {package_name} already installed")
        else :
            print(f"Collecting  wheel for the package {package_name}....")
            t.sleep(2)
            print(f"Getting things ready !!")
            t.sleep(2)
            
            self.installed_packages.append(package_name)
            print(f"Package '{package_name}' installed successfully!")	
            
    def uninstall_package(self,package_name):
        print("Checking the configurations of the package ... ")
        t.sleep(2)
        
        if package_name in self.installed_packages:
            print("Gathering dependencies...")
            t.sleep(2)
            print("Getting things ready !!")
            t.sleep(2)
            
            self.installed_packages.remove(package_name)
            print(f"Package '{package_name}' uninstalled successfully!")
        else :
            print(f"package {package_name} is not installed")
            
    def start(self):
        print("Welcome to Simple Package Manager Simulator!")
        
        print("Available Commands: \n - install <package_name> \n - uninstall <package_name> \n - list \n - exit")
        
        while True:
            command=input()
            command_dissector_results=command.split()
            
            if len(command)==0:
                print("Command not found !!")
            
            if command_dissector_results[0]=='install' and len(command_dissector_results)==2:
                if command_dissector_results[1]=='Git' or command_dissector_results[1]=='Nano' or command_dissector_results[1]=='Whatsapp':
                    self.install_package(command_dissector_results[1])
                else :
                    t.sleep(1)
                    print("Package not found!!")
                    
                    
            if command_dissector_results[0]=='uninstall' and len(command_dissector_results)==2:
                if command_dissector_results[1]=='Git' or command_dissector_results[1]=='Nano' or command_dissector_results[1]=='Whatsapp':
                    self.uninstall_package(command_dissector_results[1])
                else :
                    t.sleep(1)
                    print("Package not found!!")
                    
                    
            if command_dissector_results[0]=='list':
                
                print('Fetching packages....')
                t.sleep(2)
                
                self.get_packages()
            if command_dissector_results[0]=='exit':
                break
            
            
            if command_dissector_results[0]!='install' and command_dissector_results[0]!='uninstall' and command_dissector_results[0]!='list' and command_dissector_results[0]!='exit':
                print("Command not found!!")
                
                




manager=SimplePackageManager()
    
manager.start()
            

        