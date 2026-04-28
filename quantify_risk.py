import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your GRC data
try:
    df = pd.read_csv('risk_register.csv')
    iterations = 10000
    
    # Analyze Ransomware risk (R-001) for the visual
    row = df.iloc[0]
    
    # Monte Carlo Simulation
    freq_sim = np.random.poisson(row['likelihood'], iterations)
    loss_sim = np.random.uniform(row['min_loss'], row['max_loss'], iterations)
    ale_results = freq_sim * loss_sim
    
    # Filter scenarios where an event occurred
    loss_events = ale_results[ale_results > 0]

    # --- Create Professional Visualization ---
    plt.figure(figsize=(10, 6), dpi=300) 
    plt.hist(loss_events, bins=50, color='#2c3e50', edgecolor='white', alpha=0.8)
    
    # Calculate 95% Value at Risk (VaR)
    var_95 = np.percentile(ale_results, 95)
    plt.axvline(var_95, color='#e74c3c', linestyle='--', linewidth=2, label=f'95% VaR: ${var_95:,.0f}')

    # Add GRC Branding & Labels
    plt.title('Quantitative IT Risk: Ransomware Scenario (ALE)', fontsize=16, fontweight='bold')
    plt.xlabel('Annual Loss Exposure ($)', fontsize=12)
    plt.ylabel('Frequency (Simulated Scenarios)', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.legend(loc='upper right', frameon=True)

    # Save as high-quality PNG
    plt.tight_layout()
    plt.savefig('grc_risk_thumbnail.png')
    print("Success! Thumbnail saved as 'grc_risk_thumbnail.png' in your folder.")

except Exception as e:
    print(f"Error: {e}")
