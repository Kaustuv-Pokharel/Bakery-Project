import pandas as pd
from datetime import datetime

print("Welcome to 69 Bakery")
enter=int(input("Do you want to store(0)/access(1)/delete(2) data?"))
orderid=1000


def store():
    df=pd.read_excel('BakeryProject.xlsx')
    name = input("Enter the name of the customer")
    order = input("Enter the order of the customer")
    date = input("Enter the date of the order(YYYY-MM-DD)")
    month = int(date[5:7])
    day = int(date[8:])
    if len(date) < 8 or month > 12 or day > 31:
        print("Enter valid date")
    else:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        date = pd.to_datetime(date)


        n = len(df)
        df.loc[n, 'name'] = name
        df.loc[n, 'order'] = order
        df.loc[n, 'date'] = date
        df.loc[n, 'order id'] = orderid + len(df) + 1
        df.to_excel('BakeryProject.xlsx', index=False)


def access():
    df=pd.read_excel('BakeryProject.xlsx')
    id_number=int(input("Enter the order id"))
    new_df=df['order id'].tolist()
    if id_number in new_df:
        for n in df.index:
            if df.loc[n, 'order id'] == id_number:
                print(df.loc[n])
            else:
                n = n + 1
    if id_number not in new_df:
        print("No order with the id", id_number,"found!")

def delete():
    df=pd.read_excel('BakeryProject.xlsx')
    id_number=int(input("Enter the order id which you want to delete"))
    new_df=df['order id'].to_list()
    if id_number in new_df:
        for n in df.index:
            if df.loc[n,'order id']==id_number:
                index=n
                df.drop(index,inplace=True)
                df.to_excel('BakeryProject.xlsx', index=False)
            else:
                n=n+1
            

    if id_number not in new_df:
        print(f"No data with order id {id_number} found!")




if enter==0:
    store()
    print('Data was sucessfully saved!')

if enter==1:
    access()

if enter==2:
    delete()
    print("Data deleted sucessfully!")
