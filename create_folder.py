import os

# 定义文件夹名称
folder_name = "苹果边缘"

# 获取当前工作目录
current_directory = os.getcwd()

# 拼接完整路径
new_folder_path = os.path.join(current_directory, folder_name)

# 创建文件夹
os.makedirs(new_folder_path, exist_ok=True)

print(f"文件夹 '{folder_name}' 已成功创建在路径: {new_folder_path}")