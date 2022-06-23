import encode_decode as ed 
from termcolor import colored
import time
import os

def req_command():
    command = input(">")
    rec_command(command)

def rec_command(cmd):
    if(cmd == "help"):
        print(colored("Commands:\nencode\ndecode" , "blue"))
        req_command()
    elif(cmd == "encode"):
        print(colored("\n[*]Starting encoder...\n", "blue"))
        time.sleep(3)
        string_for_request = input(colored("Text:", "blue"))
        print(colored(ed.process.encode(string_for_request), "green"))
        req_command()
    elif(cmd == "decode"):
        print(colored("\n[*]Starting decoder...\n", "blue"))
        time.sleep(3)
        string_for_request = input(colored("Text:", "blue"))
        print(colored(ed.process.decode(string_for_request), "green"))
        req_command()
    elif(cmd == "exit"):
        exit()
    else:
        print(colored("Unknown command" ,"red"))
        req_command()