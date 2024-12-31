#游泳池收費  會員(假日120 平日70)  非會員(假日150 平日100)   年齡大於70一律50元

import time as t
time1 = t.localtime()
print(time1)

if 0 <= time1.tm_wday <= 4:
    member_price = 70
    non_member_price = 100
else:
    member_price = 120
    non_member_price = 150
       
total = 0
a = b = c = 0

while True:
    isold = input("是否大於70歲(Y or N)(按Enter結束): ")
    if isold =="":
        break
    elif isold == "Y":
        n = int(input("請輸入敬老票人數: "))
        total += 50*n
        a += n
    elif isold == "N":
        ismember = input("是否為會員(Y or N)(按Enter結束): ")
        if ismember == "":
            break
        elif ismember == "Y":
            n = int(input("請輸入會員人數: "))
            total += member_price*n
            b += n
        elif ismember == "N":
            n = int(input("請輸入非會員人數: "))
            total += non_member_price*n
            c += n
        else:
            print("請輸入正確指令")
    else:
        print("請輸入正確指令")
        
            
print(f"總共{a}張敬老票,{b}張會員票,{c}張非會員票,總共{total}元")

