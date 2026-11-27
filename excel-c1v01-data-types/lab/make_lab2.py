# lab file for learners: invented data, 12 orders, 5 seeded problems
import openpyxl, datetime as dt, pandas as pd
wb=openpyxl.Workbook(); ws=wb.active; ws.title="raw"
ws.append(["order_id","order_date","city","qty","unit_price"])
rows=[("B2001",dt.date(2026,11,3),"Cairo",4,90),("B2002",dt.date(2026,11,4),"Giza",6,150),("B2003",dt.date(2026,11,5),"Fayoum","3",200),
("B2004",dt.date(2026,11,6),"Cairo",8,60),("B2005",dt.date(2026,11,9),None,5,110),("B2006","10/11/2026","Alexandria",2,300),
("B2007",dt.date(2026,11,11),"Giza"," 7",80),("B2008",dt.date(2026,11,12),"Fayoum",9,50),("B2009",dt.date(2026,11,13),"Cairo",1,500),
("B2010",dt.date(2026,11,16),"Giza",6,150),("B2002",dt.date(2026,11,4),"Giza",6,150),("B2012",dt.date(2026,11,17),"Alexandria",4,120)]
for r in rows: ws.append(list(r))
wb.save("lab/lab2.xlsx")
df=pd.read_excel("lab/lab2.xlsx",dtype=object)
print("rows:",len(df))
print("text qty rows:",[o for o,q in zip(df.order_id,df.qty) if isinstance(q,str)])
print("text date rows:",[o for o,d in zip(df.order_id,df.order_date) if isinstance(d,str)])
print("blank cells:",int(df.isna().sum().sum()),"in",[ (o,c) for o in df.order_id for c in df.columns if pd.isna(df.loc[df.order_id==o,c]).any()][:3])
print("duplicate order ids:",list(df.order_id[df.order_id.duplicated()]))
d=df.drop_duplicates("order_id").copy(); d["qty"]=pd.to_numeric(d["qty"]); d["unit_price"]=pd.to_numeric(d["unit_price"])
print("qty total all rows after text fix (duplicate still in):", int(pd.to_numeric(df["qty"]).sum()))
print("qty total, duplicate removed:", int(d["qty"].sum()))
print("revenue, duplicate removed:", int((d["qty"]*d["unit_price"]).sum()))
