import random

# Read text file
with open("data.txt", "r") as file:
    text = file.read().lower()

words = text.split()

# Build Markov dictionary using two-word keys
markov_chain = {}

for i in range(len(words) - 2):
    key = (words[i], words[i+1])
    next_word = words[i+2]

    if key not in markov_chain:
        markov_chain[key] = []

    markov_chain[key].append(next_word)

# Choose random starting pair
start = random.choice(list(markov_chain.keys()))

generated_words = [start[0], start[1]]

# Generate sentence
for i in range(20):
    key = (generated_words[-2], generated_words[-1])

    if key in markov_chain:
        next_word = random.choice(markov_chain[key])
        generated_words.append(next_word)
    else:
        break

print("Generated Text:")
print(" ".join(generated_words))
