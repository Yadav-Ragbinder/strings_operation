// changes by developer Ragbinder Yadav


x = "Hello World"
#lower case
print (x.lower())
# hello world
-----------------------------------
#upper case
print (x.upper())
# HELLO WORLD
-----------------------------------
#range 
print (x[:6])
# Hello (it include space)
print (x[:5])
# Hello
-----------------------------------
#index
print (x[4])
# o
print (x.index("r"))
# 8
-----------------------------------
#replace
print (x.replace("World","Kohli"))
# Hello Kohli
print (x.replace("e","k"))
# Hkllo World
-----------------------------------
#find
x1 = ( x + "i")
print (x1.replace("o","k"))
# Hellk Wkrld
-----------------------------------
#add two str
y = " Kohli"
print (x + y)
# Hello World Kohli
// End of commit changes by Developer Ragbinder Yadav
-----------------------------------
// changes by developer Pratibha kohli

// variables in string
name = "hello world"
print(f"hi {name}")
# hi hello world
-------------------------------------
// Print a float with a specified number of digits:
pi = 3.1415926535897932384 
print(f"The first 5 digits of pi are {pi:.5f}")
# The first 5 digits of pi are 3.14159

--------------------------------------
// In Place Boolean Logic
new_user = False
user_name = "Alexander Hamilton"
print(f"{'Congrats on making your account' if new_user else 'Welcome back'} {user_name}!")
# Welcome back Alexander Hamilton!

------------------------------------

// Python String strip() Method

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite") 
# of all fruits banana is my favorite 

----------------------------------------------

// End of commit changes by Developer Pratibha Kohli
