from address_book import AddressBook
from sort_folder import FileSorter
from pathlib import Path
from notess import Note, Notebook

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
        notebook = Notebook()
        if Path(ab.filename).exists():
            notebook.load_notes("notes.json")
        while True:
            commandd = input('введіть команду: ')
            
            if commandd == 'exit':
                notebook.save_notes("notes.json")
                break
            
            if commandd == 'add':
                title = input()
                text = input()
                tags = input()
                new_note = Note(title, text, tags)
                notebook.add_note(new_note)
                
            if commandd == 'search':
                sh_words = input('введіть нотатку яку потрібно знайти: ')
                results = notebook.search_notes(sh_words)
                for note in results:
                    print(note.title)
                    
            if commandd == 'edit':
                note_ed = input('введіть нотатку яку потрібно змінити: ')
                new_title = input('')
                new_text = input('')
                founded_note = notebook.search_notes(note_ed)
                if notebook.edit_note(founded_note, new_title, new_text):
                    print("Нотатку було успішно відредаговано")
                else:
                    print("Нотатку з такою назвою не знайдено")
                    
            if command == 'show all':
                for note in notebook.notes:
                    print(note.title, "-", note.text)
                    
            if commandd == 'search by tags':
                results = notebook.search_notes_by_tags(["план"])
                for note in results:
                    print(note.title)
            
            if commandd == 'sort':
                notebook.sort_notes_by_tags()
            
            
    
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
                print('Введіть шлях до папки: ')
            

    if ff == '4':
        pass