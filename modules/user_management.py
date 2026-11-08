import json
import hashlib
import secrets
import hmac
from modules.email_service import verify_email_code

# Student and Admin Management


# SECTION 4: Create Account Page
def create_account():
    print("\n========== CREATE ACCOUNT ==========")

    # Collect student information
    full_name = input("Enter your full name: ")
    username = input("Create a username: ")
    email = input("Enter your email address: ")
    password = input("Create a password: ")
    confirm_password = input("Confirm your password: ")

    # Validate the information
    if full_name == "" or username == "" or email == "" or password == "" or confirm_password == "":
        print("\nError: All fields are required.")

    elif len(username) < 4:
        print("\nError: Username must have at least 4 characters.")

    elif len(password) < 6:
        print("\nError: Password must have at least 6 characters.")

    elif password != confirm_password:
        print("\nError: Passwords do not match.")

    else:
        # Load existing student accounts
        with open("data/users.json", "r") as file:
            students = json.load(file)

        # Check for duplicate username
        for student in students:
            if student["username"] == username:
                print("\nError: Username already exists!")
                return

        # Check for duplicate email
        for student in students:
            if student["email"] == email:
                print("\nError: Email already registered!")
                return
            
        # Verify student email address
        print("\nA verification code will be sent to your email.")

        if not verify_email_code(email):
            print("\nAccount creation cancelled.")
            return
                
        # Generate Student ID
        student_id = f"STU{len(students) + 1:03d}"



        password_plaintext = password
        # Protect student password
        password_salt = secrets.token_hex(16)

        password_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            password_salt.encode("utf-8"),
            100000
        ).hex()
        
        # Create student account
        new_student = {
            "student_id": student_id,
            "full_name": full_name,
            "username": username,
            "email": email,
            "password_plaintext": password_plaintext,
            "password_hash": password_hash,
            "password_salt": password_salt
        }
        # Add student to the list
        students.append(new_student)

        # Save student accounts to JSON
        with open("data/users.json", "w") as file:
            json.dump(students, file, indent=4)


        # Display success message
        print("\nAccount created successfully!")
        print("Welcome to EventVerse,", full_name)
        print("Your Student ID:", student_id)
        print("Your username:", username)

# SECTION 3: Student Login Page
def student_login(open_dashboard):
    print("\n========== STUDENT LOGIN ==========")

    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    # Load student accounts
    with open("data/users.json", "r") as file:
        students = json.load(file)

    # Find the student account
    for student in students:

        if student["username"].lower() == username.lower():

            # Hash the entered password using the stored salt
            entered_hash = hashlib.pbkdf2_hmac(
                "sha256",
                password.encode("utf-8"),
                student["password_salt"].encode("utf-8"),
                100000
            ).hex()

            # Compare the entered password hash with the stored hash
            if hmac.compare_digest(entered_hash, student["password_hash"]):

                print("\nLogin successful!")
                print("Welcome,", student["full_name"])

                open_dashboard(student)
                return

            else:
                print("\nIncorrect username or password.")
                return

    print("\nIncorrect username or password.")


# SECTION: Student Profile
def student_profile(student):

    print("\n========================================")
    print("             MY PROFILE")
    print("========================================")

    print("\nStudent ID:", student["student_id"])
    print("Full Name:", student["full_name"])
    print("Username:", student["username"])
    print("Email:", student["email"])

    print("\n========================================")




# SECTION: Forgot Password
def reset_password():

    print("\n========== FORGOT PASSWORD ==========")

    email = input("Enter your registered email address: ").strip()

    # Load student accounts
    with open("data/users.json", "r") as file:
        students = json.load(file)

    # Find the registered email
    selected_student = None

    for student in students:
        if student["email"].lower() == email.lower():
            selected_student = student
            break

    if selected_student is None:
        print("\nError: No account found with this email address.")
        return

    # Verify email ownership
    print("\nA password reset verification code will be sent to your email.")

    if not verify_email_code(email):
        print("\nPassword reset cancelled.")
        return

    # Create a new password
    new_password = input("\nEnter your new password: ")
    confirm_password = input("Confirm your new password: ")

    if len(new_password) < 6:
        print("\nError: Password must have at least 6 characters.")
        return

    if new_password != confirm_password:
        print("\nError: Passwords do not match.")
        return

    # Generate a new password salt
    new_salt = secrets.token_hex(16)

    # Hash the new password
    new_hash = hashlib.pbkdf2_hmac(
        "sha256",
        new_password.encode("utf-8"),
        new_salt.encode("utf-8"),
        100000
    ).hex()

    # Update the student account
    selected_student["password_salt"] = new_salt
    selected_student["password_hash"] = new_hash

    # Save updated accounts
    with open("data/users.json", "w") as file:
        json.dump(students, file, indent=4)

    print("\nPassword reset successfully!")
    print("You can now log in using your new password.")
