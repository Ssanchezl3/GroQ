import tiktoken

def tokenize_text(text):
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    decoded_tokens = [enc.decode([t]) for t in tokens]
    return decoded_tokens, tokens