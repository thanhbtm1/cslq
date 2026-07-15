with open("data.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
with open("data1.txt", 'w',encoding='utf-8') as f:
    for x in lines:
        i = f"{x.split('|')[0]}|{x.split('|')[1]}"
        f.write(f"{i}\n")