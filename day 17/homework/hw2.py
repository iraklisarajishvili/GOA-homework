# 2)შექმენით სია შემდგარი 7 განსხვავებული ემენეტისგან და for ციკლის მეშვეობით შეამოწმეთ თითოეული ემენეტის მონაცემთა ტიპი


mixed_list = [10, "hello", 3.14, True, None, [1, 2], {"key": "value"}]

for item in mixed_list:
    print(item, type(item))