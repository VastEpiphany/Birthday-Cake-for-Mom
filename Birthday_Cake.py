import random as r
import turtle as t
import math
import time

def drawX(a,i):
    angle = math.radians(i) # 将角度转化为弧度
    return a*math.cos(angle) # 计算我们的x坐标（椭圆的参数方程表示x = a * cosθ）

def drawY(b, i):
    angle = math.radians(i)
    return b * math.sin(angle) # 计算我们的y坐标（椭圆的参数方程表示y = b * sinθ)

# 初步的窗口设置
t.setup(800,600,startx=0,starty=0)
t.bgcolor("#f4cf8c")
t.title("给妈妈的生日蛋糕🎂")
t.speed(0) # 最快画笔移动速度
t.tracer(2, 5)
#t.tracer(0)
t.penup()
t.goto(150,0)
t.pendown()
######################1.画出基座椭圆托盘并填充#######################
t.pencolor("white")
# 用于在绘制一个要填充的形状之前调用（e.g.蛋糕内部颜色）,不接受任何参数
t.begin_fill() 
for i in range(360):
    # 绘制长轴为300，短轴为120的椭圆（通过椭圆的参数方程得到对应坐标）
    x = drawX(150,i)
    y = drawY(60,i)
    t.goto(x,y) # 移动至先前计算得到的(x,y)坐标下，注意到已经为pendown所以绘图
t.fillcolor("#f5c199") # 填充基座椭圆的颜色
t.end_fill()
######################2.填补基座椭圆下的阴影#######################
t.begin_fill()
for i in range(180):
    x = drawX(150,-i)
    y = drawY(70,-i)
    t.goto(x,y)
for i in range(180,360):
    x = drawX(150,i)
    y = drawY(60,i)
    t.goto(x,y)
t.fillcolor("#f2d7dd")
t.end_fill()
######################3.托盘上一层蛋糕与盘面的接触面椭圆#######################
t.pu() #抬起画笔
for i in range(30):
    x -= 1
    t.goto(x,0)
# t.goto(120,0)
t.pd()
t.begin_fill()
for i in range(360):
    x = drawX(120,i)
    y = drawY(48,i)
    t.goto(x,y)
t.fillcolor("#cbd9f9") # 浅蓝色
t.end_fill()
######################4.画出一层蛋糕#######################
t.begin_fill()
t.pencolor("#fee48c")
# 360°画出上平移70高的椭圆，然后画笔还要再移动180°到左侧，停止循环，
for i in range(70):
    y += 1
    t.goto(120,y)
for i in range(540):
    x = drawX(120,i)
    y = drawY(48,i) + 70
    t.goto(x,y)
for i in range(70):
    y -= 1
    t.goto(-120,y) #以屏幕中心为原点坐标相对移动到xxx位置
# t.goto(-120,0) 
t.fillcolor("#cbd9f9")
t.end_fill()
######################5.上面一层的奶盖#######################
t.pu()
for i in range(180,360):
    x = drawX(120,i)
    y = drawY(48,i)
    t.goto(x,y)
for i in range(70):
    y += 1
    t.goto(120,y) # 回到上面的那个椭圆
t.pd()
t.pencolor("#fff0f3")
t.begin_fill()
for i in range(360):
    x = drawX(120, i)
    y = drawY(48, i) + 70
    t.goto(x, y)
t.fillcolor("#fff0f3") # 盖上一层白奶油（上层椭圆的白色填充）
t.end_fill()
######################6.画一层更小的椭圆#######################
t.pu()
for i in range(10):
    x -= 1
    t.goto(x,70)
#t.goto(110,70)
t.pd()
t.pencolor("#fff9fb") # 奶白色
t.begin_fill()
for i in range(360):
    x = drawX(110, i)
    y = drawY(44, i) + 70
    t.goto(x, y)
t.fillcolor("#fff9fb")
t.end_fill()
######################7.填充最下层蛋糕与盘子间接触的部分#######################
t.pu()
for i in range(10):
    x += 1
    t.goto(x,70)
for i in range(70):
    y -= 1
    t.goto(120,y)
