#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import random
from datetime import datetime
win = Tk()
win.title("AIM_GAME")
win.geometry("550x150")
win.option_add("*Font","궁서 20")

# Label
lab = Label(win)
lab.config(text="표적 개수")
lab.grid(column=0, row=0, padx=20, pady=20)

#Entry
ent = Entry(win)
ent.grid(column=1, row=0, padx=20, pady=20)

k = 1

def cc():
    global k
    if k <num_t:
        k +=1
        btn.destroy()
        ran_btn()
    else : 
        final = datetime.now()
        dif_sec=(final-start).total_seconds()
        btn.destroy()
        lab = Label(win)
        lab.config(text="clear "+str(dif_sec)+"초")
        lab.pack(pady= 230)

def ran_btn():
    global btn
    btn=Button(win)
    btn.config(bg="red")
    btn.config(command=cc)
    btn.config(text=k)
    btn.place(relx=random.random(),rely=random.random())

def bnt_f():
    global num_t # 밖에서도 쓴다.
    global start
    num_t=int(ent.get())
    #win.gird_slaves() # [label, ent, btn]
    for wg in win.grid_slaves():
        wg.destroy()
    #win.pack_slaves() 만약 pack으로 했다면
    win.geometry("500x500")
    ran_btn()
    start = datetime.now()
    # 랜덤한 위치에서 버튼이 생성

#Button
btn=Button(win)
btn.config(text="시작")
btn.config(command=bnt_f)
btn.grid(column=0, row=1,columnspan=2)

win.mainloop()


# In[ ]:




