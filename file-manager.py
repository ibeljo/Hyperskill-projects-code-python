import os
availble_commands = {"pwd":"Working directory", "cd..":"Change directory"}
# run the user's program in our generated folders
os.chdir('module/root_folder')
list_dir =[]
list_file =[]
list_file_size =[]
def list_dirs():

    for i in sorted(os.listdir()):

        if os.path.isdir(i):
            list_dir.append(i)
        elif os.path.isfile(i):
            list_file.append(i)
            size = os.path.getsize(i)
            list_file_size.append(size)

def print_files(str):
    if str == "ls":
        print(*(i for i in list_file), sep='\n')
    elif str == "ls -l":
        for file, size in zip(list_file, list_file_size):
            print(file, size)
    elif str ==  "ls -lh":
        file_size = 0
        for file, size in zip(list_file, list_file_size):
            if size >=1024**3:
                file_size= int(size / 1024**3)
                print(f"{file} {file_size}GB")
            elif size >= 1024**2:
                file_size = int(size/1024**2)
                print(f"{file}, {file_size}MB")
            elif size >=1024:
                file_size = int(size/1024)
                print(f"{file} {file_size}KB")
            else:
                print(f"{file} {size}B")

def print_dirs():
    list_dir.sort()
    print(*(i for i in list_dir), sep='\n')
def clear_lists():
    list_dir.clear()
    list_file.clear()
    list_file_size.clear()
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
    elif str == "ls":
        list_dirs()
        print_dirs()
        print_files(str)
        clear_lists()
    elif str == "ls -l":
        list_dirs()
        print_dirs()
        print_files(str)
        clear_lists()

    elif str =="ls -lh":
        list_dirs()
        print_dirs()
        print_files(str)
        clear_lists()



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

