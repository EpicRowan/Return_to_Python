company = "Petsmart"
store = [101, 102, 103]
template = "{company} is the {store}"

for i in range(len(store)):
    print(template).format(company=company, store=store[i])
