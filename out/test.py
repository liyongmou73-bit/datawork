lines = []
print("请输入多行内容，输入空行结束：")

while True:
    line = input()
    if not line:
        break
    lines.append(line)

print("\n你输入的内容是：")
for l in lines:
    print(l)