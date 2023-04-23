import qrcode
import os
import re
import platform

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

def generate_phone_qr_code(phone_number):
    if not re.match(r'^\+\d{1,3}\d{3,}$', phone_number):
        print("Invalid phone number format. Please enter a phone number in the format +[country code][number].")
        return

    file_name = f"{phone_number}.jpg"
    generate_qr_code(f"tel:{phone_number}", file_name)
    print(f"QR code for phone number {phone_number} has been generated.")

def generate_url_qr_code(url):
    if not re.match(r'^http[s]?:\/\/', url):
        print("Invalid URL format. Please enter a valid URL starting with http:// or https://.")
        return

    file_name = f"{url.replace('/', '-')}.jpg"
    generate_qr_code(url, file_name)
    print(f"QR code for URL {url} has been generated.")

def generate_wifi_qr_code(ssid, password, security_mode, os_type):
    if os_type != "Windows" and os_type != "Linux" and os_type != "Android":
        print("This feature is only supported on Windows, Linux, and Android.")
        return

    wifi_str = f"WIFI:T:{security_mode};S:{ssid};P:{password};;"
    file_name = f"{ssid}.jpg"
    generate_qr_code(wifi_str, file_name)
    print(f"QR code for WiFi network {ssid} has been generated.")

def generate_from_file(file_name):
    if not os.path.isfile(file_name):
        print(f"{file_name} does not exist.")
        return

    with open(file_name) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith("+"):
            generate_phone_qr_code(line)
        elif re.match(r'^http[s]?:\/\/', line):
            generate_url_qr_code(line)
        else:
            print(f"Invalid data in {file_name}: {line}")

def main():
    print("Choose mode:")
    print("1. Generate QR code for a phone number")
    print("2. Generate QR code for a URL")
    print("3. Generate QR code for a WiFi network")
    print("4. Generate QR code from file")
    mode = int(input("Enter mode number: "))

    if mode == 1:
        phone_number = input("Enter phone number: ")
        generate_phone_qr_code(phone_number)
    elif mode == 2:
        url = input("Enter URL: ")
        generate_url_qr_code(url)
    elif mode == 3:
        ssid = input("Enter WiFi SSID: ")
        password = input("Enter WiFi password: ")
        security_mode = input("Enter WiFi security mode (WEP/WPA/WPA2): ")
        os_type = platform.system()
        generate_wifi_qr_code(ssid, password, security_mode, os_type)
    elif mode == 4:
        file_name = input("Enter file name: ")
        generate_from_file(file_name)
    else:
        print("Invalid mode number.")

if __name__ == "__main__":
    main()

