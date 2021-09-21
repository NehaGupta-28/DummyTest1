import shelve

with shelve.open("bike") as bike:
    bike["make"] = "honda"
    bike["model"] = "250 dream"
    bike["colour"] = "red"
    bike["engin_size"] = 250
    # bike["engine_size"] = 250 , this was added first then we purposefully made a typo
    del bike["engin_size"]
    for key in bike:
        print(key)
    print("="*40)

    print(bike["engine_size"])
    #print(bike["engin_size"])
    print(bike["colour"])
