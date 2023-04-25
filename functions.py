from colors import * #import all from colors.py module
import os
import sys

#The split method return an array with the head and the tail of the path
path= os.path.split(os.path.realpath(__file__))[0]
file_name = os.path.split(os.path.realpath(__file__))[1]


if os.path.exists(path+"/modules/bashrc.py"): 
    from modules import bashrc 
    enabled_modules=["bashrc"]
if os.path.exists(path+"/modules/docker.py"):
    from modules import docker
    enabled_modules+=["docker"]
if os.path.exists(path+"/modules/git.py"):
    from modules import git
    enabled_modules+=["git"]

#List of available modules
available_modules=["apt", "bashrc","docker","git"]

#Manager Function 
def help():
    print("[cli, modules, help, version]")
    print("[system, users, network, filesystem, packet]")
    print("[docker, baschrc]")
def show_modules():
    print("MODULES")
    for module in available_modules:
      if module in enabled_modules:
          print(GREENBOLD, "[+]",module)
      else:
          print(REDBOLD, "[-]", module)
def show_version():
    print("v0.1")

def funzione1(argn, argw):
    if len(sys.argv) > argn: #compare the lenght of array with the number of input!!!
        if sys.argv[argn] == argw:
          return True

#Commands Function  
def user_commands():
    print(REDBOLD, "Users")
    print(WHITE, "finger <user>", WHITE, " - ")
    print(WHITEBOLD, "id <user>", WHITE,"- Print real and effective user and group IDs")
    print(WHITEBOLD, "last", WHITE, " - ")
    print(WHITEBOLD, "who", WHITE, "-")
    print(WHITEBOLD, "whoami", WHITE, " - ")
    print(WHITEBOLD, "rwho", WHITE, "-")
def network_commands():
    print(REDBOLD, "Network")
    print(WHITEBOLD, "host", WHITE, " - ")
    print(WHITEBOLD, "ip addr", WHITE, " - ")
    print(WHITEBOLD, "netstat -pnltu", WHITE, "- Listening port")
    print(WHITEBOLD, "nmap <host>", WHITE, " - ")
    print(WHITEBOLD, "ping <host>", WHITE, "- ")
    print(WHITEBOLD, "whois <host>", WHITE, "- ")   
def filesystem_commands():
    print(REDBOLD, "File System")
    print(WHITEBOLD, "cat", WHITE, " - ")
    print(WHITEBOLD, "cp", WHITE, " - ")
    print(WHITEBOLD, "cd", WHITE, " - ")
    print(WHITEBOLD, "find /path/ -type f -name file-to-search", WHITE, " - ")
    print(WHITEBOLD, "mkdir", WHITE, " - ")
    print(WHITEBOLD, "nano", WHITE, " - ")
    print(WHITEBOLD, "pwd", WHITE, " - ")
    print(WHITEBOLD, "rm", WHITE, " - ")
def system_commands():
    print(REDBOLD, "System")
    print(WHITEBOLD, "hostaname - Show or set the system's host name ")
    print(WHITEBOLD, "uname - Print system information")
    print(WHITEBOLD, "uptime")