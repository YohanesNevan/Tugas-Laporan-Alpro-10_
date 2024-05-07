count = 0
dictionary_words = dict()
fname = input('Masukkan nama file : ')
fword = input('Kata yang dicari : ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('Fie tidak bisa dibuka !!', fname)
    exit()

for line in fhand:
    words = line.split()
    for word in words:
        count += 1
        if word in dictionary_words:
            continue # cek duplikasi
dictionary_words[word] = count # kata yg pertama muncul

print('\nDaftar Kamus : \n')
print(dictionary_words)

if fword in dictionary_words:
    print('\nKata %s ditemukan dalam kamus' % fword)
else:
    print('\nKata %s tidak ditemukan dalam kamus' % fword)
