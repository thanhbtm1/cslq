import uiautomator2 as u2
import time
import threading
def thoigian(tg):
    # for i in range(tg,-1,-1):
    #     print(f"đang đợi {tg} giây, còn {i} giây", end = "\r")
    #     time.sleep(1)
    #     print("                                                       ",end = "\r")
    time.sleep(tg)
ma = "Mã mời của tôi là --tW7v9m4X6J--, [[lllD61TyHN5cwG2SNp4QB2XD1SaEyPP ]]"

devices = [
    "emulator-5554"
    
]
with open("data.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
n = len(lines) // len(devices)
print(f"mỗi máy xử lí {n} acc")
def task(number,sl,serial):
    d = u2.connect(serial=serial)
    for i in range(number*sl + 510,min(sl + number * sl,len(lines)),1):        
        item = lines[i].strip()
        tk = item.split('|')[0]
        mk = item.split('|')[1]
        print(f"\033[33mĐang chạy acc {tk}\033[0m")
        # xoa du lieu lien quan 
        d.app_clear("com.garena.game.kgvn")
        print(f"\033[32m[SUCCESS] xoa du lieu acc thu {i} thanh cong\033[0m")
        thoigian(5)
        # mo lien   quan
        d.click(714,244)
        thoigian(35) # doi 35s
        d.click(757,723)
        print("click nut dang nhap")
        thoigian(4) # doi 10s
        # dang nhap
        d.click(303,235) # o nhap tai khoan
        thoigian(1)
        d.send_keys(tk) # nhap tai khoan
        thoigian(1)
        d.click(344,334) # o nhap mat khau
        thoigian(1)
        d.send_keys(mk) # nhap mat khau
        thoigian(1)
        d.click(537,482) # nut dang nhap
        thoigian(15)
        if d(textContains="trang web").exists:
            d.click(562,703)
            continue
        thoigian(25)
        d.send_keys(ma)
        d.click(823,467) # banner sk
        thoigian(3)
        d.click(1010,782)#choi ngay
        thoigian(3)
        d.click(1447,827) # nut nhap ma 
        thoigian(3)
        d.click(782,437)
        thoigian(2)
        d.send_keys(ma)
        thoigian(2)
        d.click(807,617) #xac nhan
        print(f"\033[32m[SUCCESS] Xong acc thu {i + 1}\033[0m")
        thoigian(1)
        d.press("home")
        print(f"\033[36mChạy xong acc {tk}\033[0m")

        thoigian(3)

threads = []
for i in range(len(devices)):
    t = threading.Thread(target=task, args=(i,n,devices[i]))
    threads.append(t);
    time.sleep(1);
    t.start()
for t in threads:
    t.join()
print("tat ca da chay xong")






# # Mở app Settings
# d.app_start("com.android.settings")
# time.sleep(1)

# # Click vào chữ Wi-Fi nếu thấy
# if d(text="Wi-Fi").exists:
#     d(text="Wi-Fi").click()

# # Bấm back
# d.press("back")
# Click tọa độ
# d.click(500, 1000)

# # Vuốt
# d.swipe(500, 1500, 500, 500)

# # Nhập chữ
# d.send_keys("hello")

# # Bấm phím
# d.press("home")
# d.press("back")
# d.press("enter")

# # Chụp màn hình
# d.screenshot("screen.png")

# # Lấy package app hiện tại
# print(d.app_current())