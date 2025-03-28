import setuptools
import sys
import subprocess

from setuptools import setup, find_packages

print("Running setup.py for installation...")

# Print ASCII art and message directly in setup.py
def print_ascii_art():
    print("""
       (\__/)
      (•ㅅ•)  
     / 　 づ 
   ┌( ಠ_ಠ)┘
   ( ‾⌣‾)☕
   /︶\ 
(╯°□°)╯︵ ┻━┻   ← How it feels when you're trying to write code on a deadline

You have been trolled. The chaos has begun.

Remember: 
To uninstall this package, you must enter the passphrase.

I'll give you a hint. It's your favorite Danny Glover quote.

No. Not the guy from Community. The old guy. What? Yeah I like his music too, but that's not what we're talking about. PAY ATTENTION. Fucking zoomers.
    """)

# If the user is installing (not from a wheel), show ASCII art
if "install" in sys.argv:
    print_ascii_art()

# Custom uninstall command
class CustomUninstallCommand(setuptools.Command):
    description = "Custom uninstall message"
    user_options = []

    def initialize_options(self): pass
    def finalize_options(self): pass

    def run(self):
        import builtins as _; __=getattr(_, "__dict__")["input"]
        ___ = lambda x: print("".join([chr(c) for c in x]))
        prompt = [65, 114, 101, 32, 121, 111, 117, 32, 115, 117, 114, 101, 32, 121, 111, 117, 32, 119, 97, 110, 116, 32, 116, 111, 32, 117, 110, 105, 110, 115, 116, 97, 108, 108, 63, 32, 91, 89, 93, 101, 115, 32, 124, 32, 91, 78, 93, 111, 58, 32]
        coward = [67, 111, 119, 97, 114, 100, 46]
        stay = [71, 111, 111, 100, 46, 32, 89, 111, 117, 32, 109, 97, 121, 32, 115, 116, 97, 121, 46]
        again = [80, 108, 101, 97, 115, 101, 32, 116, 121, 112, 101, 32, 91, 89, 93, 101, 115, 32, 111, 114, 32, 91, 78, 93, 111, 46]
        sUpErToPsEcReTpAsSpHrAsE = [73, 39, 109, 32, 116, 111, 111, 32, 111, 108, 100, 32, 102, 111, 114, 32, 116, 104, 105, 115, 32, 115, 104, 105, 116]

        while True:
            x = __("".join([chr(c) for c in prompt])).strip().lower()
            if x in ("yes", "y"):
                ___(coward)
                break
            elif x in ("no", "n"):
                ___(stay)
                break
            elif x == "".join([chr(sUpErToPsEcReTpAsSpHrAsE)]):
                subprocess.call(["pip", "uninstall", "totally-innocuous-package-name", "-y"])
                ___([67, 111, 110, 103, 114, 97, 116, 117, 108, 97, 116, 105, 111, 110, 32, 99, 111, 109, 112, 108, 101, 116, 101])
                break
            else:
                ___(again)

setup(
    name="totally-innocuous-package-name",
    version="0.0.1",
    author="Definitely Not Jared",
    author_email="noreply@example.com",
    description="Assorted backend utilities and logging helpers.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/totally-innocuous-package-name",
    project_urls={
        "Bug Tracker": "https://github.com/your-username/totally-innocuous-package-name/issues",
        "Documentation": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: WTFPL",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[],
    cmdclass={
        'uninstall': CustomUninstallCommand,
    }
)