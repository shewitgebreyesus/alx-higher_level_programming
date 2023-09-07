#!/usr/bin/python3
"""
a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    text_indentation a function
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace(":", ":\n\n")
    text = text.replace("?", "?\n\n")
    text = text.split("\n")
    for ch in range(0, len(text)):
        print("{:s}".format(text[ch].strip()),
              end=("" if (ch == len(text) - 1) else "\n"))
