class Debugger:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def debug(self, str):
        print("debugger {id}:{name} -> str ")

    def undebug(self,file):
        changes = []
        with open(file) as f:
            lines = "".join(f.readlines())
        lines2 = lines.replace(" ", "")
        lines2 = lines2.split("\n")
        for i in range(len(lines2)):
            if lines2[i][:len(self.name)] == self.name:
                changes.append(i)
        i = 0
        lines = lines.split("\n")
        while i<len(changes):
          lines.pop(changes[i])
          for j in range(len(changes)):
            changes[j]-=1
          i+=1
        lines = "\n".join(lines)
        with open(file,'w') as f:
          f.seek(0)
          f.write(lines)
        exit()
