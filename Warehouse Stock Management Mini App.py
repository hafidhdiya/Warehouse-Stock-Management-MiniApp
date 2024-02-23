from tabulate import tabulate
from operator import itemgetter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import datetime

print(f"\n----------------------------------------")
print("---- PT Purwadhika Coding Warehouse ----")
print(".......Warehouse Stock Management.......")
print("----------------------------------------")
InventoryData = [
    {'Item Code' : 2204001, 'Item Name' : 'Air Fryer', 'Type' : 'Cooking Ware', 'Condition' : 'Good', 'Buying Price' : 1000000, 'Selling Price' : 1500000, 'Initial Stock' : 20, 'Date of Entry' : datetime.date(2023,6,21).strftime("%d %b %Y")},
    {'Item Code' : 2204002, 'Item Name' : 'Rice Cooker', 'Type' : 'Cooking Ware', 'Condition' : 'Good', 'Buying Price' : 1200000, 'Selling Price' : 1800000, 'Initial Stock' : 30, 'Date of Entry' : datetime.date(2023,5,8).strftime("%d %b %Y")},
    {'Item Code' : 2204003, 'Item Name' : 'Refrigerator', 'Type' : 'Cooking Ware', 'Condition' : 'Good', 'Buying Price' : 7000000, 'Selling Price' : 9500000, 'Initial Stock' : 15, 'Date of Entry' : datetime.date(2023,7,2).strftime("%d %b %Y")},
    {'Item Code' : 2204004, 'Item Name' : 'Dispenser', 'Type' : 'Cooking Ware', 'Condition' : 'Good', 'Buying Price' : 500000, 'Selling Price' : 750000, 'Initial Stock' : 26, 'Date of Entry' : datetime.date(2023,4,30).strftime("%d %b %Y")},
    ]

