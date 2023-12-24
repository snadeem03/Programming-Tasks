# Virtual Machine Scheduler

## Problem Statement : 
 we are tasked with designing a virtual machine scheduler that efficiently allocates Virtual Machines (VMs) to host machines based on their specific resource requirements. Each VM has distinct CPU, memory, and storage requirements, while each host machine provides limited capacities for these resources. The goal is to maximize resource utilization across host machines and ensure that no machine is overloaded.

## Background :
 Virtual Machines (VMs) are software-based emulations of physical computers that run on a host machine. They enable efficient resource utilization, scalability, and flexibility across various computing environments. In a real-world scenario, VMs are essential for server consolidation, development/testing environments, legacy application support, disaster recovery, and cloud computing.

## Requirements :
 * Python 3.x environment
 * Basic understanding of python data structures
 * Familiarity with algorithms related to resource allocation and utilization

## Functionalities :
 * VM Representation : Each VM is represented as a dictionary containing unique identifiers (id), CPU requirements (cpu), memory requirements (memory), and storage requirements (storage).

 * Host machine representation : Each host machine is represented as a dictionary containing unique identifiers (id), available CPU capacity (available_cpu), available memory capacity (available_memory), and available storage capacity (available_storage).

 * Resource allocation : Implement a function schedule_vms(vms, hosts) that efficiently allocates VMs to host machines based on their resource requirements while considering the available capacities of host machines.

## Instructions :
 1. Input : Provide the function schedule_vms(vms, hosts) with two lists:
  * vm's : A list of dictionaries representing VMs with specified CPU, memory, and storage requirements.
  * hosts : A list of dictionaries representing host machines with available CPU, memory, and storage capacities.

 2. Output : The function should return a list of tuples (vm_id, host_id) indicating the allocation of VMs to host machines. Ensure that each VM is allocated to a suitable host machine that meets its resource requirements without overloading the machine.

 3. Constraints : Each VM can be allocated to only one host machine.Ensure that the allocated VMs do not exceed the available resources of the host machines.

 4. Optimization : Aim to maximize resource utilization across host machines by efficiently allocating VMs based on their specific requirements and available host resources.

 
