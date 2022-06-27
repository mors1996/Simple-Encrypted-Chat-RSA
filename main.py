# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import classes.RSA
from classes import RSA

RSA = classes.RSA.RSA()
enc = []
dec = ""


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    generateKeys()


def encodeMsg():
    global enc
    ci = input("Hello, Alice. Send a message to Bob: ")
    encrypted = RSA.encrypt(ci)
    enc = encrypted


def decodeMsg(msg):
    global dec
    dec = RSA.decrypt(msg)
    print("\nMESSAGE FROM ALICE: " + dec)


def generateKeys():
    RSA.main()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmd = ""
    print_hi('PyCharm')
    encodeMsg()
    cmd = input("\nHi there, Bob. You just received a message."
                "\n What would you like to do?"
                "\n e: exit, d: decrypt, s: show encrypted : ")
    if cmd != "e":
        if cmd == "d": decodeMsg(enc)
        if cmd == "s": print("\nORIGINAL MESSAGE: ",  enc)

    while cmd != "e":
        cmd = input("\n e: exit, d: decrypt, s: show encrypted : ")
        if cmd == "d": decodeMsg(enc)
        if cmd == "s": print("\nORIGINAL MESSAGE: ",  enc)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
