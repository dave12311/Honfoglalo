# coding=UTF-8
from PIL import Image
from PIL import ImageGrab
import os
import pyocr
import numpy
import MySQLdb

tools = pyocr.get_available_tools()
tool = tools[0]

db = MySQLdb.connect(host='sql11.freesqldatabase.com',
                    user='sql11166951',
                    passwd='yjqGuPF5g5',
                    db='sql11166951',
                    charset='utf8')

cur = db.cursor()

print("Start?")
os.system("pause")

while True:
    im = ImageGrab.grab()
    im = im.crop((488,342,1100,431))
    im = im.convert('LA')
    ques = unicode(tool.image_to_string(im,lang='hun'))
    ques = ques.replace("\n"," ")
    print(ques)

    #SELECT * FROM  `honfoglalo` WHERE  `question` LIKE  %kérdés%

    #Check for ''!

    ans = unicode(raw_input(), 'cp852')

    command = unicode("INSERT INTO honfoglalo (question, answer) VALUES ('" + ques + "', '" + ans + "')")

    cur.execute(command)

    db.commit()

    print(u"Következő kör?")
    if raw_input() != "":
        db.close()
        break