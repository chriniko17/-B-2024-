# 定义⼀个包含汉字的字符串
s = "你好，世界"
# 遍历字符串中的每个字符
for char in s:
    print(char) # 每次迭代都会输出⼀个完整的汉字或符号，⽽不是字节的⼀部分
# 获取字符串⻓度，这⾥返回的是字符数量，⽽不是字节数
length = len(s)