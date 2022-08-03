#!/usr/bin/python3

try:
    import pyfiglet
except ImportError:
    pass
import subprocess
import argparse
import os

# Git Clone Tools
def download(tool: str, path: str) -> subprocess.CompletedProcess:
    BASE = ['git', 'clone', '-b', 'release'] # -b release : Clones the branch named 'release' : This will be changed to the master branch after an internal CI/CD Update
    name = tool.split("/")[-1]
    path = [path+"/"+name]
    url = ["https://www.github.com/"+tool]
    cmd = BASE+url+path
    return subprocess.run(cmd)

# Install Tool Requierments (Only works for Python Tools)
def install():
    try:
        os.listdir(args.PATH)
    except FileNotFoundError:
        print("Tools Directory Not Found")
        exit()
    for tool in os.listdir(args.PATH):
        cmd = ['pip3', 'install', '-r', args.PATH+"/"+tool+"/requirements.txt"]
        subprocess.run(cmd)

def main(args):
    print(TITLE)

    # Install All Tools
    if args.ALL:
        for tool in TOOLS:
            download(tool, args.PATH)
        install()
        exit()

    # Dynamically Install Selected Tools
    elif not args.ALL and not args.UPDATE:
        for tool in TOOLS:
            t = tool.split("/")[1].replace("-","_")
            c = getattr(args, t)
            if c:
                download(tool, args.PATH)
        install()
        exit()

    # Update Tools
    elif not args.ALL and args.UPDATE:
        try:
            s = os.listdir(args.PATH)
        except FileNotFoundError:
            print("Tools Directory Not Found")
            exit()
        for tool in os.listdir(args.PATH):
            os.chdir(args.PATH+"/"+tool)
            cmd = ['git', 'pull']
            subprocess.run(cmd)

if __name__ == "__main__":
    
    __version__ = "2.0.0"
    NAME = "PyneTools"
    DESCRIPTION = "An installer and updater for the collection of tools that work well with the Pyne Nessus Parser."
    try:
        TITLE = pyfiglet.figlet_format(NAME, font="stop") + f"\n{NAME} {__version__}\n\n{DESCRIPTION}\n"
    except:
        TITLE = f"{NAME} {__version__}\n\n{DESCRIPTION}\n"
    TOOLS = []

    parser = argparse.ArgumentParser(description=f"{TITLE}", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('PATH', help='path to store tools')
    parser.add_argument('-A', '--ALL', action='store_true', help='install all tools')
    parser.add_argument('-U', '--UPDATE', action='store_true', help='update installed tools (this will update ALL tools)') # Need to to more work for this, use list input for specific tools to update? Force all tools to be updated?

    # Get Tools from Config
    with open("config/TOOLS.conf", "r") as file:
        config = file.readlines()
    for tool in config:
        TOOLS.append(tool.strip())

    # Dynamically Create Install Arguments for each Tool
    for tool in TOOLS:
        t = tool.split('/')[-1]
        a = '--' + t
        h = 'install ' + t
        parser.add_argument(a, action='store_true', help=h)
    
    args = parser.parse_args()

    main(args)