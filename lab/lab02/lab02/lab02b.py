# Author: Bintang Hari Pratama
# File name: lab02b.py
# menggunakan simultaneous assigment untuk;
# mengurutkan data
# 5 variabel dengan nilai sbb:

number1 = 25
number2 = 7
number3 = 3
number4 = -8
number5 = 19

# output yang diminta: 25 7 3 -8 19
print ("Initial data: ")
print (number1, number2, number3, number4, number5)

# 3 simultaneous assignment cukup untuk
# menukar nilai dari variabel yang ada;
# secara bersamaan, dengan bentuk: x,y = y,x

number2 , number3 = number3 , number2
number4 , number5 = number5 , number4
number5 , number1 = number1 , number5

# Menampilkan data yang telah terurut
# # output yang diminta: -8 3 7 19 25

print("Sorted data, from smallest to largest: ")
print(number1, number2, number3, number4, number5)
