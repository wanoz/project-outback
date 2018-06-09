import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')

import django
django.setup()

from search_app.models import Meals_local_db as db
import pandas as pd

def import_csv(data_dir):
    df = pd.read_csv(data_dir, sep=";")
    header_list = []
    df_list = []

    # Get header list - array
    headers_list = list(df)[0].split(",")
    headers_list = remove_last_empty(headers_list)
    
    # Get value list - matrix
    for row_index, row_value in df.iterrows():
        row_list = row_value.apply(lambda x: x.split(","))[0]
        row_list = remove_last_empty(row_list)
        df_list.append(row_list)

    return headers_list, df_list

def remove_last_empty(d_list):
    if d_list[len(d_list)-1] == "":
        d_list.pop()
    return d_list

def selectcol_by_header(header_list, selected_headers):
    headers_index = []
    headers_index = [header_list.index(header) for header in selected_headers]
    return headers_index

def save_to_django_db(headers_index, headers, values):
    # test_db = []
    for entry in values:
        val_1 = entry[headers_index[0]]
        val_2 = entry[headers_index[1]]
        val_3 = entry[headers_index[2]]
        val_4 = entry[headers_index[3]]
        val_5 = entry[headers_index[4]]
        val_6 = entry[headers_index[5]]
        val_7 = entry[headers_index[6]]
        val_8 = entry[headers_index[7]]
        val_9 = entry[headers_index[8]]
        val_10 = entry[headers_index[9]]
        val_11 = entry[headers_index[10]]
        val_12 = entry[headers_index[11]]
        val_13 = entry[headers_index[12]]
        val_14 = entry[headers_index[13]]
        val_15 = entry[headers_index[14]]
        val_16 = entry[headers_index[15]]
        val_17 = entry[headers_index[16]]
        val_18 = entry[headers_index[17]]
        val_19 = entry[headers_index[18]]
        val_20 = entry[headers_index[19]]
        val_21 = entry[headers_index[20]]
        val_22 = entry[headers_index[21]]
        
        # db.objects.get_or_create(field1=val_1, field2=val_2, field3=val_3)
        db.objects.get_or_create(
            meal_name=val_1, 
            price=val_2,
            hot_or_cold=val_3,
            cuisine_type=val_4,
            meal_category=val_5,
            cooking_method=val_6,
            meat_1=val_7,
            meat_2=val_8,
            meat_3=val_9,
            carbs_1=val_10,
            carbs_2=val_11,
            veggie_1=val_12,
            veggie_2=val_13,
            veggie_3=val_14,
            dairy_1=val_15,
            dairy_2=val_16,
            dairy_3=val_17,
            dairy_4=val_18,
            gluten_free=val_19,
            halal=val_20,
            flavouring=val_21,
            restaurant_ID=val_22,            
            )
    #     test_db.append([val_1, val_2, val_3])
    # return test_db

# Main script
if __name__ == '__main__':
    # Set the directory for the data file
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(BASE_DIR, "web_project", "static", "data", "meals_db.csv")
    headers, values = import_csv(data_dir)
    
    # Choose which headers to pick out
    selectcol_headers = [
        "meal_name",
        "price",
        "hot_or_cold",
        "cuisine_type",
        "meal_category",
        "cooking_method",
        "meat_1",
        "meat_2",
        "meat_3",
        "carbs_1",
        "carbs_2",
        "veggie_1",
        "veggie_2",
        "veggie_3",
        "dairy_1",
        "dairy_2",
        "dairy_3",
        "dairy_4",
        "gluten_free",
        "halal",
        "flavouring",
        "restaurant_ID"
    ]

    # Get the headers indices of the database
    headers_index = selectcol_by_header(headers, selectcol_headers)
    
    print("\n--------Data reading-------")
    print("Headers: ", end="")
    print(headers)
    print("Selected headers column index: ", end="")
    print(headers_index)
    print("Number of rows: " + str(len(values)))
    input("Press Enter to continue...")
    print("\n-----Saving to database----")
    save_to_django_db(headers_index,headers, values)
    # test_db = save_to_django_db(headers_index,headers, values)
    # print("Printing first few values: " + str(test_db[0]))
    print('Task completed!')
   