from colors import *
def show():
  print(GREENBOLD, "#Default", BLUE)
  print("alias ls='ls --color=auto'")
  print("alias ll='ls -hal'")
  print("alias l.='ls -d .*'")
  print("alias tree='tree -C'")
  print("alias rm='rm -i'")
  print("alias uu='sudo apt update && sudo apt upgrade -y'\n")

  print(GREENBOLD, "#Custom Script", BLUE)
  print("alias apth='/home/$(whoami)/Sistema/Script/./apt-helper.sh'")
  print("alias cmd='/home/$(whoami)/Sistema/Script/./commands.sh'")
  print("alias dok='/home/$(whoami)/Sistema/Script/./docker-helper.sh'")
  print("alias gitty='/home/$(whoami)/Sistema/Script/./git-helper.sh'")
  print("alias scl='/home/$(whoami)/Sistema/Script/./script.sh'\n")

  print(GREENBOLD, "#Custom Directories", BLUE)
  print("alias cdw='cd /var/www/html'")
  print("alias cds='cd /home/$(whoami)/Sistema/Script/'\n")


