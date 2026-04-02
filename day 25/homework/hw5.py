# 5) დაწერე ფუნქცია რომელიც იღებს სიტყვების სიას და აბრუნებს ყველაზე გრძელ სიტყვას.


def longest_word(words):
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest