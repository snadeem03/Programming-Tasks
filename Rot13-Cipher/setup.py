from cx_Freeze import setup, Executable

setup(
    
    name="Rot13Cipher",
    version="1.0",
    description="Rot13Cipher - A rot13 encrypt/decrypt tool",
    executables=[Executable("rot13_cipher.py")],
)