SalesData  = [ 
    {'Order ID' : 2311001, 'Item Name' : 'Air Fryer', 'Quantity Ordered' : 1, 'Price Each' : 1500000, 'Order Date' : datetime.date(2023,10,1).strftime("%d %b %Y"), 'Month' : 10},
    {'Order ID' : 2311002, 'Item Name' : 'Rice Cooker', 'Quantity Ordered' : 2, 'Price Each' : 1800000, 'Order Date' : datetime.date(2023,10,2).strftime("%d %b %Y"), 'Month' : 10},
    {'Order ID' : 2311003, 'Item Name' : 'Refrigerator', 'Quantity Ordered' : 3, 'Price Each' : 9500000, 'Order Date' : datetime.date(2023,10,3).strftime("%d %b %Y"), 'Month' : 10},
    {'Order ID' : 2311004, 'Item Name' : 'Dispenser', 'Quantity Ordered' : 4, 'Price Each' : 750000, 'Order Date' : datetime.date(2023,10,4).strftime("%d %b %Y"), 'Month' : 10},
    {'Order ID' : 2311005, 'Item Name' : 'Air Fryer', 'Quantity Ordered' : 1, 'Price Each' : 1500000, 'Order Date' : datetime.date(2023,10,5).strftime("%d %b %Y"), 'Month' : 10},
    {'Order ID' : 2311006, 'Item Name' : 'Rice Cooker', 'Quantity Ordered' : 2, 'Price Each' : 1800000, 'Order Date' : datetime.date(2023,10,6).strftime("%d %b %Y"), 'Month' : 10},
    {'Order ID' : 2311007, 'Item Name' : 'Dispenser', 'Quantity Ordered' : 5, 'Price Each' : 750000, 'Order Date' : datetime.date(2023,10,7).strftime("%d %b %Y"), 'Month' : 10},
    {'Order ID' : 2311008, 'Item Name' : 'Air Fryer', 'Quantity Ordered' : 3, 'Price Each' : 1500000, 'Order Date' : datetime.date(2023,10,8).strftime("%d %b %Y"), 'Month' : 10},
    {'Order ID' : 2311009, 'Item Name' : 'Rice Cooker', 'Quantity Ordered' : 4, 'Price Each' : 1500000, 'Order Date' : datetime.date(2023,10,9).strftime("%d %b %Y"), 'Month' : 10},
    {'Order ID' : 2311001, 'Item Name' : 'Air Fryer', 'Quantity Ordered' : 2, 'Price Each' : 1500000, 'Order Date' : datetime.date(2023,11,1).strftime("%d %b %Y"), 'Month' : 11},
    {'Order ID' : 2311002, 'Item Name' : 'Rice Cooker', 'Quantity Ordered' : 1, 'Price Each' : 1800000, 'Order Date' : datetime.date(2023,11,2).strftime("%d %b %Y"), 'Month' : 11},
    {'Order ID' : 2311003, 'Item Name' : 'Refrigerator', 'Quantity Ordered' : 1, 'Price Each' : 9500000, 'Order Date' : datetime.date(2023,11,3).strftime("%d %b %Y"), 'Month' : 11},
    {'Order ID' : 2311004, 'Item Name' : 'Dispenser', 'Quantity Ordered' : 3, 'Price Each' : 750000, 'Order Date' : datetime.date(2023,11,4).strftime("%d %b %Y"), 'Month' : 11},
    {'Order ID' : 2311005, 'Item Name' : 'Air Fryer', 'Quantity Ordered' : 1, 'Price Each' : 1500000, 'Order Date' : datetime.date(2023,11,5).strftime("%d %b %Y"), 'Month' : 11},
    {'Order ID' : 2311006, 'Item Name' : 'Rice Cooker', 'Quantity Ordered' : 3, 'Price Each' : 1800000, 'Order Date' : datetime.date(2023,11,6).strftime("%d %b %Y"), 'Month' : 11},
    {'Order ID' : 2311007, 'Item Name' : 'Dispenser', 'Quantity Ordered' : 2, 'Price Each' : 750000, 'Order Date' : datetime.date(2023,11,7).strftime("%d %b %Y"), 'Month' : 11},
    {'Order ID' : 2311008, 'Item Name' : 'Air Fryer', 'Quantity Ordered' : 4, 'Price Each' : 1500000, 'Order Date' : datetime.date(2023,11,8).strftime("%d %b %Y"), 'Month' : 11},
    {'Order ID' : 2311009, 'Item Name' : 'Rice Cooker', 'Quantity Ordered' : 2, 'Price Each' : 1500000, 'Order Date' : datetime.date(2023,11,9).strftime("%d %b %Y"), 'Month' : 11}
              ]

#Menu Utama
def main_menu():
    while True :
        print(f'''\nMenu : 
            1. Inventory Data Menu
            2. Add Item Menu
            3. Update Item Menu
            4. Delete Item Menu
            5. Inventory Data Visualization
            6. Sales Data Menu
            0. Exit Program
            ''')
        print()
        try : 
            menu = int(input("Enter Menu Option : "))
            print()
            if menu in [1,2,3,4,5,6,7,8] :
                break
            else :
                print("Menu yang dimasukkan salah, silahkan coba lagi.")
        except :
            print("Menu yang dimasukkan salah, silahkan coba lagi.")

    if menu == 1 : #Inventory Data Menu
        menu1()

    elif menu == 2 : #Add Item Menu
        menu2()

    elif menu == 3 : #Update Item Menu
        menu3()
            
    elif menu == 4 : #Delete Item Menu
        menu4()
    
    elif menu == 5 : #Data Visualization
        menu5()
    
    elif menu == 6 : #Sales Data Menu
        menu6()

    elif menu == 0 : #Exit Program
        print("Thank you for visiting us.")
        exit()

    elif (menu != 1) or (menu != 2) or (menu != 3) or (menu != 4) or (menu != 5) :
        print(f"Incorrect Input, please enter the correct Menu Options.\n")

