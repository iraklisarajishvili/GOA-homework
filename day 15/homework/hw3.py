# 3)მომხმარებელს შემოატანინეთ მისი ასაკი და ასევე მისი სახელი, თუ მომხმარებლის სახელი ემთხვევა თქვენს სახელს და ასევე მისი ასაკი ემთხვევა თქვენს სახელს, დაბეჭდეთ "Twins" სხვა შემთხვევაში "Not Twins".



my_name = "irakli"
my_age = 14

user_name = input("enter your name: ")
user_age = int(input("enter your age: "))

if user_name == my_name and user_age == my_age:
    print("Twins")
else:
    print("Not Twins")