import pandas as pd

label_dict = {'Food': 0,
              'Electronics': 1,
              'Personal Care': 2,
              'Toys': 3,
              'Home': 4,
              'Gifts & Registry': 5
              }

df = pd.read_csv('out_TVs.csv')
df = df[['Product_name', 'Breadcrumb_parent']]
# Here we will map the breadcrumb parent to the dictionary
df.Breadcrumb_parent.replace(label_dict, inplace=True)
df = df.rename(columns={'Product_name': 'product_name', 'Breadcrumb_parent': 'category_number'})
df.to_csv('filtered_out_TVs.csv')

print(df.head())
