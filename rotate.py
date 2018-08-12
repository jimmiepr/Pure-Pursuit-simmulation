from tkinter import *
from tkinter import ttk  
from tkinter.ttk import Notebook
import time
import math

def getposition(event):
	xp = event.x
	yp = event.y 
	print('xp = {}, yp = {}'.format(xp,yp))

def get():
	car_x = float(bot_x.get()) 
	car_y = float(bot_y.get()) 
	car_sp = float(bot_sp.get()) 
	angle = float(bot_angle.get()) 
	car = [car_x,car_y,angle,car_sp]
	print(type(car_x))
	return car 

def rotate(points, angle, center):
    angle = math.radians(angle)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    cx, cy = center
    new_points = []
    for x_old, y_old in points:
        x_old -= cx
        y_old -= cy
        x_new = x_old * cos_val - y_old * sin_val
        y_new = x_old * sin_val + y_old * cos_val
        new_points.append([x_new + cx, y_new + cy])
    return new_points

def run():
	print('RUN')

def reset():
	print('Reset')

GUI = Tk()
GUI.geometry('1000x505')
GUI.title('Pure Pursuit Controller')

box_1 = Frame(GUI)
box_1.pack(side = LEFT)

box_2 = Frame(GUI)
box_2.pack(side = RIGHT)

Tap = Notebook(GUI)
setRobot = Frame(Tap)
graphTap = Frame(Tap)
Tap.add(setRobot,text='Set Robot')
Tap.add(graphTap,text='Graph')
Tap.pack(fill=BOTH,expand=1)
bot_x = StringVar()
bot_y = StringVar() 
bot_sp = StringVar() 
bot_angle = StringVar()

lb1 = Label(setRobot,text='Enter Position X ',font=('Angsana new',18,'bold'))
lb1.grid(row=0,column=0)
ed_x = ttk.Entry(setRobot,textvariable=bot_x,font=('Angsana new',18))
ed_x.grid(row=1,column=1)

lb2 = Label(setRobot,text='Enter Position Y ',font=('Angsana new',18,'bold'))
lb2.grid(row=2,column=0)
ed_y = ttk.Entry(setRobot,textvariable=bot_y,font=('Angsana new',18))
ed_y.grid(row=3,column=1)

lb3 = Label(setRobot,text='Enter Robot Angle ',font=('Angsana new',18,'bold'))
lb3.grid(row=4,column=0)
ed_angle = ttk.Entry(setRobot,textvariable=bot_angle,font=('Angsana new',18))
ed_angle.grid(row=5,column=1)

lb4 = Label(setRobot,text='Enter Robot Speed ',font=('Angsana new',18,'bold'))
lb4.grid(row=6,column=0)
ed_sp = ttk.Entry(setRobot,textvariable=bot_sp,font=('Angsana new',18))
ed_sp.grid(row=7,column=1)


btn_get = ttk.Button(setRobot,text='Get Robot',command=get)
btn_get.place(x=50,y=350, height=50, width=100)
btn_res = ttk.Button(setRobot,text='Reset',command=reset)
btn_res.place(x=200,y=350, height=50, width=100)
btn_run = ttk.Button(setRobot,text='RUN',command=run)
btn_run.place(x=350,y=350, height=50, width=100)


cw = 500 
ch = 500 
CV = Canvas(box_1,width=cw,height=ch,bg = 'black')
CV.pack(side = TOP ,expand =1)


#-----------------------------------------------------[1   2       3     4    5      6      7      8   9     10     11     12   13    14     15   ]
pos_x = [180, 60, 60,140,220,260,280,320,380,380,320,200,177.04,157.57,140,144.57,155.57,177.04,200,222.96,242.43,255.43,260,255.43,242.43,222.96]
pos_y = [ 60,160,280,320,320,300,280,260,200,120, 60, 60, 64.57, 77.57,120,142.96,162.43,175.43,180,175.43,162.43,142.96,120, 97.04, 77.57, 64.57]

poly = [[220,380],[260,380],[260,400],[220,400]]
car = CV.create_polygon(poly,fill='blue',outline='red')

count = len(pos_x)
for i in range(count):
	if i == count-1 : 
		CV.create_line(pos_x[i],pos_y[i],pos_x[11],pos_y[11] ,fill ='yellow',width=2)	
	else :
		CV.create_line(pos_x[i],pos_y[i],pos_x[i+1],pos_y[i+1] ,fill ='yellow',width=2)		
CV.create_line(pos_x[11],pos_y[11],pos_x[0],pos_y[0] ,fill ='yellow',width=2)

for i in range(100):
	CV.move(car,1,-1)
	CV.update()
	time.sleep(0.05)

center = 320,290
new_car = rotate(poly,30,center)
car = CV.create_polygon(new_car,fill='blue',outline='red')	

GUI.bind('<Button-1>',getposition)
GUI.mainloop()