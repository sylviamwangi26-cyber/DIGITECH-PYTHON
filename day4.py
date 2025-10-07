# === LOGIN SYSTEM WITH ACCESS CONTROL + ERROR HANDLING ===

# Step 1: Store usernames, passwords, and roles
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "sylvia": {"password": "user123", "role": "user"},
    "mark": {"password": "user456", "role": "user"}
}

try:
    # Step 2: Ask for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Step 3: Validate login credentials
    if username in users and password == users[username]["password"]:
        role = users[username]["role"]
        print(f"\n✅ Login successful! Welcome, {username} ({role}).\n")

        # Step 4: Access control for admin
        if role == "admin":
            while True:
                try:
                    print("=== ADMIN MENU ===")
                    print("1. View all users")
                    print("2. Add a new user")
                    print("3. Delete a user")
                    print("4. Logout")

                    choice = int(input("Choose an option (1-4): "))

                    if choice == 1:
                        print("👥 Users:", ", ".join(users.keys()))

                    elif choice == 2:
                        new_user = input("Enter new username: ")
                        if new_user in users:
                            print("⚠️ User already exists.")
                        else:
                            new_pass = input("Enter password for new user: ")
                            users[new_user] = {"password": new_pass, "role": "user"}
                            print(f"✅ User '{new_user}' added successfully!")

                    elif choice == 3:
                        del_user = input("Enter username to delete: ")
                        if del_user in users:
                            if del_user == "admin":
                                print("❌ You cannot delete the admin.")
                            else:
                                del users[del_user]
                                print(f"🗑️ User '{del_user}' deleted successfully.")
                        else:
                            print("❌ User not found.")

                    elif choice == 4:
                        print("Logging out...")
                        break

                    else:
                        print("❌ Invalid menu option. Please enter 1–4.")

                    print()  # blank line for readability

                except ValueError:
                    print("⚠️ Invalid input! Please enter a number (1–4).")

        # Step 5: Access control for normal user
        else:
            while True:
                try:
                    print("=== USER MENU ===")
                    print("1. View my profile")
                    print("2. Change my password")
                    print("3. Logout")

                    choice = int(input("Choose an option (1-3): "))

                    if choice == 1:
                        print(f"👤 Username: {username}, Role: {role}")

                    elif choice == 2:
                        new_pw = input("Enter your new password: ")
                        users[username]["password"] = new_pw
                        print("✅ Password updated successfully!")

                    elif choice == 3:
                        print("Logging out...")
                        break

                    else:
                        print("❌ Invalid choice. Please enter 1–3.")
                    print()

                except ValueError:
                    print("⚠️ Invalid input! Please enter a number (1–3).")

    else:
        print("❌ Login failed. Invalid username or password.")

# Step 6: Handle unexpected errors
except Exception as e:
    print("🚨 An unexpected error occurred:", e)