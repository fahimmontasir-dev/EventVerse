
import os
import smtplib
import secrets
import time

from email.message import EmailMessage
from dotenv import load_dotenv


# Load Gmail credentials from .env
load_dotenv()


# Generate a 6-digit verification code
def generate_verification_code():
    return str(secrets.randbelow(900000) + 100000)


# Send verification email
def send_verification_email(recipient_email, verification_code):

    sender_email = os.getenv("EMAIL_ADDRESS")
    app_password = os.getenv("EMAIL_APP_PASSWORD")

    if not sender_email or not app_password:
        print("\nError: Email configuration is missing.")
        return False

    message = EmailMessage()

    message["Subject"] = "Your EventVerse Verification Code"
    message["From"] = f"EventVerse <{sender_email}>"
    message["To"] = recipient_email

    # Plain-text fallback
    message.set_content(f"""
Welcome to EventVerse!

Your verification code is: {verification_code}

This code expires in 5 minutes.

If you did not request this code, please ignore this email.

EventVerse Team
""")

    # HTML email version
    message.add_alternative(f"""
<!DOCTYPE html>
<html>
<body style="margin:0; padding:0; background-color:#f4f6f9;
             font-family:Arial,sans-serif;">

    <div style="max-width:600px; margin:40px auto;
                background-color:#ffffff; border-radius:12px;
                overflow:hidden;">

        <div style="background-color:#292d69; padding:30px;
                    text-align:center; color:white;">
            <h1 style="margin:0; font-size:28px;">EventVerse</h1>
            <p style="margin:10px 0 0;">
                Discover. Connect. Experience.
            </p>
        </div>

        <div style="padding:35px; text-align:center;">

            <h2 style="color:#222;">Verify Your Email</h2>

            <p style="color:#555; font-size:15px; line-height:1.6;">
                Welcome to EventVerse! We're excited to have you with us.
            </p>

            <p style="color:#555;">
                Use the verification code below to complete your registration.
            </p>

            <div style="background-color:#f0f1fa;
                        padding:20px; margin:25px 0;
                        border-radius:8px;">

                <h1 style="color:#292d69; letter-spacing:8px;
                           font-size:32px; margin:0;">
                    {verification_code}
                </h1>

            </div>

            <p style="color:#e05252; font-size:14px;">
                This code expires in 5 minutes.
            </p>

            <p style="color:#777; font-size:13px; line-height:1.6;">
                If you did not request this verification code,
                you can safely ignore this email.
            </p>

        </div>

        <div style="background-color:#f4f6f9;
                    padding:20px; text-align:center;">

            <p style="color:#888; font-size:12px;">
                © 2026 EventVerse. All rights reserved.
            </p>

            <p style="color:#888; font-size:12px;">
                Discover your next experience.
            </p>

        </div>

    </div>

</body>
</html>
""", subtype="html")

    # Send email through Gmail SMTP
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.send_message(message)

        print("\nVerification email sent successfully!")
        return True

    except Exception as error:
        print("\nFailed to send verification email.")
        print("Error:", error)
        return False


# Verify an email address using a temporary code
def verify_email_code(recipient_email):

    verification_code = generate_verification_code()

    email_sent = send_verification_email(
        recipient_email,
        verification_code
    )

    if not email_sent:
        return False

    expiry_time = time.time() + 300
    attempts = 5

    while attempts > 0:

        if time.time() > expiry_time:
            print("\nVerification code has expired.")
            return False

        entered_code = input(
            "\nEnter your 6-digit verification code: "
        ).strip()

        if time.time() > expiry_time:
            print("\nVerification code has expired.")
            return False

        if entered_code == verification_code:
            print("\nEmail verified successfully!")
            return True

        attempts -= 1

        print("\nIncorrect code!")
        print("Attempts remaining:", attempts)

    print("\nToo many incorrect attempts.")
    return False
