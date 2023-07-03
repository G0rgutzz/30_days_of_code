def reverse_words_order_and_swap_cases(sentence):
    a = sentence.split()
    print(a)
    b = ''
    for i in range(0, len(a)):
        b += a[len(a)-1-i]+' '
    print(b.swapcase())


if __name__ == '__main__':
    c = input()
    reverse_words_order_and_swap_cases(c)



