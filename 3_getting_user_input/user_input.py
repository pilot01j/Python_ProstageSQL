name = input("Enter your name: ")
print(name)
print("------------------------------------------------------------------")
size_input = input("How big is your house (m2): ")
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(f"{square_meters:_.2f} square feet is {square_meters:.2f} square meters.")
