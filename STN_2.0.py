from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser
import pyperclip
import time
import os
import json


# ! STN VERSION 2.0 !
# Developed @SSkipr


# // APPLICATION START //

# = LOCALS

InstalledVersion = "Version 2"
STNv = 2
Hsh = 0
TranslateError = 0

# = ACQUIRING VERIFIED IP

url = "https://stn-dev.w3spaces.com/user1ip.html" # ///
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
VerifiedIp = '\n'.join(chunk for chunk in chunks if chunk)

# = DEF FUNCTIONS

def TerminateSession(SecondDelay):
    print("[?] Your Session Will Terminate In",SecondDelay,"Seconds")
    time.sleep(SecondDelay)
    exit()

# -

def EnterLines(LinesToEnter):
    for _ in range(LinesToEnter):
        print("")
        
# = AQUIRING CURRENT IP

url = "http://ip-api.com/json/"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
CurrentIpString = '\n'.join(chunk for chunk in chunks if chunk)
data = json.loads(CurrentIpString)

CurrentIp = data.get("query")

# = PROCEED WITH APPLICATION // CHECK VERSION & ETC.

url = "https://stn-dev.w3spaces.com/version.html"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
AppVersion = '\n'.join(chunk for chunk in chunks if chunk)

if AppVersion == InstalledVersion:
    Hsh = 0
elif AppVersion == "Shutdown":
    EnterLines(1000)
    print("[!] STN Is Currently Shutdown")
    print("[?] Check Back Within 48 Hours")
    TerminateSession(20)
else:
    EnterLines(1000)
    print("[!] Update Available")
    print("[?] Contact Your Distributor For More Details")
    TerminateSession(20)

# = MECHANICS // IGNORE

def EncodePhrase():
    EnterLines(1000)
    TranslateError = 0
    Input = input("[!] Enter Prase To Encrypt | ")
    Input = Input.lower()
    counter = 0
    length = len(Input)
    Output = [""]
    while counter < length:
        if Input[counter] == 'c':
            Output.append("a")
                
        elif Input[counter] == 'd':
            Output.append("b")
                
        elif Input[counter] == 'e':
            Output.append("c")
                
        elif Input[counter] == 'f':
            Output.append("d")
                    
        elif Input[counter] == 'g':
            Output.append("e")
                
        elif Input[counter] == 'h':
            Output.append("f")
                
        elif Input[counter] == 'i':
            Output.append("g")
                
        elif Input[counter] == 'j':
            Output.append("h")
                
        elif Input[counter] == 'k':
            Output.append("i")
                
        elif Input[counter] == 'l':
            Output.append("j")
                
        elif Input[counter] == 'm':
            Output.append("k")
                
        elif Input[counter] == 'n':
            Output.append("l")
                
        elif Input[counter] == 'o':
            Output.append("m")
                
        elif Input[counter] == 'p':
            Output.append("n")
                
        elif Input[counter] == 'q':
            Output.append("o")
                
        elif Input[counter] == 'r':
            Output.append("p")
                
        elif Input[counter] == 's':
            Output.append("q")
                
        elif Input[counter] == 't':
            Output.append("r")
                
        elif Input[counter] == 'u':
            Output.append("s")
                
        elif Input[counter] == 'v':
            Output.append("t")
                
        elif Input[counter] == 'w':
            Output.append("u")
                
        elif Input[counter] == 'x':
            Output.append("v")
                
        elif Input[counter] == 'y':
            Output.append("w")
                
        elif Input[counter] == 'z':
            Output.append("x")
                
        elif Input[counter] == 'a':
            Output.append("y")
                
        elif Input[counter] == 'b':
            Output.append("z")
     
        elif Input[counter] == ' ':
            Output.append("#")

        elif Input[counter] == '6':
            Output.append("1")

        elif Input[counter] == '3':
            Output.append("2")

        elif Input[counter] == '7':
            Output.append("3")

        elif Input[counter] == '9':
            Output.append("4")

        elif Input[counter] == '2':
            Output.append("5")

        elif Input[counter] == '4':
            Output.append("6")

        elif Input[counter] == '8':
            Output.append("7")

        elif Input[counter] == '0':
            Output.append("8")

        elif Input[counter] == '5':
            Output.append("9")

        elif Input[counter] == '1':
            Output.append("0")

        elif Input[counter] == '?':
            Output.append(".")

        elif Input[counter] == '.':
            Output.append("?")
        else:
            TranslateError = 1
            if TranslateError == 0:
                Hsh = 0
            elif TranslateError == 1:
                print("[?] An Error In The Encryption Software Has Occorred")
                print("[?] Perhaps You Entered An Ivalid Character")
                TerminateSession(20)
            else:
                print("[&] An Internal Error Has Occurred")
                print("[&] No Explanation Given")
                TerminateSession(20)
        counter += 1
        if counter == length:
            if TranslateError == 0:
                EncryptedResult = ''.join(Output)
                print("[^] Encrypted Result:",EncryptedResult)
                pyperclip.copy(EncryptedResult)
                time.sleep(3)
                TerminateSession(20)
            
# -

