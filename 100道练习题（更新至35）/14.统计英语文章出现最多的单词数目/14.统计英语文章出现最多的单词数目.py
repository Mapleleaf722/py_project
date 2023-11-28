def count_word_in_artcle():
    word_count = {}
    with open("Python Tutorial.txt", encoding="utf-8") as f:
        for line in f:
            line = line[:-1]
            a_line_words = line.split()
            for word in a_line_words:
                if word not in word_count:
                    word_count[word] = 0
                word_count[word] += 1
    return word_count


print(count_word_in_artcle())

# 打印出现频率最高的10各词
print(
    sorted(
        count_word_in_artcle().items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]
)
