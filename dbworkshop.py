from asyncio.windows_events import NULL
from hashlib import new
from multiprocessing.sharedctypes import Value
import psycopg2


db = psycopg2.connect(user = "postgres",
                      password = "1234",
                      host = "localhost",
                      port = "5432",
                      database = "test")
imlec = db.cursor()

def Db_Products_Select():
    komut = "SELECT * FROM products ORDER BY id ASC"
    imlec.execute(komut)
    liste = imlec.fetchall()
    for deger in liste:
        print("ID:",deger[0]," | ","ÜRÜN ADI:",deger[1]," | ","AÇIKLAMA:",deger[2]," | ","TUTARI: ",deger[3])

def Db_Products_Insert(title,description,price):
    komut = "INSERT INTO products (title,description,price) VALUES (%s,%s,%s)"
    komut_parameters = (title,description,price)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("ÜRÜN BAŞARIYLA EKLENDİ...")


def Db_Products_Update(id,title,description,price):
    komut = "Update products SET title = %s,description=%s,price=%s WHERE id = %s"
    komut_parameters = (title,description,price,id)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("ÜRÜN BAŞARIYLA GÜNCELLENDİ...")

def Db_Products_Delete(id):
    
    komut = "DELETE FROM products WHERE id = %s"
    komut_parameters = str(id)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("ÜRÜN BAŞARIYLA SİLİNDİ...")

def Db_Products_Select_Where_With_Id(id):
    komut = "SELECT * FROM products Where id = %s ORDER BY id ASC"
    komut_parameters = str(id)
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    for deger in liste:
        print("ID:",deger[0]," | ","ÜRÜN ADI:",deger[1]," | ","AÇIKLAMA:",deger[2]," | ","TUTARI: ",deger[3])

def Db_Products_Select_Where_With_Id_2(id):
    komut = "SELECT * FROM products Where id = %s ORDER BY id ASC"
    komut_parameters = str(id)
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_Stock_Select(id):
    komut = "SELECT * FROM mystocks(%s)"
    komut_parameters = str(id)
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    for deger in liste:
        print("STOK NO:",deger[0]," | ","ÜRÜN KOD:",deger[1]," | ","ÜRÜN ADI:",deger[2]," | ","STOK MİKTARI: ",deger[3])

def Db_Stock_Select_2(id):
    komut = "SELECT * FROM mystocks(%s)"
    komut_parameters = str(id)
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_Stock_Insert(product_pieces,product_id):
    komut = "INSERT INTO stocks (product_pieces,product_id) VALUES (%s,%s)"
    komut_parameters = (product_pieces,product_id)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print(product_id , " KODLU ÜRÜN STOKLARA EKLENMİŞTİR...")

def Db_Stock_Update():
    product_id = int(input("ÜRÜN KODUNU GİRİNİZ: "))
    product_pieces = int(input("ÜRÜN STOK MİKTARI: "))
    myStockValues = Db_Stock_Select_2(product_id)
    if myStockValues:
        for stockValue in myStockValues:
            sumStockValues = int(stockValue[3])+int(product_pieces)
        komut = "UPDATE stocks SET product_pieces = %s WHERE product_id = %s"
        komut_parameters = (sumStockValues,product_id)
        imlec.execute(komut,komut_parameters)
        db.commit()
        print(product_id , " KODLU ÜRÜNÜN STOKLARI GÜNCELLENMİŞTİR...")
    else:
        Db_Stock_Insert(product_pieces,product_id)

def Db_Users_Select_Login(user_name,user_password):
    komut = "SELECT * FROM users Where user_name = %s and user_password = %s"
    komut_parameters = [user_name,user_password]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_Users_Search(user_name):
    komut = "SELECT * FROM users Where user_name = %s"
    komut_parameters = [user_name]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_Users_Search_With_ID(user_ID):
    komut = "SELECT staff_name,staff_surname,department FROM users Where user_id = %s"
    komut_parameters = [user_ID]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_Users_Select():
    komut = "SELECT user_id,user_name,staff_name,staff_surname,department FROM users ORDER BY user_id ASC"
    imlec.execute(komut)
    liste = imlec.fetchall()
    for deger in liste:
        print("ID:",deger[0]," | ","KULLANICI ADI:",deger[1]," | ","ADI:",deger[2]," | ","SOYADI: ",deger[3],"DEPARTMAN: ",deger[4])

