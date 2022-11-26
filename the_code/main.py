import easygui

q = ["ดินสอทำจากเยลลี่",
     "java เป็นภาษาคอม",
     "ps5ไม่เคยโดนรีเซล",
     "คนเป็นสิ่งมีชีวิต",
     "99999999999999*0 = 0",
     "1+1=11",
     "stack overflow เป็นเว็บเทรดคริปโต",
     "darksouls เป็นเกมผ่อนคลาย",
     "ปูตินเป็นผู้นำรัสเซีย",
     "ไข่เกิดก่อนไก่"
     ]
a = [False,
     True,
     False,
     True,
     True,
     False,
     False,
     False,
     True,
     False
     ]
point = 0

name = 'yes no ok'

op = easygui.ynbox('เกมตอบคำถาม10ข้อ', name, ("start", "exit"))

if op is True:
    play = [easygui.ynbox(q[0], name, ('yes', 'no')),
            easygui.ynbox(q[1], name, ('yes', 'no')),
            easygui.ynbox(q[2], name, ('yes', 'no')),
            easygui.ynbox(q[3], name, ('yes', 'no')),
            easygui.ynbox(q[4], name, ('yes', 'no')),
            easygui.ynbox(q[5], name, ('yes', 'no')),
            easygui.ynbox(q[6], name, ('yes', 'no')),
            easygui.ynbox(q[7], name, ('yes', 'no')),
            easygui.ynbox(q[8], name, ('yes', 'no')),
            easygui.ynbox(q[9], name, ('yes', 'no'))]

    for i in range(len(q)):
        if play[i] is a[i]:
            point += 1

    output = 'ตอบถูกไป' + str(point) + 'ข้อ'
    ed = easygui.msgbox(output, name, "close")
