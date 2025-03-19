import time
import math
import turtle

# 获取当前时间
current_time = time.localtime()
hour = current_time.tm_hour  # 显示用小时
hour_for_angle = current_time.tm_hour + current_time.tm_min / 60  # 计算用时间

# 计算太阳高度角（正午90°，每小时变化15°）
sun_elevation = 90 - 15 * (hour_for_angle - 12)

# 晷针高度
gnomon_height = 100

# 计算影子长度
if math.tan(math.radians(sun_elevation)) != 0:
    shadow_length = gnomon_height / math.tan(math.radians(sun_elevation))
else:
    shadow_length = 0  # 防止除以零

# 初始化画布
screen = turtle.Screen()
screen.title("简易日晷")
screen.bgcolor("white")

# 绘制日晷盘
dial = turtle.Turtle()
dial.speed(0)
dial.penup()
dial.goto(0, -150)
dial.pendown()
dial.circle(150)

# 绘制刻度（12小时制）
dial.penup()
dial.goto(0, 0)
dial.setheading(90)  # 正北为0刻度
for i in range(12):
    dial.forward(140)
    dial.pendown()
    dial.forward(10)  # 刻度线长度
    dial.penup()
    dial.goto(0, 0)
    dial.right(30)  # 每小时30°

# 绘制晷针（红色竖线）
gnomon = turtle.Turtle()
gnomon.color("red")
gnomon.pensize(4)
gnomon.penup()
gnomon.goto(0, 0)
gnomon.pendown()
gnomon.setheading(90)  # 正北方向
gnomon.forward(gnomon_height)

# 绘制影子
shadow = turtle.Turtle()
shadow.color("gray")
shadow.pensize(4)
shadow.penup()
shadow.goto(0, 0)
shadow.pendown()

if abs(shadow_length) > 1:  # 增加影子长度最小显示值
    # 调整影子角度（适配turtle坐标系）
    shadow_angle = 90 - 15 * (hour_for_angle - 12)
    if sun_elevation < 0:  # 太阳低于地平线时调整方向
        shadow_angle += 180
    shadow.setheading(shadow_angle)
    shadow.forward(abs(shadow_length))
else:
    shadow.write("太阳接近直射或角度异常", align="center", font=("Arial", 12, "normal"))

# 显示当前时间和影长
info = turtle.Turtle()
info.hideturtle()
info.penup()
info.goto(-120, -180)
info.write(
    f"当前时间: {hour}:{current_time.tm_min:02d}\n影子长度: {abs(shadow_length):.1f}像素",
    font=("Arial", 14, "normal")
)

screen.mainloop()
