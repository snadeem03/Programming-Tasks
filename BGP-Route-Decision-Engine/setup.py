from cx_Freeze import setup, Executable

setup(
    
    name="BGP Route Decision Engine",
    version="1.0",
    description="BGP Route Decision Engine - prototype of BGP routers",
    executables=[Executable("bgp-route-finder.py")],
)