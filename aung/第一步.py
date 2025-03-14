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

sketch_apple.py
from PIL import Image
import numpy as np


def convert_to_sketch(image_path):
    original_image = Image.open(image_path).convert("L")  # 打开图片, 并转换为灰度图

    img_array = np.array(original_image)  # 将图片转换为 np数组

    # 创建一个空的画布用于素描图
    sketch_img = np.zeros_like(img_array)  # 用 np 创建一个跟 img_array 数组模型一样的全 0 数组

    # 计算梯度
    for i in range(1, img_array.shape[0] - 1):
        for j in range(1, img_array.shape[1] - 1):  # 遍历图像的每个像素点 (按照坐标轴看 i是y j是x)
            gx = int(img_array[i, j + 1]) - int(img_array[i, j - 1])  # 计算x方向梯度
            gy = int(img_array[i + 1, j]) - int(img_array[i - 1, j])  # 计算y方向梯度
            magnitude = np.sqrt(gx ** 2 + gy ** 2)  # 计算梯度幅值
            sketch_img[i, j] = magnitude  # 将梯度幅值赋给sketch_img

    # 反转颜色以获得素描效果
    sketch_img = 255 - sketch_img  # 因为全 0 数组是黑色的，所以这里用 255 相减得反色

    # 将numpy数组转换回PIL图像
    sketch_image = Image.fromarray(sketch_img.astype(np.uint8))

    return sketch_image


input_image_path = "cropped_apple_no_bg.png"
output_image_path = "cropped_apple_sketch.png"

sketch_image = convert_to_sketch(input_image_path)
sketch_image.save(output_image_path)  # 保存图片