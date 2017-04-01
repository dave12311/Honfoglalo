# coding=UTF-8
from PIL import Image
from PIL import ImageGrab
import os
import pyocr
import numpy
import MySQLdb

tools = pyocr.get_available_tools()
tool = tools[0]

db = MySQLdb.connect(host='dbstudio.pe.hu',
                    user='u444572030_user',
                    passwd='4Tbr1jjsstlQ',
                    db='u444572030_honfo')

cur = db.cursor()

print("Start?")
os.system("pause")

while True:
    im = ImageGrab.grab()

    im = im.crop((488,342,1100,431))

    im = im.convert('LA')

    im.save("temp.png")

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