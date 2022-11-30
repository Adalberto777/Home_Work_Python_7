def readImportText(donor: str) -> str:
    with open(donor, "r", encoding = "utf-8") as file_data_donor:
        data = file_data_donor.read()
        data = ','.join(filter(lambda x: ' ' not in x, data.split()))
        data = data.split(",")
    return data


def writeImportText(data, recipient: str) -> None:
    with open(recipient, "a", encoding = "utf-8") as file_data_recipient:
        file_data_recipient.write(f'{data}\n') 


def createNewData(data: list) -> None:
    for i in range(0, len(readImportText('phone_book.txt')) - 3, 4):
        count = i
        my_str = ''
        my_str += data[count] + ','
        my_str += data[count + 1] + ','
        my_str += data[count + 2] + ','
        my_str += data[count + 3] 
        writeImportText(my_str, 'phone_book.csv')   