from cx_Freeze import setup, Executable

setup(
    
    name="CaesarCipher",
    version="1.0",
    description="Caesar Cipher - A encrypt/decrypt tool",
    executables=[Executable("caesar_cipher.py")],
)