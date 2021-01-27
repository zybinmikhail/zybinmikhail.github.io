import re

with open("dataset.txt") as fin:
    text = fin.read()

    prepared_text = re.sub(r'[a-zA-Z0-9]', '', text)
    prepared_text = re.sub(r'[/%=:#()$@]', '', prepared_text)
    prepared_text = re.sub(r'( [,.])', '', prepared_text)
    prepared_text = ' '.join(prepared_text.split())
    print(prepared_text[:2000])
with open("prepared_dataset.txt", "w") as fout:
    fout.write(prepared_text)
print(len(prepared_text), len(prepared_text.split()))
