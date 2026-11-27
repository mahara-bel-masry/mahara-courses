# leading zeros: IDs and phones are text, not numbers
import pandas as pd
df = pd.DataFrame({"phone_text": ["01012345678", "01198765432"]})
df["as_number"] = pd.to_numeric(df["phone_text"])
print(df.to_string(index=False))
print("as number the leading zero is gone:", df["as_number"].iloc[0])
print("rule: if you never do math on it, keep it text")
