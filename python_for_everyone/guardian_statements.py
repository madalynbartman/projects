han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    # print statements for debugging 
    # print('Line:', line)
    
    # if line == '':
    #     print('Skip Blank')
    #     continue
    wds = line.split()
    # print('Words:',wds)

    # Guardian pattern
    # if len(wds) < 3:
    #     continue
    # if wds[0] != 'From' :

    # Guardian in a compund statement
    # Order matters. The guardian comes before
    # If true, it won't continue. Called short-circuit evaluation
    if len(wds) < 3 or wds[0] != 'From' :
        # print('Ignore')
        continue
    print(wds[2])