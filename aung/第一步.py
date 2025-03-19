#num1 = float(input("输入第一个数值；"))
#num2 = float(input("输入第一个数值；"))
#num3 = float(input("输入第一个数值；"))
#average = (num1 + num2 + num3)/3
#print("平均值为：",average)

#摄氏度 = eval(input("输入一个摄氏度读数:"))
#华氏度 = 摄氏度 * 9 / 5 + 32
#print("华氏度为：",华氏度)

#radius,height = eval(input("输入圆锥体的底面半径与高的值："))
#area = 3.14 * radius **2
#volume = 1/3*area*height
#print("圆锥体的体积：",volume)

#num1 = int(input("输入三位数："))
#height1 = num1 % 10
#height2 = num1 // 10 % 10
#height3 = num1 // 100
#sum  = height1 + height2 + height3
#print ("三位数的和：",sum)

print("今天是星期4，求第n天之后是星期几？")
n = int(input("输入n的值:"))
weekday = (4*n)%7
print(n,"天之后，星期",weekday)

