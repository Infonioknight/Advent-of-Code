import re
from copy import deepcopy
data = open("PartFlow.txt", "r").read()
# data = open("Test.txt", "r").read()
flows, parts = data.split('\n\n')
flows = flows.split('\n')
parts = parts.split('\n')
parts = [item[1:-1].split(',') for item in parts]
flows = [item[:-1].split('{') for item in flows] 

flow = {}
for i in flows:
    flow[i[0]] = i[1].split(',')


# /////////// Function starts from here //////////////


mapper = {'x':0, 'm':1, 'a':2, 's':3}
sum = 0
def something(guide, xmas, curr, pos):
    global sum
    print(xmas, curr, pos)
    if curr == 'A':
       acc = 1
       for thing in xmas: 
           acc *= ((thing[1] - thing[0])+1)
       sum += acc
       return

    elif curr == 'R':
        return
    
    elif pos > len(guide[curr]):
        return

    check = guide[curr][pos]
    # print('Check', check)
    if '>' in check or '<' in check:
        parameter, value, destination = re.split(r'[><:]', check)
        xmas_copy = deepcopy(xmas)
        if '>' in check:
            xmas_copy[mapper[parameter]][0] = int(value)+1
            something(guide, xmas_copy, destination, 0)
            xmas[mapper[parameter]][1] = int(value)
            something(guide, xmas, curr, pos+1)
        elif '<' in check:
            xmas_copy[mapper[parameter]][1] = int(value)-1
            something(guide, xmas_copy, destination, 0)
            xmas[mapper[parameter]][0] = int(value)
            something(guide, xmas, curr, pos+1)
    elif check == 'A':
        acc = 1
        for thing in xmas: 
            acc *= ((thing[1] - thing[0]) + 1)
        sum += acc

    elif check == 'R':
        return
    
    else:
        something(guide, xmas, check, 0)

something(flow, [[1, 4000], [1, 4000], [1, 4000], [1, 4000]], 'in', 0)
print(sum)