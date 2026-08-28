from transformers import AutoModelForCausalLM, AutoTokenizer

colors_list = [
'102;194;165', '252;141;98', '141;160;203',
'231;138;195', '166;216;84', '255;217;47'
]

def show_tokens(sentence, tokenizer_name):
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    token_ids = tokenizer(sentence).input_ids
    for idx, t in enumerate(token_ids):
        print(f'\x1b[0;30;48;2;{colors_list[idx % len(colors_list)]}m'
              +tokenizer.decode(t) +'\x1b[0m',end=' ')

tokenizer_list=[
    "bert-base-uncased","bert-base-cased","gpt2","google/flan-t5-base",
    "bigcode/starcoder2-3b","facebook/galactica-1.3b",
    "microsoft/Phi-3-mini-4k-instruct"
]

text = """
English and CAPITALIZATION
鸟
show_tokens False None elif == >= else: two tabs:" " Three tabs: " "
12.0*50=600
"""

import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
token_ids = enc.encode(text)          # 注意：不是 .input_ids
for idx, t in enumerate(token_ids):
    token_text = enc.decode_single_token_bytes(t).decode("utf-8", errors="replace")
    print(f'\x1b[0;30;48;2;{colors_list[idx % len(colors_list)]}m{token_text}\x1b[0m', end=' ')

for it in tokenizer_list:
    show_tokens(text,it)
    print()

tokenizer=AutoTokenizer.from_pretrained("gpt2")
print(tokenizer.decode([8582, 236, 113]))