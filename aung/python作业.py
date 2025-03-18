fahrenheit = float(input("输入一个华氏温度："))
celsiust = 5/9*(fahrenheit-32)
print("摄氏温度值为：",celsiust)

print("今天是星期4，求第n天之后是星期几？")
n = int(input("输入n的值:"))
weekday = (4*n)%7
print(n,"天之后，星期",weekday)

import math #三角函数
import time #时间

def main():
 g = 9.8
v0 = float(input("请输入火球的初速度（m/s）："))
theta = float(input("请输入施法角度（度）:"))
D = float(input("请输入目标水平距离："))

print(" 正在施法火球术，咒语聆听中...")

start_time = time.time()
施法时间 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
vx = v0 * math.cos(theta)
vy = v0 * math.sin(theta)
t_flight = D / vx
h_max = vy ** 2 / (2 * 9.8)
E = 50 * t_flight
end_time = time.time()
actual_time = end_time - start_time

print("===== 火球术弹道报告 =====")
print(f"施法时间：{施法时间}")
print(f"水平初速度：{vx:.2f}m/s")
print(f"垂直初速度：{vy:.2f}m/s")
print(f"飞行时间：{t_flight:.2f}秒")
print(f"最大高度：{h_max:.2f}米")
print(f"魔法能量消耗：{E:.2f}单位")
print(f"施法实际时间：{actual_time:.2f}秒")

print("戒！")
print("===== 火球术弹道报告 =====")
print(f"施法时间：{施法时间}")
print(f"水平初速度：{vx:.2f}m/s")
print(f"垂直初速度：{vy:.2f}m/s")
print(f"飞行时间：{t_flight:.2f}秒")
print(f"最大高度：{h_max:.2f}米")
print(f"魔法能量消耗：{E:.2f}单位")
print(f"施法实际时间：{actual_time:.2f}秒")