#Menu 1
#Fungsi Menampilkan Data Pasien
def show_data() :
    print("All Inventory Data")
    headersP = InventoryData[0].keys()
    dataP = [i.values() for i in InventoryData]
    print(tabulate(dataP,headersP, tablefmt="grid"))

def sort(sorting, reverse = False):
    list = sorted(InventoryData, key=itemgetter(sorting), reverse = reverse)
    headersP = list[0].keys()
    dataP = [j.values() for j in list]
    print(tabulate(dataP,headersP, tablefmt="grid"))

def menu1() :
    menu1_con = True
    while menu1_con:
        while True :
            print()
            print(f'''Inventory Data Menu : 
                    1. Show All Inventory Data
                    2. Show the Latest Stock Data
                    3. Show Item based on ID
                    4. Sorting Menu
                    5. Main Menu
                    \n''')        
            print()
            try : 
                menu_1 = int(input("Please enter the menu : "))
                print()
                if menu_1 in [1,2,3,4,5] :
                    break
                else :
                    print("Incorrect input, please try again.")
            except :
                print("Incorrect input, please try again.")

        if menu_1 == 1 :
            show_data()

        elif menu_1 == 2 :
            pass

        elif menu_1 == 3:
            ID_conf = True
            while ID_conf :
                itemCode = int(input("Enter Item Code : "))
                for k in range(len(InventoryData)) :
                    if itemCode == InventoryData[k]['Item Code'] :
                        print(f'The Item with the code {itemCode} is shown below : ')
                        print(f"\nItem Name        \t: {InventoryData[k]['Item Name']}")
                        print(f"Item Code          \t: {InventoryData[k]['Item Code']}")
                        print(f"Type               \t: {InventoryData[k]['Type']}")
                        print(f"Condition             \t: {InventoryData[k]['Condition']}")
                        print(f"Buying Pric         \t: {InventoryData[k]['Buying Price']}")
                        print(f"Selling Price        \t: {InventoryData[k]['Selling Price']}")
                        print(f"Initial Stock        \t: {InventoryData[k]['Initial Stock']}")
                        print(f"Date of Entry      \t: {InventoryData[k]['Date of Entry']}\n")
                        ID_conf = False
                        break
                    else : 
                        print(f"Incorrect item code, please try again.\n")
                        break

        elif menu_1 == 4 :
            sorting_conf = True

            while sorting_conf :
                try :
                    print('''Sorting Menu
                        Sort the data based on :
                        1. Item Name (A - Z)
                        2. Item Name (Z - A)
                        3. Buying Price (Min - Max)
                        4. Buying Price (Max - Min)
                        5. Amount of Stock
                        6. Date of Entry
                        ''')
                    menu_sorting = int(input("Enter the Menu Option : "))
                    
                    if menu_sorting == 1 :
                        sort('Item Name')

                    elif menu_sorting == 2 :
                        sort('Item Name', reverse=True)

                    elif menu_sorting == 3 :
                        sort('Buying Price')

                    elif menu_sorting == 4 :
                        sort('Buying Price', reverse=True)

                    elif menu_sorting == 5 :
                        sort('Initial Stock')

                    elif menu_sorting == 6 :
                        InventoryData.sort(key = lambda i:i['Date of Entry'], reverse=True)
                        headersP = InventoryData[0].keys()
                        dataP = [j.values() for j in InventoryData]
                        print(tabulate(dataP,headersP))
                
                    jawab_sorting = input(f"\nTry sorting menu again? (Yes / No) : ")
                    print()

                    if jawab_sorting.lower() == 'yes' :
                        continue
                    elif jawab_sorting.lower() == 'no' :
                        sorting_conf = False
                except :
                    print("Incorrect input, please try again.")

        elif menu_1 == 5 :
            menu1_con = False
            main_menu()

