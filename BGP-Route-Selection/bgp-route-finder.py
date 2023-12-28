def findBestRoute(route1,route2):
    
    # check for the local preferences
    if route1['local_preference']>route2['local_preference']:
        return route1
    elif route1['local_preference']<route2['local_preference']:
        return route2
    else :
        # check for the AS_PATH
            
        if len(route1['as_path']) > len(route2['as_path']):
            return route2
        elif len(route1['as_path']) < len(route2['as_path']):
            return route1
        else :
            return route1
            



if __name__=='__main__':
    
    route1_info={
        'prefix':'192.168.1.0/24',
        'as_path': [100, 200],
        'next_hop': '10.0.0.1',
        'local_preference': 200
    }    
    
    route2_info={
        'prefix': '192.168.1.0/24',
        'as_path': [200],
        'next_hop': '10.0.0.2',
        'local_preference': 200
    }
    
    print(findBestRoute(route1_info, route2_info))