#t.goto(120, 0)
t.pd()
t.begin_fill()
t.pencolor("#ffa79d") # 浅粉红色
for i in range(180):
    x = drawX(120, -i)
    y = drawY(48, -i) + 10
    t.goto(x, y)
t.goto(-120, 0)
for i in range(180, 360):
    x = drawX(120, i)
    y = drawY(48, i)
    t.goto(x, y)
t.fillcolor("#ffa79d")
t.end_fill()
######################8.画出底层大蛋糕周围一圈的波浪线奶油淋盖#######################
t.pu()
for i in range(70):
    y += 1
    t.goto(120,y)
#t.goto(120,70) # 回到上层最大的那个椭圆的最右侧端点
t.pd()
t.begin_fill()
t.pensize(4) # 画笔变粗
t.pencolor("#fff0f3") #白奶油色
for i in range(1800):
    x = drawX(120, 0.1 * i)
    y = drawY(-18, i) + 10
    t.goto(x, y)
for i in range(70):
    y += 1
    t.goto(-120,y)
#t.goto(-120, 70) #回到上层最大的那个椭圆的最左侧端点,沿着上层椭圆再描一次使曲线闭合
t.pensize(1)
for i in range(180,360):
    x = drawX(120,i)
    y = drawY(48,i) + 70
    t.goto(x,y)
t.fillcolor("#fff0f3")
t.end_fill()
######################9.开始绘制上层的小椭圆蛋糕层#######################
t.pu()
for i in range(40):
    x -= 1
    t.goto(x,70)
#t.goto(80,70) # 找到上层小椭圆下部的锚点，a=80
t.pd()
t.begin_fill() 
t.pencolor("#6f3732") # 巧克力色
for i in range(50):
    y +=1 
    t.goto(80,y)
#t.goto(80,120) #直接上移，证明上层蛋糕高度为50 （下层为70）
for i in range(540):
    x = drawX(80,i)
    y = drawY(32,i) + 120
    t.goto(x,y)
for i in range(50):
    y -=1
    t.goto(-80,y)
#t.goto(-80,70) # 回到下层的左侧锚点，但是还没完，还要沿着下层再画一次
for i in range(180,360):
    x = drawX(80,i)
    y = drawY(32,i) + 70
    t.goto(x,y)
t.fillcolor("#6f3732") # 填充上层的巧克力色
t.end_fill()
######################10.巧克力上层上部的奶盖覆盖#######################
t.pu()
for i in range(50):
    y += 1
    t.goto(80,y)
#t.goto(80, 120)
t.pd()
t.pencolor("#f5ffbd")
t.begin_fill()
for i in range(360):
    x = drawX(80, i)
    y = drawY(32, i) + 120
    t.goto(x, y)
t.fillcolor("#f5ffbd")
t.end_fill()
######################11.上层椭圆上部的小奶油圆圈部分#######################
t.pu()
for i in range(10):
    x -= 1
    t.goto(x,120)
#t.goto(70,120) #上层椭圆上部的小奶油圆圈部分（准备插蜡烛的）
t.pd()
t.pencolor("#fddaff")
t.begin_fill()
for i in range(360):
    x = drawX(70, i)
    y = drawY(28, i) + 120
    t.goto(x, y)
t.fillcolor("#fddaff")
t.end_fill()
######################12.上层蛋糕的波浪形奶盖#######################
t.pu()
time.sleep(5)
t.tracer(1,5)
for i in range(10):
    x += 1
    t.goto(x,120)
# t.goto(80, 120)
t.pd()
t.begin_fill()
t.pencolor("#f5ffbd")
t.pensize(3)
for i in range(1800):
    x = drawX(80, 0.1 * i)
    y = drawY(-12, i) + 80
    t.goto(x, y)
for i in range(40):
    y +=1
    t.goto(-80,y)
#t.goto(-80, 120) #回到上层最大的那个椭圆的最左侧端点,沿着上层椭圆再描一次使曲线闭合
t.pensize(1)
for i in range(180,360):
    x = drawX(80,i)
    y = drawY(32,i) + 120
    t.goto(x,y)
