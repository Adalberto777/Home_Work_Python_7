def writeToFile(surmname: str, name: str, tel: str, description: str, file_name: str) -> None:
    with open(file_name, mode="a", encoding="utf-8") as file:
        file.write(f'{surmname}\n\n')
        file.write(f'{name}\n\n')
        file.write(f'{tel}\n\n')
        file.write(f'{description}\n\n')


# def createNewData(surmname: str, name: str, tel: str, description: str) -> list:
#     my_list = []
#     my_list.append(surmname)
#     my_list.append(name)
#     my_list.append(tel)
#     my_list.append(description)
#     return my_list