fname = input('Enter File (press enter for default): ')
if len(fname) < 1 : fname = 'fox.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1

# print(di)

tmp = list()
for k,v in di.items() :
    # print(k,v)
    newt = (v,k)
    tmp.append(newt)

# print('Flipped',tmp)

tmp = sorted(tmp,reverse=True)
# print('Sorted',tmp[:5])

for v,k in tmp[:5] :
    print(k,v)

# x = sorted(di.items())
# print(x[:5])
