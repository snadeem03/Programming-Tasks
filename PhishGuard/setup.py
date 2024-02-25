from cx_Freeze import setup, Executable


setup(

    name="PhishGuard",
    version="1.0",
    description="PhishGuard - A simple phishing detection tool",
    executables=[Executable("phishingTracker.py")],
)