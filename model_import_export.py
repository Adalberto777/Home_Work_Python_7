def readImportText(donor: str) -> str:
    with open(donor, "r", encoding = "utf-8") as file_data_donor:
        data = file_data_donor.read()
    return data


def writeImportText(data, recipient: str) -> None:
    with open(recipient, "a", encoding = "utf-8") as file_data_recipient:
        file_data_recipient.write(data)  
