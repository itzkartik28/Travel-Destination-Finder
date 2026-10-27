print("===== Travel Destination Finder =====")

print("\nEnter your travel budget:")
print("1. Low Budget")
print("2. Medium Budget")
print("3. High Budget")

budget = int(input("Choose your budget (1-3): "))

print("\nChoose your interest:")
print("1. Nature")
print("2. Adventure")
print("3. History")

interest = int(input("Enter your interest (1-3): "))

print("\nRecommended Travel Destinations:")

if budget == 1:
    if interest == 1:
        print("Destination: Lonavala")
    elif interest == 2:
        print("Destination: Matheran")
    elif interest == 3:
        print("Destination: Pune")
    else:
        print("Invalid interest choice")

elif budget == 2:
    if interest == 1:
        print("Destination: Mahabaleshwar")
    elif interest == 2:
        print("Destination: Rishikesh")
    elif interest == 3:
        print("Destination: Jaipur")
    else:
        print("Invalid interest choice")

elif budget == 3:
    if interest == 1:
        print("Destination: Kerala")
    elif interest == 2:
        print("Destination: Manali")
    elif interest == 3:
        print("Destination: Agra")
    else:
        print("Invalid interest choice")

else:
    print("Invalid budget choice")

print("\nThank you for using Travel Destination Finder!")
