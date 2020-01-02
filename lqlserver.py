import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=HUU;'
                      'Database=QUAN_LY_NHAN_VIEN;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute("insert into abc values('E009', 'Nguyen Van Anh','Nam','1234','Dev')")
#conn.commit()
cursor.execute("select employee_id from dbo.abc")
for row in cursor:
    print(row)
