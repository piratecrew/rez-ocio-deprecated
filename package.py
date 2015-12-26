name = "ocio"

version = "1.0.9"

description = \
    """
    Open Color IO
    """

variants = [
    ["platform-linux"]
]

requires = [
    "python"
]

uuid = "repository.ocio"

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
