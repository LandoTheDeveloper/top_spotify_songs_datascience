import pandas as pd
import matplotlib.pyplot as plt

file_path = "Your_All-Time_Top_Songs.csv"
df = pd.read_csv(file_path)

artist_counts = (
    df["Album Name"]
    .str.split(";")
    .explode()
    .value_counts()
    .head(10)
)

print(artist_counts)
artist_counts.plot(kind="bar")
plt.title('Top 100 Songs by Artists')
plt.xlabel('Artist')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha="right")
plt.show()