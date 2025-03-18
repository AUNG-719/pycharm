import time
p = float(input("请输入贷款总额（单位：元）："))
annual_interest_rate = float(input("请输入年利率（百分比）："))
years = float(input("请输入贷款年限："))

r = annual_interest_rate /100 / 12
n = years * 12

print("正在计算每月还款金额，程序将延时2秒...")
time.sleep(2)

M = p * (r * ((1 + r)** n))/(((1 + r)** n) - 1)

print(f"贷款总额:{p}元")
print(f"年利润：{annual_interest_rate}%")
print(f"贷款年限：{years}年")
print(f"每月还款金额：{M:.2f}元")