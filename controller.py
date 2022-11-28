import view
import model_new_phone
import model_import_export
import model_export_csv


def getMenuItem() -> str:
    result_menu = view.menu()
    if result_menu == '1':        
        model_new_phone.writeToFile(view.getSurname(), view.getName(), view.getTel(), view.getDescription(), 'phone_book.txt')
    elif result_menu == '2': 
        model_import_export.writeImportText(model_import_export.readImportText('new_phone_book.txt'), 'phone_book.txt')
        print('Export data from new_phone_book.txt to phone_book')        
    elif result_menu == '3': 
        model_import_export.writeImportText(model_import_export.readImportText('phone_book.txt'), 'export_phone_book.txt')
        print('Export data from phonebook to export_phone_book.txt') 
    elif result_menu == '4': 
        model_export_csv.createNewData(model_export_csv.readImportText('phone_book.txt'))
        print('Export data from phonebook to phone_book.csv') 
    elif result_menu == '5': 
        print("в разработке")
        getMenuItem()
    elif result_menu == '6': 
        print("Good Bye!")        
    else: 
        print("введен несуществующий пункт, выберите пункт меню от 1 до 5")
        getMenuItem()  

