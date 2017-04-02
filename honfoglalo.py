# coding=UTF-8
from PIL import Image
from PIL import ImageGrab
import pyocr
import MySQLdb
import sys

coords = (497,358,1087,466)

tools = pyocr.get_available_tools()
tool = tools[0]

db = MySQLdb.connect(host='sql11.freesqldatabase.com',
                    user='sql11166951',
                    passwd='yjqGuPF5g5',
                    db='sql11166951',
                    charset='utf8')

cur = db.cursor()

def getQuestion():
    im = ImageGrab.grab()
    if debug == True: im.save("full.png")
    im = im.crop(coords)
    if debug == True: im.save("cropped.png")
    im = im.convert('LA')
    if debug == True: im.save("greyscale.png")

    text = unicode(tool.image_to_string(im, lang='hun'))
    text = text.replace('\n',' ')

    return text

print("Start?")

debug = False

while True:

    command = raw_input()

    if command == "debug":
        debug = True
        print(u"Debug-mód bekapcsolva.")
    elif command == "normal":
        debug = False
        print(u"Debug-mód kikapcsolva.")
    elif command != "":
        db.close()
        sys.exit()
    else:
        ques = getQuestion()
        ques = ques.replace("'", "")
        print(ques)

        if cur.execute("SELECT answer FROM honfoglalo WHERE question LIKE '" + ques + "'") != 0:
            correct = cur.fetchone()
            print(correct)
        else:
            print(u"A válasz nem található az adatbázisban. Helyes válasz hozzáadása?")

        ans = unicode(raw_input(), 'cp852')

        if ans != "":
            command = unicode("INSERT INTO honfoglalo (question, answer) VALUES ('" + ques + "', '" + ans + "')")
            cur.execute(command)
            db.commit()
            print(u"Hozzáadva az adatbázishoz.")
        else:
            print(u"Adatbázisba írás kihagyva...")

        print(u"Következő kör?")