def solution(string, ending):
    index = -(len(ending))
    print(index)
    print(string[index:])
    if string[index:] == ending:
        return True
    elif en == ' ':
        return True
    else:
        return False

print(solution('samurai','ai'))

______________________________________________________________
def find_it(seq):
    end = 0
    for i in seq:
        koll = seq.count(i)
        if not koll%2 == 0:
            return i
seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
print(find_it(seg))
_____________________________________________________________________________
def binary_array_to_number(arr):
    arr1 = str(arr[0]) + str(arr[1]) + str(arr[2]) + str(arr[3])
    print(arr1)
    dict1 = {'0001':1,'0010':2,'0011':3,'0100':4,'0101':5,'0110':6,'0111':7,'1000':8,'1001':9,'1010':10,'1011':11,'1100':12,'1101':13,'1110':14,'1111':15}
    return dict1.get(arr1)
n=list([0,1,0,1])
d=len(n)
f=0
c=0
h=1
for i in range(0,d):
    f+=int(n[c])*(2**(d-h))
    c+=1
    h+=1
print(f)

nechet = []
index = []
list1 = [5, 8, 6, 3, 4]
for i in range(len(list1)):
    if not list1[i]%2 == 0:
        nechet.append(list1[i])
        index.append(i)
        list1.remove(list1[i])
        list1.insert(i,'+')
nechet.sort()

for i in range(len(index)):
    list1.remove('+')
    list1.insert(index[i],nechet[i])

print(list1)
print(nechet)
print(index)

#expanded_form(12) # Should return '10 + 2'
#expanded_form(42) # Should return '40 + 2'
#expanded_form(70304) # Should return '70000 + 300 + 4'
num = str(70320)
stroka = ''
for i in range(len(num)):
    if not num[i] == 0:
        n = len(num)
        stroka = intnum[i]
print(stroka)
