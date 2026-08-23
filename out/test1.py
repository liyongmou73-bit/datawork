import re

s2 = "我现在的时间是2019-05-05 09:05:05"
print(re.findall(r"[0-9]{4}-[0-9]{2}-[0-9]{2}",s2))
print(re.findall(r"(\d{2})(\d{2})",s2))