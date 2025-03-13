import rembg
from PIL import Image, ImageDraw, ImageFilter

# 定义图片路径
image_path = "a.png"
output_path = "无背景.png"
final_output_path = "单色苹果.png"

# 读取图片
input_image = Image.open(image_path)

# 去除背景
output_image = rembg.remove(input_image)

# 保存去除背景后的图片
output_image.save(output_path)

print(f"已成功去除背景并保存为: {output_path}")
