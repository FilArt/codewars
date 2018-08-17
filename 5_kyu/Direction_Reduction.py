""" Task
Write a function dirReduc which will take an array of strings and
returns an array of strings with the needless directions removed (W<->E or
S<->N side by side). 
"""


def dirReduc(path):
    for i in range(len(path) - 1):
        if (path[i] == 'NORTH' and path[i + 1] == 'SOUTH'
                or path[i] == 'SOUTH' and path[i + 1] == 'NORTH'
                or path[i] == 'EAST' and path[i + 1] == 'WEST'
                or path[i] == 'WEST' and path[i + 1] == 'EAST'):
            del path[i]
            del path[i]
            return dirReduc(path)
    return path


test = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(test))
