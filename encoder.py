import base64
from tkinter import StringVar

def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        c = key[i % len(key)]
        enc.append(chr((ord(msg[i]) + ord(c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, msg):
    dec = []
    msg = base64.urlsafe_b64decode(msg).decode()
    for i in range(len(msg)):
        c = key[i % len(key)]
        dec.append(chr((256 + ord(msg[i]) - ord(c)) % 256))
    return "".join(dec)

def messageProcessor(mode, key, msg):
    result = StringVar()
    if (mode.get() == "encode"):
        result = encode(key.get(), msg.get())
    elif (mode.get() == "decode"):
        result = decode(key.get(), msg.get())
    else:
        result = "Invalid Mode"
    return result
