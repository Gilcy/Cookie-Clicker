import turtle
import random
import time
turtle.register_shape("Cookie.gif")
turtle.register_shape("Breaked_Cookie.gif")
obj= turtle.Turtle()
writing= turtle.Turtle()
writing1= turtle.Turtle()
writing1.setpos(0,165)
writing2=turtle.Turtle()
writing2.setpos(0,-175)
writing3=turtle.Turtle()
writing3.setpos(0,-195)
obj.shape("Cookie.gif")
screen=turtle.Screen()
clicks = 0

def clicked(x,y):
    global clicks
    clicks = clicks + 1
    writing.penup()
    writing.setpos(0,140)
    writing.pendown()
    writing.clear() 
    writing.write("clicks="+str(clicks),font=("Arial",20,"bold"))

obj.onclick(clicked)
Timer=0
while(Timer<60):
  screen.update()
  Timer=Timer+1
  time.sleep(0.07)
  writing2.clear()
  writing2.write("Timer="+str(Timer),font=("Arial",20,"bold"))
  if((clicks > Timer)and(Timer== 60)):
    writing3.write('You won! Celebrate!!;)',font=("Arial",20,"bold"))
  elif((clicks<Timer) and(Timer==60)):
    writing3.write('You lost the cricket code! Try again!',font=("Arial",20,"bold"))

turtle.done()
