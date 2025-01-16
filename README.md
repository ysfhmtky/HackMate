# HackMate

HackMate is a Python-based tool that simplifies payload generation and listener management using the Metasploit Framework and `msfvenom`. It is designed for cybersecurity professionals and ethical hackers to quickly and efficiently create and manage payloads for various platforms.

## Features

- **Payload generation** for Windows, Linux, Android, MacOS, and Web.
- **Staged and Stageless** payload options.
- Dynamic **LHOST** and **LPORT** configuration.
- Customize payloads with **encoder** and **iterations**.
- Automatically start a **Metasploit listener**.

## Installation

### Requirements

- Python 3.x
- Metasploit Framework
- `pyfiglet` and `colorama` libraries

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/ysfhmtky/HackMate.git
   cd HackMate
   ```

2. Install the required Python libraries:
   ```bash
   pip install pyfiglet colorama
   ```

3. Ensure Metasploit Framework is installed:
   ```bash
   sudo apt install metasploit-framework
   ```

4. Run HackMate:
   ```bash
   python HackMate.py
   ```

## Usage

### Starting the Program

When you start the program, you will see the following menu:

```
Payload Options:
1. Windows Payloads
2. Linux Payloads
3. Android Payloads
4. MacOS Payloads
5. Web Payloads
6. Staged vs. Stage-less Payloads
0. Exit
```

### Generating a Payload

1. Select the desired payload type (e.g., Windows Payloads).
2. Choose the payload (e.g., `windows/meterpreter/reverse_tcp`).
3. Enter the **LHOST** (your IP) and **LPORT** (your port).
4. Specify the output file name (e.g., `payload.exe`).
5. Optionally, provide an encoder and iterations.
6. The payload will be generated, and a Metasploit listener will start automatically.

### Stopping the Listener

To stop the listener and return to the main menu, type `exit`.

## Examples

### Generating a Windows Payload

1. Select **Windows Payloads**.
2. Choose `windows/meterpreter/reverse_tcp`.
3. Enter the **LHOST** and **LPORT** values.
4. Specify the output file name (e.g., `payload.exe`).
5. The payload will be generated, and a listener will start.

### Generating a Linux Payload

1. Select **Linux Payloads**.
2. Choose `linux/x86/meterpreter_reverse_tcp`.
3. Enter the **LHOST** and **LPORT** values.
4. Specify the output file name (e.g., `payload.elf`).
5. The payload will be generated, and a listener will start.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request. Bug fixes and feature suggestions are appreciated.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

GitHub: [ysfhmtky](https://github.com/ysfhmtky)
