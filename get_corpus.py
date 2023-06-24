with open("data/《斗破苍穹》.txt", "r", encoding="utf-8") as fp:
    data = fp.read().strip().split("\n")
sentences = []

for d in data:
    d = d.strip()
    if "===" in d or len(d) == 0 or d == "《斗破苍穹》来自:":
        continue
    sentences.append(d)

with open("data/corpus.txt", "w", encoding="utf-8") as fp:
    fp.write("\n".join(sentences))