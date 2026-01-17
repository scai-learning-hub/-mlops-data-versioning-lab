import argparse
import json
import pandas as pd

def main(inp, out):
    df = pd.read_csv(inp)
    report = {
        "rows": df.shape[0],
        "cols": df.shape[1],
        "missing": int(df.isna().sum().sum()),
    }
    with open(out, "w") as f:
        json.dump(report, f, indent=2)
    print("Profile written:", out)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--inp", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    main(args.inp, args.out)
