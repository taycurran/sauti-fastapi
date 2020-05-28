import pandas as pd

qc_ws = pd.read_csv("app/qc_wholesale.csv")
qc_ws = qc_ws.to_json()
print(qc_ws)