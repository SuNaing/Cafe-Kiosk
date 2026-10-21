
# Extract & Verify Attacker IPs from Logs

raw_log = "ALERT , 2026-10-19 , 192.168.4.11 , SQL_Injection_Attempt"
ip = raw_log.split(" , ")[2]
print(ip)

date=raw_log.split(" , ")[1]
print(date)

warning_message = raw_log.split(" , ")[3]
print(warning_message)

banned_ips = ("10.0.0.1", "192.168.4.11", "172.16.0.5")
if ip in banned_ips:
    print("Trigger Alert XXX!!!: Banned IP detected!",ip)

    user_input = input("Enter your IP address to verify: ")
    if user_input == ip:
        print("IP address verified successfully.")