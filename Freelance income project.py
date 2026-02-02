import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2022-01-01", end="2024-12-31", freq="M")

records = []

for month in dates:
    n_events = np.random.poisson(lam=3)  # average ~3 payments/month
    
    for _ in range(n_events):
        record = {
            "date": month - pd.to_timedelta(np.random.randint(0, 27), unit="D"),
            "amount_eur": round(np.random.lognormal(mean=7.5, sigma=0.6), 2),
            "source": np.random.choice(
                ["Theater A", "Theater B", "Festival", "Teaching", "Other"]
            ),
            "category": np.random.choice(
                ["performance", "rehearsal", "teaching", "other"]
            ),
        }
        records.append(record)

income_events = pd.DataFrame(records)