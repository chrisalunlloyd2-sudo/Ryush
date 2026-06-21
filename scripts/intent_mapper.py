import sys
import json
import os
import subprocess

VOCAB_PATH = os.path.expanduser('~/Ryush/scripts/vocabulary.json')

def load_vocab():
    if not os.path.exists(VOCAB_PATH):
        return {}
    with open(VOCAB_PATH, 'r') as f:
        return json.load(f)

def save_vocab(vocab):
    with open(VOCAB_PATH, 'w') as f:
        json.dump(vocab, f, indent=4)

def resolve_intent(intent):
    vocab = load_vocab()
    if intent in vocab:
        print(f"Executing: {vocab[intent]}")
        subprocess.run(vocab[intent], shell=True)
    else:
        print(f"Unknown intent: '{intent}'. Please define the mapping.")
        # Logic to learn could go here

if __name__ == "__main__":
    if len(sys.argv) > 1:
        resolve_intent(" ".join(sys.argv[1:]))
