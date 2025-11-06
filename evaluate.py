import pandas as pd, os
from src.config import OUTPUT_DIR

def evaluate_districts(partition):
    pops = list(partition["population"].values())
    ratio = max(pops) / min(pops)
    df = pd.DataFrame({"district": range(len(pops)), "population": pops})
    df.loc[len(df)] = ["max/min", ratio]
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df.to_csv(f"{OUTPUT_DIR}/metrics.csv", index=False)
    return {"ratio": ratio}
