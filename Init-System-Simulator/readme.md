# Simple Init System Simulator


## Problem statement 
 Develop a Python-based simulator to mimic the functionalities of a simplified init system. This system will focus on managing services, their dependencies, and ensuring proper service start-up and shutdown sequences.

## Background
 An init system is responsible for initializing system services during boot-up, managing their lifecycle, and handling dependencies between services. This project will simulate these functionalities in a simplified Python environment.

## Requirements
 * Python 3.x installed on your system.
 * Basic understanding of Python classes and object-oriented programming concepts.

## Functionalities
 * Service definition : Define services with their names, dependencies, and statuses.
 * Service management : 
  * Start a service ensuring all its dependencies are met.
  * Stop a service if no other services depend on it.
 * Dependency management : Manage dependencies between services and ensure they start in the correct sequence.
 * Command Line Interface : Provide commands to interact with the init system, such as starting or stopping services and listing their statuses.

## Instructions
 * Add services :  Within the simulator, you can add services with their respective dependencies.
 * Start Services : Use the provided commands to start services. The system will automatically handle dependencies and ensure services start in the correct order.
 * Stop services : Similarly, use commands to stop services. The system will ensure services stop if no other services depend on them.
 * List services : Use the list command to display all services and their current statuses.

