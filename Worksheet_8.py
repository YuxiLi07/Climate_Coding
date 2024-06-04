import pandas as pd
import matplotlib.pyplot as plt

def plot_sunrise_sunset_times(file_path):
    df = pd.read_csv(file_path, parse_dates=["DATE"], low_memory=False)
    df = df.set_index("DATE")
    
    sunrise = 'DailySunrise'
    sunset = 'DailySunset'
    
    if sunrise not in df.columns or sunset not in df.columns:
        available_columns = df.columns
        return f"Columns '{sunrise}' or '{sunset}' not found in the dataset. Available columns: {available_columns}"
    
    print(f"First few values in {sunrise}:")
    print(df[sunrise].head())
    print(f"First few values in {sunset}:")
    print(df[sunset].head())
    
    df[sunrise] = pd.to_datetime(df[sunrise], format='%H%M').dt.time
    df[sunset] = pd.to_datetime(df[sunset], format='%H%M').dt.time
    
    df[sunrise] = pd.to_datetime(df.index.date.astype(str) + ' ' + df[sunrise].astype(str))
    df[sunset] = pd.to_datetime(df.index.date.astype(str) + ' ' + df[sunset].astype(str))
    
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df[sunrise], label='Sunrise Time', color='orange')
    plt.plot(df.index, df[sunset], label='Sunset Time', color='red')
    plt.title('Sunrise and Sunset Times Throughout the Year')
    plt.xlabel('Date')
    plt.ylabel('Time')
    plt.legend()
    plt.show()
    
def plot_daily_snow_depth(file_path):
    df = pd.read_csv(file_path, parse_dates=["DATE"])
    
    df = df.set_index("DATE")
    
    snow_depth_column = 'DailySnowDepth'
    
    if snow_depth_column not in df.columns:
        available_columns = df.columns
        return f"Column '{snow_depth_column}' not found in the dataset. Available columns: {available_columns}"
    
    print(f"First few values in {snow_depth_column}:")
    print(df[snow_depth_column].head())
    
    df[snow_depth_column] = df[snow_depth_column].replace('T', '0')
    
    df = df.dropna(subset=[snow_depth_column])
    
    df[snow_depth_column] = pd.to_numeric(df[snow_depth_column], errors='coerce')
    
    unique_values = df[snow_depth_column].unique()
    print(f"Unique values in {snow_depth_column}:", unique_values)

    df_daily = df[snow_depth_column].resample('D').mean()

    df_daily = df_daily.dropna()
    
    df_daily.plot()
    plt.title('Daily Snow Depth in Madison in 2020')
    plt.xlabel('Date')
    plt.ylabel('Snow Depth (inches)')
    plt.show()
