#This is to read int in first line which tells number of commands
N = int(raw_input())
print N

#This is list where we apply next command operation
egg = []

for x in range(N):
  cmd = raw_input() # Your Input
  #print command , " - INPUT ", x
  cmdlist = cmd.split()   # Input processing to split around spaces
  # cmdlist datatype is list, access list element by index or position
  if cmdlist[0] == 'insert':
    position = int(cmdlist[1])
    element = int(cmdlist[2])
    egg.insert(position,element)
  elif cmdlist[0] == 'print':
    print egg
  elif cmdlist[0] == 'remove':
    element = int(cmdlist[1])
    egg.remove(element)
  elif cmdlist[0] == 'append':
    element = int(cmdlist[1])
    egg.append(element)
  elif cmdlist[0] == 'sort':
    egg.sort()
  elif cmdlist[0] == 'pop':
      egg.pop()
  elif cmdlist[0] == 'reverse':
    egg.reverse()
