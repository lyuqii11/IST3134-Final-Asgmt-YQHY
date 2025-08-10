#!/usr/bin/env python3
import sys
import os

# Load stopwords into a set for fast lookup
stopwords_path = "stopwords.txt"
stopwords = set()

try:
    with open(stopwords_path, 'r') as f:
        for line in f:
            stopwords.add(line.strip().lower())
except FileNotFoundError:
    pass # In production, you might log this

# Process input
for line in sys.stdin:
    line - line.strip()
    words = line.split()
    for word in words:
        word = word.lower()
        if word and word not in stopwords:
            print(f"{word}\t")
