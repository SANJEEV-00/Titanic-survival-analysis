import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('titanic.csv')
df.info()
# Handling missing values
df.fillna(df.median(), inplace=True)
# Data visualization
sns.countplot(x='Survived', data=df)
plt.show()