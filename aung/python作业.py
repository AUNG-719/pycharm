fahrenheit = float(input("输入一个华氏温度："))
celsiust = 5/9*(fahrenheit-32)
print("摄氏温度值为：",celsiust)

print("今天是星期4，求第n天之后是星期几？")
n = int(input("输入n的值:"))
weekday = (4*n)%7
print(n,"天之后，星期",weekday)
