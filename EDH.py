
import pydirectinput
import speech_recognition as sr 
import pyttsx3 as tts 
from playsound import playsound 
import time
from sys import exit
import argparse,csv
import json
import tkinter as tk
from os import system
import random
import numpy
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import mss
import cv2
pydirectinput.FAILSAFE = False
system("title " + "FC autopilot EDH")
sleep_time= 10
json_exit = open("exit")
variablesexit = json.load(json_exit)
x = (variablesexit["var"][0]["varX"])
x = int(x)
if x < 3:
    x = "0"
    data = {}
    data['var'] = []
    data['var'].append({
        'varX': x
    })
    with open('exit', 'w') as outfile:
        json.dump(data, outfile)
json_exit = open("voice")
variablesexit = json.load(json_exit)
x = (variablesexit["var"][0]["varX"])
x = int(x)
if x < 2:
    x = "0"
    data = {}
    data['var'] = []
    data['var'].append({
        'varX': x
    })
    with open('voice', 'w') as outfile:
        json.dump(data, outfile)
json_OIL = open("OIL")
OIL = json.load(json_OIL)
x = (OIL["var"][0]["varX"])
x = int(x)
if x < 2:
    x = "0"
    data = {}
    data['var'] = []
    data['var'].append({
        'varX': x
    })
    with open('OIL', 'w') as outfile:
        json.dump(data, outfile)
r = sr.Recognizer()
engine = tts.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_Text():
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio, language='pl-PL')
            if text != "":
                return text
            return 0
        except:
            return 0
