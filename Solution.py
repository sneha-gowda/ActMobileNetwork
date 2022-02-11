import json
 
# Opening JSON file
f = open('data.json')
#loading data
data = json.load(f)
# Closing file
f.close()

#Contiries sale detailes
countries={}
productsList=[]
for i in data["sales"]:
    if(i["country"] in countries):
        products=countries[i["country"]]
        if(i["prod"] not in productsList):
            productsList.append(i["prod"])
        if(i["prod"] in products):
            details=products[i["prod"]]
            details["count"]+=1
            details["price"]+=i["price"]
            products[i["prod"]]=details
        else:
            products[i["prod"]]={"count":1,"price":i["price"]}
        countries[i["country"]]=products
    else:
        countries[i["country"]]={i["prod"]:{"count":1,"price":i["price"]}}

def findCountry(prod):
    maximumSale=float("-inf")
    result=""
    Revenue=0
    for i in countries:
        countrySaleDetail=countries[i]
        if(prod in countrySaleDetail):
            if(maximumSale<countrySaleDetail[prod]["count"]):
                maximumSale=countrySaleDetail[prod]["count"]
                Revenue=countrySaleDetail[prod]["price"]
                result=i
            elif(maximumSale==countrySaleDetail[prod]["count"]and Revenue<countrySaleDetail[prod]["price"]):
                Revenue=countrySaleDetail[prod]["price"]
                result=i
    print("************************")
    print("The country with maximum total sales for product",productInput,"is:-")
    print(result)
    print("Total number of items sold: ",maximumSale)
    print("Total revenue: ",Revenue)
    print("************************")
    return

#Taking user input
productInput=input("Please provide product name ")
if(productInput not in productsList):
    print("This product is not registered in database")
else:
    findCountry(productInput)
    