# Menu 2 : Add Item
def menu2() :
    menu2_con = True
    while menu2_con :
        while True :
            print(f'''\nAdd Item Menu
            1. Add Item in Inventory Data
            2. Main Menu\n''')
            print()
            try : 
                menu_2 = int(input("Please enter the menu : "))
                print()
                if menu_2 in [1,2] :
                    break
                else :
                    print("Incorrect input, please try again.")
            except :
                print("Incorrect input, please try again.")

        if menu_2 == 1 :
            New_Code = InventoryData[-1]['Item Code']+1
            New_Item_Name = input("Please Enter the New Item Name : ")
            New_Type = input("Please Enter the New Item Type : ")
            New_Condition = input("Please Enter the Condition : ")
            try : 
                New_BPrice = int(input("Please Enter the Buying Price : "))
            except :
                print("Incorrect input, please insert the correct price.")
            try : 
                New_SPrice = int(input("Please Enter the Selling Price : "))
            except :
                print("Incorrect input, please insert the correct price.")
            try : 
                New_inStock = int(input("Please Enter the amount of stock : "))
            except :
                print("Incorrect input, please insert the correct amount.")
            New_Date = datetime.date.now()

            InventoryData.append(
                {'Item Code' : New_Code, 
                 'Item Name' : New_Item_Name.title(), 
                 'Type' : New_Type.title(), 
                 'Condition' : New_Condition.capitalize(), 
                 'Buying Price' : New_BPrice, 
                 'Selling Price' : New_SPrice, 
                 'Initial Stock' : New_inStock,
                 'Date of Entry' : New_Date.strftime("%d %b %Y")}
            )
        
        elif menu_2 == 2 :
            menu2_con = False
            main_menu()

#Menu 3
#Update Item Menu
def menu3() :
    menu3_con = True
    while menu3_con :
        while True :
            print('''Update Item
                1. Update the available item
                2. Menu Utama
                ''')
            print()
            try : 
                menu_3 = int(input("Please enter the menu  : "))
                print()
                if menu_3 in [1,2] :
                    break
                else :
                    print("Incorrect input, please try again.")
            except :
                print("Incorrect input, please try again.")
            
        if menu_3 == 1 :
            answer = True
            while answer : 
                code_update = int(input("Please input the item code to be updated : "))
                for i in len(InventoryData) :
                    if code_update == InventoryData[i]['Item Code'] :
                        print(f"The detail data of the Item {code_update} : ")
                        print(f"{InventoryData[i]['Item Name']}\t|{InventoryData[i]['Type']}\t|{InventoryData[i]['Condition']}\t|{InventoryData[i]['Buying Price']}\t|{InventoryData[i]['Selling Price']}\t|{InventoryData[i]['Initial Stock']}\t|{InventoryData[i]['Date of Entry']}\t|")
                        
                        answer2 = True
                        while answer2 :
                            resp2 = str(input(f"Do you want to update the item with the code of {code_update}? (Yes / No) : "))

                            if resp2.lower() == 'yes' :
                                print('''Choose the column to be updated : 
                                    1. Item Name
                                    2. Type
                                    3. Condition
                                    4. Buying Price
                                    5. Selling Price
                                    6. Initial Stock
                                    ''')
                                column_update = int(input("Please choose the column : "))
                                if column_update == 1 :
                                    update_name = input("Please insert the updated Item Name : ")
                                    InventoryData[i]["Item Name"] = update_name.title()

                                elif column_update == 2 :
                                    update_type = input("Please insert the updated Item Type : ")
                                    InventoryData[i]["Type"] = update_type.title()

                                elif column_update == 3 :
                                    update_condition = input("Please insert the updated Item Condition : (Good / Bad)")
                                    InventoryData[i]["Condition"] = update_condition.title()

                                elif column_update == 4 :
                                    try :
                                        update_bPrice = int(input("Please insert the updated Buying Pricee : "))
                                        InventoryData[i]["Buying Price"] = update_bPrice
                                    except :
                                        print("Incorrect input, please try again.")

                                elif column_update == 5 :
                                    try :
                                        update_sPrice = int(input("Please insert the updated Selling Price : "))
                                        InventoryData[i]["Selling Price"] = update_sPrice
                                    except :
                                        print("Incorrect input, please try again.")

                                elif column_update == 6 :
                                    try :
                                        update_stock = int(input("Please insert the updated Stock : "))
                                        InventoryData[i]["Initial Stock"] = update_stock.title()
                                    except :
                                        print("Incorrect input, please try again.")

                                else : 
                                    print(f"Incorrect input, please try again.\n")
                                
                                resp = str(input("Do you want to update another column? (Yes / No) : "))

                                if resp.lower() == 'yes' :
                                    continue
                                elif resp.lower() == 'no' :
                                    answer2 == False
                                    break
                            
                            elif resp2.lower() ==  'no' :
                                break
                        
                        answer = False
                        break
                    
                    else :
                        print("Incorrect item code, please try again.")

        elif menu_3 == 2 :
            menu3_con = False
            main_menu()

