# Pre Request

```sudo apt install android-tools-adb```

```sudo apt install android-tools-fastboot```

```sudo apt install python```

```sudo apt install git```

```git clone https://github.com/panchalravi004/AiCrack```

# Process to find IP

```adb devices``` --> To show all devices

Connect your PC and targeted android on same network

```nmap 192.168.43.0/24``` --> To scan whole subnet

You find targeted device ip in my case 192.168.43.100

# Process to connect with targeted phone

```adb connect 192.168.43.100:5034```

Allow on targeted device for debugging for the first time

# Use AiCrack

```cd AiCrack```

```python3 AiCrack.py```

Now you will be able to control android phone


