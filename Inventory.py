# IT Procurement and Deployment - Laptop Inventory Tracker

# 1. Immutable approved models list (tuple)
approved_models = ("MacBook Pro", "Dell XPS", "ThinkPad")

# 2. Dynamic device storage (list)
device_inventory = []

# 3. Persistent menu
while True:
    print("\n--- Device Inventory Menu ---")
    print("1: Add")
    print("2: Remove")
    print("3: View")
    print("4: Exit")
    choice = input("Choose an action (1-4): ")

    # 4. Add a device (validated against the tuple)
    if choice == "1":
        device = input("Enter a device name: ")
        if device in approved_models:
            device_inventory.append(device)
            print(device + " added to inventory.")
        else:
            print("Error: Device model not approved for company use.")

    # 5. Safe removal
    elif choice == "2":
        device = input("Enter a device to remove: ")
        if device in device_inventory:
            device_inventory.remove(device)
            print(device + " removed from inventory.")
        else:
            print("Device not found.")

    # 4. View inventory
    elif choice == "3":
        print("Current inventory:", device_inventory)

    # Exit
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")