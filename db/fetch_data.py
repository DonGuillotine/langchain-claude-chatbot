import pprint

import pandas as pd

MAX_TEXT_LENGTH=1000  
 

def auto_truncate(val):
    return val[:MAX_TEXT_LENGTH]
 

all_prods_df = pd.read_csv("product_data/product_data_main.csv", converters={
 
    'bullet_point': auto_truncate,
 
    'item_keywords': auto_truncate,
 
    'item_name': auto_truncate
 
})
 
all_prods_df['item_keywords'].replace('', None, inplace=True)
 
all_prods_df.dropna(subset=['item_keywords'], inplace=True)
 
all_prods_df.reset_index(drop=True, inplace=True)


NUMBER_PRODUCTS = 200  
 

product_metadata = ( 
    all_prods_df
     .head(NUMBER_PRODUCTS)
     .to_dict(orient='index')
)