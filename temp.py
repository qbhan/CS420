# s = "%d %d %d" % [1,2,3]
# print(s)

def interpret(node):
    return node + 1

list = [1, 2, 1, 1]
args = list[1:]
interpreted_args = tuple(map(interpret, args))
print(interpreted_args)