#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import websockets
import serial
import time
import threading

morse_dict = {
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
    'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
    'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--',
    'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
    '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----',
    ',':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'
}

async def send_char_morse(websocket, char):
    if char == " ":
        await websocket.send(" ")
    elif char in morse_dict:
        mc = morse_dict[char]
        for c in mc:
            await websocket.send(c)
    else:
        print("no such char : ", char)

async def send_hello(websocket, path):
    while True:
        await send_char_morse(websocket, "H")
        await send_char_morse(websocket, " ")
        await send_char_morse(websocket, "E")
        await send_char_morse(websocket, " ")
        await send_char_morse(websocket, "L")
        await send_char_morse(websocket, " ")
        await send_char_morse(websocket, "L")
        await send_char_morse(websocket, " ")
        await send_char_morse(websocket, "O")
        await send_char_morse(websocket, " ")
        await send_char_morse(websocket, " ")
        print("sending hello")
        await asyncio.sleep(5)

async def serial_reciever(websocket, path):
    print("start serial receiver")
    with serial.Serial('/dev/tty.usbserial-DJ00LWVR',9600,timeout=None) as ser:
        while True:
            signal = ser.read()
            print(signal.decode("ascii"))
            await websocket.send(signal.decode("ascii"))

if __name__ == '__main__':
    # start_server = websockets.serve(serial_reciever, 'localhost', 5001)
    start_server = websockets.serve(send_hello, 'localhost', 5001)
    print("running server...")
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
