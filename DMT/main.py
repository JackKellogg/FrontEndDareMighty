import pandas as pd


def fn():
    lease_data = pd.read_csv("datasets/Lease.csv", sep=",")
    availability_data = pd.read_csv("datasets/Availability.csv", sep=",")
    property_data = pd.read_csv("datasets/Property.csv", sep=",")
    sales_data = pd.read_csv("datasets/Sales.csv", sep=",")

    # df['preTestScore'].where(df['postTestScore'] > 50)
    # print(sales_data['PropertyID'].where(sales_data['Bldg Name'] == 'Aon Center'))
    things_i_need = ['Bldg Name', 'Address', 'City', 'Submarket', 'Market', 'Bldg Class', 'Bldg Type',
                     'Bldg Subtype', 'Stories', 'Bldg Size at Sale',
                     'Sale Status', 'Sales Price', 'Renovated Date'
                     ]
    x = sales_data[sales_data['Bldg Name'] == 'AON Center'][things_i_need]# SELECT B FROM df WHERE A = 2
    # y = "" + x
    return "This will return the data"
