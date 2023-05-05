import os
import chardet

# 获取当前工作目录
cwd = os.getcwd()

# 读取1.txt文件中的目录名
with open(os.path.join(cwd, '1.txt'), 'rb') as f1:
    data = f1.read()
    encoding = chardet.detect(data)['encoding']
    dirs1 = set(data.decode(encoding).splitlines())

# 读取2.txt文件中的目录名
with open(os.path.join(cwd, '2.txt'), 'rb') as f2:
    data = f2.read()
    encoding = chardet.detect(data)['encoding']
    dirs2 = set(data.decode(encoding).splitlines())

# 查找1.txt中缺少在2.txt中的目录名
missing_dirs1 = dirs2 - dirs1

# 查找2.txt中缺少在1.txt中的目录名
missing_dirs2 = dirs1 - dirs2

# 输出结果
print('1.txt缺少2.txt中的目录：')
for d in missing_dirs1:
    print(d)

print('2.txt缺少1.txt中的目录：')
for d in missing_dirs2:
    print(d)
