from input import*
from read_write_file import*
def implement(val):
    #Taking data from the text file
    Vax_Old_Data = Download_Data(True)
    Non_Vax_Old_Data = Download_Data(False)

    #Making a New List
    Vax_Data_List = linked_list()
    Non_Vax_Data_List = linked_list()

    #Inserting Data from file to List
    for D in Vax_Old_Data:
        #Removing extra characters from the string
        D = D.replace("[","")
        D = D.replace("]","")
        D = D.replace("'","")
        Vax_Data_List.insert(D.split(","))

    #Inserting Data from file to List
    for D in Non_Vax_Old_Data:
        #Removing extra characters from the string
        D = D.replace("[","")
        D = D.replace("]","")
        D = D.replace("'","")
        Non_Vax_Data_List.insert(D.split(","))

    #print List
    #Data_List.print()

    #Take the Student's Information
    Information = val
    vax_status = Information[5]
    # #Insert new Information to Text file
    Update_Data(str(Information), vax_status)

    #Insert Information to List
    Vax_Data_List.insert(Information)
    Non_Vax_Data_List.insert(Information)