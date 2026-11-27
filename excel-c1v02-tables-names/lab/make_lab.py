# lab file for video 2 (invented data): messy layout the learner must turn into a Table
import openpyxl, pandas as pd, datetime as dt
wb=openpyxl.Workbook(); ws=wb.active; ws.title="orders"
ws["A1"]="Weekly orders (invented data)"; ws.merge_cells("A1:E1")
ws.append([]); ws.append(["order_id","order_date","city","qty","price"])
rows=[("C101",dt.date(2026,11,1),"Cairo",4,120),("C102",dt.date(2026,11,2),"Giza",2,300),("C103",dt.date(2026,11,2),"Fayoum",10,45),
("C104",dt.date(2026,11,3),"Cairo",1,800),("C105",dt.date(2026,11,4),"Alexandria",6,95),("C106",dt.date(2026,11,5),"Giza",3,210),
("C107",dt.date(2026,11,6),"Cairo",5,60),("C108",dt.date(2026,11,7),"Fayoum",2,330)]
for i,r in enumerate(rows):
    ws.append(list(r))
    if i==3: ws.append([None]*5)        # a blank row inside the data
wb.save("lab/lab_orders.xlsx")
df=pd.read_excel("lab/lab_orders.xlsx",header=2).dropna(how="all")
df["amount"]=df.qty*df.price
print("data rows:",len(df))
print("total qty:",int(df.qty.sum()),"| revenue:",int(df.amount.sum()))
print(df.groupby("city").amount.sum().astype(int).to_dict())
print("revenue with 14 percent added:",round(df.amount.sum()*1.14,2))