def Db_Users_Insert(user_name,user_password,staff_name,staff_surname,department):
    komut = "INSERT INTO users (user_name,user_password,staff_name,staff_surname,department) VALUES (%s,%s,%s,%s,%s)"
    komut_parameters = (user_name,user_password,staff_name,staff_surname,department)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("KULLANICI BAŞARIYLA EKLENDİ...")

def Db_User_Update(staff_name,staff_surname,department,user_id):
     komut = "Update users SET staff_name = %s,staff_surname=%s,department=%s WHERE user_id = %s"
     komut_parameters = (staff_name,staff_surname,department,user_id)
     imlec.execute(komut,komut_parameters)
     db.commit()
     print("KULLANICI BAŞARIYLA GÜNCELLENDİ...")

def Db_User_Change_Password(user_password,user_id):
     komut = "Update users SET user_password = %s WHERE user_id = %s"
     komut_parameters = (user_password,user_id)
     imlec.execute(komut,komut_parameters)
     db.commit()
     print("ŞİFRE GÜNCELLENDİ...")

def Db_User_Delete(user_id):
    komut = "DELETE FROM users WHERE user_id = %s"
    komut_parameters = str(user_id)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("KULLANICI BAŞARIYLA SİLİNDİ...")


def Db_Customers_Select():
    komut = "select * from myCustomers()"
    imlec.execute(komut)
    liste = imlec.fetchall()
    for deger in liste:
        print("ID:",deger[0]," | ","ADI:",deger[1]," | ","ADRES:",deger[2]," | ","TELEFON: ",deger[3]," | ","EMAİL: ",deger[4])

def Db_Customers_Insert(customer_name,customer_address,customer_number,customer_email):
    komut = "INSERT INTO customers (customer_name,customer_address,customer_number,customer_email) VALUES (%s,%s,%s,%s)"
    komut_parameters = (customer_name,customer_address,customer_number,customer_email)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("MÜŞTERİ BAŞARIYLA EKLENDİ...")

def Db_Customers_Update(customer_name,customer_address,customer_number,customer_email,customer_id):
     komut = "Update customers SET customer_name = %s,customer_address=%s,customer_number=%s,customer_email=%s WHERE customer_id = %s"
     komut_parameters = (customer_name,customer_address,customer_number,customer_email,customer_id)
     imlec.execute(komut,komut_parameters)
     db.commit()
     print("MÜŞTERİ BAŞARIYLA GÜNCELLENDİ...")

def Db_Customers_Delete(customer_id):
    komut = "DELETE FROM customers WHERE customer_id = %s"
    komut_parameters = str(customer_id)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("MÜŞTERİ BAŞARIYLA SİLİNDİ...")

def Db_Orders_Select():
    komut = "select * from myOrders_2()"
    imlec.execute(komut)
    liste = imlec.fetchall()
    for deger in liste:
        print("SİPARİŞ NO:",deger[0]," | ","MÜŞTERİ KOD:",deger[1]," | ","MÜŞTERİ ADI:",deger[2]," | ","SİPARİŞ TAR.: ",deger[3]," | ","DURUM: ",deger[4])

def Db_Orders_Insert(customer_id):
    komut = "INSERT INTO orders (customer_id) VALUES (%s)"
    komut_parameters = str(customer_id)
    imlec.execute(komut,komut_parameters)
    db.commit()

def Db_Orders_Last_Row(customer_id):
    komut = "SELECT order_id FROM orders WHERE customer_id = %s ORDER BY order_id DESC LIMIT 1"
    komut_parameters = [customer_id]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_Product_Stock(product_id):
    komut = "select product_pieces from stocks where product_pieces >0 and product_id = %s"
    komut_parameters = [product_id]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_Product_Stock_Update(product_id,stock_pieces):
     komut = "Update stocks SET product_pieces = %s WHERE product_id = %s"
     komut_parameters = (stock_pieces,product_id)
     imlec.execute(komut,komut_parameters)
     db.commit()

