import pandas as p
import pyodbc
f = open("E:\\PYTHON\\buoi10\\DATA_FILE.txt");
listSanphamStr=[];
sanphanSTR="";
for line in f:
    if line=='{SAN_PHAM\n':
        continue
    if line=='}SAN_PHAM\n':
        listSanphamStr.append(sanphanSTR)
        sanphanSTR=""
        continue
    sanphanSTR +=line
#print(listSanphamStr)
class Product:
    ProductID = "";
    ProductName = "";
    ProductPrice = "";
    ProductQTY ="0";
danhsachProduct=[]
   # def __init__(self):
       # pass
for i in range(len(listSanphamStr)):
    s= listSanphamStr[i]
    listAttribute = s.split('\n')
    listAttribute = list(filter(None,listAttribute));
    product = Product()

    for j in range(len(listAttribute)):
        productAttribute = listAttribute[j].split(':')
        if productAttribute[0] == "ID_SP":
            product.ProductID = productAttribute[1]
        if productAttribute[0] == "TEN_SP":
            product.ProductName = productAttribute[1]
        if productAttribute[0] == "GIA_SP":
            product.ProductPrice = productAttribute[1]
        if productAttribute[0] == "SL_SP":
            product.ProductQTY = productAttribute[1]

    danhsachProduct.append(product)
for s in danhsachProduct:
    print(s.ProductID, "-", s.ProductName, "-", s.ProductPrice, "-", s.ProductQTY)
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=HUU;'
                      'Database=QUAN_LY_NHAN_VIEN;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
for p in danhsachProduct:
    s="";
    ma = p.ProductID
    ten=p.ProductName
    gia=p.ProductPrice
    sl=p.ProductQTY
    s = "INSERT INTO DBO.PRODUCT1 VALUES('"+ ma+"','" + ten +"','"+ gia +"',"+ sl +")"
    cursor.execute(s)
    conn.commit()
cursor.execute("select * from DBO.PRODUCT1")
for row in cursor:
    print(row)


