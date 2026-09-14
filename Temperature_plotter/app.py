import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load temperature data from a CSV file."""
    try:
        data = pd.read_csv(file_path, parse_dates=["Date"])
        data["Temperature"] = pd.to_numeric(data["Temperature"], errors="coerce")
        data["Temperature"] = data["Temperature"].astype(float)
        print("Data loaded successfully!")
        return data
    except Exception as e:
        print("Error loading data:", e)
        return None

def plot_temperature(data, save_file=None):
    """Plot temperature trends with options for rolling average and anomalies."""
    # Add Rolling Average
    data["7-Day Average"] = data["Temperature"].rolling(window=7).mean()
    
    # Identify Anomalies (robust IQR method + missing values)
    valid = data["Temperature"].dropna()
    q1 = valid.quantile(0.25)
    q3 = valid.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outlier = (data["Temperature"] < lower) | (data["Temperature"] > upper)
    missing = data["Temperature"].isna()
    data["Anomaly"] = outlier | missing
    
    # Plot
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "axes.edgecolor": "#555555",
        "axes.linewidth": 1.0,
        "axes.titleweight": "bold",
        "axes.titlesize": 14,
        "grid.linestyle": "--",
        "grid.alpha": 0.5,
        "grid.color": "#bbbbbb",
        "legend.frameon": True,
        "legend.framealpha": 0.9,
    })
    plt.figure(figsize=(10, 6))
    plt.plot(data["Date"], data["Temperature"], label="Daily Temperature", color="blue")
    plt.plot(data["Date"], data["7-Day Average"], label="7-Day Average", linestyle="--", color="orange")
    anomalies = data[data["Anomaly"] & data["Temperature"].notna()]
    plt.scatter(anomalies["Date"], anomalies["Temperature"], color="red",
                label="Anomalies", s=90, marker="o", edgecolors="black", zorder=3)
    for _, row in anomalies.iterrows():
        plt.annotate(f"{row['Temperature']:.1f}°C", (row["Date"], row["Temperature"]),
                     textcoords="offset points", xytext=(6, 6), fontsize=9,
                     color="darkred", weight="bold")
    plt.title("Temperature Trends")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)

    # Save or Show Plot
    if save_file:
        plt.savefig(save_file)
        print(f"Plot saved as {save_file}")
    else:
        plt.show()

def main():
    print("Welcome to the Temperature Plotter!")
    
    # Load Data
    file_path = input("Enter the path to your temperature CSV file: ")
    data = load_data(file_path)
    if data is None:
        return
    
    # Plot Temperature
    save_choice = input("Do you want to save the plot? (yes/no): ").lower()
    if save_choice == "yes":
        file_name = input("Enter the file name (e.g., temperature_plot.png): ")
        plot_temperature(data, save_file=file_name)
    else:
        plot_temperature(data)

if __name__ == "__main__":
    main()












    
