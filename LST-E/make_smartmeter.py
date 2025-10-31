# save as make_smartmeter.py in LST-E, then run: python make_smartmeter.py
from datasets import load_dataset
import pandas as pd, numpy as np

ds = load_dataset("EDS-lab/electricity-demand")
df = ds["demand"].to_pandas()          # if the key differs, print(ds) to see
# Pick the right columns in your split:
# assume columns: 'timestamp' and one load column (e.g., 'load'/'consumption_kwh')
load_col = [c for c in df.columns if c.lower().startswith(("load","consumption","demand","value"))][0]

df = df.rename(columns={load_col: "value"})
df["timestamp"] = pd.to_datetime(df["timestamp"]).dt.floor("H")
df = df.groupby("timestamp", as_index=False)["value"].sum()

# Add the columns LST-E expects
df["device_id"] = "meter-001"
df["device_name"] = "main"
df["property"] = "consumption"

df[["device_id","device_name","property","value","timestamp"]].to_csv("smartmeter.csv", index=False)
print("smartmeter.csv written:", len(df), "rows")
