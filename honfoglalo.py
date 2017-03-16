from PIL import Image
from PIL import ImageGrab
import os
import pyocr
import numpy

tools = pyocr.get_available_tools()
tool = tools[0]

mydict = {}
lines = [line.rstrip('\n') for line in open('db.csv')]

for data in lines:
    tmp = data.split(';;')
    mydict[tmp[0]] = tmp[1]

print("Start?")
os.system("pause")

while True:
    im = ImageGrab.grab()
    im = im.crop((400,342,1200,460))

    txt = tool.image_to_string(im,lang='hun')

    txt = txt.replace("\n"," ")

    print(txt)

    try:
        mydict[txt]
    except KeyError:
        print("A válasz nem található az adatbázisban. Helyes válasz:")
        ans = input()
        if txt != "" and ans != "":
            mydict[txt] = ans
            wr = txt + ";;" + ans + "\n"
            with open("db.csv", "a") as myfile:
                myfile.write(wr)
    else:
        print(mydict[txt])

    print("Következő kör?")
    if input() != "":
        break