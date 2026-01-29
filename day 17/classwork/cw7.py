# 7)შექმენით სახელების სია შემდეგ გადაუარეთ და შეამოწმეთ რომელი სახელიც იწყება "g" ასოთი დაბეჭდეთ ეს სახელი და გვერდით მიუწერეთ True



names = ["gio", "Nika", "goga", "Ana", "Giorgi", "luka"]

for i in names:
    if i.lower().startswith("g"):
        print(i, True)