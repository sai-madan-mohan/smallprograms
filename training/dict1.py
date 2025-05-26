
# suits = {
#     "name":"mark45",
#     "year":2024,
#     "specification":"Arc"
# }

# # accessing the elements
# print(suits["year"])

# # replacing
# suits["year"]=2025
# print(suits)


# suits = {"mark45":{"year":2024,"tech":"Arc"},
#             "mark90":{"year":2025,"tech":"Nano"}}
# print(suits["mark90"]["tech"])

# # mergeing two dictionaries
# suit_a = {"mark45":2018,"mark90":2022}
# suit_b = {"mark100":2023,"hulkbuster":2024}
# suit_a.update(suit_b)
# print(suit_a)


# age= 20
# if age<18:
#     print("you are not eligible to vote")
# else:
#     print("you are eligible to vote")



import time

for i in range(5, 0, -1):
    print(f"Self-destruct in {i}...")
    time.sleep(1)
print("Boom! 💥")