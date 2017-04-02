# coding=UTF-8
from PIL import Image
from PIL import ImageGrab
import pyocr
import MySQLdb

coords = (515,361,1061,466)

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

debug = True if raw_input() == "/debug" else False

while True:
    ques = getQuestion()
    print(ques)

    #SELECT * FROM  `honfoglalo` WHERE  `question` LIKE  %kérdés%

    #Check for ''!

    ans = unicode(raw_input(), 'cp852')

    if ans != "":
        command = unicode("INSERT INTO honfoglalo (question, answer) VALUES ('" + ques + "', '" + ans + "')")
        cur.execute(command)
        db.commit()
    else:
        print(u"Adatbázisba írás kihagyva...\n")

    print(u"Következő kör?")
    if raw_input() != "":
        db.close()
        break