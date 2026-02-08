# 4) შექმენით პროგრამა, სადაც მომხმარებელი შემოიტანს თავის გვარს, თუ პირველი 5 ასო შენი გვარის პირველი 5 ასოს მსგავსია, დაპრინტე 'almost same' სხვა შემთხვევაში დაპრინტე 'bye'


my_surname = "Sarajishvili"

user_surname = input("enter your surname: ")

if user_surname[:5] == my_surname[:5]:
    print("almost same")
else:
    print("bye")