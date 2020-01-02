import pyodbc
f = open("E:\\PYTHON\\buoi10\\DATA_FILE.txt");
listSanphamStr=[];
sanphanSTR="";
#test gifhub
for line in f:
    if line=='{SAN_PHAM\n':
        continue
    if line=='}SAN_PHAM\n':
        listSanphamStr.append(sanphanSTR)
        sanphanSTR=""
        continue
    sanphanSTR +=line
print(listSanphamStr)
print(sanphanSTR)
# test
