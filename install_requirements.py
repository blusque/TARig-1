def install(pkg):
    import subprocess
    import sys

    try:
        __import__(pkg.split('==')[0])
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
    else:
        print(f"{pkg} is already installed.")

def read_requirements(file_path):
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    return [req.split('@')[0].strip() for req in requirements]

def install_requirements(file_path):
    requirements = read_requirements(file_path)
    print("Installing requirements...")
    print("Requirements:", requirements)
    for pkg in requirements:
        install(pkg)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python install_requirements.py <requirements_file>")
        sys.exit(1)
    requirements_file = sys.argv[1]
    install_requirements(requirements_file)