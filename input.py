def menu():  #collects input from user
    #Enter The whole inputs to a loop for it to repeat if user has an error in input
    while(True):
        #Enter the whole inputs into a try/except to catch errors and let the program continue instead of execute
        try:
            print("===========================================")
            id = input("Student ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            college = input("College: ")
            location = input("Location: ")
            vaccine_status = input("Are you vaccinated: Yes or No? ")
            if vaccine_status == "Yes":
                dosage = int(input("Number of vaccine shots taken: "))
                vaccine_type = input("Name of Vaccine: ")
            else:
                dosage = None 
                vaccine_type = None
            print("===========================================")
            val = [id, name, age, college, location, vaccine_status, dosage, vaccine_type]
            #once ALL inputs are valid exit loop
            break
        except:
            print("===========================================")
            print("Wrong Input: Try Again")
    #return the array of inputs
    return val
        

class list_node:
    def __init__(self, val, next=None):
        self.id = val[0]
        self.name = val[1]
        self.age = val[2]
        self.college = val[3]
        self.location = val[4]
        self.vaccine_status = val[5]
        self.dosage = val[6]
        self.vaccine_type = val[7]
        self.next = next

class linked_list():
    def __init__(self, head=None):
        self.head = head

    def insert(self, val):
        node = list_node(val)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while True: #traverses linked list
                if current_node.next is None:
                    current_node.next = node
                    break
                current_node = current_node.next
    
    def print(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.id, end=" ")
            print(current_node.name, end=" ")
            print(current_node.age, end=" ")
            print(current_node.college, end=" ")
            print(current_node.location, end=" ")
            print(current_node.vaccine_status, end=" ")
            print(current_node.dosage, end=" ")
            print(current_node.vaccine_type, end=" ")
            print()
            current_node = current_node.next


            