def Db_Order_Product_Insert(order_id,product_id,product_piece,total_price):
     komut = "INSERT INTO order_products (order_id,product_id,product_piece,total_price) VALUES (%s,%s,%s,%s)"
     komut_parameters = [order_id,product_id,product_piece,total_price]
     imlec.execute(komut,komut_parameters)
     db.commit()

def Db_Order_Status(order_id):
    komut = "select order_status from orders where order_id = %s"
    komut_parameters = [order_id]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_Product_Information(product_id):
    komut = "select price from products where id = %s"
    komut_parameters = [product_id]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_Order_Delete(order_id):
    komut = "DELETE FROM orders WHERE order_id = %s"
    komut_parameters = [order_id]
    imlec.execute(komut,komut_parameters)
    db.commit()
    

def Db_Order_Product_Delete(order_id):
    komut = "DELETE FROM order_products WHERE order_id = %s"
    komut_parameters = [order_id]
    imlec.execute(komut,komut_parameters)
    db.commit()

def Db_Order_Products_Information(order_id):
    komut = "select product_id,product_piece from order_products where order_id = %s"
    komut_parameters = [order_id]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_Order_Information(order_id):
    komut = "select customer_id from orders where order_id = %s"
    komut_parameters = [order_id]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_Order_Producs_Price_Information(order_id):
    komut = "select product_id,total_price from order_products where order_id = %s"
    komut_parameters = [order_id]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_Order_Status_Update(order_id):
    komut = "UPDATE orders SET order_status = 'Kapalı' Where order_id = %s"
    komut_parameters = [order_id]
    imlec.execute(komut,komut_parameters)
    db.commit()

def Db_Invoices_Insert(customer_id,order_id,total_price):
     komut = "INSERT INTO invoices (customer_id,order_id,total_price) VALUES (%s,%s,%s)"
     komut_parameters = [customer_id,order_id,total_price]
     imlec.execute(komut,komut_parameters)
     db.commit()

def Db_Invoices_Delete(invoice_id):
    komut = "DELETE FROM invoices WHERE invoice_id = %s"
    komut_parameters = [invoice_id]
    imlec.execute(komut,komut_parameters)
    db.commit()

def Db_Invoices_Information(invoice_id):
    komut = "select order_id from invoices where invoice_id = %s"
    komut_parameters = [invoice_id]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste


def Db_Order_Status_Update2(order_id):
    komut = "UPDATE orders SET order_status = 'Açık' Where order_id = %s"
    komut_parameters = [order_id]
    imlec.execute(komut,komut_parameters)
    db.commit()

# 1 - PRODUCT SELECT
# 2 - PRODUCT INSERT
# 3 - PRODUCT UPDATE
# 4 - PRODUCT DELETE
# 5 - PRODUCT SELECT_WHERE_ID
# 6 - STOCK SELECT
# 7 - STOCK UPDATE
# 8 - USER SELECT
# 9 - USER INSERT
# 10 - USER UPDATE
# 11 - USER DELETE
# 12 - USER PASSWORD CHANGE
# 13 - CUSTOMERS SELECT
# 14 - CUSTOMERS INSERT
# 15 - CUSTOMERS UPDATE
# 16 - CUSTOMERS DELETE
# 17 - ORDERS SELECT
# 18 - ORDERS INSERT
# 19 - ORDERS DELETE


######### İŞLEMİN GERÇEKLEŞTİĞİ METHODLAR #########

def my_login_to_system():
    print("")
    print("# 1 - PRODUCT SELECT"
           " # 2 - PRODUCT INSERT"
            "# 3 - PRODUCT UPDATE"
           " # 4 - PRODUCT DELETE"
            "# 5 - PRODUCT SELECT_WHERE_ID"
            "# 6 - STOCK SELECT"
           " # 7 - STOCK UPDATE"
            "# 8 - USER SELECT"
            "# 9 - USER INSERT"
            "# 10 - USER UPDATE"
            "# 11 - USER DELETE"
            "# 12 - USER PASSWORD CHANGE"
            "# 13 - CUSTOMERS SELECT"
            "# 14 - CUSTOMERS INSERT"
            "# 15 - CUSTOMERS UPDATE"
            "# 16 - CUSTOMERS DELETE"
            "# 17 - ORDERS SELECT"
            "# 18 - ORDERS INSERT"
            "# 19 - ORDERS DELETE")
    print("")
    print("SİSTEME GİRİŞ İŞLEMİ")
    print("")
    myUserName = input("Kullanıcı Adınızı Giriniz: ")
    myUserPassword = input("Şifrenizi Giriniz: ")
    myLoginValues = Db_Users_Select_Login(myUserName,myUserPassword)
    if myLoginValues:
        print("GİRİŞ GERÇEKLEŞTİRİLDİ")
        print("")
        My_Process_C()
    else:
        print("HATALI KULLANICI ADI VEYA ŞİFRE")


