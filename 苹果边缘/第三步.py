
import cv2
import numpy as np

# 读取单色苹果图片
apple_image = cv2.imread('单色苹果.png', cv2.IMREAD_GRAYSCALE)

# 使用Canny边缘检测算法找到苹果的轮廓
edges = cv2.Canny(apple_image, threshold1=30, threshold2=100)

# 创建一个全白的背景板
white_background = np.ones_like(apple_image) * 255

# 在白色背景上绘制黑色轮廓线
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(white_background, contours, -1, (0, 0, 0), thickness=2)

# 将结果保存为轮廓.png
cv2.imwrite('轮廓.png', white_background)
