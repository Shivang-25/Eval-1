



def addContact(contacts):
    name = input("Enter Name: ")
    ph = input("Enter Phone no. : ")
    email = input("Enter email : ")
    
    info = {"name": name, "Phone no.": ph, "E-mail" : email}
    contacts.append(info)
    return contacts


def updateContact(contacts, name):
    ph = input("Enter New Phone no. :")
    email = input("Enter email: ")
    
    for i in contacts:
        if i['name'] == name:
            i["Phone No."] = ph
            i["E=mail"] = email
            
    
    return contacts


def deleteContact(contacts, name):
    
    for i in contacts:
        if i['name'] == name:
            contacts.remove(i)
            
    return contacts




def searchContact(contacts):
    ch = input("1 - Search by name\n2 - Search by email");
    if ch == 1:
        n = input("Enter name")
        for i in contacts:
            if i['name'] == n:
                print(i)
                
    elif ch == 2:
        n = input("Enter E-mail:")
        for i in contacts:
            if i['E-mail'] == n:
                print(i)
    
    else:
        print("Invalid Choice")
    
            


def displayAll(contacts):
    
    for i in contacts:
        for key,val in i.items():
            print(key,":",val)

            

def searchByletter(contacts):
    let = input("Enter letter: ")
    
    for i in contacts:
        if i["name"][0] == let:
            print(i)
            

def main():
    name = "Shivang"
    phone = 86754323
    email = ""

    contacts = []
    details = {"name": name, "Phone no." : phone, "E-mail" : email}

    contacts.append(details)
    print(contacts)
    
    print("1 - Add Contact")
    print("2 - Update a Contact")
    print("3 - Delete a Contact")
    print("4 - List all contact")
    print(" ...")
    
    ch = input("Enter choice")
    
    if ch == 1:
        addContact(contacts)
    elif ch == 2:
        n = input("Enter name:")
        updateContact(contacts,n)
    elif ch == 3:
        n = input("Enter name:")
        deleteContact(contacts,n)
    elif ch == 4:
        

main()