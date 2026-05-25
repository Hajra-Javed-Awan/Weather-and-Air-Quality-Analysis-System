import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# STYLE
sns.set_style("whitegrid")

# LOAD CSV FILE
df = pd.read_csv(r"C:\Users\CS\Desktop\weather\pakistan_air_quality_final_clean.csv")

print("Dataset Loaded Successfully")

# SHOW DATA
print(df.head())

# REMOVE DUPLICATES
df.drop_duplicates(inplace=True)

# MISSING VALUES
print(df.isnull().sum())

# GRAPH 1
if 'city' in df.columns and 'temperature' in df.columns:

    plt.figure(figsize=(12,6))

    temp = df.groupby('city')['temperature'].mean()

    plt.bar(temp.index, temp.values)

    plt.title("Average Temperature")
    plt.xlabel("City")
    plt.ylabel("Temperature")

    plt.xticks(rotation=45)

    plt.show()

# GRAPH 2
if 'temperature' in df.columns and 'humidity' in df.columns:

    plt.figure(figsize=(10,6))

    sns.scatterplot(
        data=df,
        x='temperature',
        y='humidity',
        hue='city'
    )

    plt.title("Temperature vs Humidity")

    plt.show()

# GRAPH 3
if 'pm2_5' in df.columns:

    plt.figure(figsize=(12,6))

    pollution = df.groupby('city')['pm2_5'].mean()

    sns.barplot(
        x=pollution.index,
        y=pollution.values
    )

    plt.title("PM2.5 Pollution")

    plt.xticks(rotation=45)

    plt.show()

print("Project Completed Successfully")