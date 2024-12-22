# %%
from datasets import load_dataset

dataset = load_dataset("openwebtext", trust_remote_code=True)

# %%
dataset
# %%
train_dataset = dataset['train']
# %%
total_words = sum(len(text.split()) for text in train_dataset['text'])
print(f"Total words in dataset: {total_words:,}")

# %%
number_of_words = 6559499127
bytes_per_word = 40000000000 / number_of_words
number_of_tokens = number_of_words * 4 / 3

# %%
print(f"Bytes per word: {bytes_per_word:.2f}")
print(f"Number of tokens: {number_of_tokens:,}")
