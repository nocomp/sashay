#
import os
import quo
import json
from time import sleep
from quo import echo, prompt
from .outlook import *
from .system import *

class main:
  def install_tools(self):
    while True:
      tool=tools()
      num=1
      total=len(tool.names)
      os.system("clear")
      logo.install_tools()
      echo("\007")
      for tool_name in tool.names:
        echo(f'{num} install {tool_name}', bold=True, fg="vblue")
        num+=1
      echo("")
      logo.back()
      cmd=prompt("/>>>")
      if cmd=="00" or cmd=="back":
        self.menu()
        break
      else:
        try:
          if int(cmd)>=1 and int(cmd)<=int(total):
            os.system("clear")
            logo.installing()
            echo(f"Installing...Good things come to those who wait", bold=True, fg="vgreen")
            tool.install(tool.names[int(cmd)-1])
          else:
            echo(f"Sorry, '{cmd}' is an invalid input!", fg="vred") 
            sleep(1)
        except ValueError:
          echo(f"Sorry, '{cmd}' is an invalid input!", fg="vred")
          sleep(1)

  def category(self):
    while True:
      tool=tools()
      total=len(tool.category)
      num=1
      os.system("clear")
      logo.tool_header()
      echo("")
      for cat in tool.category:
        echo(f'{num} {tool.category_data[cat]}', bold=True, fg="vblue")
        num+=1
      echo("")
      logo.back()
      cmd=prompt("/>>>") 
      if cmd=="00" or cmd=="back":
        self.menu()
        break
      else:
        try:
          if int(cmd) in range(1,int(total)+1):
            while True:
              print(int(cmd)-1)
              print(tool.category[int(cmd)-1])
              cnt=1
              os.system("clear")
              logo.tool_header()
              echo("")
              tmp_cat_tool=[]
              for i in tool.names:
                if tool.category[int(cmd)-1] in tool.data[i]["category"]:
                  tmp_cat_tool.append(tool.data[i]['name'])
                  print(f" \033[01;32m[ \033[00m{cnt} \033[01;32m] \033[01;33minstall \033[01;32m{tool.data[i]['name']}\033[00m")
                  cnt+=1
              print("")
              logo.back()
              tcmd=prompt("/>>>")
              if tcmd=="00" or tcmd=="back":
                break
              else:
                try:
                  cat_total=len(tmp_cat_tool)
                  if int(tcmd) in range(1,int(cat_total)+1):
                    os.system("clear")
                    logo.installing()
                    echo(f"Installing...Good things come to those who wait", fg="vgreen") 
                    tool.install(tmp_cat_tool[int(tcmd)-1])
                  else:
                    print(f"\007\033[01;31mSorry \033[01;37m: '{tcmd}' \033[01;31minvalid input! try again\033[00m")
                    sleep(1)
                except ValueError:
                  echo(f"\007\033[01;31mSorry \033[01;37m: '{tcmd}' \033[01;31minvalid input! try again\033[00m")
                  sleep(1)
          else:
            print(f"\007\033[01;31mSorry \033[01;37m: '{cmd}' \033[01;31minvalid input! try again\033[00m")
            sleep(1)
        except ValueError:
          print(f"\007\033[01;31mSorry \033[01;37m: '{cmd}' \033[01;31minvalid input! try again\033[00m")
          sleep(1)

  def update(self):
    while True:
      os.system("clear")
      logo.update()
      cmd=prompt("/>>>")
      if cmd=="1":
        system=sys()
        if system.connection():
          os.system("clear")
          logo.updating()
          if system.sudo != None:
            if os.path.exists(system.home+"/sashay"):
              pass
            else:
              os.system(system.sudo+" git clone https://github.com/secretum-inc/sashay.git "+system.home+"/sashay")
            if os.path.exists(system.home+"/sashay/install.sshy"):
              os.system("cd "+system.home+"/sashay && "+system.sudo+" sh install.sshy")
              if os.path.exists(system.bin+"/sashay") and os.path.exists(system.conf_dir+"/sashay"):
                os.system("clear")
                logo.updated()
                cmd=prompt("/>>>")
              else:
                os.system("clear")
                logo.update_error()
                cmd=prompt("/>>>")
            else:
              os.system("clear")
              logo.update_error()
              cmd=prompt("/>>>")
          else:
            if os.path.exists(system.home+"/sashay"):
              pass
            else:
              os.system("git clone https://github.com/secretum-inc/sashay.git "+system.home+"/sashay")
            if os.path.exists(system.home+"/sashay/install.sshy"):
              os.system("cd "+system.home+"/sashay && sh install.sshy")
              if os.path.exists(system.bin+"/sashay") and os.path.exists(system.conf_dir+"/sashay"):
                os.system("clear")
                logo.updated()
                cmd=input("\033[1;36m >>> \033[00m")
              else:
                os.system("clear")
                logo.update_error()
                cmd=input("\033[1;36m >>> \033[00m")
            else:
              os.system("clear")
              logo.update_error()
              cmd=input("\033[1;36m >>> \033[00m")
        else:
          os.system("clear")
          logo.nonet()
          tmp=input("\033[1;36m >>> \033[00m")
      elif cmd=="0" or cmd=="back":
        self.menu()
        break
      else:
        echo(f"\007\033[01;31mSorry \033[01;37m: '{cmd}' \033[01;31minvalid input !!\033[00m")
        sleep(1)

  def about(self):
    while True:
      tool=tools()
      total=len(tool.names)
      os.system("clear")
      logo.about(total)
      cmd=input("\033[1;36m >>> \033[00m")
      self.menu()
      break

  @classmethod
  def menu(self):
    while True:
      tool=tools()
      total=len(tool.names)
      os.system("clear")
      logo.menu(total)
      cmd=input("\033[1;36m >>> \033[00m")
      if cmd == "1":
        self.install_tools(self)
        break
      elif cmd == "2":
        self.category(self)
        break
      elif cmd == "3":
        self.update(self)
        break
      elif cmd == "4":
        self.about(self)
        break
      elif cmd=="x" or cmd=="X" or cmd=="exit":
        os.system("clear")
        logo.exit()
        break
      elif cmd=="rm -s" or cmd=="rm -S" or cmd=="uninstall sshy" or cmd=="unistall sashay":
        system=sys()
        if system.sudo:
          os.system(system.sudo+" rm -rf "+system.bin+"/sashay")
          os.system(system.sudo+" rm -rf "+system.bin+"/sshy")
          os.system(system.sudo+" rm -rf "+system.conf_dir+"/sashay")
        else:
          os.system("rm -rf "+system.bin+"/sashay")
          os.system("rm -rf "+system.bin+"/sshy")
          os.system("rm -rf "+system.conf_dir+"/sashay")
        os.system("clear")
        logo.exit()
        break
      else:
        print(f"\007\033[01;31mSorry \033[01;37m: '{cmd}' \033[01;31minvalid input !!\033[00m")
        sleep(1)

