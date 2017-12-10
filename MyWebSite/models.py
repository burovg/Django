def CalcAvg(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum / len(arr)

def GetPersonGreet(m, y):
    return "Hello person : Month " + m + " , Year : " + y


products  = [{ 'ProductID' : '1', 'Name' : 'Computer', 'Price' : '100$', 'Exist' : True},
             {'ProductID': '2', 'Name': 'Screen', 'Price': '200$', 'Exist': True},
             {'ProductID': '3', 'Name': 'Mouse', 'Price': '300$', 'Exist': True}]



def GetProduct(id):
    return filter(lambda p : p['ProductID'] == id, products)

def GetProducts():
    return products