import re

m = re.finditer(r'[1-9]\d{5}','BIT100081 TSU100084')
for i in m:
    print(i.group())
