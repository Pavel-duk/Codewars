#не проходит по таймингу, а так работает
"""def common(a, b, c):
    summa = []
    for i in a:
        if i in b and c:
            summa.append(i)
    return (sum(summa))


w = common([1,2,2,3],[5,3,2,2],[7,3,2,2])

print(w)"""
"""def duplicate_encode(word):
    i = 0
    new_word = ''
    yes = '('
    no = ')'
    while i < len(word):
        word = word[:i] + word[i+1:]
        if i in word:
            new_word = no
        else:
            new_word = yes
        i+=1
    print(new_world)"""
e = "weewfwg"



"""def unique_in_order(iterable):
    spisok = []
    for i in range(len(iterable)):
        if i == 0:
            spisok.append(iterable[0])
        new_simb = i == 0 or iterable[i] == iterable[i-1]
        if new_simb:
            i += 1
            continue
        else:
            spisok.append(iterable[i])
            i += 1
    return spisok
unique_in_order('AAAABBBCCDAABBB')
print(spisok)"""


"""def song_decoder(song):
    list1 = []
    i = 0
    while i < len(song):
        if song[i:i+3] == 'WUB':
            list1.append(song[i:i+3])
            i+=3
            continue
        list1.append(song[i])
        i+=1
        list2 = []
        for j in list1:
            if not j == 'WUB':
                list2.append(j)
    s = ' '
    new_stroka = s.join(list2)
    print(new_stroka)
song = "AWUBWUBWUBBWUBWUBWUBC"
song_decoder(song)

stroka = 'wert'
stroka = stroka[::-1]
print(stroka)"""

"""def common(a, b, c):
    summa = []
    for i in a:
        if i in b and c:
            summa.append(i)
    return (sum(summa))

w = common([1,2,2,3],[5,3,2,2],[7,3,2,2])
print(w)"""
stroka = "1 3 4"
spisok = []
stroka = stroka.split(' ')
print(stroka)

