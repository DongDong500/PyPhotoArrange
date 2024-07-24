# PyPhotoArrange
photo arrangement program in python

## Creating executable (exe) from python script using PyInstaller

This guide will walk you through the steps to convert a Python script into an executable (.exe) file using PyInstaller.

### Prerequisites

Make sure you have Python installed on your system. Additionally, ensure that you have installed PyInstaller, which is a Python package that bundles a Python application and its dependencies into a single package.

```
pip install pyinstaller
```

### Steps

1. Navigate to your python script

Open a terminal or command prompt and navigate to the directory where your Python script (your_script.py) is located.

```
cd path/to/your/script/directory
```

2. Create executable

Use PyInstaller to create the executable file. PyInstaller supports various options to customize the packaging process. For a simple executable, use the --onefile option.

```
pyinstaller --onefile your_script.py
```

- `--onefile` generates a single bundled executable file.
- `--add-data` includes additional files (data files or configuration files) which are dependent on your script.

3. Locate the executable

After PyInstaller finishes its job, it will create a dist directory in your script's directory. Inside the dist directory, you will find the generated executable file (your_script.exe on Windows).