# scenario 2: price lookup after a price table grows by a pasted block of 3 rows (LibreOffice 26.8.3, invented data)
# [L] the script extends the table ref to include the pasted rows; it does not test Excel's auto-expand.
import openpyxl, subprocess
from openpyxl.worksheet.table import Table, TableStyleInfo
base=[("P100","pen",10),("P101","notebook",30),("P102","stapler",55),("P103","folder",8),("P104","marker",15)]
pasted=[("P105","tape",12),("P106","scissors",40),("P107","ruler",6)]
orders=[("O1","P101",2),("O2","P105",5),("O3","P102",1),("O4","P106",3),("O5","P107",10)]
def build(name,rows):
    wb=openpyxl.Workbook(); p=wb.active; p.title="products"
    p.append(["sku","item","price"])
    for r in rows: p.append(list(r))
    last=len(rows)+1
    t=Table(displayName="tblProducts",ref=f"A1:C{last}"); t.tableStyleInfo=TableStyleInfo(name="TableStyleMedium2"); p.add_table(t)
    o=wb.create_sheet("orders"); o.append(["order","sku","qty","price_fixed","price_table","revenue_table"])
    for i,(a,b,c) in enumerate(orders,start=2):
        o.append([a,b,c,
          f'=IFERROR(INDEX(products!$C$2:$C$6,MATCH(B{i},products!$A$2:$A$6,0)),"missing")',
          f'=IFERROR(INDEX(tblProducts[price],MATCH(B{i},tblProducts[sku],0)),"missing")',
          f'=IFERROR(C{i}*E{i},0)'])
    o["H1"]="total revenue (table lookup)"; o["H2"]="=SUM(F2:F6)"
    o["H3"]="rows found, fixed range"; o["H4"]='=COUNT(D2:D6)'
    o["H5"]="rows found, table"; o["H6"]='=COUNT(E2:E6)'
    wb.save(f"data/{name}.xlsx")
    subprocess.run(["soffice","--headless","--convert-to","xlsx:Calc MS Excel 2007 XML","--outdir","data/out9",f"data/{name}.xlsx"],capture_output=True,timeout=90)
    x=openpyxl.load_workbook(f"data/out9/{name}.xlsx",data_only=True)["orders"]
    print(f"{name}: products={len(rows)} | fixed-range lookups found={x['H4'].value} of 5 | table lookups found={x['H6'].value} of 5 | revenue (table)={x['H2'].value}")
    print("  price_fixed:",[x[f'D{i}'].value for i in range(2,7)]," price_table:",[x[f'E{i}'].value for i in range(2,7)])
build("p5",base)
build("p8",base+pasted)
