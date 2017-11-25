#!/usr/bin/env python3

"""Foobar.py: Description of what foobar does.

__author__ = "WangYiwen"
__pkuid__  = "1700011805"
__email__  = "wangyiwen@pku.edu.cn"
"""

import turtle
import math

   
def drawFnScaled (ttl, a,e,ttlcolor,fn1,fn2,t):
    ttl.penup
    ttl.color(ttlcolor)
    ttl.pensize(2)
    ttl.shapesize(0.5,0.5)
    ttl.shape("circle")
    x = fn1 (t)
    y = fn2 (t)
    b=a*math.sqrt(1-e**2)
    scaledX = x * a
    scaledY = y * b
    ttl.goto (scaledX, scaledY)
    ttl.pendown()

    
def  drawGalaxy(t1,t2,t3,t4,t5,t6,k1,k2,k3,k4,k5,k6):
    drawFnScaled (t1,39,0.4,"red",math.cos,math.sin,k1)
    drawFnScaled (t2,72,0.1,"orange",math.cos,math.sin,k2)
    drawFnScaled (t3,100,0.3,"yellow",math.cos,math.sin,k3)   
    drawFnScaled (t4,150,0.2,"green",math.cos,math.sin,k4)
    drawFnScaled (t5,210,0.25,"blue",math.cos,math.sin,k5)   
    drawFnScaled (t6,300,0.15,"purple",math.cos,math.sin,k6)

       
def main():
    wn=turtle.Screen()
    wn.bgcolor("black")
    t0=turtle.Turtle()
    t1= turtle.Turtle()
    t2= turtle.Turtle()
    t3= turtle.Turtle()
    t4= turtle.Turtle()
    t5= turtle.Turtle()
    t6= turtle.Turtle()
    t0.color("yellow")
    t0.shape("circle")
    for ttl in [t1,t2,t3,t4,t5,t6]:
        ttl.penup()
        
    k1,k2,k3,k4,k5,k6=0,0,0,0,0,0
    while k5<1000:
        drawGalaxy(t1,t2,t3,t4,t5,t6,k1,k2,k3,k4,k5,k6)
        k1=k1+0.002
        k2=k2+0.006
        k3=k3+0.010
        k4=k4+0.004
        k5=k5+0.012
        k6=k6+0.008

if __name__ == "__main__":
    main()
