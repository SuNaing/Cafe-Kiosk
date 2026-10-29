#Initialize queue and start main loop
alert_queue=[]
while True:
# System Main Menu options:
    print("1. Log New Alert")
    print("2. View Alert Queue")
    print("3. Resolve Oldest Alert")
    print("4. Exit System")

    choice = input("Select an option: (1-4): ")
    if choice == "1":
        threat = input("Enter threat description: ")
        alert_queue.append(threat)
        print("Alert logged successfully!")

    elif choice == "2":
        print("--- Current Pending Alerts ---")
        # If the list is empty, this loop simply doesn't run
        for alert in alert_queue:
            print(alert)

    elif choice == "3":
        if len(alert_queue) > 0:
            resolved_threat = alert_queue.pop(0)
            print(f"Resolved and cleared: {resolved_threat}")
        else:
            print("No pending alerts. The queue is clear.")

    elif choice == "4":
        print("Exiting system. Goodbye, analyst.")
        break

    else:
        print("Invalid option. Please enter 1, 2, 3, or 4.")