def rounding_of_numbers(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 
        for row in csvReader: 
            jsonArray.append(row)
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
csvFilePath = r'jump.csv'
jsonFilePath = r'data.json'
csv_to_json(csvFilePath, jsonFilePath)
json_file = open("data.json")
variables = json.load(json_file)

root= tk.Tk()
root.title('Ustawienia autopilota')
root.iconbitmap('icon.ico')
canvas1 = tk.Canvas(root, width = 500, height = 280)
canvas1.pack()
l1 = tk.Label(root, text = "Podaj ilo???? skok??w:")
l1.config(font =("Courier", 10))   
canvas1.create_window(246, 15, window=l1)    
entry1 = tk.Entry (root)
canvas1.create_window(390, 15, window=entry1) 
l = tk.Label(root, text = "Podaj ilo???? skok??w do pomini??cia:")
l.config(font =("Courier", 10))   
canvas1.create_window(190, 35, window=l)    
entry2 = tk.Entry (root)
canvas1.create_window(390, 35, window=entry2) 
l2 = tk.Label(root, text = "Po klikni??ciu uruchom autopilota w ci??gu 15 sekund\nnale??y przej???? na okno Elite Dangerous")
l2.config(font =("Courier", 10))   
canvas1.create_window(250, 90, window=l2)  
def getSquareRoot (): 
    json_conf = open("window.conf")
    wh = json.load(json_conf)
    width  = (wh["var"][0]["varY"])
    height = (wh["var"][0]["varZ"])
    width = int(width)
    height = int(height)
    if height != 0 and width != 0:
        y = entry1.get()
        z = entry2.get()
        data = {}
        data['var'] = []
        data['var'].append({
            'varY': y,
            'varZ': z
        })
        with open('jump.conf', 'w') as outfile:
            json.dump(data, outfile)
    
        root.after(0, root.destroy) 
ustawienia = tk.Label(root, text = "Wymagane ustawienia:")
ustawienia.config(font =("Courier", 10))   
canvas1.create_window(85, 130, window=ustawienia)  
def getSquareRoot1 ():  
    y = 1280
    z = 720
    data = {}
    data['var'] = []
    data['var'].append({
        'varY': y,
        'varZ': z
    })
    with open('window.conf', 'w') as outfile:
        json.dump(data, outfile)
    
    root.after(0, button2.destroy)
    root.after(0, button3.destroy)
    button1 = tk.Button(text='Uruchom autopilota', command=getSquareRoot)
    canvas1.create_window(390, 60, window=button1)  

button2 = tk.Button(text='1280x720', command=getSquareRoot1)
canvas1.create_window(35, 155, window=button2)
def getSquareRoot2 ():  
    y = 1920
    z = 1080
    data = {}
    data['var'] = []
    data['var'].append({
        'varY': y,
        'varZ': z
    })
    with open('window.conf', 'w') as outfile:
        json.dump(data, outfile)
    
    root.after(0, button2.destroy)
    root.after(0, button3.destroy)
    button1 = tk.Button(text='Uruchom autopilota', command=getSquareRoot)
    canvas1.create_window(390, 60, window=button1)  

button3 = tk.Button(text='1920x1080', command=getSquareRoot2)
canvas1.create_window(100, 155, window=button3)
ustawienia1 = tk.Label(root, text = "Dodatkowe ustawienia:")
ustawienia1.config(font =("Courier", 10))   
canvas1.create_window(88, 180, window=ustawienia1) 
def getSquareRoot3 ():  
    x = "0"
    data = {}
    data['var'] = []
    data['var'].append({
        'varX': x
    })
    with open('voice', 'w') as outfile:
        json.dump(data, outfile)

button4 = tk.Button(text='W????cz komunikaty g??osowe', command=getSquareRoot3)
canvas1.create_window(83, 205, window=button4)
def getSquareRoot4 ():  
    x = "2"
    data = {}
    data['var'] = []
    data['var'].append({
        'varX': x
    })
    with open('voice', 'w') as outfile:
        json.dump(data, outfile)

button5 = tk.Button(text='Wy????cz komunikaty g??osowe', command=getSquareRoot4)
canvas1.create_window(244, 205, window=button5)
def getSquareRoot5 (): 
    x = "0"
    data = {}
    data['var'] = []
    data['var'].append({
        'varX': x
    })
    with open('exit', 'w') as outfile:
        json.dump(data, outfile)

button6 = tk.Button(text='W????cz nas??uchiwanie', command=getSquareRoot5)
canvas1.create_window(65, 235, window=button6)
def getSquareRoot6 ():  
    x = "3"
    data = {}
    data['var'] = []
    data['var'].append({
        'varX': x
    })
    with open('exit', 'w') as outfile:
        json.dump(data, outfile)

button7 = tk.Button(text='Wy????cz nas??uchiwanie', command=getSquareRoot6)
canvas1.create_window(191, 235, window=button7)
def getSquareRoot7 (): 
    x = "0"
    data = {}
    data['var'] = []
    data['var'].append({
        'varX': x
    })
    with open('OIL', 'w') as outfile:
        json.dump(data, outfile)

button8 = tk.Button(text='W????cz tankowanie i ??adowanie trytu', command=getSquareRoot7)
canvas1.create_window(103, 265, window=button8)
def getSquareRoot8 ():  
    x = "2"
    data = {}
    data['var'] = []
    data['var'].append({
        'varX': x
    })
    with open('OIL', 'w') as outfile:
        json.dump(data, outfile)

button9 = tk.Button(text='Wy????cz tankowanie i ??adowanie trytu', command=getSquareRoot8)
canvas1.create_window(306, 265, window=button9)
root.mainloop()
json_conf = open("jump.conf")
variablesconf = json.load(json_conf)
y = (variablesconf["var"][0]["varY"])
z = (variablesconf["var"][0]["varZ"])
y = int(y)
z = int(z)
y = y - z
z = z + 1
for x in range(y):
    v = x + z
    rdm3 = [3, 4, 5]
    rdm5 = [5, 6, 7]
    rdm10 = [10, 11, 12]
    rdm15 = [15, 16, 17]
    value = (variables[v]["System Name"])
    textold = "Cel podr????y: "
    text1 = textold
    json_exit = open("exit")
    variablesexit = json.load(json_exit)
    x = (variablesexit["var"][0]["varX"])
    x = int(x)
    json_voice= open("voice")
    voice = json.load(json_voice)
    voice = (voice["var"][0]["varX"])
    voice = int(voice)
    if x == 0:
        if voice == 0:
            speak("Kapitanie czekam na rozkazy")
            engine.runAndWait()
        print("Kapitanie czekam na rozkazy")
        while True:
    
            try:
                txt = get_Text().lower()
                txt = txt.split()   
                if txt != 0 and txt[0] == 'autopilot':
                    if txt != 0 and txt[1] == 'podaj':
                        if txt != 0 and txt[2] == 'swoje':
                            if txt != 0 and txt[3] == 'mo??liwo??ci':
                                if voice == 0:
                                    speak("Oto moje mo??liwo??ci.")
                                    speak("Potrafi??:")
                                    speak("Skaka?? fleet carierem po galaktyce")
                                    speak("Poda?? ilo???? skok??w do ko??cowego celu")
                                    speak("Poda?? nast??pny system")
                                    speak("Op????ni?? nast??pny skok")
                                print("Oto moje mo??liwo??ci.")
                                print("Potrafi??:")
                                print("Skaka?? fleet carierem po galaktyce")
                                print("Poda?? ilo???? skok??w do ko??cowego celu")
                                print("Poda?? nast??pny system")
                                print("Op????ni?? nast??pny skok")
                                continue
                            else:
                                text1 = "Nie posiadam polecenia podaj swoje "
                                text2 = txt[3]
                                text = text1 + text2 
                                if voice == 0:
                                    speak(text)
                                print(text)
                                continue
                        elif txt != 0 and txt[2] == 'ilo????':
                            if txt != 0 and txt[3] == 'pozosta??ych':
                                if txt != 0 and txt[4] == 'skok??w':
                                    jumps = int(y) - int(v)
                                    converted_jumps = str(jumps)
                                    textjump1 = "Pozosta??o "
                                    textjump2 = " skok??w do ko??cowego celu."
                                    textjump = textjump1 + converted_jumps + textjump2
                                    if voice == 0:
                                        speak(textjump)
                                    print(textjump)
                                    continue
                                else:
                                    text1 = "Nie posiadam polecenia podaj ilo???? pozosta??ych "
                                    text2 = txt[4]
                                    text = text1 + text2 
                                    if voice == 0:
                                        speak(text)
                                    print(text)
                                    continue 
                            else:
                                text1 = "Nie posiadam polecenia podaj ilo???? "
                                text2 = txt[3]
                                text = text1 + text2 
                                if voice == 0:
                                    speak(text)
                                print(text)
                                continue
                        elif txt != 0 and txt[2] == 'nazw??':
                            if txt != 0 and txt[3] == 'nast??pnego':
                                if txt != 0 and txt[4] == 'systemu':
                                    textsystem1 = "Nast??pny system nazywa si?? " 
                                    if voice == 0:
                                        speak(textsystem1)
                                        engine.setProperty('rate', 120)
                                        speak(value)
                                        engine.setProperty('rate', 150)
                                    textsystem1 = textsystem1 + value
                                    print(textsystem1)
                                    continue
                                else:
                                    text1 = "Nie posiadam polecenia podaj nazw?? nast??pnego "
                                    text2 = txt[5]
                                    text = text1 + text2 
                                    if voice == 0:
                                        speak(text)
                                    print(text)
                                    continue
                            else:
                                text1 = "Nie posiadam polecenia podaj nazw?? "
                                text2 = txt[3]
                                text = text1 + text2 
                                if voice == 0:
                                    speak(text)
                                print(text)
                                continue
                        else:
                            text1 = "Nie posiadam polecenia podaj "
                            text2 = txt[2]
                            text = text1 + text2 
                            if voice == 0:
                                speak(text)
                            print(text)
                            continue
                    elif txt != 0 and txt[1] == 'wycisz':
                        if txt != 0 and txt[2] == 'si??':
                            if voice == 0:
                                speak("Przechodz?? w tryb milczenia")
                            print("Przechodz?? w tryb milczenia")
                            x = "1"
                            data = {}
                            data['var'] = []
                            data['var'].append({
                                'varX': x
                            })
                            with open('voice', 'w') as outfile:
                                json.dump(data, outfile)
                            break
                        elif txt != 0 and txt[2] == 'komunikaty':
                            if txt != 0 and txt[3] == 'g??osowe':
                                if txt != 0 and txt[4] == 'na':
                                    if txt != 0 and txt[5] == 'sta??e':
                                        if voice == 0:
                                            speak("Przechodz?? w tryb milczenia na sta??e")
                                        print("Przechodz?? w tryb milczenia na sta??e")
                                        x = "2"
                                        data = {}
                                        data['var'] = []
                                        data['var'].append({
                                            'varX': x
                                        })
                                        with open('voice', 'w') as outfile:
                                            json.dump(data, outfile)
                                        break
                                    else:
                                        text1 = "Nie posiadam polecenia wycisz komunikaty g??osowe na "
                                        text2 = txt[5]
                                        text = text1 + text2 
                                        if voice == 0:
                                            speak(text)
                                        print(text)
                                        continue
                                else:
                                    text1 = "Nie posiadam polecenia wycisz komunikaty g??osowe "
                                    text2 = txt[4]
                                    text = text1 + text2
                                    if voice == 0:
                                        speak(text)
                                    print(text)
                                    continue
                            else:
                                text1 = "Nie posiadam polecenia wycisz komunikaty "
                                text2 = txt[3]
                                text = text1 + text2 
                                if voice == 0:
                                    speak(text)
                                print(text)
                                continue
                        else:
                            text1 = "Nie posiadam polecenia wycisz "
                            text2 = txt[2]
                            text = text1 + text2 
                            if voice == 0:
                                speak(text)
                            print(text)
                            continue
                    elif txt != 0 and txt[1] == 'wy????cz':
                        if txt != 0 and txt[2] == 'si??':
                            if voice == 0:
                                speak("Do us??yszenia kapitanie")
                            print("Do us??yszenia kapitanie")
                            x = "1"
                            data = {}
                            data['var'] = []
                            data['var'].append({
                                'varX': x
                            })
                            with open('exit', 'w') as outfile:
                                json.dump(data, outfile)
                            break
                        elif txt != 0 and txt[2] == 'nas??uchiwanie':
                            if voice == 0:
                                speak("Wy????czam nas??uchiwanie do ko??ca podr????y")
                            print("Wy????czam nas??uchiwanie do ko??ca podr????y")
                            x = "2"
                            data = {}
                            data['var'] = []
                            data['var'].append({
                                'varX': x
                            })
                            with open('exit', 'w') as outfile:
                                json.dump(data, outfile)
                            break
                        elif txt != 0 and txt[2] == 'wsparcie':
                            if txt != 0 and txt[3] == 'g??osowe':
                                if txt != 0 and txt[4] == 'na':
                                    if txt != 0 and txt[5] == 'sta??e':
                                        if voice == 0:
                                            speak("Wy????czam si?? na sta??e")
                                        print("Wy????czam si?? na sta??e")
                                        x = "3"
                                        data = {}
                                        data['var'] = []
                                        data['var'].append({
                                            'varX': x
                                        })
                                        with open('exit', 'w') as outfile:
                                            json.dump(data, outfile)
                                        break
                                    else:
                                        text1 = "Nie posiadam polecenia wy????cz wsparcie g??osowe na "
                                        text2 = txt[5]
                                        text = text1 + text2 
                                        if voice == 0:
                                            speak(text)
                                        print(text)
                                        continue
                                else:
                                    text1 = "Nie posiadam polecenia wy????cz wsparcie g??osowe "
                                    text2 = txt[4]
                                    text = text1 + text2 
                                    if voice == 0:
                                        speak(text)
                                    print(text)
                                    continue
                            else:
                                text1 = "Nie posiadam polecenia wy????cz wsparcie "
                                text2 = txt[3]
                                text = text1 + text2 
                                if voice == 0:
                                    speak(text)
                                print(text)
                                continue
                        elif txt != 0 and txt[2] == 'tankowanie':
                            if voice == 0:
                                speak("Wy????czam tankowanie na sta??e")
                            print("Wy????czam tankowanie na sta??e")
                            x = "2"
                            data = {}
                            data['var'] = []
                            data['var'].append({
                                'varX': x
                            })
                            with open('OIL', 'w') as outfile:
                                json.dump(data, outfile)
                            break
                        else:
                            text1 = "Nie posiadam polecenia wy????cz "
                            text2 = txt[2]
                            text = text1 + text2 
                            if voice == 0:
                                speak(text)
                            print(text)
                            continue
                    elif txt != 0 and txt[1] == 'w????cz':
                        if txt != 0 and txt[2] == 'wsparcie':
                            if txt != 0 and txt[3] == 'g??osowe':
                                if txt != 0 and txt[4] == 'na':
                                    if txt != 0 and txt[5] == 'sta??e':
                                        if voice == 0:
                                            speak("W????czam si?? na sta??e")
                                        print("W????czam si?? na sta??e")
                                        x = "0"
                                        data = {}
                                        data['var'] = []
                                        data['var'].append({
                                            'varX': x
                                        })
                                        with open('exit', 'w') as outfile:
                                            json.dump(data, outfile)
                                        break
                                    else:
                                        text1 = "Nie posiadam polecenia w????cz wsparcie g??osowe na "
                                        text2 = txt[5]
                                        text = text1 + text2 
                                        if voice == 0:
                                            speak(text)
                                        print(text)
                                        continue
                                else:
                                    text1 = "Nie posiadam polecenia w????cz wsparcie g??osowe "
                                    text2 = txt[4]
                                    text = text1 + text2 
                                    if voice == 0:
                                        speak(text)
                                    print(text)
                                    continue
                            else:
                                text1 = "Nie posiadam polecenia w????cz wsparcie "
                                text2 = txt[3]
                                text = text1 + text2 
                                if voice == 0:
                                    speak(text)
                                print(text)
                                continue
                        elif txt != 0 and txt[2] == 'tankowanie':
                            if voice == 0:
                                speak("W????czam tankowanie na sta??e")
                            print("W????czam tankowanie na sta??e")
                            x = "0"
                            data = {}
                            data['var'] = []
                            data['var'].append({
                                'varX': x
                            })
                            with open('OIL', 'w') as outfile:
                                json.dump(data, outfile)
                            break
                        else:
                            text1 = "Nie posiadam poecenia w????cz "
                            text2 = txt[2]
                            text = text1 + text2 
                            if voice == 0:
                                speak(text)
                            print(text)
                            continue
                    elif txt != 0 and txt[1] == 'pomijaj':
                        if txt != 0 and txt[2] == 'tankoanie':
                            if voice == 0:
                                speak("Od teraz pomijam tankowanie do ko??ca podr????y")
                            print("Od teraz pomijam tankowanie do ko??ca podr????y")
                            x = "1"
                            data = {}
                            data['var'] = []
                            data['var'].append({
                                'varX': x
                            })
                            with open('OIL', 'w') as outfile:
                                json.dump(data, outfile)
                            break
                        else:
                            text1 = "Nie posiadam polecenia pomijaj "
                            text2 = txt[2]
                            text = text1 + text2 
                            if voice == 0:
                                speak(text)
                            print(text)
                            continue
                    elif txt != 0 and txt[1] == 'wzn??w':
                        if txt != 0 and txt[2] == 'tankoanie':
                            if voice == 0:
                                speak("Wznawiam tankowanie do ko??ca podr????y")
                            print("Wznawiam tankowanie do ko??ca podr????y")
                            x = "0"
                            data = {}
                            data['var'] = []
                            data['var'].append({
                                'varX': x
                            })
                            with open('OIL', 'w') as outfile:
                                json.dump(data, outfile)
                            break
                        else:
                            text1 = "Nie posiadam polecenia wzn??w "
                            text2 = txt[2]
                            text = text1 + text2 
                            if voice == 0:
                                speak(text)
                            print(text)
                            continue
                    elif txt != 0 and txt[1] == 'kontynuuj':
                        if txt != 0 and txt[2] == 'podr????':
                            if voice == 0:
                                speak("Kontynuuje podr????")
                            print("Kontynuuje podr????")
                            break
                        else:
                            text1 = "Nie posiadam polecenia kontynuuj "
                            text2 = txt[2]
                            text = text1 + text2 
                            if voice == 0:
                                speak(text)
                            print(text)
                            continue
                    elif txt != 0 and txt[1] == 'op????nij':
                        if txt != 0 and txt[2] == 'skok':
                            if txt != 0 and txt[3] == 'o':
                                timexyz = txt[4]
                                timej = txt[5]
                                data = {}
                                data['var'] = []
                                data['var'].append({
                                    'vartimeXYX': timexyz,
                                    'vartimeJ': timej,
                                })
                                with open('timeXYZ', 'w') as outfile:
                                    json.dump(data, outfile)
                                if voice == 0:
                                    speak("Op????nienie ustawione")
                                print("Op????nienie ustawione")
                                continue
                            else:
                                text1 = "Nie posiadam polecenia op????nij skok "
                                text2 = txt[3]
                                text = text1 + text2 
                                if voice == 0:
                                    speak(text)
                                print(text)
                                continue
                        else:
                            text1 = "Nie posiadam polecenia op????nij "
                            text2 = txt[2]
                            text = text1 + text2 
                            if voice == 0:
                                speak(text)
                            print(text)
                            continue
                    else:
                        if voice == 0:
                            speak("Nie posiadam takiego polecenia.")
                        print("Nie posiadam takiego polecenia.")
                        continue
                else:
                    if voice == 0:
                        speak("Nie rozumiem polecenia powt??rz prosz??")
                    print("Nie rozumiem polecenia powt??rz prosz??")
                    continue
            except:
                time.sleep(sleep_time)
                if voice == 0:
                    speak("Brak rozkaz??w, kontynuuje podr????")
                print("Brak rozkaz??w, kontynuuje podr????")
                break
    json_exit = open("voice")
    voice = json.load(json_exit)
    voice = (voice["var"][0]["varX"])
    voice = int(voice)
    json_timeXYZ = open("timeXYZ")
    variablesexit = json.load(json_timeXYZ)
    timexyz = (variablesexit["var"][0]["vartimeXYX"])
    timej = (variablesexit["var"][0]["vartimeJ"])
    timexyz = int(timexyz)
    if timexyz != 0:
        if timej == "sekund" or timej == "sekund??" or timej == "sekundy":
            timexyz = int(timexyz) * 1
            texttime1 = "Skok op????niony o "
            texttime2 = str(timexyz)
            texttime3 = timej
            space = " "
            texttime = texttime1 + texttime2 + space + texttime3
            if voice == 0:
                speak(texttime)
            print(texttime)
        elif timej == "minut" or timej == "minut??" or timej == "minuty":
            timexyz = int(timexyz) * 60
            timexyz2 = int(timexyz) / 60
            texttime1 = "Skok op????niony o "
            texttime2 = str(int(timexyz2))
            texttime2 = str(int(timexyz2))
            texttime3 = timej
            space = " "
            texttime = texttime1 + texttime2 + space + texttime3
            if voice == 0:
                speak(texttime)
            print(texttime)
        elif timej == "dodzin" or timej == "godzine" or timej == "godziny":
            timexyz = int(timexyz) * 360
            timexyz2 = int(timexyz) / 360
            texttime1 = "Skok op????niony o "
            texttime2 = str(int(timexyz2))
            texttime3 = timej
            space = " "
            texttime = texttime1 + texttime2 + space + texttime3
            if voice == 0:
                speak(texttime)
            print(texttime)
    timexyznew = 0
    timejnew = "none"
    data = {}
    data['var'] = []
    data['var'].append({
        'vartimeXYX': timexyznew,
        'vartimeJ': timejnew,
    })
    with open('timeXYZ', 'w') as outfile:
        json.dump(data, outfile)
    json_exit = open("exit")
    variablesexit = json.load(json_exit)
    x = (variablesexit["var"][0]["varX"])
    x = int(x)
    if x == 1:
        x = "0"
        data = {}
        data['var'] = []
        data['var'].append({
            'varX': x
        })
        with open('exit', 'w') as outfile:
            json.dump(data, outfile)
        exit()
    time.sleep(15)
    time.sleep(timexyz)
    print (text1)
    print (value)
    if voice == 0:
        engine.say(text1)
        engine.runAndWait()
        engine.setProperty('rate', 120)
        speak(value)
        engine.setProperty('rate', 150)
        engine.runAndWait()
    pydirectinput.press('4')
    time.sleep(int(random.choice(rdm5)))
    pydirectinput.press('4')
    time.sleep(int(random.choice(rdm3)))
    json_exit = open("OIL")
    OIL = json.load(json_exit)
    OIL = (OIL["var"][0]["varX"])
    OIL = int(OIL)
    if OIL == 0:
        print ("Rozpoczynam tankowanie FC")
        if voice == 0:
            engine.say("Rozpoczynam tankowanie FC")
            engine.runAndWait()
        pydirectinput.press('s')
        time.sleep(int(random.choice(rdm3)))
        pydirectinput.press('space')
        time.sleep(int(random.choice(rdm15)))
        pydirectinput.press('s')
        time.sleep(int(random.choice(rdm3)))
        pydirectinput.press('s')
        time.sleep(int(random.choice(rdm3)))
        pydirectinput.press('space')
        time.sleep(int(random.choice(rdm3)))
        pydirectinput.press('space')
        time.sleep(int(random.choice(rdm3)))
        pydirectinput.press('w')
        time.sleep(int(random.choice(rdm3)))
        pydirectinput.press('space')
        time.sleep(int(random.choice(rdm3)))
        pydirectinput.press('backspace')
        time.sleep(int(random.choice(rdm5)))
        pydirectinput.press('backspace')
        time.sleep(int(random.choice(rdm5)))
        pydirectinput.press('backspace')
        print ("Tankowanie FC zako??czone")
        if voice == 0:
            engine.say("Tankowanie FC zako??czone")
            engine.runAndWait()
        time.sleep(int(random.choice(rdm5)))
        print ("Rozpoczynam ??adowanie trytu na statek")
        if voice == 0:
            engine.say("Rozpoczynam ??adowanie trytu na statek")
            engine.runAndWait()
        pydirectinput.press('4')
        time.sleep(int(random.choice(rdm15)))
        pydirectinput.press('d')
        time.sleep(int(random.choice(rdm3)))
        pydirectinput.press('w')
        time.sleep(int(random.choice(rdm3)))
        pydirectinput.press('d')
        time.sleep(int(random.choice(rdm3)))
        pydirectinput.press('space')
        time.sleep(int(random.choice(rdm3)))
        pydirectinput.keyDown('w')
        time.sleep(int(random.choice(rdm5)))
        pydirectinput.keyUp('w')
        time.sleep(int(random.choice(rdm3)))
        pydirectinput.keyDown('a')
        time.sleep(int(random.choice(rdm15)))
        pydirectinput.keyUp('a')
        time.sleep(int(random.choice(rdm3)))
        pydirectinput.press('space')
        time.sleep(int(random.choice(rdm3)))
        pydirectinput.press('space')
        time.sleep(int(random.choice(rdm3)))
        pydirectinput.press('4')
        print ("??adowanie trytu na statek zako??czone")
        if voice == 0:
            engine.say("??adowanie trytu na statek zako??czone")
            engine.runAndWait()
    else:
        print ("Pomijam tankowanie FC i ??adowanie trytu na statek")
        if voice == 0:
            engine.say("Pomijam tankowanie FC i ??adowanie trytu na statek")
            engine.runAndWait()
    time.sleep(int(random.choice(rdm5)))
    print ("Wyznaczanie celu skoku")
    if voice == 0:
        engine.say("Wyznaczanie celu skoku")
        engine.runAndWait()
    pydirectinput.press('s')
    time.sleep(int(random.choice(rdm3)))
    pydirectinput.press('space')
    time.sleep(int(random.choice(rdm15)))
    pydirectinput.press('d')
    time.sleep(int(random.choice(rdm3)))
    pydirectinput.press('d')
    time.sleep(int(random.choice(rdm3)))
    pydirectinput.press('s')
    time.sleep(int(random.choice(rdm3)))
    pydirectinput.press('s')
    time.sleep(int(random.choice(rdm3)))
    pydirectinput.press('space')
    time.sleep(int(random.choice(rdm15)))
    pydirectinput.press('s')
    time.sleep(int(random.choice(rdm3)))
    pydirectinput.press('space')
    time.sleep(int(random.choice(rdm3)))
    pydirectinput.press('space')
    time.sleep(int(random.choice(rdm15)))
    pydirectinput.press('end')
    time.sleep(int(random.choice(rdm3)))
    pydirectinput.press('space')
    time.sleep(int(random.choice(rdm5)))
    command = 'echo ' + value + '| clip'
    system(command)
    time.sleep(int(random.choice(rdm3)))
    pydirectinput.keyDown('ctrl')
    time.sleep(0.2)
    pydirectinput.keyDown('v')
    time.sleep(0.2)
    pydirectinput.keyUp('v')
    time.sleep(0.2)
    pydirectinput.keyUp('ctrl')
    time.sleep(5)
    pydirectinput.press('enter')
    time.sleep(5)
    pydirectinput.press('enter')
    time.sleep(int(random.choice(rdm10)))
    print ("Wyznaczanie celu skoku zako??czone")
    if voice == 0:
        engine.say("Wyznaczanie celu skoku zako??czone")
        engine.runAndWait()
    time.sleep(int(random.choice(rdm3)))
    print ("Zatwierdzam skok na", value)
    text = "Zatwierdzam skok na "
    text1 = text
    if voice == 0:
        engine.say(text1)
        engine.runAndWait()
        engine.setProperty('rate', 120)
        speak(value)
        engine.setProperty('rate', 150)
        engine.runAndWait()
    pydirectinput.press('space')
    time.sleep(int(random.choice(rdm5)))
    pydirectinput.press('backspace')
    time.sleep(int(random.choice(rdm10)))
    c = 0
    d = 0
    while d == 0:
        if c >= 50:
            pydirectinput.press('enter')
            time.sleep(int(random.choice(rdm5)))
            pydirectinput.press('enter')
            time.sleep(int(random.choice(rdm5)))
            pydirectinput.press('backspace')
            time.sleep(int(random.choice(rdm5)))
            pydirectinput.press('backspace')
            time.sleep(int(random.choice(rdm5)))
            pydirectinput.press('backspace')
            time.sleep(int(random.choice(rdm5)))
            pydirectinput.press('backspace')
            time.sleep(int(random.choice(rdm5)))
            pydirectinput.press('backspace')
            time.sleep(int(random.choice(rdm5)))
            pydirectinput.press('backspace')
            time.sleep(int(random.choice(rdm5)))
            pydirectinput.press('backspace')
            time.sleep(int(random.choice(rdm5)))
            pydirectinput.press('backspace')
            print ("B????d sekwencji wyznaczania i zatwierdzania skoku")
            if voice == 0:
                engine.say("B????d sekwencji wyznaczania i zatwierdzania skoku")
                engine.runAndWait()
            print ("Ponowne wyznaczanie celu skoku")
            if voice == 0:
                engine.say("Ponowne wyznaczanie celu skoku")
                engine.runAndWait()
            pydirectinput.press('s')
            time.sleep(int(random.choice(rdm3)))
            pydirectinput.press('space')
            time.sleep(int(random.choice(rdm15)))
            pydirectinput.press('d')
            time.sleep(int(random.choice(rdm3)))
            pydirectinput.press('d')
            time.sleep(int(random.choice(rdm3)))
            pydirectinput.press('s')
            time.sleep(int(random.choice(rdm3)))
            pydirectinput.press('s')
            time.sleep(int(random.choice(rdm3)))
            pydirectinput.press('space')
            time.sleep(int(random.choice(rdm15)))
            pydirectinput.press('s')
            time.sleep(int(random.choice(rdm3)))
            pydirectinput.press('space')
            time.sleep(int(random.choice(rdm3)))
            pydirectinput.press('space')
            time.sleep(int(random.choice(rdm15)))
            pydirectinput.press('end')
            time.sleep(int(random.choice(rdm3)))
            pydirectinput.press('space')
            time.sleep(int(random.choice(rdm5)))
            command = 'echo ' + value + '| clip'
            system(command)
            time.sleep(int(random.choice(rdm3)))
            pydirectinput.keyDown('ctrl')
            time.sleep(0.2)
            pydirectinput.keyDown('v')
            time.sleep(0.2)
            pydirectinput.keyUp('v')
            time.sleep(0.2)
            pydirectinput.keyUp('ctrl')
            time.sleep(5)
            pydirectinput.press('enter')
            time.sleep(5)
            pydirectinput.press('enter')
            time.sleep(int(random.choice(rdm10)))
            print ("Ponowne wyznaczanie celu skoku zako??czone")
            if voice == 0:
                engine.say("Ponowne wyznaczanie celu skoku zako??czone")
                engine.runAndWait()
            time.sleep(int(random.choice(rdm3)))
            print ("Ponowne zatwierdzanie skoku na", value)
            text = "Ponowne zatwierdzanie skoku na "
            text1 = text
            if voice == 0:
                engine.say(text1)
                engine.runAndWait()
                engine.setProperty('rate', 120)
                speak(value)
                engine.setProperty('rate', 150)
                engine.runAndWait()
            pydirectinput.press('space')
            time.sleep(int(random.choice(rdm5)))
            pydirectinput.press('backspace')
            time.sleep(int(random.choice(rdm10)))
            c = 0
        else:
            json_conf = open("window.conf")
            wh = json.load(json_conf)
            width  = (wh["var"][0]["varY"])
            height = (wh["var"][0]["varZ"])
            width = int(width)
            height = int(height)
            dzielnikx = 73.625
            dzielnikx2 = 6.5625

            dzielnikx3 = 50
            dzielnikx4 = 21.875

            dzielniky = 89.755
            dzielniky2 = 3.5

            dzielniky3 = 93.472
            oblicz1 = width / 100 * dzielnikx
            oblicz1x = width / 100 * dzielnikx2
            oblicz2 = height / 100 * dzielniky
            oblicz2y = height / 100 * dzielniky2

            oblicz2x = width / 100 * dzielnikx3
            oblicz3x = width / 100 * dzielnikx4
            oblicz3y = height / 100 * dzielniky3
            oblicz4y = height / 100 * dzielniky2
            mon = {'top': int(round(oblicz3y)), 'left': int(round(oblicz2x)), 'width': int(round(oblicz3x)), 'height': int(round(oblicz4y))}
            mon = {'top': int(round(oblicz2)), 'left': int(round(oblicz1)), 'width': int(round(oblicz1x)), 'height': int(round(oblicz2y))}

            with mss.mss() as sct:
                li = 0
                while c < 50:
                    im = numpy.asarray(sct.grab(mon))
                    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

                    text = pytesseract.image_to_string(im)
                    if text:
                        if text != ' \n':
                            data = {}
                            data['var'] = []
                            data['var'].append({
                                'li1': text[0],
                                'li2': text[2],
                                'li3': text[3],
                                'li4': text[5],
                                'li5': text[6]

                            })
                            with open('time.conf', 'w') as outfile:
                                json.dump(data, outfile)
                            json_conf = open("time.conf")
                            li = json.load(json_conf)
                            li1 = (li["var"][0]["li1"])
                            li2 = (li["var"][0]["li2"])
                            li3 = (li["var"][0]["li3"])
                            li4 = (li["var"][0]["li4"])
                            li5 = (li["var"][0]["li5"])
                            li1 = 360 * int(li1)
                            li2 = 60 * 10 * int(li2)
                            li3 = 60 * int(li3)
                            li4 = 10 * int(li4)
                            li5 = int(li5)
                            li = li1 + li2 + li3 + li4 + li5
                            cv2.destroyAllWindows()
                            d = 1
                            break
                        else:
                            c = c + 1
                            if c == 0 or c == 10 or c == 20 or c == 30 or c == 40:
                                print("Sprawdzam...")
                                if voice == 0:
                                    engine.say("Sprawdzam...")
                                    engine.runAndWait()
                    else:
                        c = c + 1
                        if c == 0 or c == 10 or c == 20 or c == 30 or c == 40:
                            print("Sprawdzam...")
                            if voice == 0:
                                engine.say("Sprawdzam...")
                                engine.runAndWait()
    print ("Zatwierdzanie skoku zako??czone")
    if voice == 0:
        engine.say("Zatwierdzanie skoku zako??czone")
        engine.runAndWait()
    pydirectinput.press('backspace')
    time.sleep(3)
    pydirectinput.press('backspace')
    time.sleep(3)
    text1a1 = "Autopilot wstrzymany do nast??pnego skoku, masz "
    li1 = (li - 6) / 60
    li1 = int(li1)
    li2 = (li - 6) - li1 * 60
    li1 = int(li1)
    li2 = int(li2)
    li1s = str(li1)
    li2s = str(li2)
    if li1 == 1:
        text1a2 = " minut?? "
        text1a2x = " minuty "
        li1x = "jedn??"
        li1x2 = "jednej"
        textvara2b = str(li1x2) + text1a2x
        textvara2a = str(li1) + text1a2x
        textvara1b = str(li1x) + text1a2
        textvara1a = str(li1) + text1a2
    elif li1 <= 0:
        textvara2b = "zeru minut "
        textvara2a = "0 minut "
        textvara1b = "zero minut "
        textvara1a = "0 minut "
    elif li1 >= 2 and li1 <= 4 or int(li1s[-1]) >= 2 and int(li1s[-1]) <= 4 and li1 != 12 and li1 != 13 and li1 != 14:
        text1a2 = " minuty "
        text1a2x = " minut "
        if li1 == 2:
            li1x = "dwie"
            li1x2 = "dw??ch"
        elif li1 == 3:
            li1x = "trzy"
            li1x2 = "trzech"
        elif li1 == 4:
            li1x = "cztery"
            li1x2 = "czterech"
        else:
            if int(li1s[-1]) == 2:
                zero = "0"
                text000 = " dwie"
                li1x = str(li1s[0]) + zero + text000
                if int(li1s[0]) == 2:
                    li1x2 = "dwudziestu"
                    text000 = " dw??ch"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 3:
                    li1x2 = "trzydziestu"
                    text000 = " dw??ch"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 4:
                    li1x2 = "czterdziestu"
                    text000 = " dw??ch"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 5:
                    li1x2 = "pi????dziesi??ciu"
                    text000 = " dw??ch"
                    li1x2 = li1x2 + text000
            elif int(li1s[-1]) == 3:
                zero = "0"
                text000 = " trzy"
                li1x = str(li1s[0]) + zero + text000
                if int(li1s[0]) == 2:
                    li1x2 = "dwudziestu"
                    text000 = " trzech"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 3:
                    li1x2 = "trzydziestu"
                    text000 = " trzech"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 4:
                    li1x2 = "czterdziestu"
                    text000 = " trzech"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 5:
                    li1x2 = "pi????dziesi??ciu"
                    text000 = " trzech"
                    li1x2 = li1x2 + text000
            elif int(li1s[-1]) == 4:
                zero = "0"
                text000 = " cztery"
                li1x = str(li1s[0]) + zero + text000
                if int(li1s[0]) == 2:
                    li1x2 = "dwudziestu"
                    text000 = " czterech"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 3:
                    li1x2 = "trzydziestu"
                    text000 = " czterech"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 4:
                    li1x2 = "czterdziestu"
                    text000 = " czterech"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 5:
                    li1x2 = "pi????dziesi??ciu"
                    text000 = " czterech"
                    li1x2 = li1x2 + text000
        textvara2b = str(li1x2) + text1a2x
        textvara2a = str(li1) + text1a2x
        textvara1b = str(li1x) + text1a2
        textvara1a = str(li1) + text1a2
    else:
        text1a2 = " minut "
        text1a2x = " minut "
        if li1 == 5:
            li1x = "pi????"
            li1x2 = "pi??ciu"
        elif li1 == 6:
            li1x = "sze????"
            li1x2 = "sze??ciu"
        elif li1 == 7:
            li1x = "siedem"
            li1x2 = "siedmiu"
        elif li1 == 8:
            li1x = "osiem"
            li1x2 = "o??miu"
        elif li1 == 9:
            li1x = "dziewi????"
            li1x2 = "dziewi??ciu"
        elif li1 == 10:
            li1x = "dziesi????"
            li1x2 = "dziesi??ciu"
        elif li1 == 11:
            li1x = "jedena??cie"
            li1x2 = "jedenastu"
        elif li1 == 12:
            li1x = "dwana??cie"
            li1x2 = "dwunastu"
        elif li1 == 13:
            li1x = "trzyna??cie"
            li1x2 = "trzynastu"
        elif li1 == 14:
            li1x = "czterna??cie"
            li1x2 = "czternastu"
        elif li1 == 15:
            li1x = "pi??tna??cie"
            li1x2 = "pi??tnastu"
        elif li1 == 16:
            li1x = "szesna??cie"
            li1x2 = "szesnastu"
        elif li1 == 17:
            li1x = "siedemna??cie"
            li1x2 = "siedemnastu"
        elif li1 == 18:
            li1x = "osiemna??cie"
            li1x2 = "osiemnastu"
        elif li1 == 19:
            li1x = "dziewi??tna??cie"
            li1x2 = "dziewi??tnastu"
        elif li1 == 20:
            li1x = "dwadzie??cia"
            li1x2 = "dwudziestu"
        elif li1 == 30:
            li1x = "trzydzie??ci"
            li1x2 = "trzydziestu"
        elif li1 == 40:
            li1x = "czterdzie??ci"
            li1x2 = "czterdziestu"
        elif li1 == 50:
            li1x = "pi????dziesi??t"
            li1x2 = "pi????dziesi??ciu"
        else:
            if int(li1s[-1]) == 1:
                zero = "0"
                text000 = " jeden"
                li1x = str(li1s[0]) + zero + text000
                if int(li1s[0]) == 2:
                    li1x2 = "dwudziestu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 3:
                    li1x2 = "trzydziestu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 4:
                    li1x2 = "czterdziestu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 5:
                    li1x2 = "pi????dziesi??ciu"
                    li1x2 = li1x2 + text000
            elif int(li1s[-1]) == 5:
                zero = "0"
                text000 = " pi????"
                li1x = str(li1s[0]) + zero + text000
                if int(li1s[0]) == 2:
                    li1x2 = "dwudziestu"
                    text000 = " pi??ciu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 3:
                    li1x2 = "trzydziestu"
                    text000 = " pi??ciu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 4:
                    li1x2 = "czterdziestu"
                    text000 = " pi??ciu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 5:
                    li1x2 = "pi????dziesi??ciu"
                    text000 = " pi??ciu"
                    li1x2 = li1x2 + text000
            elif int(li1s[-1]) == 6:
                zero = "0"
                text000 = " sze????"
                li1x = str(li1s[0]) + zero + text000
                if int(li1s[0]) == 2:
                    li1x2 = "dwudziestu"
                    text000 = " sze??ciu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 3:
                    li1x2 = "trzydziestu"
                    text000 = " sze??ciu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 4:
                    li1x2 = "czterdziestu"
                    text000 = " sze??ciu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 5:
                    li1x2 = "pi????dziesi??ciu"
                    text000 = " sze??ciu"
                    li1x2 = li1x2 + text000
            elif int(li1s[-1]) == 7:
                zero = "0"
                text000 = " siedem"
                li1x = str(li1s[0]) + zero + text000
                if int(li1s[0]) == 2:
                    li1x2 = "dwudziestu"
                    text000 = " siedmiu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 3:
                    li1x2 = "trzydziestu"
                    text000 = " siedmiu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 4:
                    li1x2 = "czterdziestu"
                    text000 = " siedmiu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 5:
                    li1x2 = "pi????dziesi??ciu"
                    text000 = " siedmiu"
                    li1x2 = li1x2 + text000
            elif int(li1s[-1]) == 8:
                zero = "0"
                text000 = " osiem"
                li1x = str(li1s[0]) + zero + text000
                if int(li1s[0]) == 2:
                    li1x2 = "dwudziestu"
                    text000 = " o??miu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 3:
                    li1x2 = "trzydziestu"
                    text000 = " o??miu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 4:
                    li1x2 = "czterdziestu"
                    text000 = " o??miu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 5:
                    li1x2 = "pi????dziesi??ciu"
                    text000 = " o??miu"
                    li1x2 = li1x2 + text000
            elif int(li1s[-1]) == 9:
                zero = "0"
                text000 = " dziewi????"
                li1x = str(li1s[0]) + zero + text000
                if int(li1s[0]) == 2:
                    li1x2 = "dwudziestu"
                    text000 = " dziewi??ciu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 3:
                    li1x2 = "trzydziestu"
                    text000 = " dziewi??ciu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 4:
                    li1x2 = "czterdziestu"
                    text000 = " dziewi??ciu"
                    li1x2 = li1x2 + text000
                elif int(li1s[0]) == 5:
                    li1x2 = "pi????dziesi??ciu"
                    text000 = " dziewi??ciu"
                    li1x2 = li1x2 + text000
        textvara2b = str(li1x2) + text1a2x
        textvara2a = str(li1) + text1a2x
        textvara1b = str(li1x) + text1a2
        textvara1a = str(li1) + text1a2
    if li2 == 1:
        text1a3 = " sekund?? "
        text1a3x = " sekundy "
        li2x = "jedn??"
        li2x2 = "jednej"
        textvarb2b = str(li2x2) + text1a3x
        textvarb2a = str(li2) + text1a3x
        textvarb1b = str(li2x) + text1a3
        textvarb1a = str(li2) + text1a3
    elif li2 <= 0:
        textvarb2b = "zeru sekund "
        textvarb2a = "0 sekund "
        textvarb1b = "zero sekund "
        textvarb1a = "0 sekund "
    elif li2 >= 2 and li2 <= 4 or int(li2s[-1]) >= 2 and int(li2s[-1]) <= 4 and li2 != 12 and li2 != 13 and li2 != 14:
        text1a3 = " sekundy "
        text1a3x = " sekund "
        if li2 == 2:
            li2x = "dwie"
            li2x2 = "dw??ch"
        elif li2 == 3:
            li2x = "trzy"
            li2x2 = "trzech"
        elif li2 == 4:
            li2x = "cztery"
            li2x2 = "czterech"
        else:
            if int(li2s[-1]) == 2:
                zero = "0"
                text000 = " dwie"
                li2x = str(li2s[0]) + zero + text000
                if int(li2s[0]) == 2:
                    li2x2 = "dwudziestu"
                    text000 = " dw??ch"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 3:
                    li2x2 = "trzydziestu"
                    text000 = " dw??ch"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 4:
                    li2x2 = "czterdziestu"
                    text000 = " dw??ch"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 5:
                    li2x2 = "pi????dziesi??ciu"
                    text000 = " dw??ch"
                    li2x2 = li2x2 + text000
            elif int(li2s[-1]) == 3:
                zero = "0"
                text000 = " trzy"
                li2x = str(li2s[0]) + zero + text000
                if int(li2s[0]) == 2:
                    li2x2 = "dwudziestu"
                    text000 = " trzech"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 3:
                    li2x2 = "trzydziestu"
                    text000 = " trzech"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 4:
                    li2x2 = "czterdziestu"
                    text000 = " trzech"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 5:
                    li2x2 = "pi????dziesi??ciu"
                    text000 = " trzech"
                    li2x2 = li2x2 + text000
            elif int(li2s[-1]) == 4:
                zero = "0"
                text000 = " cztery"
                li2x = str(li2s[0]) + zero + text000
                if int(li2s[0]) == 2:
                    li2x2 = "dwudziestu"
                    text000 = " czterech"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 3:
                    li2x2 = "trzydziestu"
                    text000 = " czterech"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 4:
                    li2x2 = "czterdziestu"
                    text000 = " czterech"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 5:
                    li2x2 = "pi????dziesi??ciu"
                    text000 = " czterech"
                    li2x2 = li2x2 + text000
        textvarb2b = str(li2x2) + text1a3x
        textvarb2a = str(li2) + text1a3x
        textvarb1b = str(li2x) + text1a3
        textvarb1a = str(li2) + text1a3
    else:
        text1a3 = " sekund "
        text1a3x = " sekund "
        if li2 == 5:
            li2x = "pi????"
            li2x2 = "pi??ciu"
        elif li2 == 6:
            li2x = "sze????"
            li2x2 = "sze??ciu"
        elif li2 == 7:
            li2x = "siedem"
            li2x2 = "siedmiu"
        elif li2 == 8:
            li2x = "osiem"
            li2x2 = "o??miu"
        elif li2 == 9:
            li2x = "dziewi????"
            li2x2 = "dziewi??ciu"
        elif li2 == 10:
            li2x = "dziesi????"
            li2x2 = "dziesi??ciu"
        elif li2 == 11:
            li2x = "jedena??cie"
            li2x2 = "jedenastu"
        elif li2 == 12:
            li2x = "dwana??cie"
            li2x2 = "dwunastu"
        elif li2 == 13:
            li2x = "trzyna??cie"
            li2x2 = "trzynastu"
        elif li2 == 14:
            li2x = "czterna??cie"
            li2x2 = "czternastu"
        elif li2 == 15:
            li2x = "pi??tna??cie"
            li2x2 = "pi??tnastu"
        elif li2 == 16:
            li2x = "szesna??cie"
            li2x2 = "szesnastu"
        elif li2 == 17:
            li2x = "siedemna??cie"
            li2x2 = "siedemnastu"
        elif li2 == 18:
            li2x = "osiemna??cie"
            li2x2 = "osiemnastu"
        elif li2 == 19:
            li2x = "dziewi??tna??cie"
            li2x2 = "dziewi??tnastu"
        elif li2 == 20:
            li2x = "dwadzie??cia"
            li2x2 = "dwudziestu"
        elif li2 == 30:
            li2x = "trzydzie??ci"
            li2x2 = "trzydziestu"
        elif li2 == 40:
            li2x = "czterdzie??ci"
            li2x2 = "czterdziestu"
        elif li2 == 50:
            li2x = "pi????dziesi??t"
            li2x2 = "pi????dziesi??ciu"
        else:
            if int(li2s[-1]) == 1:
                zero = "0"
                text000 = " jeden"
                li2x = str(li2s[0]) + zero + text000
                if int(li2s[0]) == 2:
                    li2x2 = "dwudziestu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 3:
                    li2x2 = "trzydziestu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 4:
                    li2x2 = "czterdziestu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 5:
                    li2x2 = "pi????dziesi??ciu"
                    li2x2 = li2x2 + text000
            elif int(li2s[-1]) == 5:
                zero = "0"
                text000 = " pi????"
                li2x = str(li2s[0]) + zero + text000
                if int(li2s[0]) == 2:
                    li2x2 = "dwudziestu"
                    text000 = " pi??ciu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 3:
                    li2x2 = "trzydziestu"
                    text000 = " pi??ciu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 4:
                    li2x2 = "czterdziestu"
                    text000 = " pi??ciu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 5:
                    li2x2 = "pi????dziesi??ciu"
                    text000 = " pi??ciu"
                    li2x2 = li2x2 + text000
            elif int(li2s[-1]) == 6:
                zero = "0"
                text000 = " sze????"
                li2x = str(li2s[0]) + zero + text000
                if int(li2s[0]) == 2:
                    li2x2 = "dwudziestu"
                    text000 = " sze??ciu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 3:
                    li2x2 = "trzydziestu"
                    text000 = " sze??ciu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 4:
                    li2x2 = "czterdziestu"
                    text000 = " sze??ciu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 5:
                    li2x2 = "pi????dziesi??ciu"
                    text000 = " sze??ciu"
                    li2x2 = li2x2 + text000
            elif int(li2s[-1]) == 7:
                zero = "0"
                text000 = " siedem"
                li2x = str(li2s[0]) + zero + text000
                if int(li2s[0]) == 2:
                    li2x2 = "dwudziestu"
                    text000 = " siedmiu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 3:
                    li2x2 = "trzydziestu"
                    text000 = " siedmiu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 4:
                    li2x2 = "czterdziestu"
                    text000 = " siedmiu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 5:
                    li2x2 = "pi????dziesi??ciu"
                    text000 = " siedmiu"
                    li2x2 = li2x2 + text000
            elif int(li2s[-1]) == 8:
                zero = "0"
                text000 = " osiem"
                li2x = str(li2s[0]) + zero + text000
                if int(li2s[0]) == 2:
                    li2x2 = "dwudziestu"
                    text000 = " o??miu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 3:
                    li2x2 = "trzydziestu"
                    text000 = " o??miu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 4:
                    li2x2 = "czterdziestu"
                    text000 = " o??miu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 5:
                    li2x2 = "pi????dziesi??ciu"
                    text000 = " o??miu"
                    li2x2 = li2x2 + text000
            elif int(li2s[-1]) == 9:
                zero = "0"
                text000 = " dziewi????"
                li2x = str(li2s[0]) + zero + text000
                if int(li2s[0]) == 2:
                    li2x2 = "dwudziestu"
                    text000 = " dziewi??ciu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 3:
                    li2x2 = "trzydziestu"
                    text000 = " dziewi??ciu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 4:
                    li2x2 = "czterdziestu"
                    text000 = " dziewi??ciu"
                    li2x2 = li2x2 + text000
                elif int(li2s[0]) == 5:
                    li2x2 = "pi????dziesi??ciu"
                    text000 = " dziewi??ciu"
                    li2x2 = li2x2 + text000
        textvarb2b = str(li2x2) + text1a3x
        textvarb2a = str(li2) + text1a3x
        textvarb1b = str(li2x) + text1a3
        textvarb1a = str(li2) + text1a3
    text1a5 = "u??ytkowania komputera"
    text1a = text1a1 + textvara1a + textvarb1a + text1a5
    print (text1a)
    if voice == 0:
        text1a = text1a1 + textvara1b + textvarb1b + text1a5
        engine.say(text1a)
        engine.runAndWait()
    text1a1 = "Po up??ywie "
    text1a5 = "wr???? do Elite Dangerous"
    text1a = text1a1 +  textvara2a + textvarb2a  + text1a5
    print (text1a)
    if voice == 0:
        text1a = text1a1 + textvara2b + textvarb2b + text1a5
        engine.say(text1a)
        engine.runAndWait()
    json_exit = open("OIL")
    OIL = json.load(json_exit)
    OIL = (OIL["var"][0]["varX"])
    OIL = int(OIL)
    if OIL == 0:
        li = li - 6
    else:
        li = int(li) - 6 + 4 * 14 + 6 * 4 + 16 * 3
    time.sleep(li)
    playsound('alarm.wav')
    print ("Zosta??a minuta do nast??pnego skoku, wr???? do Elite Dangerous")
    if voice == 0:
        engine.say("Zosta??a minuta do nast??pnego skoku")
        engine.say("wr???? do Elite Dangerous")
        engine.runAndWait()
        engine.runAndWait()
    time.sleep(60)
print ("Koniec trasy")
if voice == 0:
    engine.say("Koniec trasy")
    engine.runAndWait()
exit()