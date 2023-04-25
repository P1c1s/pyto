from colors import * #import all from colors.py module
import os
import sys
if os.path.exists("functions.py"): 
    import functions 
if os.path.exists("bashrc.py"): 
    import bashrc 
    enabled_modules=["bashrc"]
if os.path.exists("docker.py"):
    import docker
    enabled_modules+=["docker"]
if os.path.exists("git.py"):
    import git
    enabled_modules+=["git"]

#Completed list of modules
co=["apt", "bashrc","docker","git"]

#List function manager
def show_modules():
    print("MODULES")
    for module in co:
      if module in enabled_modules:
          print(GREENBOLD, "[+]",module)
      else:
          print(REDBOLD, "[-]", module)

def show_version():
    print("v0.1")

def a():
    print("s")

def funzione1(argn, argw):
    if len(sys.argv) > argn: #compare the lenght of array with the number of input!!!
        if sys.argv[argn] == argw:
          return True
    



def funzione():
   #get the name of file from the path e.g. path="/home/user/script.py" return script.py
    app=sys.argv[0].split("/")
    file_name = app[len(sys.argv[0].split("/"))-1]
    if len(sys.argv) > 1:
        if file_name == "main.py" and sys.argv[1] == "docker":
            docker.show()
        elif file_name == "main.py" and sys.argv[1] == "git":
            git.show()
        elif file_name == "main.py" and sys.argv[1] == "arg1":
            git.show()

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