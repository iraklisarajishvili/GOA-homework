# 5)შექმენით სახელების სია და მომხმარებლებს შემოატანინეთ მისი სახელი ასევე count ცვლადი, გადაუარეთ ამ სიას და რამდენჯერაც მომხმარებლის სახელი შეგხვდებათ დაპრინტე "user name" და count მოუმატე ერთი საბოლოოდ  დაპრინტე count ცვლადი



names = ["Nika", "Gio", "Ana", "Nika", "Luka", "Nika"]

user_name = input("შეიყვანე შენი სახელი: ")

count = 0

for i in names:
    if i == user_name:
        print("user name")
        count += 1

print(count)