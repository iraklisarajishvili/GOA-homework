# 7)შექმენით sum ფუნქციის იდენტური ვარიანტი (sum ფუნქციას გადაეცემა ინტეჯერების სია და გამოაქ ამ ინტეჯერების ჯამი)



def my_sum(arr):
    total = 0
    for i in arr:
        total += i
    return total

print(my_sum([1,2,3]))
print(my_sum([5,6,7,8]))