import pandas as pd
# creating a simple datA Set
data ={
    'product':['laptop','mouse','keyboard'],
    'price' : [50000,250,500],
    'stock' :[150,200,150]
}

df = pd.DataFrame(data)

df['Total_value'] = df['price'] * df['stock']