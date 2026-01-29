# 5) for ციკლით გადაუარე სიას და დაბეჭდე მხოლოდ ის ელემენტები, რომელთა ინდექსი ლუწია.


numbers = [10, 20, 30, 40, 50]

for index, value in enumerate(numbers):
    if index % 2 == 0:
        print(value)