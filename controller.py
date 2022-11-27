import view
import model_new_phone


def getMenuItem() -> str:
    result_menu = view.menu()
    if result_menu == '1':        
        model_new_phone.writeToFile(view.getSurname(), view.getName(), view.getTel(), view.getDescription(), 'phone_book.txt')

    elif result_menu == '2': 
        print("в разработке")
        getMenuItem()
    elif result_menu == '3': 
        print("в разработке")
        getMenuItem()
    elif result_menu == '4': 
        print("в разработке")
        getMenuItem()
    elif result_menu == '5': 
        print("в разработке")
        getMenuItem()
    else: 
        print("введен несуществующий пункт, выберите пункт меню от 1 до 5")
        getMenuItem()  

