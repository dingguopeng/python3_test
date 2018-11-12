import re

s1 = re.findall(r'\/.*?(?=ing\/)', '/comming/recommand/reseting/')
s2 = re.findall(r'(?<=re).*?\/', '/comming/recommand/reseting/')
s3 = re.findall(r'\/(?!re).+?\/', '/comming/recommand/reseting/')
s4 = re.findall(r'\/.*?(?<!ing)\/)', '/comming/recommand/reseting/')
print(s1)
print(s2)
print(s3)
print(s4)
