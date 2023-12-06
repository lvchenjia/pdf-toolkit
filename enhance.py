from PIL import Image, ImageEnhance
import os

def darken_and_increase_contrast(image_path, output_path, factor=1, contrast_factor=1.5):
    # 打开图像
    img = Image.open(image_path)

    # 获取图像的RGB通道
    r, g, b = img.split()

    # 将每个通道中的像素值乘以一个因子，以加深颜色
    r = r.point(lambda i: i * factor)
    g = g.point(lambda i: i * factor)
    b = b.point(lambda i: i * factor)

    # 合并通道
    darkened_img = Image.merge('RGB', (r, g, b))

    # 增加对比度
    enhancer = ImageEnhance.Contrast(darkened_img)
    darkened_and_contrasted_img = enhancer.enhance(contrast_factor)

    # 保存处理后的图像
    darkened_and_contrasted_img.save(output_path)

# 处理文件夹中的所有图片
input_folder = 'input'  # 替换为你的图片文件夹路径
output_folder = 'output'  # 替换为你的输出文件夹路径

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        darken_and_increase_contrast(input_path, output_path)
