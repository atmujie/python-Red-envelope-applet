import random
import time
import turtle

'''
作者：Atmujie
制作时间：2022/7/12

以下是为了让学生看懂代码加的阅读说明：
想要发红包，主界面自然是必不可少的，所以发红包小程序第一步如下：
第一步：创建主界面(包括以下内容)
    第29行：[定义窗口] 
    第36行：[显示红包图片] 
    第44行：[定义初始画笔]
有了主界面，自然需要让他点一下就发红包，所以第二步如下：
第二步：将鼠标左键和要执行的方法绑定：
    第106行：[将ask方法和鼠标左键绑定]
    第97行：[设置鼠标点击事件 —— ask方法]
ask方法依次引用了
    第51行：get_random_amount()函数 [随机获取金额] 这个函数传入了红包总数和总金额
    第67行：picture_disappears()函数 [让大红包图片消失]
    第77行：send_red_packets()函数 [发送红包] 这个函数传入了计算得到的每个小红包的金额
读程序记得按上面提到的顺序去读，才不会乱套
打包成windows可执行的exe文件需要先`pip install pyinstaller`安装pyinstaller工具
然后`pyinstaller.exe --onefile --windowed [python文件名].py`执行
--onefile 表示打包成一个文件，--windowed表示打包成windows系统可以执行的文件，即exe文件
'''

"""定义窗口"""
screen = turtle.Screen()  # 得到一个窗口
screen.setup(1280, 700)  # 设置
screen.bgpic('./data/背景图1280_960.gif')  # 设置背景图
screen.register_shape('./data/红包200_200.gif')  # 注册大红包图片
screen.register_shape('./data/小红包_64.gif')  # 注册小红包图片

"""显示红包图片"""
red_image = turtle.Turtle()  # 获取一个Turtle对象
red_image.hideturtle()  # 隐藏Turtle画笔
red_image.penup()  # 抬笔
red_image.goto(-300, 0)  # 确定位置
red_image.showturtle()  # 显示Turtle画笔
red_image.shape('./data/红包200_200.gif')  # 使用注册好的大红包图片

"""定义初始画笔"""
pen = turtle.Turtle()  # 获取一个Turtle对象
pen.hideturtle()  # 隐藏Turtle画笔
pen.penup()  # 抬笔
pen.goto(-300, -130)  # 确定位置
pen.write("点我发送红包",
          align="center", font=("宋体", 30, "normal"))  # 写入文字


# 随机获取金额
def get_random_amount(red_envelope_num, red_envelope_amount):
    amount_list = []  # 定义一个空列表
    for i in range(int(red_envelope_num)):  # 循环该列表
        if i == red_envelope_num - 1:  # 判断是否到最后一个红包
            amount = round(red_envelope_amount, 2)  # 最后一个红包得到剩下的全部金额
        else:
            expect = red_envelope_amount / (red_envelope_num - i)  # 设置期望值
            amount = round(random.uniform(0.01, expect * 2), 2)  # 获取金额
            red_envelope_amount -= amount  # 更新红包总金额
        amount_list.append(amount)  # 将取得的结果写入列表
    return amount_list  # 返回计算好的金额列表


# 让大红包图片消失
def picture_disappears():
    pen.clear()  # 清除原来的笔迹
    pen.write("正在生成红包....",
              align="center", font=("宋体", 30, "normal"))  # 设置新的笔迹
    time.sleep(2)  # 让程序暂停两秒
    pen.clear()  # 清除原来的笔迹
    red_image.hideturtle()  # 隐藏大红包图片


# 发送红包
def send_red_packets(amount_list):
    init_x, init_y = -600, 150  # 设置小红包初始坐标
    x, y = init_x, init_y  # 赋值给可变的坐标
    for i in range(1, len(amount_list) + 1):  # 循环计算得到的金额列表
        small_red_envelope = turtle.Turtle()  # 获取一个Turtle对象
        small_red_envelope.shape('./data/小红包_64.gif')  # 使用注册好的小红包图片
        small_red_envelope.penup()  # 抬笔
        small_red_envelope.goto(x, y)  # 将画笔移动到指定位置
        pen.goto(x, y - 50)  # 设置文字画笔的位置
        pen.write("{}".format(amount_list[i - 1]),
                  align="center", font=("宋体", 15, "normal"))  # 写入小红包的金额
        # 做判断，让小红包每输出5个就换一行
        if i % 5 == 0:
            y -= 100
            x = init_x
        else:
            x += 80


# 设置鼠标点击事件
def ask(x, y):
    red_envelope_amount = turtle.numinput("红包金额", "请输入红包金额", 100, 1, 200)  # 让玩家输入红包总金额
    red_envelope_num = turtle.numinput("红包数", "请输入红包数", 5, 1, 20)  # 让玩家输入红包总数
    amount_list = get_random_amount(red_envelope_num, red_envelope_amount)  # 获取每个小红包的金额
    picture_disappears()  # 让大红包图片消失
    send_red_packets(amount_list)  # 显示小红包图片和每个小红包的金额


"""将ask方法和鼠标左键绑定"""
red_image.onclick(ask, 1)

# 防止窗口关闭
turtle.done()
