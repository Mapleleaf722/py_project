# 判断一个句子是否为标题文本
def is_title(sentence):
    # 在此处编写代码
    sentence_list = sentence.split(" ")
    first_list = [i[0] for i in sentence_list]
    str_first = "".join(first_list)
    return str_first.isupper()


# 从用户处获取输入
input_sentence = "The Quick Brown Fox"
# 调用函数
print(is_title(input_sentence))
