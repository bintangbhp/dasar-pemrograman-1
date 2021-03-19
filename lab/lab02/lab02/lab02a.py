# Author: Bintang Hari Pratama
# File name: lab02a.py
# menggunakan turtle untuk menggambar pentagon dan spiral pentagon
# meminta input komponen warna (r,g,b) dari user

import turtle
turtle.shape('turtle')
turtle.title('Lab 02')

# mengambil nilai dari komponen warna merah yang diinput user
r = float(turtle.textinput(
 "Lab 02", "The red color component [between 0 and 1]: "))

# mengambil nilai dari komponen warna hijau yang diinput user
g = float(turtle.textinput(
 "Lab 02", "The green color component [between 0 and 1]: "))

# mengambil nilai dari komponen warna biru yang diinput user
b = float(turtle.textinput(
 "Lab 02", "The blue color component [between 0 and 1]: "))

# membuat warna dari kombinasi nilai rgb yang diberi user
turtle.color(r , g, b)

# memindahkan turtle ke sebelah kiri turtle window
# dan mengatur headingnya menjadi 0

turtle.penup()
turtle.goto(-250,0)
turtle.setheading(0)
turtle.pendown()

# gambar dan beri warna pentagon dengan warna
# yang sudah diatur di atas
# gunakan for loop

turtle.begin_fill()
for i in range (5):
    turtle.forward(150)
    turtle.right(72)
turtle.end_fill()

# geser turtle ke sebelah kanan di turtle window
# dan atur headingnya menjadi 0

turtle.penup()
turtle.goto(100,0)
turtle.setheading(0)
turtle.pendown()

# gambar sebuah spiral pentagon

side = 150
for i in range(75):
 turtle.forward(side)
 turtle.right(72) # sudut luar dari pentagon adalah 72 derajat
 side -= 2 # kurangi variabel side dengan 2
 
# membuat turtle tidak terlihat

turtle.hideturtle()

# pesan untuk user

turtle.up()
turtle.goto(0, 200)
turtle.down()
turtle.color('blue')
turtle.write("Please click on the graphics window to exit ...",
 False, align='center', font=('Arial', 20, 'normal'))

# tunggu user mengclick screen untuk
# mengexit window turtle

turtle.exitonclick()
turtle.mainloop()

# the end
