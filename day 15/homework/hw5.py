# 5) დაწერე პროგრამა, რომელიც ამოწმებს პაროლის სიგრძეს.
# თუ პაროლი 8 სიმბოლოზე ნაკლებია → „სუსტი პაროლი“,
# წინააღმდეგ შემთხვევაში → „კარგი პაროლი“.



password = input("enter the password: ")

if len(password) < 8:
    print("Weak password")
else:
    print("Good password")