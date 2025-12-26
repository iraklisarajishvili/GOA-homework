# 4) მომხმარებელს შემოატანინეთ მისი ასაკი და სახელი, შემოუშვით საიტზე თუ ის იქნება 18 წელზე მეტის ან მისი სახელი იქნება "Andrew"



age = int(input("enter your age: "))
name = input("enter your name: ")

if age > 18 or name == "irakli":
    print("welcome!")
else:
    print("error")