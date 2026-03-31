# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

apple_count = shelf.count("apples")
print(f"Number of Apples: {apple_count}")

banana_index = shelf.index("bananas")
print(f"first Banana Index: {banana_index}")

if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")
    
if (shelf.count("grapes") < 2):
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficently stocked.")

if "oranges" in shelf:
    orange_index = shelf.index("oranges")
    print(f"Oranges are at index: {orange_index}")
else:
    print("Oranges are out of stock.")
