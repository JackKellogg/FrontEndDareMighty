import pandas as pd
import json
import numpy as np


def get_info(building_name):
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
    x = sales_data[sales_data['Bldg Name'] == building_name][things_i_need]  # SELECT B FROM df WHERE A = 2
    print(x)
    if x.empty:
        return "No such thing"

    print("------------")
    all_the_data = {}
    for thing in things_i_need:
        all_the_data[thing] = ""+str(np.array((x[thing]))[0])
        if type(np.array((x[thing]))[0]) == "<class 'numpy.int64'>":
            print("got em")
            all_the_data[thing] = int(np.array((x[thing]))[0])
        print(type(all_the_data[thing]))
    print(all_the_data)
    json_data = "" #json.dumps(all_the_data)
    print("------------")
    print(type(x))
    print(x)

    return all_the_data


def getAllBuildingNames():
    lease_data = pd.read_csv("datasets/Lease.csv", sep=",")
    availability_data = pd.read_csv("datasets/Availability.csv", sep=",")
    property_data = pd.read_csv("datasets/Property.csv", sep=",")
    sales_data = pd.read_csv("datasets/Sales.csv", sep=",")

    print(sales_data['Bldg Name'].unique())
    x = list(sales_data['Bldg Name'].unique())
    x.pop(20)
    print(x)
    return x

def getAllBuildingNamesReact():
    names = getAllBuildingNames()
    print(names)
    entry = '{{label: "{0}"}},'
    final = ""
    print(final)
    for name in names:
        if name == "nan":
            pass
        final = final + entry.format(name)
    final = "[" + final + "]"
    print(final)
    return final


if __name__ == '__main__':
    getAllBuildingNames()
