name = "ocio"

version = "1.0.9"

description = \
    """
    Open Color IO
    """

variants = [
    ["platform-linux", "python-2.7"]
]

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
    if building:
    	env.CMAKE_MODULE_PATH.append("{root}/cmake")
