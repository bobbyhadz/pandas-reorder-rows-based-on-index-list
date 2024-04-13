# Pandas: Reorder DataFrame rows based on Index List 

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan', 'Ethan'],
    'experience': [1, 1, 5, 7, 7],
    'salary': [175.1, 180.2, 190.3, 205.4, 210.5],
}, index=['A', 'B', 'C', 'D', 'E'])

print(df)

print('-' * 50)

index_list = ['C', 'D', 'E', 'B', 'A']

new_df = df.reindex(labels=index_list)
print(new_df)