t.fillcolor("#f5ffbd")
t.end_fill()
######################13.画出第一个蜡烛（64,120）#######################
t.pu()
for i in range(16):
    x -=1
    t.goto(x,120)
# t.goto(64, 120)
t.pd()
t.pencolor("#fd1f00") # 蜡烛芯颜色（天蓝b1c9e9，红色fd1f00）
t.begin_fill()
# 画一个很小的蜡烛的底座
for i in range(360):
    x = drawX(4, i) + 60
    y = drawY(1, i) + 120
    t.goto(x, y)
for i in range(50):
    y += 1
    t.goto(64,y)
#t.goto(64, 170)
# 画完整个蜡烛
for i in range(540):
    x = drawX(4, i) + 60
    y = drawY(1, i) + 170
    t.goto(x, y)
for i in range(50):
    y -= 1
    t.goto(56,y)
#t.goto(56, 120)
t.fillcolor("#fd1f00")
t.end_fill()
t.pencolor("white") # 蜡烛上的白色螺旋曲线
t.pensize(2) # 白色螺旋曲线是加粗的
# 画蜡烛螺旋圈
for i in range(1, 6):
    t.goto(64, 120 + 10 * i)
    t.pu()
    t.goto(56, 120 + 10 * i)
    t.pd()
t.pu()
t.goto(60, 170)
t.pd()
t.goto(60, 180)
t.pensize(1)
######################14.画蜡烛上面的火#######################
t.pu()
t.goto(64, 190)
t.pd()
t.pencolor("#ffbf0f") # 橙色火焰
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 60
    y = drawY(10, i) + 190
    t.goto(x, y)
t.fillcolor("#ffbf0f")
t.end_fill()
######################15.第二根蜡烛(-56,120)#######################
t.pu()
t.goto(-56, 120)
t.pd()
t.pencolor("#fd1f00")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 60
    y = drawY(1, i) + 120
    t.goto(x, y)
for i in range(50):
    y += 1
    t.goto(-56,y)
#t.goto(-56, 170)
for i in range(540):
    x = drawX(4, i) - 60
    y = drawY(1, i) + 170
    t.goto(x, y)
for i in range(50):
    y -= 1
    t.goto(-64,y)
#t.goto(-64, 120)
t.fillcolor("#fd1f00")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(-56, 120 + 10 * i)
    t.pu()
    t.goto(-64, 120 + 10 * i)
    t.pd()
t.pu()
t.goto(-60, 170)
t.pd()
t.goto(-60, 180)
t.pensize(1)
# 蜡烛上面的火
t.pu()
t.goto(-56, 190)
t.pd()
t.pencolor("#ffbf0f") # 橙色火焰
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 60
    y = drawY(10, i) + 190
    t.goto(x, y)
t.fillcolor("#ffbf0f")
t.end_fill()
######################16.第三根蜡烛（0，130）#######################
t.pu()
t.goto(0, 130)
t.pd()
t.pencolor("#fd1f00")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) 
    y = drawY(1, i) + 130
    t.goto(x, y)
for i in range(50):
    y += 1
    t.goto(4,y)
#t.goto(4, 180)
for i in range(540):
    x = drawX(4, i) 
    y = drawY(1, i) + 180
    t.goto(x, y)
for i in range(50):
    y -= 1
    t.goto(-4,y)
#t.goto(-4, 130)
t.fillcolor("#fd1f00")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(4, 130 + 10 * i)
    t.pu()
    t.goto(-4, 130 + 10 * i)
    t.pd()
t.pu()
t.goto(0, 180)
t.pd()
t.goto(0, 190)
t.pensize(1)
# 蜡烛上面的火
t.pu()
t.goto(4, 200)
t.pd()
t.pencolor("#ffbf0f") # 橙色火焰
t.begin_fill()
for i in range(360):
    x = drawX(4, i) 
    y = drawY(10, i) + 200
    t.goto(x, y)
t.fillcolor("#ffbf0f")
t.end_fill()
######################17.第四根蜡烛（30,110）#######################
t.pu()
t.goto(30, 110)
t.pd()
t.pencolor("#fd1f00")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 30
    y = drawY(1, i) + 110
    t.goto(x, y)
