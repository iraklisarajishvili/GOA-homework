# 5)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგი და ინტეჯერი, ასევე ფუნქციას ქონდეს სია რომელშიც ჩაამატებ მომხმარებლის შემოტანილ სტრინგს იმ ინდექსზე რომელიც მან შემოიტანა


def insert_item(text, index):
    arr = []
    arr.insert(index, text)
    print(arr)

insert_item("hello", 0)
insert_item("giorgi", 0)