def menu() -> str:
    print("MAIN MENU: \n"
            "1 - New records\n"
            "2 - Import as file\n"
            "3 - Export in csv\n"
            "4 - Export in xml")
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
    