def My_Process_C(myLocalValue=0):
    if myLocalValue==0:
        myChoose = input("YAPILACAK İŞLEM NUMARASINI GİRİNİZ: ")
        myChooseValue = int(myChoose)
    else:
        myChooseValue = myLocalValue

    if myChooseValue == 1:
        Db_Products_Select()
    elif myChooseValue ==2:
        print("ÜRÜN YENİ KAYIT İŞLEMİ...")
        print()
        valueTitle = input("ÜRÜN ADINI GİRİNİZ: ")
        valueDescription = input("ÜRÜN AÇIKLAMASI: ")
        valuePrice = int(input("ÜRÜN FİYATINI GİRİNİZ: "))
        Db_Products_Insert(valueTitle,valueDescription,valuePrice)
    elif myChooseValue == 3:
        print("ÜRÜN GÜNCELLEME İŞLEMİ...")
        print()
        myID = int(input("GÜNCELLEMEK İSTEDİĞİNİZ ÜRÜN KODU: "))
        myProductValues = Db_Products_Select_Where_With_Id_2(myID)
        for productValues in myProductValues:
            productTitle = productValues[1]
            productDescription = productValues[2]
            productPrice = productValues[3]
        
        newMyTitle = input("Yeni Başlık Değeri: ")
        newMyDescription = input("Yeni Açıklama Değeri: ")
        newMyPrice = int(input("Yeni Fiyat Değeri: "))
        if newMyTitle == "":
            newMyTitle = productTitle
        elif newMyDescription == "":
            newMyDescription = productDescription
        elif newMyPrice == 0:
            newMyPrice = productPrice
        Db_Products_Update(myID,newMyTitle,newMyDescription,newMyPrice)
    elif myChooseValue == 4:
        print("ÜRÜN SİLME İŞLEMİ: ")
        print()
        myID = int(input("SİLMEK İSTEDİĞİNİZ ÜRÜN KODU: "))
        Db_Products_Delete(myID)
    elif myChooseValue ==5:
        print("ÜRÜN GETİRME İŞLEMİ")
        print()
        myID = int(input("GETİRMEK İSTEDİĞİNİZ ÜRÜN KODU: "))
        Db_Products_Select_Where_With_Id(myID)
    elif myChooseValue ==6:
        print("ÜRÜNÜN STOK BİLGİSİ")
        print("")
        myID = int(input("ÜRÜN KODU: "))
        myStockValues = Db_Stock_Select_2(myID)
        if myStockValues:
            Db_Stock_Select(myID)
        else:
            print("STOK DA BÖYLE BİR ÜRÜN BULUNMAMAKTADIR.")
    elif myChooseValue ==7:
        print("ÜRÜN STOK GÜNCELLEME")
        print("")
        Db_Stock_Update()
    
    elif myChooseValue ==8:
        print("KULLANICI LİSTESİ")
        print("")
        Db_Users_Select()

    elif myChooseValue ==9:
        print("KULLANICI EKLEME")
        print("")
        myUserName = input("KULLANICI ADI: ")
        myUserPassword = input("ŞİFRE: ")
        myStaffName = input("PERSONEL ADI: ")
        myStaffSurname = input("PERSONEL SOYADI: ")
        myDepartment = input("DEPARTMAN: ")

        mySearchUser = Db_Users_Search(myUserName)
        if mySearchUser:
            print("Böyle Bir Kullanıcı Mevcut Ekleyemezsiniz")
            My_Process_C(9)
        else:
            Db_Users_Insert(myUserName,myUserPassword,myStaffName,myStaffSurname,myDepartment)
    
    elif myChooseValue ==10:
        print("KULLANICI GÜNCELLEME")
        print()
        myUserID = int(input("KULLANICI ID: "))
        myUserValues = Db_Users_Search_With_ID(myUserID)
        for deger in myUserValues:
            myOldStaffName = deger[0]
            myOldStaffSurname = deger[1]
            myOldDepartment = deger[2]
        
        myNewStaffName = str(input("PERSONEL ADINI GİRİNİZ: "))
        myNewStaffSurname = str(input("PERSONEL SOYADINI GİRİNİZ: "))
        myNewDepartment = str(input("DEPARTMAN GİRİNİZ: "))

        if myNewStaffName =="":
            myNewStaffName = myOldStaffName
        elif myNewStaffSurname == "":
            myNewStaffSurname = myOldStaffSurname
        elif myNewDepartment == "":
            myNewDepartment = myOldDepartment
        
        Db_User_Update(myNewStaffName,myNewStaffSurname,myNewDepartment,myUserID)
    
    elif myChooseValue ==11:
        print("KULLANICI SİLME")
        print()
        myUserID = int(input("KULLANICI ID: "))
        myDeleteAnswer = input("KULLANICIYI SİLMEK İSTİYOR MUSUNUZ ?: ")
        if myDeleteAnswer == 'E':
            Db_User_Delete(myUserID)
        elif myDeleteAnswer == 'H':
            print("SİLME İŞLEMİ İPTAL EDİLDİ...")
    
    elif myChooseValue == 12:
        print("ŞİFRE DEĞİŞTİRME")
        print("")
        myUserID = int(input("KULLANICI ID: "))
        myUserPassword = input("YENİ ŞİFREYİ GİR: ")
        Db_User_Change_Password(myUserPassword,myUserID)
    elif myChooseValue == 13:
        print("MÜŞTERİLER LİSTESİ")
        print("")
        Db_Customers_Select()
    elif myChooseValue == 14:
        print("MÜŞTERİ GİRİŞ İŞLEMİ")
        print("")
        myNewName = input("ÜNVANI GİRİNİZ: ")
        myNewAdress = input("ADRESİ GİRİNİZ: ")
        myNewNumber = input("TELEFON GİRİNİZ: ")
        myNewEmail = input("EMAİL GİRİNİZ: ")
        Db_Customers_Insert(myNewName,myNewAdress,myNewNumber,myNewEmail)
        print("")
        Db_Customers_Select()
    elif myChooseValue == 15:
        print("MÜŞTERİ GÜNCELLEME İŞLEMİ")
        print("")
        myCustomerID = int(input("MÜŞTERİ ID: "))
        myUpdateName = input("ÜNVANI GİRİNİZ: ")
        myUpdateAdress = input("ADRESİ GİRİNİZ: ")
        myUpdateNumber = input("TELEFON GİRİNİZ: ")
        myUpdateEmail = input("EMAİL GİRİNİZ: ")
        Db_Customers_Update(myUpdateName,myUpdateAdress,myUpdateNumber,myUpdateEmail,myCustomerID)
        print("")
        Db_Customers_Select()
    
    elif myChooseValue == 16:
        print("MÜŞTERİ SİLME İŞLEMİ")
        print("")
        myCustomerID = int(input("MÜŞTERİ ID: "))
        Db_Customers_Delete(myCustomerID)
        print("")
        Db_Customers_Select()
    elif myChooseValue == 17:
        print("SİPARİŞ LİSTESİ")
        print("")
        Db_Orders_Select()
    elif myChooseValue ==18:
        print("SİPARİŞ GİRİŞİ")
        print("")
        myCustomerNo = int(input("MÜŞTERİ KODUNU GİRİN: "))
        Db_Orders_Insert(myCustomerNo)
        myOrdersValue = Db_Orders_Last_Row(myCustomerNo)
        myLastOrderNo =0
        for myOrderNumberValue in myOrdersValue:
            myLastOrderNo = myOrderNumberValue[0]
        
        print("")
        print("İLGİLİ SİPARİŞİN ÜRÜNLERİNİ GİR")
        print("")
        myProductCount = int(input("KAÇ ADET ÜRÜN GİRİŞİ OLACAK ?"))
        myCount = 1
        while myCount<=myProductCount:
            print(myCount, " .ÜRÜNÜ GİRİNİZ")
            myProductCode = int(input("ÜRÜN KODUNU GİRİNİZ: "))
            myOrderProductCount = int(input("SİPARİŞ VERİLECEK ADET SAYISI: "))
            myProductStockInformation = Db_Product_Stock(myProductCode)
            myProductInformation = Db_Product_Information(myProductCode)
            productLastStock = 0
            for myProductPriceInformation in myProductInformation:
                myPriceInformation = myProductPriceInformation[0]

            for myProductStock in myProductStockInformation:
                newLastStock = int(myProductStock[0])
                productLastStock = newLastStock-myOrderProductCount
                productTotalPrice = myPriceInformation * myOrderProductCount
                Db_Product_Stock_Update(myProductCode,productLastStock)
                Db_Order_Product_Insert(myLastOrderNo,myProductCode,myOrderProductCount,productTotalPrice)
                print("ÜRÜN GİRİŞİ YAPILDI...")
            myCount = myCount +1
        print("")
        print("SİPARİŞ OLUŞTURULDU...")
    
    elif myChooseValue ==19:
        print("SİPARİŞ SİLME...")
        print("")
        myOrderID = int(input("SİPARİŞ NUMARASINI GİRİNİZ: "))
        myOrderStatus = Db_Order_Status(myOrderID)
        myOrderLastStatus = ""
        myOrderProductInformations = Db_Order_Products_Information(myOrderID)
        for myOrderStatusList in myOrderStatus:
            myOrderLastStatus = myOrderStatusList[0]
        
        if myOrderLastStatus !='Açık':
            print("SİPARİŞ KAPALI OLDUĞUNDAN SİLME İŞLEMİ YAPAMAZSINIZ!")
        else:
            for myOrderProductStock in myOrderProductInformations:
                myOrderProductCode = myOrderProductStock[0]
                myOrderProductPiece = myOrderProductStock[1]
                myProductStockInformation = Db_Product_Stock(myOrderProductCode)
                for myLastStock in myProductStockInformation:
                    myLastProductStock = myLastStock[0]
                LastTotalStockPiece = myLastProductStock + myOrderProductPiece
                Db_Product_Stock_Update(myOrderProductCode,LastTotalStockPiece)

        Db_Order_Product_Delete(myOrderID)
        Db_Order_Delete(myOrderID)
        print("")
        print("SİPARİŞ SİLİNDİ...")

    elif myChooseValue == 20:
        print("")
        print("FATURA OLUŞTURMA İŞLEMİ")
        print("")
        mySelectionOrderID = int(input("SİPARİŞ NUMARASI: "))
        myTotalPrice = 0
        myCustomerOfOrder = Db_Order_Information(mySelectionOrderID)
        myOrderProductInfo = Db_Order_Producs_Price_Information(mySelectionOrderID)
        for myCustomerIDInformation in myCustomerOfOrder:
            mySelectionCustomerID = myCustomerIDInformation[0]
        for myOrderProductPriceInfo in myOrderProductInfo:
            myTotalPrice = myOrderProductPriceInfo[1] + myTotalPrice
        
        Db_Invoices_Insert(mySelectionCustomerID,mySelectionOrderID,myTotalPrice)
        Db_Order_Status_Update(mySelectionOrderID)
        print("FATURA OLUŞTURULDU...")
    
    elif myChooseValue == 21:
        print("")
        print("FATURA İPTAL İŞLEMİ")
        print("")
        myInvoiceID = int(input("FATURA NUMARASI: "))
        myInvoiceInformation = Db_Invoices_Information(myInvoiceID)
        for myOrderNumber in myInvoiceInformation:
            myInvoiceOrderID = int(myOrderNumber[0])
        
        Db_Order_Status_Update2(myInvoiceOrderID)
        Db_Invoices_Delete(myInvoiceID)
        print("FATURA İPTALİ GERÇEKLEŞTİRİLDİ...")


        




        
######### ANA METHOD ÇAĞIRILDIĞI ALAN ##########

# my_login_to_system()
my_login_to_system()