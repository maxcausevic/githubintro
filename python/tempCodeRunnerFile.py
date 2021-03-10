dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    print(sum,"locations")
    for key, val in some_dict.items():
        print(len(val), key)
        for i in range(0,len(val)):
            print(val[i])

printInfo(dojo)