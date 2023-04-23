import qrcode
import os
import re
import subprocess

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

# function to generate QR code for wifi
def generate_wifi_qr_code(ssid, password, security_type, os):
    if os == "android":
        if security_type == "WEP":
            network_type = "WEP"
        elif security_type == "WPA" or security_type == "WPA2":
            network_type = "WPA"
        else:
            raise ValueError("Invalid security type")

        subprocess.call(["qrencode", "-s", "10", "-o", ssid + ".png", "WIFI:S:" + ssid + ";T:" + network_type + ";P:" + password + ";;"])
    elif os == "windows" or os == "linux":
        if security_type == "WEP":
            network_type = "WEP"
        elif security_type == "WPA" or security_type == "WPA2":
            network_type = "WPA"
        else:
            raise ValueError("Invalid security type")

        subprocess.call(["qrencode", "-s", "10", "-o", ssid + ".png", "WIFI:T:" + network_type + ";S:" + ssid + ";P:" + password + ";;"])
    else:
        raise ValueError("Invalid operating system")

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
print("3. WiFi")
print("4. Custom Text")
print("5. Banking Account")
mode = int(input("Enter mode number: "))

if mode == 1:
    phone_option = input("Enter '1' to manually input phone numbers or '2' to read from file: ")
    if phone_option == '1':
        phone_number = input("Enter phone number (including country code): ")
        generate_phone_qr_code(phone_number)
    elif phone_option == '2':
        filename = input("Enter filename: ")
        with open(filename) as f:
            for line in f:
                phone_number = line.strip()
                generate_phone_qr_code(phone_number)

elif mode == 2:
    url = input("Enter URL: ")
    generate_url_qr_code(url)

elif mode == 3:
    ssid = input("Enter SSID: ")
    password = input("Enter password: ")
    security_type = input("Enter security type (WEP, WPA, WPA2): ")
    os = input("Enter operating system (android, windows, linux): ")
    generate_wifi_qr_code(ssid, password, security_type, os)

elif mode == 4:
    custom_text_option = input("Enter '1' to manually input custom text or '2' to read from file: ")
    if custom_text_option == '1':
        custom_text = input("Enter custom text: ")
        generate_custom_text_qr_code(custom_text)
    elif custom_text_option == '2':
        filename = input("Enter filename: ")
        with open(filename) as f:
            for line in f:
                custom_text = line.strip()
                generate_custom_text_qr_code(custom_text)

elif mode == 5:
    account_number = input("Enter account number: ")
    bank_code = input("Enter bank code: ")
    generate_banking_qr_code(account_number, bank_code)

else:
    print("Invalid mode number. Exiting program.")


