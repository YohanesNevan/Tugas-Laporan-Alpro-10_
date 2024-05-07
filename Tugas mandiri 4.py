def menghitung_email(email):
    return email.split('@')[-1]

def menghitung_email1(filename):
    counts = {}

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('From '):
                email = line.split()[1]
                awal = menghitung_email(email)
                counts[awal] = counts.get(awal, 0) + 1

    return counts

filename = input("Masukkan nama file: ")
counts = menghitung_email1(filename)

print(counts)