import zipfile
import os
import shutil
from concurrent.futures import ThreadPoolExecutor

# 定义解压目标路径
base_dir = './autodl-tmp/data/scene_datasets/hm3d'
train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'val')

# 确保目标文件夹存在
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# 压缩包文件路径
train_zip_files = ['./autodl-fs/train1.zip', './autodl-fs/train2.zip', './autodl-fs/train3.zip', './autodl-fs/train4.zip', './autodl-fs/train5.zip']
val_zip_file = './autodl-fs/val.zip'

# 解压函数，保留文件夹结构
def extract_and_preserve_structure(zip_file, target_dir):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        for member in zip_ref.namelist():
            # 提取目标路径（保持文件夹结构）
            target_path = os.path.join(target_dir, member)
            
            if member.endswith('/'):
                # 如果是文件夹，创建文件夹
                os.makedirs(target_path, exist_ok=True)
            else:
                # 如果是文件，提取文件
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                with zip_ref.open(member) as source, open(target_path, 'wb') as target:
                    shutil.copyfileobj(source, target)
    
    print(f"{zip_file} 解压完成！")

# 创建多线程解压
with ThreadPoolExecutor() as executor:
    # 对 train1-5.zip 文件并行解压
    for zip_file in train_zip_files:
        executor.submit(extract_and_preserve_structure, zip_file, train_dir)

    # 解压 val.zip 文件
    executor.submit(extract_and_preserve_structure, val_zip_file, val_dir)

print("所有文件解压完成，文件夹结构保留！")