#Menu 4
#Delete the item
def menu4():
    menu4_con = True 
    while menu4_con :
        while True :
            print('''Delete Item Menu
                1. Delete the available item
                2. Main Menu
                ''')
            try : 
                menu_4 = int(input("Please enter the menu : "))
                print()
                if menu_4 in [1,2] :
                    break
                else :
                    print("Incorrect input, please try again.")
            except :
                print("Incorrect input, please try again.")

        if menu_4 == 1 :
            show_data()
            print()
            index_delete = int(input("Please input the Item Code to be deleted : "))

            for x in range (len(InventoryData)):
                if index_delete == InventoryData[x]['Item Code'] :
                    del InventoryData[x]
                    print(f"\nItem with the code {index_delete} is successfully deleted.\n")
                    show_data()
                    break
        elif menu_4 == 2 :
            menu4_con = False
            main_menu()

#Data Visualization
def menu5() :
    list1 = []
    list2 = []

    for i in range(len(InventoryData)) :
        list1.append(InventoryData[i]['Item Name'])
        list2.append(InventoryData[i]['Initial Stock'])

    plt.bar(list1, list2)
    plt.title('Inventory Data Visualization')
    plt.xlabel('Item Name')
    plt.ylabel('Initial Stock')
    plt.show()

def show_salesData(month=all) :
    print("Sales Data")
    newlist_sales = []
    if month == all :
        headersP = SalesData[0].keys()
        dataP = [i.values() for i in SalesData]
        print(tabulate(dataP,headersP, tablefmt="grid"))
    else :
        for i in range(len(SalesData)) :
            if SalesData[i]['Month'] == month :
                newlist_sales.append({'Order ID' : SalesData[i]['Order ID'], 'Item Name' : SalesData[i]['Item Name'], 'Quantity Ordered' : SalesData[i]['Quantity Ordered'], 'Price Each' : SalesData[i]['Price Each'], 'Order Date' : SalesData[i]['Order Date']})
        headersP = newlist_sales[0].keys()
        dataP = [i.values() for i in newlist_sales]
        print(tabulate(dataP,headersP, tablefmt="grid"))

