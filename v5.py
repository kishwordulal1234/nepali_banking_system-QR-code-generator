import qrcode
import os
import re

# function to generate QR code for phone number
def generate_phone_qr_code(phone_number):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data("tel:" + phone_number)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')
    img.save(phone_number + ".jpg")

# function to generate QR code for URL
def generate_url_qr_code(url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')
    img.save(re.sub('[^0-9a-zA-Z]+', '', url) + ".jpg")

# function to generate QR code for custom text
def generate_custom_text_qr_code(custom_text):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(custom_text)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')
    img.save(custom_text + ".jpg")

# function to generate QR code for banking account
def generate_banking_qr_code(account_number, bank_code):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data("bank:" + bank_code + ";account:" + account_number)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')
    img.save(account_number + ".jpg")

# main program
print("Choose mode:")
print("1. Phone Number")
print("2. URL")
print("3. Custom Text")
print("4. Banking Account")
mode = int(input("Enter mode number: "))

if mode == 1:
    phone_option = input("Enter '1' to manually input phone numbers or '2' to read from file: ")
    if phone_option == '1':
        phone_number = input("Enter phone number (including country code): ")
        generate_phone_qr_code(phone_number)
    elif phone_option == '2':
        filename = input("Enter the name of the file with phone numbers: ")
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                for phone_number in f:
                    generate_phone_qr_code(phone_number.strip())
        else:
            print("File not found.")
elif mode == 2:
    url_option = input("Enter '1' to manually input URLs or '2' to read from file: ")
    if url_option == '1':
        url = input("Enter URL: ")
        generate_url_qr_code(url)
    elif url_option == '2':
        filename = input("Enter the name of the file with URLs: ")
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                for url in f:
                    generate_url_qr_code(url.strip())
        else:
            print("File not found.")
elif mode == 3:
    custom_text = input("Enter text: ")
    generate_custom_text_qr_code(custom_text)
elif mode == 4:
    account_number = input("Enter account number: ")
    bank_code = input("Enter bank code: ")
    generate_banking_qr_code(account_number, bank_code)
else:
    print("Invalid mode number.")

