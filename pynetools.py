#!/usr/bin/python3

try:
    import pyfiglet
except ImportError:
    pass
import subprocess
import argparse
import os

def download(tool: str, path: str) -> subprocess.CompletedProcess:
    BASE = ['git', 'clone', '-b', 'release']
    name = tool.split("/")[-1]
    path = [path+"/"+name]
    url = ["https://www.github.com/"+tool]
    cmd = BASE+url+path
    return subprocess.run(cmd)

def main(args):
    print(TITLE)

    TOOLS = []

    with open("config/TOOLS.conf", "r") as file:
        config = file.readlines()
    for tool in config:
        TOOLS.append(tool.strip())

    # Install All Tools
    if args.ALL:
        for tool in TOOLS:
            download(tool, args.path)

    # Install Selected Tools
    if not args.ALL:
        if args.pyne:
            download('hoplite-consulting/pyne', args.path)
        if args.vulnage:
            download('hoplite-consulting/vulnage', args.path)
        if args.epss:
            download('hoplite-consulting/epss-cli', args.path)

    # Update Tools
    # if args.Update:
    #     pass
    
    # Install Tools
    try:
        os.listdir(args.path)
    except FileNotFoundError:
        print("Tools Directory Not Found")
        exit()
    for tool in os.listdir(args.path):
        cmd = ['pip3', 'install', '-r', args.path+"/"+tool+"/requirements.txt"]
        subprocess.run(cmd)

if __name__ == "__main__":
    
    __version__ = "1.0.0"
    NAME = "PyneTools"
    DESCRIPTION = "An installer and updater for the collection of tools that work well with the Pyne Nessus Parser."
    try:
        TITLE = pyfiglet.figlet_format(NAME, font="stop") + f"\n{NAME} {__version__}\n\n{DESCRIPTION}\n"
    except:
        TITLE = f"{NAME} {__version__}\n\n{DESCRIPTION}\n"

    parser = argparse.ArgumentParser(description=f"{TITLE}", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('path', help='path to store tools')
    # parser.add_argument('-U', '--Update', action='store_true', help='update installed tools') # Need to to more work for this, use list input for specific tools to update? Force all tools to be updated?
    parser.add_argument('-A', '--ALL', action='store_true', help='install all tools')
    parser.add_argument('--pyne', action='store_true', help='install pyne')
    parser.add_argument('--vulnage', action='store_true', help='install vulnage')
    parser.add_argument('--epss', action='store_true', help='install epss cli')
    args = parser.parse_args()

    main(args)