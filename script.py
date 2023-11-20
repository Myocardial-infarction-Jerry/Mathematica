import pytesseract
from pdf2image import convert_from_path
import os
import sys

def pdf_to_markdown(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image, lang='eng')
    return text

# 通过命令行参数传入文件路径
if len(sys.argv) < 2:
    print("请提供PDF文件路径作为参数")
else:
    pdf_path = sys.argv[1]
    markdown_text = pdf_to_markdown(pdf_path)

    # 保存为Markdown文件
    base_path = os.path.dirname(pdf_path)
    file_name = os.path.splitext(os.path.basename(pdf_path))[0]
    markdown_path = os.path.join(base_path, file_name + ".md")

    with open(markdown_path, "w", encoding="utf-8") as file:
        file.write(markdown_text)

    print(f"转换完成，Markdown文件保存为：{markdown_path}")
