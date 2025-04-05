import torch

try:
    # 检查 CUDA 是否可用
    if torch.cuda.is_available():
        device = torch.device("cuda")
        total_memory = torch.cuda.get_device_properties(device).total_memory
        print(f"GPU 可用！")
        print(f"GPU 名称：{torch.cuda.get_device_name(device)}")
        print(f"总显存大小：{total_memory / (1024 ** 3):.2f} GB")

        # 检查当前显存使用情况
        reserved_memory = torch.cuda.memory_reserved(device) / (1024 ** 3)
        allocated_memory = torch.cuda.memory_allocated(device) / (1024 ** 3)
        free_memory = total_memory / (1024 ** 3) - allocated_memory
        print(f"已分配显存：{allocated_memory:.2f} GB")
        print(f"已保留显存：{reserved_memory:.2f} GB")
        print(f"剩余可用显存：{free_memory:.2f} GB")

        # 尝试分配几乎所有显存
        try:
            x = torch.empty(int(total_memory * 0.9), dtype=torch.int8, device=device)
            print("显存分配成功！")
        except RuntimeError as e:
            print(f"显存分配失败：{e}")
    else:
        print("GPU 不可用！")
except Exception as e:
    print(f"程序运行错误：{e}")