for i in range(50):
    y += 1
    t.goto(34,y)
#t.goto(34, 160)
for i in range(540):
    x = drawX(4, i) + 30
    y = drawY(1, i) + 160 # 一个蜡烛高50
    t.goto(x, y)
for i in range(50):
    y -= 1
    t.goto(26,y)
#t.goto(26, 110)
t.fillcolor("#fd1f00")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(34, 110 + 10 * i)
    t.pu()
    t.goto(26, 110 + 10 * i)
    t.pd()
t.pu()
t.goto(30, 160)
t.pd()
t.goto(30, 170)
t.pensize(1)
# 蜡烛上面的火
t.pu()
t.goto(34, 180)
t.pd()
t.pencolor("#ffbf0f") # 橙色火焰
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 30
    y = drawY(10, i) + 180
    t.goto(x, y)
t.fillcolor("#ffbf0f")
t.end_fill()
######################18.第五根蜡烛（-30，110）#######################
t.pu()
t.goto(-30, 110)
t.pd()
t.pencolor("#fd1f00")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 30
    y = drawY(1, i) + 110
    t.goto(x, y)
for i in range(50):
    y += 1
    t.goto(-26,y)
#t.goto(-26, 160)
for i in range(540):
    x = drawX(4, i) - 30
    y = drawY(1, i) + 160 # 一个蜡烛高50
    t.goto(x, y)
for i in range(50):
    y -= 1
    t.goto(-34,y)
#t.goto(-34, 110)
t.fillcolor("#fd1f00")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(-26, 110 + 10 * i)
    t.pu()
    t.goto(-34, 110 + 10 * i)
    t.pd()
t.pu()
t.goto(-30, 160)
t.pd()
t.goto(-30, 170)
t.pensize(1)
# 蜡烛上面的火
t.pu()
t.goto(-26, 180)
t.pd()
t.pencolor("#ffbf0f") # 橙色火焰
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 30
    y = drawY(10, i) + 180
    t.goto(x, y)
t.fillcolor("#ffbf0f")
t.end_fill()
######################19.开始撒随机颜色的糖霜#######################
# 随机颜色的list（七彩色：红橙黄绿青蓝紫）
rand_colors = ["#FF0000","#FFA500","#FFFF00","#00FF00","#00FFFF","#0000FF","#800080"]
# 下层大蛋糕的随机糖霜
for i in range(80):
    t.pu()
    x = r.randint(-120,120)
    y = r.randint(-25,30)
    t.goto(x,y)
    t.pd()
    t.dot(r.randint(2,5),rand_colors[r.randint(0,6)])
for i in range(40):
    t.pu()
    x = r.randint(-90, 90)
    y = r.randint(-35, 10)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), rand_colors[r.randint(0, 6)])
# 上层蛋糕糖霜的制作
for i in range(40):
    t.pu()
    x = r.randint(-80, 80)
    y = r.randint(60, 90)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), rand_colors[r.randint(0, 6)])
for i in range(50):
    t.pu()
    x = r.randint(-50, 50)
    y = r.randint(45, 70)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), rand_colors[r.randint(0, 6)])
# 主界面上的随机撒花糖霜
for i in range(50):
    t.pu()
    x = r.randint(-500, 500)
    y = r.randint(120, 300)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(3, 5), rand_colors[r.randint(0, 6)])
######################20.画笔抬起归位，准备加入祝福字体#######################
t.pu()
t.goto(0,0)
texts = [
        ("祝 妈 妈 生 日 快 乐！", (-320, -200), "red", 30),
        ("永 远 健 康 幸 福 ~", (-320, -230), "#b8aaff", 24),
        ("——XP",(-320,-260),"#ff8994",24)
    ]
    
for text, pos, color, size in texts:
    t.penup()
    t.goto(pos)
    t.color(color)
    t.write(text, font=("楷体", size, "bold"))

# 走到这里标志着我们绘图任务的完成，防止窗口立即关闭
t.update()
t.done()