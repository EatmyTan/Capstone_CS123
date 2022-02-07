def Download_Data(Vaxxed:str):
    if Vaxxed == "Yes":
        with open('Vaccinated.txt', "r") as reader:
            data = reader.readlines()
        return data
    else:
        with open('Non_Vaccinated.txt', "r") as reader:
            data = reader.readlines()
        return data

def Update_Data(DATA, vax_status):
    if vax_status == "Yes":
        with open('Vaccinated.txt', "a") as reader:
            reader.writelines(DATA)
            reader.write("\n")
    elif vax_status == "No":
        with open('Non_Vaccinated.txt', "a") as reader:
            reader.writelines(DATA)
            reader.write("\n")
    else:
        pass