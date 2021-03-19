print('Lab 05: Converter with read/write features')
print()

namaFileInput = input("Input File: ")
namaFileOutput = input("Output File: ")

fileInput = open(namaFileInput, "r")
fileOutput = open(namaFileOutput , "w")

index = 0

# Mengubah bilangan desimal menjadi bilangan biner
for dec_input in fileInput:
    if index == 0:
        num_of_bit = int(dec_input)
        print(num_of_bit, file = fileOutput)
    elif 0 < index <= 10:
        decimal = int(dec_input)
        temp = decimal
        binstr = '' # Accumulator untuk hasil biner, awalnya berupa string kosong
        if decimal > 0: # Handling input positif
            while temp != 0: # While-loop untuk mengubah bilangan desimal ke biner
                bindigit = temp % 2 
                binstr = str(bindigit) + binstr 
                temp //= 2
            print("{:<16d} = {}".format(decimal , binstr.zfill(num_of_bit)), file = fileOutput)
            
        elif decimal < 0: # Handling input negatif
            complement = (2**num_of_bit) + temp # Mencari representasi biner dalam sistem 2's complement
            while complement != 0: # While-loop untuk mengubah bilangan desimal ke biner
                bindigit = complement % 2
                binstr = str(bindigit) + binstr
                complement //= 2
            print("{:<16d} = {}".format(decimal , binstr.zfill(num_of_bit)), file = fileOutput)
            
        else: # Handling input 0
            print("{:<16} = {}".format(decimal , binstr.zfill(num_of_bit)), file = fileOutput)
    else:
        newInt = 0 # Accumulator untuk bilangan desimal, awalnya 0
        temp = dec_input.strip()
        for i in range (num_of_bit): # Mengubah bilangan biner menjadi bilangan desimal
            if len(temp) == 1: # Handling untuk bit paling kiri
                bindigit = int(temp) # Casting menjadi integer
                newInt += bindigit*(-(2**i)) # Kalikan dengan -2^(jumlah bit - 1)
            else:
                bindigitstr = temp[-1] # Mengambil digit paling kanan
                bindigit = int(bindigitstr) # Casting menjadi integer
                newInt += bindigit*2**i # Menambah pangkat yang sesuai
            temp = temp[0:-1] # Membuang digit paling kanan
        print("{:<16s} = {}".format(dec_input.zfill(num_of_bit).strip() , newInt), file = fileOutput)
    index += 1

fileInput.close()
fileOutput.close()

print()
print("Thanks for using this program.")
print()
input("Press Enter to continue...")