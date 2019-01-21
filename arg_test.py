def testing(*inp):
    print(', '.join(map(str, inp[0::])))
    #print(str(inp[-1]))
    #str(v) for v in value_list

def funct(inp, *out):
    inp(', '.join(map(str, out)))
    #print(', '.join(map(str, out)))
    #inp(', '.join(map(str, out)))

testing(1, 2)
testing(1, 2, 3)

funct(testing, 1)
funct(testing, 1, 2, 3)
