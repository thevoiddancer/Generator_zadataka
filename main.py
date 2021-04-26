import os
path = "."
while True:
    folders = [i.name for i in os.scandir() if i.is_dir() and i.name[0] not in '._']
    prompt = input(path + ">").split(" ", 1)
    if prompt[0].lower() == "cd" and len(prompt) == 2:
        if prompt[1] in folders:
            os.chdir(prompt[1])
            path += "/"+prompt[1]
        elif prompt[1] == "..":
            path = "/".join(path.split("/")[:-1])
            os.chdir(prompt[1])
        else:
            print("Syntax error")
            print(folders)
    elif len(prompt) == 1:
        print(folders)
# cd - change directory
# if x = cd, 
# add_q
# add_g

