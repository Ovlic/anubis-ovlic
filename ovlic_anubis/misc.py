import sys
import subprocess

def update():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'git+https://github.com/Ovlic/anubis-ovlic'])
    return