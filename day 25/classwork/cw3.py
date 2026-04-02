# 3)შექმენი ფუნქცია რომელსაც გადაეცემა სია, შენ უნდა დააბრუნო ამ სიის სიგრძე


def list_len(arr):
    count = 0
    for i in arr:
        count += 1
    return count

print(list_len([1,2,3]))
print(list_len(["a","b","c","d"]))