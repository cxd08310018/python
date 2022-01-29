import turtle
import time
import random
import tkinter as tk
import threading
import draw_tiger

# 实现清屏
def clear_screen():
    turtle.screensize(50, 50, bg='yellow')
    turtle.penup()             #画笔抬起
    turtle.goto(0,0)        #定位到（0，0）
    turtle.color('white')
    turtle.pensize(800)         #画笔粗细
    turtle.pendown()           #画笔落下
    turtle.setheading(0)        #设置朝向
    turtle.fd(300)       #前进
    turtle.bk(600)      #后退

# 初始化海龟的位置
def go_start(x, y, state):
    turtle.pendown() if state else turtle.penup()
    turtle.goto(x, y)

#画线，state为真时海龟回到原点，为假时不回到原来的出发点
def draw_line(length, angle, state):
    turtle.pensize(1)
    turtle.pendown()
    turtle.setheading(angle)
    turtle.fd(length)
    turtle.bk(length) if state else turtle.penup()
    turtle.penup()

#显示倒数3,2,1
def draw_0(i):
    turtle.screensize(50, 50, bg='yellow')
    turtle.title("新春快乐，虎年大吉")
    turtle.speed(0)
    turtle.penup()
    turtle.hideturtle()  # 隐藏箭头显示
    turtle.goto(-50, -100)
    turtle.color('red')
    write = turtle.write(i, font=('宋体', 200, 'normal'))
    time.sleep(1)

# 显示文字
def draw_1():
    turtle.penup()
    turtle.hideturtle()    #隐藏箭头显示
    turtle.goto(-410, 0)
    turtle.color('red')
    write = turtle.write('叮咚~新年礼物到啦💕', font=('宋体', 60, 'normal'))
    time.sleep(2)


# 弹窗设置
def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('虎来喽！')
    window.geometry("200x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
             text='虎年快乐虎虎生威',  # 标签的文字
             bg='red',  # 背景颜色
             font=('..', 17),  # 字体和字体大小
             width=18, height=2  # 标签长宽
             ).pack()  # 固定窗口位置
    window.mainloop()

number=[3,2,1]    #储存显示界面倒数数字1,2,3


if __name__ == '__main__':
    turtle.setup(900, 500)     #调画布的尺寸
    for i in number:
        turtle.screensize(50, 50, bg='yellow')
        draw_0(i)
        clear_screen()
    turtle.screensize(50, 50, bg='yellow')
    draw_1()
    clear_screen()
    #turtle.screensize(50, 50, bg='yellow')
    draw_tiger.tiger()
    time.sleep(2)
    threads = []
    for i in range(20):  # 需要的弹框数量
        t = threading.Thread(target=dow)
        threads.append(t)
        time.sleep(0.01)
        threads[i].start()
