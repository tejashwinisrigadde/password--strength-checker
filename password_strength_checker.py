import string

password = input("🔐 Enter password: ")
print()

has_upper = any(ch in string.ascii_uppercase for ch in password)
has_lower = any(ch in string.ascii_lowercase for ch in password)
has_digit = any(ch in string.digits for ch in password)
has_special = any(ch in string.punctuation for ch in password)

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("✅ Strong Password! 🎉🔒")
else:
    print("❌ Weak Password\n")

    if len(password) < 8:
        print("📏 Password should contain at least 8 characters.\n")

    if not has_upper:
        print("🔠 Password should contain uppercase letters.\n")

    if not has_lower:
        print("🔡 Password should contain lowercase letters.\n")

    if not has_digit:
        print("🔢 Password should contain digits.\n")

    if not has_special:
        print("🔒 Password should contain special characters.\n")