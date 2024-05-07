def bacalog(filename):
    email_= {}
    pesan = 0

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('From '):
                email = line.split()[1]
                email_[email] = email_.get(email, 0) + 1
                pesan += 1

    return email_, pesan

bacalog2 = input("Masukkan nama file: ")
email_, pesan  = bacalog(bacalog2)

print(email_)