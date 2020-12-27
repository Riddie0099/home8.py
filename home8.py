s={}
while True:
    print("1 建立字彙表")
    print("2 列出全部單字") 
    print("3 英翻中")
    print("4 中翻英")
    print("5 測驗")
    print("6 離開系統")
    a = input("請輸入代號")


    if a == "1":
        while True:
            b=input("請輸入詞彙英文(6離開)")
            if b == "6":
                break
            c=input("請輸入詞彙中文(6離開)")        
            if c == "6":
                break
            s [c] = b
    elif a == "2":
      for key,value in s.items():
          print (key,value)
    elif a == "3":
        b1=input("請輸入英文")
        for key,value in s.items():
            if value == b1:
                print(key)
    elif a == "4":
        c1=input("請輸入中文")
        for key,value in s.items():
            if c1 == key:
                print(s[c1])
    elif a == "5":
        d=0
        for key,value in s.items():
            e = input("請輸入"+ key + "英文")
            if e == value:
                d=d+1
                print("答對了,目前答對" + str(d) + "題")
            else:
                print("答錯了,目前答對" + str(d) + "題")
    else:
        break
       
            
        
    
         
        
         
        
    
    
    
    
    

 




   
    