import os
from PIL import Image

def compress_images(input_folder, output_folder, quality=85, max_width=1920, max_height=1080):
    """
    压缩指定文件夹内的图片并输出到目标文件夹。
    
    :param input_folder: 原始图片所在文件夹路径
    :param output_folder: 压缩后图片的存放路径
    :param quality: 压缩质量 (1-100)，值越高画质越好
    :param max_width: 最大宽度，超过此宽度则等比例缩小
    :param max_height: 最大高度，超过此高度则等比例缩小
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)
        if os.path.isfile(input_path):
            try:
                with Image.open(input_path) as img:
                    # 获取原始图片尺寸
                    original_width, original_height = img.size
                    
                    # 计算新的尺寸（等比例缩放）
                    scale = min(max_width / original_width, max_height / original_height, 1)
                    new_width = int(original_width * scale)
                    new_height = int(original_height * scale)
                    
                    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    
                    # 保存图片到目标文件夹
                    output_path = os.path.join(output_folder, file_name)
                    img.save(output_path, optimize=True, quality=quality)
                    print(f"压缩完成: {file_name} -> {output_path}")
            except Exception as e:
                print(f"处理失败: {file_name}, 错误信息: {e}")

# 示例：压缩当前文件夹下的图片
input_dir = "./"
output_dir = "./compressed_images"
compress_images(input_dir, output_dir, quality=85, max_width=1920, max_height=1080)
