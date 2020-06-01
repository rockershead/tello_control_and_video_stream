import tello 
import time
from tkinter import *
from tkinter import ttk


def takeoff(event):
 drone.takeoff() 
 

def left(event):
 drone.move_left(0.3)
 
 print("move left")
 
 
def right(event):
 drone.move_right(0.3)
 print("move right")

def forward(event):
 drone.move_forward(0.3)
 print("move forward")
 
def back(event):
 drone.move_backward(0.3)
 print("move back")
 
def up(event):
 drone.move_up(0.3)
 print("move up")
 
def down(event):
 drone.move_down(0.3)
 print("move down")


def land(event):
 drone.land()
 print("land")
 print ("Flight time: %s" % drone.get_flight_time())
 
def up(event):
 drone.move_up(0.3)
 print("going up")

def down(event):
 drone.move_down(0.3)
 print("going down")
 
def flip_left(event):
 drone.flip('l')
 print("flip left")
 
def flip_right(event):
 drone.flip('r')
 print("flip right")
 
 
def video_on(event):
 drone.streamon()
 
def video_off(event):
 drone.streamoff


 
 
root = Tk()
drone = tello.Tello("192.168.10.2", 80)
batt_level=drone.get_battery()
print(batt_level)


root.bind("<v>", video_on)##press v to on video
root.bind("<b>", video_off)##press b to off video




#button_takeoff=Button(root, text="takeoff")
root.bind("<t>", takeoff)
#button_takeoff.grid(row=1,column=1)

#button_left=Button(root, text="left")
root.bind("<Left>", left)
#button_left.grid(row=3,column=0)

#button_forward=Button(root, text="forward")
root.bind("<Up>", forward)
#button_forward.grid(row=2,column=1)

#button_back=Button(root, text="back")
root.bind("<Down>", back)
#button_back.grid(row=4,column=1)

#button_right=Button(root, text="right")
root.bind("<Right>", right)
#button_right.grid(row=3,column=2)

#button_land=Button(root, text="land")
root.bind("<l>", land)
#button_land.grid(row=5,column=1)

#button_up=Button(root, text="up")
root.bind("w",up)
root.bind("s",down)
root.bind("a",flip_left)
root.bind("d",flip_right)



root.mainloop()





 
 



