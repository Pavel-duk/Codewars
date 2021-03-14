def is_pangram(s):
    er = 0
    s = s.upper()
    set = {i for i in s}
    for j in set:
        stroka = str(j)
        if stroka.isalpha():
            er += 1
    print(er)
    if er == 26:
        print(True)
    else:
        print(False)

s = 'The quick, brown fox jumps over the lazy dog!'
is_pangram(s)


def sum_dig_pow(a, b):
    list1 = [i for i in range(a,b+1)]
    list_final = []
    list_prom = []
    print (list1)
    for i in list1:
        i = str(i)
        index = len(i)
        for j in range(0,index):
            res = int(i)^j+1
            list_prom.append(res)
        summa = sum(list_prom)
        if summa == i:
            summa.append(list_final)
    print(list_prom,list_final)
sum_dig_pow(1,100)