class tools:
  data=None
  names=None
  category=None
  category_data=None
  def __init__(self):
    system=sys()
    with open(system.conf_dir+"/sashay/assets/data.json") as data_file:
      self.data=json.load(data_file)
    with open(system.conf_dir+"/sashay/assets/cat.json") as cat_file:
      self.category_data=json.load(cat_file)
    self.names=list(self.data.keys())
    self.category=list(self.category_data.keys())

  def install(self,name):
    package_name=self.data[name]["package_name"]
    package_manager=self.data[name]["package_manager"]
    url=self.data[name]["url"]
    req=list(self.data[name]["dependency"])
    system=sys()

    if system.connection():
      if len(req)!=0 and req[0]!=None:
        for dep in req:
          if os.path.exists(system.bin+"/"+dep):
            pass
          else:
            if system.sudo != None:
              os.system(system.sudo+" "+system.pac+" install "+dep+" -y")
            else:
              os.system(system.pac+" install "+dep+" -y")

      if package_manager=="package_manager":
        if os.path.exists(system.bin+"/"+package_name):
          os.system("clear")
          logo.already_installed(name)
          tmp=input("\033[1;36m >>> \033[00m")
        else:
          if system.sudo != None:
            os.system(system.sudo+" "+system.pac+" install "+package_name+" -y")
          else:
            os.system(system.pac+" install "+package_name+" -y")
          # check tool is installed or not
          if os.path.exists(system.bin+"/"+package_name):
            os.system("clear")
            logo.installed(name)
            tmp=input("\033[1;36m >>> \033[00m")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp=input("\033[1;36m >>> \033[00m")

      elif package_manager=="git":
        if os.path.exists(system.home+"/"+package_name):
          os.system("clear")
          logo.already_installed(name)
          tmp=input("\033[1;36m >>> \033[00m")
        else:
          if system.sudo != None:
            os.system(system.sudo+" git clone "+url+" "+system.home+"/"+package_name)
          else:
            os.system("git clone "+url+" "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            os.system("clear")
            logo.installed(name)
            tmp=input("\033[1;36m >>> \033[00m")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp=input("\033[1;36m >>> \033[00m")

      elif package_manager=="wget":
        if os.path.exists(system.home+"/"+package_name):
          os.system("clear")
          logo.already_installed(name)
          tmp=input("\033[1;36m >>> \033[00m")
        else:
          if system.sudo != None:
            os.system(system.sudo+" wget "+url+" -o "+system.home+"/"+package_name)
          else:
            os.system("wget "+url+" -o "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            os.system("clear")
            logo.installed(name)
            tmp=input("\033[1;36m >>> \033[00m")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp=prompt("/>>>")

      elif package_manager=="curl":
        if os.path.exists(system.home+"/"+package_name):
          os.system("clear")
          logo.already_installed(name)
          tmp=prompt("/>>>")
        else:
          if system.sudo != None:
            os.system(system.sudo+" curl "+url+" -o "+system.home+"/"+package_name)
          else:
            os.system("curl "+url+" -o "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            os.system("clear")
            logo.installed(name)
            tmp=prompt("/>>>")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp=prompt("/>>>")
    else:
      os.system("clear")
      logo.nonet()
      tmp=prompt("/>>>")
