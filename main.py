import os
import pandas as pd

def find_csv_with_postcode(folder_path, postcode):
    matched_files = []
    # 遍历文件夹内的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            try:
                # 使用pandas读取CSV文件
                df = pd.read_csv(file_path)
                # 检查POSTCODE列是否包含指定的postcode
                if postcode in df['POSTCODE'].values:
                    matched_files.append(filename)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    return matched_files

# 请将folder_path替换为你的CSV文件所在的文件夹路径
folder_path = 'D:/PyCharmProject/findPostcode/New'
postcode = 2100
matched_files = find_csv_with_postcode(folder_path, postcode)

print("含有POSTCODE 2099的文件名有:")
for file in matched_files:
    print(file)
