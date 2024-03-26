fname = input('Enter File: ')
if len(fname) < 1 : fname = 'fox.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        # print('**', w,di.get(w,-99))

        # if the key is not there, the count is 0
        # oldcount = di.get(w,0)
        # print(w,'old',oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount

        # combines 15-18 into one line
        # it's effectively an idiom
        # Idiom: retrieve, create, update, counter
        di[w] = di.get(w,0) + 1
        # print(w,'new',di[w])

        # print(w)
        # if w in di:
        #     di[w] = di[w] + 1
            # print('**Existing**')
        # else:
        #     di[w] = 1
            # print('**NEW**')
        # print(w,di[w])

# print(di)

# now we wanna find the most common word
largest = -1
theword = None
for k,v in di.items() :
    # print(k,v)
    if v > largest : 
        largest = v
        theword = k # capture/remember the key that was largest

print('The word used most often is:',theword,"and it's used",largest,'times')
