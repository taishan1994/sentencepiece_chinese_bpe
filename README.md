# sentencepiece_chinese_bpe
使用sentencepiece中BPE训练中文词表，并在transformers中进行使用。

具体介绍可参考知乎：https://zhuanlan.zhihu.com/p/639144223

# 使用方法

## 训练中文词表

```python
python train_bpe.py
```

得到tokenizer.model和tokenizer.vocab

## 使用transformers加载sentencepie模型

```python
python chinese_bpe.py

"""
Chinese tokenizer has been saved to ./transformers_tokenizer/chinese/
['<s>', '</s>', '<unk>']
[1, 2, 0]
{'bos_token': '<s>', 'eos_token': '</s>', 'unk_token': '<unk>'}
Test text:
 白日依山尽，黄河入海流。欲穷千里目，更上一层楼。
The primary use of LLaMA is research on large language models, including
Tokenized by Chinese-LLaMA tokenizer:['▁', '白日', '依', '山', '尽', ',', '黄', '河', '入', '海', '流', '。', '欲', '穷', '千里', '目', ',', '更', '上一层', '楼', '。', '▁', 'T', 'h', 'e', '▁', 'p', 'r', 'i', 'm', 'a', 'r', 'y', '▁', 'u', 's', 'e', '▁', 'o', 'f', '▁', 'LL', 'a', 'MA', '▁i', 's', '▁', 'r', 'e', 's', 'e', 'a', 'r', 'ch', '▁', 'o', 'n', '▁', 'l', 'a', 'r', 'g', 'e', '▁', 'l', 'an', 'g', 'u', 'a', 'g', 'e', '▁', 'm', 'o', 'd', 'e', 'l', 's', ',', '▁i', 'n', 'c', 'lu', 'd', 'i', 'ng']

"""
```

## 合并中文词表到llama中

```python
python chinese_llama_bpe.py

"""
32000 50000
['<s>', '</s>', '<unk>']
[1, 2, 0]
{'bos_token': '<s>', 'eos_token': '</s>', 'unk_token': '<unk>'}
32000
Before:32000
New model pieces: 81163
Chinese-LLaMA tokenizer has been saved to transformers_tokenizer/llama_chinese
['<s>', '</s>', '<unk>']
[1, 2, 0]
{'bos_token': '<s>', 'eos_token': '</s>', 'unk_token': '<unk>'}
Test text:
 白日依山尽，黄河入海流。欲穷千里目，更上一层楼。
The primary use of LLaMA is research on large language models, including
Tokenized by LLaMA tokenizer:['▁', '白', '日', '<0xE4>', '<0xBE>', '<0x9D>', '山', '<0xE5>', '<0xB0>', '<0xBD>', '，', '黄', '河', '入', '海', '流', '。', '<0xE6>', '<0xAC>', '<0xB2>', '<0xE7>', '<0xA9>', '<0xB7>', '千', '里', '目', '，', '更', '上', '一', '<0xE5>', '<0xB1>', '<0x82>', '<0xE6>', '<0xA5>', '<0xBC>', '。', '<0x0A>', 'The', '▁primary', '▁use', '▁of', '▁L', 'La', 'MA', '▁is', '▁research', '▁on', '▁large', '▁language', '▁models', ',', '▁including']
Tokenized by Chinese-LLaMA tokenizer:['▁白', '日', '依', '山', '尽', '，', '黄', '河', '入', '海', '流', '。', '欲', '穷', '千里', '目', '，', '更', '上一层', '楼', '。', '<0x0A>', 'The', '▁primary', '▁use', '▁of', '▁L', 'La', 'MA', '▁is', '▁research', '▁on', '▁large', '▁language', '▁models', ',', '▁including']
"""
```

