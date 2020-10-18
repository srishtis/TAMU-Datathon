import pandas as pd


def map_df_labels_to_ints(df):
    label_dict = {'Food': 0,
                  'Electronics': 1,
                  'Personal Care': 2,
                  'Toys': 3,
                  'Home': 4,
                  'Gifts & Registry': 5,
                  'Cell Phones': 6,
                  'Office Supplies': 7,
                  'Auto & Tires': 8,
                  'Musical Instruments': 9,
                  'Sports & Outdoors': 10,
                  'Seasonal': 11,
                  'Industrial & Scientific': 12,
                  'Household Essentials':13,
                  'Shop by Brand': 14,
                  'Party & Occasions': 15,
                  'Baby': 16,
                  'Walmart for Business': 17,
                  'Books': 18,
                  'Shop by Movie': 19,
                  'Feature': 20,
                  'Movies & TV Shows': 21,
                  'Shop by TV Show': 22,
                  'Arts Crafts & Sewing': 23,
                  'Music': 24,
                  'Home Improvement': 25,
                  'Pets': 26,
                  'Patio & Garden': 27,
                  'Beauty': 28,
                  'Shop by Video Game': 29,
                  'Character Shop': 30,
                  'Health': 31,
                  'Video Games': 32,
                  'Clothing': 33,
                  'Services': 34
                  }
    df = df[['Product_name', 'Breadcrumb_parent']]
    # Here we will map the breadcrumb parent to the dictionary
    df.Breadcrumb_parent.replace(label_dict, inplace=True)
    df = df.rename(columns={'Product_name': 'product_name', 'Breadcrumb_parent': 'category_number'})
    print(df.category_number.unique())

    df.to_csv('big_df.csv')
    pd.set_option('display.max_columns', None)


# FUNCTION CALL FOR EXTRACTING RELEVANT INFO
# NOTE YOU HAVE TO CHANGE LAST LINE IN FUNCTION TO DESIRED NAME
# concatenating the created sets
# should be easy since they have the same feature names
df1 = pd.read_csv('Food_out.csv')
print(len(df1))

df2 = pd.read_csv('books_out.csv')
print(len(df2))

df3 = pd.read_csv('electronics_out.csv')
print(len(df3))

df4 = pd.read_csv('home_out.csv')
print(len(df4))


df6 = pd.read_csv('toys_out.csv')
print(len(df6))

df7 = pd.read_csv('clothes_out.csv')
print(len(df7))

df8 = pd.read_csv('automotive_out.csv')
print(len(df8))

df9 = pd.read_csv('VideoGames_out.csv')
print(len(df9))

df10 = pd.read_csv('personal_care.csv')
print(len(df10))

frames = [df1, df2, df3, df4, df6, df7, df8, df9, df10]
big_df = pd.concat(frames)

big_df = big_df[['Product_name', 'Breadcrumb_parent']]
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

#what will my mapping be?
print(big_df.Breadcrumb_parent.unique())
map_df_labels_to_ints(big_df)

