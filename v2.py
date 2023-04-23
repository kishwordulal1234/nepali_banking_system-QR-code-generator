import qrcode
import os

# function to validate if input is a valid phone number
def is_valid_phone_number(phone_number):
    if phone_number.startswith("+"):
        phone_number = phone_number[1:]
    if phone_number.isdigit() and len(phone_number) >= 10 and len(phone_number) <= 15:
        return True
    else:
        return False

# function to validate if input is a valid URL
def is_valid_url(url):
    if url.startswith("http://") or url.startswith("https://"):
        return True
    else:
        return False

# function to generate QR code for phone number
def generate_phone_number_qr_code(phone_number):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data("tel:" + phone_number)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("phone_number_qr_code.jpg", "JPEG", quality=100)

# function to generate QR code for URL
def generate_url_qr_code(url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("url_qr_code.jpg", "JPEG", quality=100)

# function to generate QR code for wifi
def generate_wifi_qr_code(ssid, security_type, password, os_type):
    if os_type == "Android":
        wifi_str = f"WIFI:S:{ssid};T:{security_type};P:{password};;"
    elif os_type == "Windows" or os_type == "Linux":
        wifi_str = f"WIFI:T:{security_type};S:{ssid};P:{password};;"
    else:
        print("QR code generation for wifi is only supported on Android, Windows, and Linux.")
        return

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(wifi_str)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("wifi_qr_code.jpg", "JPEG", quality=100)

# main program
print("Choose mode:")
print("1. Phone Number")
print("2. URL")
print("3. Wi-Fi")
mode = int(input("Enter mode number: "))

if mode == 1:
    phone_number = input("Enter phone number: ")
    if is_valid_phone_number(phone_number):
        generate_phone_number_qr_code(phone_number)
        print("QR code generated successfully.")
    else:
        print("Invalid phone number. Please enter a valid phone number.")

elif mode == 2:
    url = input("Enter URL: ")
    if is_valid_url(url):
        generate_url_qr_code(url)
        print("QR code generated successfully.")
    else:
        print("Invalid URL. Please enter a valid URL.")

elif mode == 3:
    os_type = input("Enter your operating system (Android/Windows/Linux): ").lower()
    if os_type == "android" or os_type == "windows" or os_type == "linux":
        ssid = input("Enter SSID: ")
        security_type = input("Enter security type (WEP/WPA/WPA2): ")
        password = input("Enter password: ")
        bssid = input("Enter BSSID (optional): ")
        if ssid and security_type and password:
            generate_wifi_qr_code(ssid='MyWiFiNetwork', password='MyPassword', security='WPA', os='Android')


