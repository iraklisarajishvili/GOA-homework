# 4)დაწერე ფუნქცია, რომელიც დააბრუნებს მხოლოდ ლუწ რიცხვებს ახალი list-ის სახით


def get_even(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list