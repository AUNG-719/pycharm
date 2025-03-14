apple_extraction.py
from rembg import remove

# 读取原始图片
input_path = "cropped_apple.png"  # 替换为你的图片路径
output_path = "cropped_apple_no_bg.png"   # 处理后保存路径

# 打开图片并去除背景
with open(input_path, "rb") as inp_file:
    input_image = inp_file.read()
    output_image = remove(input_image)  # 使用 rembg 进行背景去除

# 保存去背景后的图片
with open(output_path, "wb") as out_file:
    out_file.write(output_image) # 写入图片
import cv2

# 读取图像
image = cv2.imread('apple.png')

# 获取图像的高度和宽度
height, width = image.shape[:2]

# 计算新的高度范围
new_height_start = height // 3  # 从上面裁剪掉1/3
new_height_end = height  # 留下面2/3的部分

# 裁剪图像宽度的一半，并且裁剪高度的下2/3部分
cropped_image = image[new_height_start:new_height_end, width//2:]

# 保存裁剪后的图像
cv2.imwrite('cropped_apple.png', cropped_image)

