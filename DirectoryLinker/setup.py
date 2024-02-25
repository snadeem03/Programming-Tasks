from cx_Freeze import setup, Executable


setup(
    
    name="SymLink Mason",
    version="1.0",
    description="Seamlessly connect files",
    executables=[Executable("identification_links.py")],
    
)