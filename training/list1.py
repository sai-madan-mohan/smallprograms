suits = ["mark25", "mark45", "hulkbuster"]

# for accessing elements using index
print(suits[0])
print(suits[-1])
# replacing element
suits[1]="mark90"
print(suits)
suits.append("mark85")
print(suits)
suits.insert(1,"mark45")
print(suits)
suits.remove("mark25")
print(suits)

for suit in suits:
    print("Deploying suits : ",suits)