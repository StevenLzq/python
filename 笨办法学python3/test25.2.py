import test25 as t25

sentence="All good things come to those who wait "
words=t25.break_word(sentence)
print('words;',words)

sorted_word=t25.sort_word(words)
print('sorted_word:',sorted_word)

t25.print_first_word(words)
t25.print_last_word(words)
#words

t25.print_first_word(sorted_word)
t25.print_last_word(sorted_word)
#sorted_word

sorted_word=t25.sort_sentence(sentence)

#sorted_word
t25.print_first_and_last(sentence)
t25.print_first_and_last_sorted(sentence)

