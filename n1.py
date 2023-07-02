'''
def counter(s): #O(N**2)
    for i in s:
        count = 0
        for j in s:
            if i==j:
                count+=1
        print(i, count)

counter('aacabccccccc')
'''

'''
def counter2(s): #O(N*M)
    for i in set(s):
        count = 0
        for j in s:
            if i==j:
                count+=1
        print(i, count)

C:/Users/dasha/'Рабочий стол new'/Python/kyrs/'modol 4'/new1
counter2('aabc')
'''

def counter3(s):
    syns = {}
    for i in s:
        syns[i] = syns.get(i, 0) + 1
    for i, count in syns.items():
        print(i, count)

counter3('aabc')