#Sales Data Menu
def menu6() :
    menu6_conf = True
    while menu6_conf:
        while True :
            print('''Sales Data Menu :
                1. Show All Sales Data
                2. Show Sales Data by Month
                3. Add Sales Data
                4. Update Sales Data
                5. Main Menu
                ''')
            print()
            try : 
                menu_6 = int(input("Enter Menu Option : "))
                print()
                if menu_6 in [1,2,3,4,5] :
                    break
                else :
                    print("Incorrect input, please try again.")
            except :
                print("Incorrect input, please try again.")

        if menu_6 == 1 :
            show_salesData()
            print()

        elif menu_6 == 2 :
            try : 
                sales_month = int(input("Please enter the month code (Jan : 1, Feb : 2, etc) : "))
                show_salesData(sales_month)
            except :
                print("Incorrect input, please try again.")
        
        elif menu_6 == 3 :
            print(f'''\nAdd Sales Data Menu''')
            show_data()
            New_sales_itemCode = int(input("Please input the Item Code : "))
            New_order = SalesData[-1]['Order ID']+1
            
            for i in range(len(InventoryData)) :
                if New_sales_itemCode == InventoryData[i]['Item Code'] :
                    New_sales_item = InventoryData[i]['Item Name']
                    new_priceEach = InventoryData[i]["Selling Price"]
                    break
            
            try : 
                New_quantity = int(input("Please input the quantity : "))
            except :
                print("Incorrect input, please try again.")

            New_orderDate = datetime.datetime.now()

            SalesData.append(
                {'Order ID' : New_order, 
                    'Item Name' : New_sales_item, 
                    'Quantity Ordered' : New_quantity, 
                    'Price Each' : new_priceEach,
                    'Order Date' : New_orderDate.strftime("%d %b %Y"),
                    'Month' : int(New_orderDate.strftime("%m"))}
            )

        elif menu_6 == 4 :
            answer_update = True
            while answer_update : 
                salescode_update = int(input("Please input the item code to be updated : "))
                for i in len(InventoryData) :
                    if salescode_update == InventoryData[i]['Item Code'] :
                        print(f"The detail sales data of the Item {salescode_update} : ")
                        print(f"{SalesData[i]['Order ID']}\t|{SalesData[i]['Item Name']}\t|{SalesData[i]['Quantity Ordered']}\t|{SalesData[i]['Price Each']}\t|{SalesData[i]['Order Date']}\t|{SalesData[i]['Month']}\t|")
                        
                        answer2 = True
                        while answer2 :
                            resp2 = str(input(f"Do you want to update the item with the code of {salescode_update}? (Yes / No) : "))

                            if resp2.lower() == 'yes' :
                                print('''Choose the column to be updated : 
                                    1. Item Name
                                    2. Type
                                    3. Condition
                                    4. Buying Price
                                    5. Selling Price
                                    6. Initial Stock
                                    ''')
                                column_update = int(input("Please choose the column : "))
                                if column_update == 1 :
                                    update_name = input("Please insert the updated Item Name : ")
                                    InventoryData[i]["Item Name"] = update_name.title()

                                elif column_update == 2 :
                                    update_type = input("Please insert the updated Item Type : ")
                                    InventoryData[i]["Type"] = update_type.title()

                                elif column_update == 3 :
                                    update_condition = input("Please insert the updated Item Condition : (Good / Bad)")
                                    InventoryData[i]["Condition"] = update_condition.title()

                                elif column_update == 4 :
                                    try :
                                        update_bPrice = int(input("Please insert the updated Buying Pricee : "))
                                        InventoryData[i]["Buying Price"] = update_bPrice
                                    except :
                                        print("Incorrect input, please try again.")

                                elif column_update == 5 :
                                    try :
                                        update_sPrice = int(input("Please insert the updated Selling Price : "))
                                        InventoryData[i]["Selling Price"] = update_sPrice
                                    except :
                                        print("Incorrect input, please try again.")

                                elif column_update == 6 :
                                    try :
                                        update_stock = int(input("Please insert the updated Stock : "))
                                        InventoryData[i]["Initial Stock"] = update_stock.title()
                                    except :
                                        print("Incorrect input, please try again.")

                                else : 
                                    print(f"Incorrect input, please try again.\n")
                                
                                resp = str(input("Do you want to update another column? (Yes / No) : "))

                                if resp.lower() == 'yes' :
                                    continue
                                elif resp.lower() == 'no' :
                                    answer2 == False
                                    break
                            
                            elif resp2.lower() ==  'no' :
                                break
                        
                        answer_update = False
                        break
                    
                    else :
                        print("Incorrect item code, please try again.")

        elif menu_6 == 5 :
            menu6_conf = False
            main_menu()

 
main_menu() #Run the program