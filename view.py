def menu() -> str:
    print("MAIN MENU: \n"
            "1 - New records\n"
            "2 - Import from file to phonebook\n"
            "3 - Export from phonebook to file\n"
            "4 - Export in csv\n"
            "5 - Export in xml\n"
            "6 - Exit")
    result = input('Select a menu item: ')
    return result


def getSurname() -> str:
    data = input('Enter surname: ')
    return data


def getName() -> str:
    data = input('Enter name: ')
    return data


def getTel() -> str:
    data = input('Enter tel: ')
    return data


def getDescription() -> str:   
    data = input('Enter description: ')
    return data
    






