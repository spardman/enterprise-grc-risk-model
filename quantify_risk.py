import pandas as pd
import numpy as np

try:
    df = pd.read_csv('risk_register.csv')
    print("\n--- GRC Risk Quantification Report ---\n")
    iterations = 10000
    for index, row in df.iterrows():
        freq_sim = np.random.poisson(row['likelihood'], iterations)
        loss_sim = np.random.uniform(row['min_loss'], row['max_loss'], iterations)
        ale_results = freq_sim * loss_sim
        print(f"Risk: {row['threat_event']}")
        print(f"  > Average Expected Loss: ${np.mean(ale_results):,.2f}")
        print(f"  > 95th Percentile (VaR): ${np.percentile(ale_results, 95):,.2f}\n")
except Exception as e:
    print(f"Error: {e}")
