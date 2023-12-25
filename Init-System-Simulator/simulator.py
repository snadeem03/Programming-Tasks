class Service:
    def __init__(self, name, dependencies=None):
        self.name = name
        self.dependencies = dependencies if dependencies else []
        self.status = "STOPPED"
    
    def start(self):
        for dependency in self.dependencies:
            if dependency.status != "STARTED":
                print(f"Cannot start {self.name} because {dependency.name} is not started.")
                return
        self.status = "STARTED"
        print(f"Started {self.name}")

    def stop(self):
        for service in service_list:  # Assuming service_list contains all services
            if self.name in service.dependencies and service.status == "STARTED":
                print(f"Cannot stop {self.name} because {service.name} depends on it.")
                return
        self.status = "STOPPED"
        print(f"Stopped {self.name}")


class InitSystem:
    def __init__(self):
        self.services = {}
        # To store service instances for dependency resolution
        self.service_instances = {}

    def add_service(self, name, dependencies=None):
        new_service = Service(name, dependencies)
        self.services[name] = new_service
        self.service_instances[name] = new_service

    def start_service(self, service_name):
        if service_name in self.services:
            self.service_instances[service_name].start()
            for dependency in self.service_instances[service_name].dependencies:
                self.start_service(dependency.name)
        else:
            print(f"No service named {service_name} found.")

    def stop_service(self, service_name):
        if service_name in self.services:
            self.service_instances[service_name].stop()
        else:
            print(f"No service named {service_name} found.")

    def list_services(self):
        for service_name, service in self.services.items():
            print(f"Service: {service_name}, Status: {service.status}")


# Example usage:
init_system = InitSystem()

# Add services with dependencies
init_system.add_service("C")
init_system.add_service("B", [init_system.service_instances["C"]])
init_system.add_service("A", [init_system.service_instances["B"]])

# Start Service A
init_system.start_service("A")
init_system.list_services()

# Stop Service B
init_system.stop_service("B")
init_system.list_services()
