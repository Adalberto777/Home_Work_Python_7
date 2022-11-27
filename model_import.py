def read_import_text(filename: str) -> list:
    with open(filename, "r", encoding = "utf-8") as file:
        for line in file:
            print(line)

            
#         text_for_work = list(data.read())       
#         return text_for_work
        

# def unzip_file(zipText: str) -> str:
#     unzip_text =''

#     for i in range(0, len(zipText), 2):
#            unzip_text = unzip_text + (zipText[i + 1] * int(zipText[i]))
#     return unzip_text


# sourse_text = read_source_text('source_text_task_3.txt')
# sourse_text_1 = ''.join(read_source_text('source_text_task_3.txt'))
# zip_text=zip_file(sourse_text)
# unzip_text = unzip_file(zip_text)

# with open(r"D:\test.txt", "r") as file:
#     for line in file:
#         print(line)