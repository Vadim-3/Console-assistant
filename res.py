from address_book import AddressBook as ab
from pathlib import Path

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
        break
        
                
    if ff == '1':
        pass
    
    if ff == '1':
        pass
    
    if ff == '1':
        pass