a = []
while True:
    s = input()
    if s == "ok":
        break
    if s.split("BAND : ")[1] == "NO":
        a.append(s);
with open('data.txt', 'a', encoding='utf-8') as f:
    for item in a:
        f.write(f"{item}\n") # Ghi xong tự xuống dòng
# print("+-------------------------------------+")
# for i in range(len(a)):
#     print(a[i])