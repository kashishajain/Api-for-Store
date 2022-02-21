import json
import datetime
from tabulate import tabulate
import operator


def calculateTotal(j):

    totalbill=0  #to store total bill
    items_list=[['Item','Item Category','Price','Quantity','Total Price','Total Tax']]  #list to store item details
    bill_str="" #string to store Total amount payable

    required_keys=["itemCategory","item","quantity","price"] #required keys for input

    #calculating final price and applicable tax for each item
    for i in range (0,len(j)):

        all_keys_exist=0

    #checking if input has all the required keys
        for key in required_keys:
            if key in j[i].keys():
                all_keys_exist=1
            else:
                all_keys_exist=0
                break

        if all_keys_exist:

            if j[i]['itemCategory'] == "Medicine" or j[i]['itemCategory'] == "Food":
                quantity=j[i]['quantity']
                price=j[i]['price']
                finalprice=quantity*price
                tax=5
                totaltax=(finalprice*tax)/100
                totalbill+=finalprice+totaltax

            elif j[i]['itemCategory'] == "Clothes" :
                quantity=j[i]['quantity']
                price=j[i]['price']
                finalprice=quantity*price
                if finalprice > 1000:
                    tax=12
                else:
                    tax=5
                totaltax=(finalprice*tax)/100
                totalbill+=finalprice+totaltax

            elif j[i]['itemCategory'] == "Music" :
                quantity=j[i]['quantity']
                price=j[i]['price']
                finalprice=quantity*price
                tax=3
                totaltax=(finalprice*tax)/100
                totalbill+=finalprice+totaltax

            elif j[i]['itemCategory'] == "Imported" :
                quantity=j[i]['quantity']
                price=j[i]['price']
                finalprice=quantity*price
                tax=18
                totaltax=(finalprice*tax)/100
                totalbill+=finalprice+totaltax

            elif j[i]['itemCategory'] == "Book" :
                quantity=j[i]['quantity']
                price=j[i]['price']
                finalprice=quantity*price
                tax=0
                totaltax=(finalprice*tax)/100
                totalbill+=finalprice+totaltax

            #adding item details to the list
            items_list.append([j[i]['item'],j[i]['itemCategory'],price,quantity,finalprice,totaltax])

        else:
            print("\nRequired key is missing in input"+str(j[i]))

    #calculating discount on total bill
    if totalbill>2000:
        discount=5
        bill_str=bill_str+"\nTotal Amount: "+str(totalbill)+"\nYou have got additional 5% discount\n"
        totalbill-=(totalbill*discount)/100
        bill_str=bill_str+"Total amount payable: "+str(totalbill)
    else:
        bill_str=bill_str+"\nTotal amount payable: "+str(totalbill)

    return items_list,bill_str


def createbill():
    #taking user input
    items=input()

    #coverting user input to json
    items_json=json.loads(items)

    #sorting json data based on item to print bill in ascending order of the commodity names
    items_json.sort(key=operator.itemgetter('item'))

    #calling calculateTotal to get list of items with their respective details and total amount
    items_list,totalamount=calculateTotal(items_json)

    #Printing bill in required format
    s="\nReceipt\n"+"Date and Time: "+str(datetime.datetime.now())+"\n"
    print(s,tabulate(items_list),totalamount)

createbill()