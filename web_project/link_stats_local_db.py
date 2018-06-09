import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')

import django
django.setup()

from stats_app.models import Usage_stats_local_db as db
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
        val_23 = entry[headers_index[22]]
        
        # db.objects.get_or_create(field1=val_1, field2=val_2, field3=val_3)
        db.objects.get_or_create(
            user_name=val_1, 
            search_time=val_2,
            search_date=val_3,
            search_frequency=val_4,
            search_time_mean=val_5,
            search_time_stddev=val_6,
            search_date_interval_mean=val_7,
            search_date_interval_stddev=val_8,
            meat_1_last=val_9,
            meat_2_last=val_10,
            meat_3_last=val_11,
            veggie_1_last=val_12,
            veggie_2_last=val_13,
            veggie_3_last=val_14,
            carbs_1_last=val_15,
            carbs_2_last=val_16,
            dairy_1_last=val_17,
            dairy_2_last=val_18,
            dairy_3_last=val_19,
            gluten_free_last=val_20,
            halal_last=val_21,
            flavouring_last=val_22,
            restaurant_ID_last=val_23,            
            )
    #     test_db.append([val_1, val_2, val_3])
    # return test_db

# Main script
if __name__ == '__main__':
    # Set the dirctory for the data file
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(BASE_DIR, "web_project", "static", "data", "usage_stats_db.csv")
    headers, values = import_csv(data_dir)
    
    # Choose which headers to pick out
    selectcol_headers = [
        "user_name",
        "search_time",
        "search_date",
        "search_frequency",
        "search_time_mean",
        "search_time_stddev",
        "search_date_interval_mean",
        "search_date_interval_stddev",
        "meat_1_last",
        "meat_2_last",
        "meat_3_last",
        "veggie_1_last",
        "veggie_2_last",
        "veggie_3_last",
        "carbs_1_last",
        "carbs_2_last",
        "dairy_1_last",
        "dairy_2_last",
        "dairy_3_last",
        "gluten_free_last",
        "halal_last",
        "flavouring_last",
        "restaurant_ID_last"
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