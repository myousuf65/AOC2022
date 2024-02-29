with open("./demo.txt") as file:
    lines = file.read()

all_dirs = {}
cwd = ''
stack = []

for line in lines.split("\n"):
    if line[0] == "$":

        # change directory command
        if line[2] == 'c':
            dir = line[5:]
            
            if dir == '/':
                cwd = dir
                all_dirs[cwd] = {}
                stack = []

            # elif dir == '..':
            #     cwd = stack.pop()

            else:
                if dir not in all_dirs[cwd]:
                    all_dirs[cwd][dir] = {}
                    cwd = dir


        # ls command
        elif line[2] == 'l' :
            break
        
    else:
        if line[0:2] == 'dir':
            all_dirs[cwd][dir] = {}

        elif line[0].isdigit():
            all_dirs[cwd] = 
