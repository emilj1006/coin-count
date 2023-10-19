# Get the volunteer's name from the user
volunteer_name = input("Enter the volunteer's name: ")

# Get the type of coin from the user
coin_type = input("Enter the type of coin: ")

# Get the weight of the bag from the user
weight_of_bag = float(input("Enter the weight of the bag: "))

# Print the collected information
print("Volunteer's Name:", volunteer_name)
print("Type of Coin:", coin_type)
print("Weight of bag in grams:", weight_of_bag)

# List of valid coin types
valid_coin_types = ["pounds"]

# Get the coin type from the user
coin_type = input("Enter the type of coin: ")

# Check if the entered coin type is valid
if coin_type.lower() in valid_coin_types:
    print("Valid coin type:", coin_type)
else:
    print("Invalid coin type. Please enter a valid coin type from the following: " + ", ".join(valid_coin_types))

# List of valid coin types and their weights in grams
valid_coin_types = {
    "pounds": 5.67,
}

# Get the coin type from the user
coin_type = input("Enter the type of coin: ")

# Get the weight of the bag from the user
weight_of_bag = float(input("Enter the weight of the bag (in grams): "))

# Check if the entered coin type is valid
if coin_type.lower() in valid_coin_types:
    coin_weight = valid_coin_types[coin_type.lower()]
    expected_weight = coin_weight  # Assuming one coin for now

    # Calculate the number of coins needed to correct the weight
    num_coins_needed = round(weight_of_bag / expected_weight)
    if num_coins_needed == 0:
        print("The bag weight is accurate.")
    else:
        print(f"You need to add or remove {abs(num_coins_needed)} {coin_type}{'s' if num_coins_needed < 0 else ''} to correct the bag's weight.")
else:
    print("Invalid coin type. Please enter a valid coin type.")

# Initialize variables for running totals
bags_checked = 0
total_value = 0

# List of valid coin types and their values
valid_coin_types = {
    "pounds": 0.25,
    
}

while True:
    # Get the coin type from the user
    coin_type = input("Enter the type of coin (or 'exit' to quit): ")

    # Check if the user wants to exit
    if coin_type.lower() == 'exit':
        break

    # Get the weight of the bag from the user
    weight_of_bag = float(input("Enter the weight of the bag (in grams): "))

    # Check if the entered coin type is valid
    if coin_type.lower() in valid_coin_types:
        coin_weight = valid_coin_types[coin_type.lower()]
        expected_weight = coin_weight  # Assuming one coin for now

        # Calculate the number of coins in the bag
        num_coins = round(weight_of_bag / expected_weight)

        # Update running totals
        bags_checked += 1
        total_value += num_coins * valid_coin_types[coin_type.lower()]

        print(f"You've checked {num_coins} {coin_type}{'s' if num_coins > 1 else ''} in the bag.")
    else:
        print("Invalid coin type. Please enter a valid coin type.")

# Display the final results
print(f"Total bags checked: {bags_checked}")
print(f"Total value of all coins: £{total_value:.2f}")
