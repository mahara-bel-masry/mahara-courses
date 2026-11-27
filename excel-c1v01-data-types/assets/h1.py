# same five checks, run on the RAW file (before the fix) and on the fixed data
import pandas as pd
def checks(df):
    out=[]
    out.append(("order_id not duplicated", not df["order_id"].duplicated().any()))
    out.append(("no empty cells", not df.isna().any().any()))
    q=df["qty"]; out.append(("qty is whole and positive number", all(isinstance(v,(int,float)) and not isinstance(v,bool) and v>0 and float(v).is_integer() for v in q)))
    out.append(("dates are real dates", all(hasattr(v,"year") for v in df["order_date"])))
    out.append(("price is numeric", all(isinstance(v,(int,float)) for v in df["unit_price"])))
    return out
raw=pd.read_excel("data/raw.xlsx",dtype=object)
print("RAW FILE"); [print(" ","PASS" if ok else "FAIL","-",n) for n,ok in checks(raw)]
fx=raw.copy(); fx["qty"]=pd.to_numeric(fx["qty"]); fx["unit_price"]=pd.to_numeric(fx["unit_price"])
print("AFTER FIX"); [print(" ","PASS" if ok else "FAIL","-",n) for n,ok in checks(fx)]
# a deliberately broken copy to prove each check can fail
b=fx.astype(object).copy(); b.loc[0,"order_id"]=b.loc[1,"order_id"]; b.loc[2,"city"]=None; b.loc[3,"qty"]=-2; b.loc[4,"order_date"]="05/11/2026"; b.loc[5,"unit_price"]="abc"
print("DELIBERATELY BROKEN COPY"); [print(" ","PASS" if ok else "FAIL","-",n) for n,ok in checks(b)]
