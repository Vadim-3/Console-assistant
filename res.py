from address_book import AddressBook
from sort_folder import FileSorter
from pathlib import Path

ab = AddressBook()
while True:
    ff = input('Введіть команду: ')
    if ff == '1':
        if Path(ab.filename).exists():
            ab.unpackaging()
            
        while True:
            command = input('введіть команду ')

            if command == 'add':
                name = input("введіть ім'я ")
                address = input('Введіть адресу ')
                email = input("введіть email ")
                number = input("введіть number ")
                birthday = input('Введіть введіть дату народження ')
                ab.add_contact(name, address, email, number, birthday)
                
            if command == 'exit':
                ab.packaging()
                break
            
    if ff == 'exit':
        print('Good Bye!')
        break
        
                
    if ff == '2':
        pass
    
    if ff == '3':
        while True:
            path = input('Введіть шлях до папки: ')
            
            if path == 'exit':
                break 
            
            if path:
                folder = Path(path)
                file_sorter = FileSorter(folder)
                file_sorter.sort_files()
            
            else:
                print('Введіть шлях допапки: ')
            

    if ff == '4':
        pass