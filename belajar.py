# Test = dict()
# print(Test)

# coba = dict()
# coba ['one'] = 'uno'
# print(coba)

# coba = dict()
# coba = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# print('one' in coba)
# print('alo' in coba)
# # print(coba)


# print(coba['two'])

# print(coba['four'])

# len(coba)

# 'one' in coba
# 'uno' in coba

# vals = list(coba.values())
# 'uno' in vals
# print(vals)

# word = 'brontosaurus'
# d = dict() #dictionary kosong
# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] = d[c] + 1
# print(d)

# counts = {'chuck': 1, 'annie' : 42, 'jan' : 100}
# print(counts.get('jan', 0))
# print(counts.get('tin', 0))

# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()

# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
# print(counts)

# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in counts:
#     print(key, counts[key])

# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in counts:
#     if counts[key] > 10 :
#         print(key, counts[key])

# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# lst = list(counts.keys())
# print(lst)
# lst.sort()
# for key in lst:
#     print(key, counts[key])

# line.translate(str.maketrans(fromstr, tostr, deletestr))

import string
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
    else:
        counts[word] += 1
print(counts)

