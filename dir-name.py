import os

# 获取当前工作目录
cwd = os.getcwd()

# 获取当前目录下所有文件夹的名称
dirs = [d for d in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, d))]

# 输出所有文件夹的名称，每个名称一行
for d in dirs:
    print(d)