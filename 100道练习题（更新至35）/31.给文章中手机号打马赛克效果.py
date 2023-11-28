content = """
白日依19989881888山尽，黄河入45645546468798978海流。
欲穷12345千里目，更上15619292345一层楼。
"""
import re

pattern = r'(1[3-9])(\d)(\d{4})(\d{4})'

search = re.sub(pattern, r'\1\2####\4', content)
print(search)
