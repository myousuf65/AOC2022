class FileEntry:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class DirectoryEntry(FileEntry):
    def __init__(self, parentDir, DirName, size):
        self.parentDir = parentDir
        self.DirName = DirName
        self.entries = []
        self.size = size

    def add_file(self, file_entry):
        if isinstance(file_entry, FileEntry):
            self.entries.append(file_entry)
        else:
            raise TypeError("file is not of type File Entry")

    def getParent(self):
        return self.parentDir

    def get_size(self):
        size = 0
        for e in self.entries:
            try:
                """ print(e.name, e.size) """
                size += int(e.size)
            except AttributeError:
                pass

            try:
                """ print(e.DirName, e.get_size()) """
                size += int(e.get_size())
            except AttributeError:
                pass
        return size


allDirectories = []
rootdirectory = DirectoryEntry(None, "/", 0)
currentdirectory = rootdirectory

with open("./input.txt") as file:
    lines = file.read()

print(len(lines.splitlines()))

for line in lines.splitlines():
    # print(line)
    if line[0] == "$":
        if line[2] == "c":
            dir = line[5:]

            if dir == "/":
                currentdirectory = rootdirectory

            elif dir == "..":
                if currentdirectory.getParent() == None:
                    currentdirectory = rootdirectory
                    print("parent dir was none")
                else:
                    currentdirectory = currentdirectory.getParent()

            else:

                all = [d.DirName for d in allDirectories]

                if dir in all:
                    for i in range(len(allDirectories)):
                        if allDirectories[i].DirName == dir:
                            print(dir, "is already there")
                            currentdirectory = allDirectories[i]
                            break
                else:
                    # if not found during loop, do this
                    newDir = DirectoryEntry(currentdirectory, dir, 0)
                    currentdirectory = newDir
                    allDirectories.append(newDir)

        elif line[0] == 'l':
            break
    else:
        if line.startswith("dir"):
            all = [d.DirName for d in allDirectories]

            do = False
            for i in range(len(allDirectories)):
                if allDirectories[i].DirName == dir:
                    newDir = DirectoryEntry(currentdirectory, line[4:], 0)
                    currentdirectory.add_file(newDir)
                    do = True
                    break

            # if not found during loop, do this
            if not do:
                newDir = DirectoryEntry(currentdirectory, line[4:], 0)
                print(newDir.DirName, "is added to all allDirectories ")
                currentdirectory.add_file(newDir)
                allDirectories.append(newDir)

        elif line[0].isdigit():
            size, name = line.split(" ")
            file = FileEntry(name, size)
            currentdirectory.add_file(file)
            print("File added to ", currentdirectory.DirName,
                  len(currentdirectory.entries))


print("*"*8)


# size = 0
# for i in allDirectories:
#     if i.get_size() <= 100000:
#         size += int(i.get_size())
# """     print(i.DirName, i.get_size()) """
#
#
# print(size)
#
print(rootdirectory.get_size())
