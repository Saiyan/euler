
from util import is_triangle_number
from util import get_integer_value_from_char
import csv

all_words = []
with open('files/p042_words.txt', 'r') as csvfile:
    creader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in creader:
        for col in row:
            all_words.append(col)


triangle_word_count = 0
for word in all_words:
    word_sum = 0

    for i in range(0, len(word)):
        word_sum += get_integer_value_from_char(word[i])

    if is_triangle_number(word_sum):
        triangle_word_count += 1

print(triangle_word_count)