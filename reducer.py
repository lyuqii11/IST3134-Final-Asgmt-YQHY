#!/usr/bin/env python3
import sys

current_word = None
current_count = 0
word_counts = []

for line in sys.stdin:
    word, count = line.strip().split('\t')
    count = int(count)
    if word == current_word:
        current_count += count
    else:
        if current_word:
            word_counts.append((current_word, current_count))
        current_word = word
        current_count = count

if current_word:
    word_counts.append((current_word, current_count))

# Sort by frequency and get top 20
for word, count in sorted(word_counts, key=lambda x: x[1], reverse=True)[:20]:
    print(f"{word}\t{count}")
