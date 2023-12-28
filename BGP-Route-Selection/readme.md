# BGP Route Selection Challenge

## Problem statement : This challenge revolves around simulating a simplified Border Gateway Protocol (BGP) route selection algorithm. Given two routes from two different Autonomous Systems (ASes), your task is to determine the best route based on specific BGP route attributes.

## Background
 BGP is the standard protocol for exchanging routing information between different Autonomous Systems on the Internet. Each BGP route comes with attributes that help in route selection when there are multiple paths to the same destination.

 ### Attributes to consider 
 * prefix : The destination IP network (e.g., 192.168.1.0/24).
 * AS_PATH :  The sequence of Autonomous System numbers the route has traversed.
 * Next hop : The IP address of the next-hop router.
 * Local preference : A preference value indicating the route's desirability (higher values are preferred).

## Task Description
 Given two routes from two ASes, implement a function that decides the best path to a destination network based on the following criteria:

 1. Local Preference : Prefer the route with the higher Local Preference value.
 2. AS_PATH_LENGTH : If the Local Preference values are the same, prefer the route with the shortest AS_PATH (fewest AS hops).
 3. Equal criteria :  If both Local Preference and AS_PATH length are the same for both routes, choose any route.


## Input format 
 The function will receive two route objects, each representing a route from an AS, in the following format:

        route1 = {
    'prefix': '192.168.1.0/24',
    'as_path': [100, 200],
    'next_hop': '10.0.0.1',
    'local_preference': 200
        }

        route2 = {
    'prefix': '192.168.1.0/24',
    'as_path': [200],
    'next_hop': '10.0.0.2',
    'local_preference': 150
        }

## Output format 
 Return the best route (either from AS100 or AS200) based on the defined criteria. If both routes are equally good, the function can return either route.