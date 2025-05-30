import os
availble_commands = {"pwd":"Working directory", "cd..":"Change directory",}
# run the user's program in our generated folders
os.chdir('module/root_folder')
def get_command(str):
    if str == "pwd":
        print(os.getcwd())
    elif str == "cd ..":
        split = os.path.split(os.getcwd())
        print(split[1])
        os.chdir(split[0])
    elif str.startswith("cd"):
        path = str[3:]
        os.chdir(os.path.join(os.getcwd(),path))
        print(path)
    else:
        print("Invalid command")

command = input()
while command != "quit":
    try:
        get_command(command)
        command = input()
    except Exception as e:
        print(f"An error occurred: {e}")
        break