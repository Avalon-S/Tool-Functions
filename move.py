import os
import shutil

# 定义基础路径
base_dir = './autodl-tmp/data/scene_datasets/hm3d/train'
# base_dir = './autodl-tmp/data/scene_datasets/hm3d/val'

# 定义需要合并的子文件夹
subfolders = ['train1', 'train2', 'train3', 'train4', 'train5']
# subfolders = ['val']

# 遍历每一个子文件夹
for subfolder in subfolders:
    subfolder_path = os.path.join(base_dir, subfolder)
    
    if not os.path.exists(subfolder_path):
        print(f"文件夹 {subfolder_path} 不存在，跳过。")
        continue

    # 遍历子文件夹中的每一个文件夹或文件
    for item in os.listdir(subfolder_path):
        item_path = os.path.join(subfolder_path, item)
        target_path = os.path.join(base_dir, item)

        # 如果目标路径已经存在，则跳过或重命名处理
        if os.path.exists(target_path):
            print(f"{item} 已经存在于 {base_dir}，跳过。")
            continue
        
        # 移动文件夹或文件
        shutil.move(item_path, target_path)
        print(f"{item} 已成功移动到 {base_dir}")

    # 删除空的子文件夹
    shutil.rmtree(subfolder_path)
    print(f"子文件夹 {subfolder} 已删除。")

print("所有文件夹内容已成功移动到 train 目录下！")
