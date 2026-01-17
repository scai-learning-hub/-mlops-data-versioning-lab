import argparse
import yaml
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification

def main(out_path):
    with open("params.yaml") as f:
        p = yaml.safe_load(f)["data"]

    rng = np.random.default_rng(p["seed"])

    X, y = make_classification(
        n_samples=p["n_samples"],
        n_features=p["n_features"],
        n_informative=p["n_informative"],
        random_state=p["seed"],
    )

    X = X + p["shift_mean"]

    if p["noise_std"] > 0:
        y = y + rng.normal(0, p["noise_std"], size=len(y))
        y = (y > np.median(y)).astype(int)

    df = pd.DataFrame(X, columns=[f"f{i}" for i in range(X.shape[1])])
    df["target"] = y

    for c in df.columns[:3]:
        idx = rng.choice(len(df), int(len(df) * p["missing_rate"]), replace=False)
        df.loc[idx, c] = np.nan

    df.to_csv(out_path, index=False)
    print("Dataset written:", out_path)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    main(args.out)
