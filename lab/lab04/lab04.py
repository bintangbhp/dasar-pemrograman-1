print('Lab 04')
print()

print("From decimal to 2's complement system")
print("--------------------------------------")

num_of_bit = int(input("How many to use in the 2's complement system? ")) # Meminta input jumlah bit dari user
dec_input = int(input("Give an integer in decimal representation: ")) # Meminta input bilangan desimal dari user

# Mengubah bilangan desimal dari dec_input menjadi bilangan biner
binstr = '' # Accumulator untuk hasil biner, awalnya berupa string kosong
temp = dec_input

if dec_input > 0: # Handling input positif
    while temp != 0: # While-loop untuk mengubah bilangan desimal ke biner
        bindigit = temp % 2 
        binstr = str(bindigit) + binstr 
        temp //= 2
    print("The 2's complement representation of", dec_input, "is", binstr.zfill(num_of_bit))
elif dec_input < 0: # Handling input negatif
    complement = (2**num_of_bit) + temp # Mencari representasi biner dalam sistem 2's complement
    while complement != 0: # While-loop untuk mengubah bilangan desimal ke biner
        bindigit = complement % 2
        binstr = str(bindigit) + binstr
        complement //= 2
    print("The 2's complement representation of", dec_input, "is", binstr.zfill(num_of_bit))
else: # Handling input 0
    print("The 2's complement representation of", dec_input, "is", '0'.zfill(num_of_bit))

print()

print("From 2's complement system to decimal")
print("--------------------------------------")

myBin = input("Give an integer in 2's complement representation (" + str(num_of_bit) + " bits): ") # Meminta input bilangan biner
temp = myBin.zfill(num_of_bit) # Mengubah input menjadi representasi jumlah bit yang diminta di awal
newInt = 0 # Accumulator untuk bilangan desimal, awalnya 0

# Mengubah bilangan biner dari myBin menjadi bilangan desimal
for i in range (num_of_bit):
    if len(temp) == 1: # Handling untuk bit paling kiri
        bindigit = int(temp) # Casting menjadi integer
        newInt += bindigit*(-(2**i)) # Kalikan dengan -2^(jumlah bit - 1)
    else:
        bindigitstr = temp[-1] # Mengambil digit paling kanan
        bindigit = int(bindigitstr) # Casting menjadi integer
        newInt += bindigit*2**i # Menambah pangkat yang sesuai
    temp = temp[0:-1] # Membuang digit paling kanan

print("The decimal representation of", myBin.zfill(num_of_bit), "is", newInt)
print()
print("Thanks for using this program.")
print()
input("Press Enter to continue...")
