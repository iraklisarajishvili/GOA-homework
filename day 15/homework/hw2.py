# 2)ცვლადში შეინახეთ თქვენი საყვარელი რიცხვი და მომხმარებელს შემოატანინეთ ასევე მისი საყვარელი რიცხვი, თუ თქვენი რიცხვები ემთხვევა მაშინ დაბეჭდეთ "Perfect" თუ მისი რიცხვი მეტია, დაბეჭდეთ "More", სხვა შემთხვევაში "Less".


my_number = 9

user_number = int(input("enter your favoritr number: "))

if user_number == my_number:
    print("Perfect")
elif user_number > my_number:
    print("More")
else:
    print("Less")