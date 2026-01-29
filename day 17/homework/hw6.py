# 6) შექმენით ინტეჯერების ლისტი, და ორი ცვლადი positive, negative. გამოიტანეთ სიაში არსებული დადებითი რიცხცების ჯამი, უარყოფითები რიცხვების რაოდენობა და დაპრინტე "zero" რამდენჯერაც შეგხვდება 0



numbers = [5, -3, 0, 12, -7, 0, 8, -1, 0]
positive = 0
negative = 0
zero_count = 0

for num in numbers:
    if num > 0:
        positive += num 
    elif num < 0:
        negative += 1
    else:
        zero_count += 1

print("დადებითი ჯამი:", positive)
print("უარყოფითი რიცხვების რაოდენობა:", negative)
print("ნულების რაოდენობა:", zero_count)