def DecodePhrase():
    EnterLines(1000)
    TranslateError = 0
    Input = input("[!] Enter Phrase To Decrypt | ")
    Input = Input.lower()
    counter = 0
    length = len(Input)
    Output = [""]
    while counter < length:
        if Input[counter] == 'a':
            Output.append("c")
                
        elif Input[counter] == 'b':
            Output.append("d")
                
        elif Input[counter] == 'c':
            Output.append("e")
                
        elif Input[counter] == 'd':
            Output.append("f")
                    
        elif Input[counter] == 'e':
            Output.append("g")
                
        elif Input[counter] == 'f':
            Output.append("h")
                
        elif Input[counter] == 'g':
            Output.append("i")
                
        elif Input[counter] == 'h':
            Output.append("j")
                
        elif Input[counter] == 'i':
            Output.append("k")
                
        elif Input[counter] == 'j':
            Output.append("l")
                
        elif Input[counter] == 'k':
            Output.append("m")
                
        elif Input[counter] == 'l':
            Output.append("n")
                
        elif Input[counter] == 'm':
            Output.append("o")
                
        elif Input[counter] == 'n':
            Output.append("p")
                
        elif Input[counter] == 'o':
            Output.append("q")
                
        elif Input[counter] == 'p':
            Output.append("r")
                
        elif Input[counter] == 'q':
            Output.append("s")
                
        elif Input[counter] == 'r':
            Output.append("t")
                
        elif Input[counter] == 's':
            Output.append("u")
                
        elif Input[counter] == 't':
            Output.append("v")
                
        elif Input[counter] == 'u':
            Output.append("w")
                
        elif Input[counter] == 'v':
            Output.append("x")
                
        elif Input[counter] == 'w':
            Output.append("y")
                
        elif Input[counter] == 'x':
            Output.append("z")
                
        elif Input[counter] == 'y':
            Output.append("a")
                
        elif Input[counter] == 'z':
            Output.append("b")

        elif Input[counter] == '1':
            Output.append("6")

        elif Input[counter] == '2':
            Output.append("3")

        elif Input[counter] == '3':
            Output.append("7")

        elif Input[counter] == '4':
            Output.append("9")

        elif Input[counter] == '5':
            Output.append("2")

        elif Input[counter] == '6':
            Output.append("4")

        elif Input[counter] == '7':
            Output.append("8")

        elif Input[counter] == '8':
            Output.append("0")

        elif Input[counter] == '9':
            Output.append("5")

        elif Input[counter] == '0':
            Output.append("1")

        elif Input[counter] == '#':
            Output.append(" ")

        elif Input[counter] == '.':
            Output.append("?")

        elif Input[counter] == '?':
            Output.append(".")
        else:
            TranslateError = 1
            if TranslateError == 0:
                Hsh = 0
            elif TranslateError == 1:
                print("[?] An Error In The Encryption Software Has Occorred")
                print("[?] Perhaps You Entered An Ivalid Character")
                TerminateSession(20)
            else:
                print("[&] An Internal Error Has Occurred")
                print("[&] No Explanation Given")
                TerminateSession(20)
        counter += 1
        if counter == length:
            if TranslateError == 0:
                DecryptedResult = ''.join(Output)
                print("[^] Decrypted Result:",DecryptedResult)
                time.sleep(3)
                TerminateSession(20)

# = INFORMATION

def Information():
    print("[?] STN Version ", STNv," Is An Encryption Service That Is Registered To Three People", sep="")
    time.sleep(4)
    print("[?] Beyond The Various Layers Of Security, The User May Enter Any Of The Following Characters:")
    print("A-Z, 0-9, ?, .")
    time.sleep(6)
    print("[?] Additioanlly, The Encrypted (Not Decrypted) Message Will Be Copyed To The User's Clipboard For Convenience")
    time.sleep(5)
    print("[!] This Window Will Disappear In 10 Seconds")
    time.sleep(10)
    EnterLines(1000)
    HomePage()
    
# = Ui // IMPORTANT

def HomePage():
        UserActionHomePage = input("[!] Encrypt/Decrypt(?)| ")
        UserActionHomePageLower = UserActionHomePage.lower()
        
        if UserActionHomePageLower == 'd':
            DecodePhrase()
        elif UserActionHomePageLower == 'decrypt':
            DecodePhrase()
        elif UserActionHomePageLower == 'e':
            EncodePhrase()
        elif UserActionHomePageLower == 'encrypt':
            EncodePhrase()
        elif UserActionHomePageLower == '?':
            Information()
        else:
            print("[!] Invalid Character")
            EnterLines(1000)
            HomePage()
            
# = VERIFICATION
    
def Verification():        
    time.sleep(0.3)
    print("[!] Verifying Access to STN")
    if VerifiedIp == CurrentIp:
        time.sleep(0.6)
        print("[!] Ip Match Found")
        time.sleep(0.3)
        print("[!] Authentication Complete")
        time.sleep(1)
        EnterLines(100)
        print("[?] STN Version ", STNv, " | @SSkipr", sep="")
        time.sleep(4)
        EnterLines(100)
        HomePage()
    else:
        time.sleep(0.9)
        print("[!] Ip Match Not Found")
        print("[*] Booting Recovery Mode")
        TerminateSession(5)
        
Verification()




    

