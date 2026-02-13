# James Karuri
# Date: 11/02/2026
# String formatting

# Get string length
sentence = "I star gaze"

string_length = len(sentence)

print(f"The length is: {string_length}")

# Spliting a string
sentence_2 = "Mathematics Physics"
split = sentence_2.split(" ")

print(f"the first subject is: ", split[0])

# Make everything caps
mpesa_code = "udb1234"

capitalized = mpesa_code.upper()

print(f"New mpesa code: ", capitalized)

#Splitting a message
mpesa_text = "You have received 40KES from Phillip"
split_mpesa = mpesa_text.split(" 40KES ")

print(f"New mpesa_text:", split_mpesa[0])

# Make everything lower
mpesa_code = "New oFFeR"

made_lower = mpesa_code.lower()

print("New mpesa code: ", made_lower)


# Replacing characters in a string

balance = "9000Kes"      
amount_added = "400Kes"

cleaned_balance = balance.replace("Kes", "")

print("new_balance: ", cleaned_balance)

cleaned_ammount_added = amount_added.replace("Kes", "")

print("new_amount_added: ", cleaned_ammount_added)

new_balance = int(cleaned_balance) + int(cleaned_ammount_added)

print("The new balance is:", new_balance)

sentence_4 = "You have received 40KES from Phillip"
split = sentence_4.split(" ")
print(f"The first word is: ", split[3]) 

balance = "12.02 KES"
amount_added = "40 KES"

cleaned_balance = balance.replace("KES", "")
print("new_balance: ", cleaned_balance)

cleaned_ammount_added = amount_added.replace("KES", "")
print("new_amount_added: ", cleaned_ammount_added)

new_balance = float(cleaned_balance) + float(cleaned_ammount_added)
print("The new balance is:", new_balance)
 