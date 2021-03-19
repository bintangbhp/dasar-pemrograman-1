#  Program template for Lab Tutorial 8
import string
# string of all uppercase letters: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 

def main():
    # Gather input from the user:
    # keyword, input file name, output file name, kind of operation
    keyword = input("Enter the secret keyword: ").upper()
    in_name = input("Enter the input file name: ")
    out_name = input("Enter the output file name: ")
    operation = input("(E)ncrypt or (D)ecrypt? ").upper()
    uppercase = string.ascii_uppercase
    
    # Read all of the text out of the file.
    inf = open(in_name, 'r')
    text = inf.read()
    inf.close() # Menutup file
    
    # Create dictionaries for encryption and decryption
    dictHuruf = dict(zip(uppercase, range(26))) # Membuat dictionary huruf:urutan angka
    dictAngka = dict(zip(range(26), uppercase)) # Membuat dictionary urutan angka:huruf

    # While-loop untuk memastikan panjang keyword sama dengan panjang kata
    while len(keyword) != len(text):
        if len(keyword) > len(text):
            keyword = keyword[:len(text)]
        else:
            keyword += keyword
    
    # Encrypt or decrypt the text string provided by the user, letter by letter
    result = ""  # accumulate the result of encryption/decryption here
    for i in range(len(text)):
        iterasiFile = text[i] # Melakukan iterasi pada isi file
        iterasiKeyword = keyword[i] # Melakukan iterasi pada keyword agar dapat menentukan dict yang dipakai
        if iterasiFile.isalpha(): # Jika iterasi berupa huruf maka akan dilakukan enkripsi atau dekripsi
            hurufBaru = dictHuruf[iterasiFile]
            angkaBaru = dictHuruf[iterasiKeyword]
            if operation == "E":
                enkripsi = (hurufBaru + angkaBaru) % 26 # Modulo untuk memilih dictionary
                enkripsi = dictAngka[enkripsi]
                result += enkripsi
            elif operation == "D":
                dekripsi = (hurufBaru - angkaBaru) % 26 # Modulo untuk memilih dictionary
                dekripsi = dictAngka[dekripsi]
                result += dekripsi
        else: # Jika bukan huruf, hanya akan dikembalikan
            result += iterasiFile

    # Menulis hasil ke dalam file .txt baru
    outf = open(out_name, "w") 
    outf.write(result) 
    outf.close()

if __name__ == '__main__': 
    main()