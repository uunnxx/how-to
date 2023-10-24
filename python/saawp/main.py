text = 'hello world'.split()

text_len = len(text) - 1

for index, word in enumerate(text):
    if index != text_len:
        print(word.capitalize(), end=' ')
    else:
        print(word.capitalize())

# print(word)


print(' '.join([word.capitalize() for word in text]))


print('-' * 80)


def word_processing(word):
    return word.capitalize()


head_tail_iter = iter(text)
head = next(head_tail_iter)
word_processing(head)

for word in head_tail_iter:
    print(word_processing(word))
