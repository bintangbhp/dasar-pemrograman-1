print ('Lab 03\n')
print ('From decimal to binary')
print ('----------------------')

# Membaca bilangan desimal pengguna
myInt = int(input('Give a positive integer in decimal representation: '))

# Mengubah bilangan desimal pada myInt menjadi biner
binstr = '' # Accumulator untuk hasil biner, awalnya kosong
temp = myInt

while temp > 0:
    bindigit = temp % 2
    binstr = str(bindigit) + binstr
    temp //= 2

print('The binary representation of',myInt,'is','0b' + binstr)
print()
print('From binary to decimal')
print('----------------------')

# Membaca string biner dari pengguna
binstr = input('Give a positive integer in binary representation: ')

# Mengubah string biner menjadi bilangan desimal
temp = binstr[2:] # Menghapus '0b' menggunakan string slicing
newInt = 0 # Accumulator untuk hasil desimal
length = len(temp)

for power in range(length):
    bindigitstr = temp[-1] # Mengambil digit terkanan
    bindigit = int(bindigitstr)
    newInt = newInt + bindigit*2**power # Menambahkan pangkat yang sesuai
    temp = temp[0:-1] # Membuang digit terkanan

print('The decimal representation of', binstr, 'is', newInt)
print()
print('Thanks for using this program.')
print()
input('Press Enter to continue ...') # Menahan layar agar tidak keluar