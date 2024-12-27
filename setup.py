from setuptools import setup, find_packages

setup(
    name="cycle-animation",  # The name of your package
    version="0.1",           # The version of your package
    packages=find_packages(),  # Automatically find all the packages
    scripts=['cycle/cycle.sh'],  # Add your Bash script as an executable
    entry_points={
        'console_scripts': [
            'cycle = cycle.cycle:main',  # We'll create the 'main' function in Python
        ],
    },
    install_requires=[],  # Add any Python packages your program needs here
    python_requires='>=3.6',  # This specifies the minimum Python version required
)

