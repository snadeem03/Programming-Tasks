import math

def schedule_vms(vms, hosts):
    formatted_vms = [(idx, vm['CPU'] + vm['memory'] + vm['storage']) for idx, vm in enumerate(vms, start=1)]
    sorted_vms = sorted(formatted_vms, key=lambda x: x[1], reverse=True)
    
    formatted_hosts = [(idy, host['available_cpu'] + host['available_memory'] + host['available_storage']) for idy, host in enumerate(hosts, start=1)]
    sorted_hosts = sorted(formatted_hosts, key=lambda x: x[1], reverse=True)
    
    final_return_value = []
    vm_allocation = [False] * len(vms)
    
    for each_sorted_host in sorted_hosts:
        flag = 0  # Reset flag for each host
        
        for each_sorted_vm in sorted_vms:
            if not vm_allocation[flag] and vms[each_sorted_vm[0]-1]['CPU'] <= hosts[each_sorted_host[0]-1]['available_cpu'] and vms[each_sorted_vm[0]-1]['memory'] <= hosts[each_sorted_host[0]-1]['available_memory'] and vms[each_sorted_vm[0]-1]['storage'] <= hosts[each_sorted_host[0]-1]['available_storage']:
                
                final_return_value.append((each_sorted_vm[0], hosts[each_sorted_host[0]-1]['id']))
                
                hosts[each_sorted_host[0]-1]['available_cpu'] -= vms[each_sorted_vm[0]-1]['CPU']
                hosts[each_sorted_host[0]-1]['available_memory'] -= vms[each_sorted_vm[0]-1]['memory']
                hosts[each_sorted_host[0]-1]['available_storage'] -= vms[each_sorted_vm[0]-1]['storage']
                
                vm_allocation[flag] = True
                
            flag += 1  # Increment flag for next iteration
    
    return final_return_value
                



if __name__=='__main__':
    pass
    # Call the function here by providing the arguments
    

