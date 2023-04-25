#from colors import * #import all from colors.py module
#from git import * #import all from colors.py module
import os
import sys

#The split method return an array with the head and the tail of the path
path= os.path.split(os.path.realpath(__file__))[0]
file_name = os.path.split(os.path.realpath(__file__))[1]

#import modules
if os.path.exists(path+"/functions.py"): 
    from functions import *


#Call Manager Function 
if funzione1(1,"help"):
   help()
if funzione1(1,"modules"):
   show_modules()
if funzione1(1,"version"):
   show_version()


if funzione1(1,"user"):
   network_commands()
if funzione1(1,"network"):
   network_commands()
if funzione1(1,"filesystem"):
    filesystem_commands()
if funzione1(1,"system"):
    system_commands()

if funzione1(1, "bashrc"):
    bashrc.show() 
if funzione1(1, "docker"):
    if funzione1(2, "description"):
        docker.show_description()
    elif funzione1(2, "configuration"):
        docker.show_configuration()
    elif funzione1(2, "about"):
        docker.show_about()
    elif funzione1(2, "images"):
        docker.show_images()
    elif funzione1(2, "containers"):
        docker.show_containers()
    elif funzione1(2, "network"):
        docker.show_network()
    elif funzione1(2, "volumes"):
        docker.show_volumes()
    elif funzione1(2, "volumes"):
        docker.show_dockerfile()
    elif funzione1(2, "list"):
        docker.list()
    else:
        docker.show()
if funzione1(1, "git"):
    if funzione1(2, "list"):
        docker.list()
    else:
        git.show() 


command=""

if funzione1(1, "cli"):
    print("Welcome to Pyto Cli: command_name argument1")
    print("From shell: pm command_name argument1")
    while command!="exit":
        command = input("\033[1;37mInput: ")
        if command == "help":
            help()
        if command == "modules":
            show_modules()

        if command == "version":
            show_version()


        if command == "clear":
            print("\033c")
        if command == "user":
            network_commands()
        if command == "network":
            network_commands()
        if command == "filesystem":
            filesystem_commands()
        if command == "system":
            system_commands()
        if command == "bashrc":
            bashrc.show() 
        #docker
        if "docker description" in command:
            docker.show_description()
        if "docker configuration" in command:
            docker.show_configuration()
        if "docker about" in command:
                docker.show_about()
        if "docker images" in command:
                docker.show_images()
        if "docker containers" in command:
            docker.show_containers()
        if "docker network" in command:
            docker.show_network()
        if "docker about" in command:
                docker.show_about()
        if "docker images" in command:
                docker.show_images()




