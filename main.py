print("=== OTP SMART NOTIFICATION AGENT ===\n")

notifications = []

print("Enter notifications one by one.")
print("Type 'done' when finished.\n")

while True:
    msg = input("> ")
    if msg.lower() == "done":
        break
    if msg.strip() == "":
        continue
    notifications.append(msg)

otp_keywords = ["otp", "one time password", "valid", "code"]

otp_messages = []
spam_messages = []

for message in notifications:
    text = message.lower()
    is_otp = False

    for word in otp_keywords:
        if word in text:
            is_otp = True
            break

    if is_otp:
        otp_messages.append(message)
    else:
        spam_messages.append(message)

print("\n------------------------------")
print("IMPORTANT OTP MESSAGES")
print("------------------------------")

if len(otp_messages) == 0:
    print("No OTP messages found.")
else:
    for otp in otp_messages:
        print("- " + otp)

print("\n------------------------------")
print("SPAM / OTHER MESSAGES")
print("------------------------------")

if len(spam_messages) == 0:
    print("No spam messages found.")
else:
    for spam in spam_messages:
        print("- " + spam)

print("\n------------------------------")
print("SUMMARY")
print("------------------------------")
print("Total messages received :", len(notifications))
print("OTP messages detected  :", len(otp_messages))
print("Spam messages detected :", len(spam_messages))
