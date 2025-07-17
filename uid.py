import time
from os import system as c

# Color Codes
G = '\033[1;32m'
R = '\033[1;31m'
Y = '\033[1;33m'
C = '\033[1;36m'
P = '\033[95m'
W = '\033[1;37m'

def banner():
    c("clear")
    print(f"""{G}
██╗    ██╗██╗███████╗██╗
██║    ██║██║██╔════╝██║
██║ █╗ ██║██║███████╗██║
██║███╗██║██║╚════██║╚═╝
╚███╔███╔╝██║███████║██╗
 ╚══╝╚══╝ ╚═╝╚══════╝╚═╝
{Y}WIFI PASSWORD HACK TOOL (NON-ROOT)
       {C}VIP | HACKING WORLD™
""")

def loading(msg, sec):
    for i in range(sec):
        print(f"{Y}{msg}{'.' * (i % 4)}", end='\r')
        time.sleep(1)

def main():
    banner()
    wifi = input(f"{C}Enter WiFi Network Name (SSID): {W}")
    print()
    loading("🔎 Scanning Nearby Networks", 3)
    print(f"{G}✓ Network Detected: {wifi}")
    time.sleep(1.5)
    print(f"{Y}[!] BSSID Found: 44:1A:92:AB:CD:99")
    time.sleep(1)
    print(f"{C}[✓] Signal Strength: -54dBm")
    time.sleep(1)
    print(f"{P}[✓] Network Vulnerable: WPS Enabled")
    time.sleep(2)

    loading("🚀 Launching Password Attack", 4)
    print(f"{G}✓ Password Cracked Successfully!\n")
    time.sleep(1.5)

    fake_pass = "alamin1122"
    print(f"{R}★ Cracked Password: {W}{fake_pass}")
    print(f"{C}Use this password to connect.\n")

    input(f"{Y}Press Enter to Exit...")

main()