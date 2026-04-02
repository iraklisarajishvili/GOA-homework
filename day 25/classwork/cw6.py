# 6)შექმენით len ფუნქციის იდენტური ვარიანტი


def my_len(arr):
    count = 0
    for i in arr:
        count += 1
    return count

print(my_len([1,2,3,4]))
print(my_len("hello"))