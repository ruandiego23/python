import re


def remove_punctuation(word):
    return re.sub(r'[!?.:;,"()-]', "", word)


text = """Some people, when confronted with a problem, think
... "I know, I'll use regular expressions."
... Now they have two problems. Jamie Zawinski"""

words = text.split()
print("Words with punctuation")
print(words)
print()

print("Words without punctuation")
print(list(map(remove_punctuation, words)))
print()
