a = []
with open(r"C:\Users\LENOVO\Downloads\thanh_cong_2026-04-28T16_17_21.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()


for s in lines:

    if s == "ok":
        break
    if "BAND : " in s:
        # Tách chuỗi và lấy phần sau "BAND : "
        parts = s.split("BAND : ")
        if len(parts) > 1 and parts[1].strip() == "NO":
            a.append(s)
    else:
        print("Dòng này không đúng định dạng 'BAND : ', bỏ qua...")
i = 0        
with open('data.txt', 'a', encoding='utf-8') as f:
    for item in a:
        i = i + 1
        f.write(f"{item}") # Ghi xong tự xuống dòng
print(f"\033[32m[SUCCESS] Lưu thành công {i} tài khoản\033[0m")
# print("+-------------------------------------+")
# for i in range(len(a)):
#     print(a[i])