# Skapar en klass NoteManager för att hantera anteckningar
class NoteManager:
    # Konstruktormetod som initierar klassen med anteckningarna som jag skapat själv
    def __init__(self):
        # Dictionary för att lagra anteckningar med titlar och texter
        self.notes = {
            'Meddelande från laget': 'Ändrad match tid på lördag',
            'Kom ihåg': 'Städa bilen',
            'Inlämningsuppgift': 'Gör klart programmet och lyssna på föreläsningen',
        }

    # Metod för att visa alla befintliga anteckningar
    def view_notes(self):
        for title, text in self.notes.items():
            print(f'{title}: {text}')

    # Huvudmeny som låter användaren välja olika åtgärder
    def menu(self):
        while True:
            # Presenterar meny alternativ för användaren
            print(17 * '-')
            print('View | view note')
            print('Add  | add note')
            print('RM   | remove note')
            print('Exit | exit program')
            print(17 * '-')

            # Användaren får välja vad den vill göra
            choice = input('Menu >  ').lower()

            # Gör vad användaren har skrivit in vad den vill göra och om man inte har skrivit in något får man göra om
            if choice == 'view':
                self.view_notes()
            elif choice == 'add':
                self.add_note()
            elif choice == 'rm':
                # Användaren får ange titeln på anteckningen de vill ta bort
                success = self.remove_note(input('Ange titel på den anteckning du vill ta bort: '))
                # Meddelar användaren om det gick att ta bort anteckningen eller ej
                if success:
                    print('Anteckningen togs bort')
                else:
                    print('Anteckningen finns inte')
            elif choice == 'exit':
                # Avslutar programmet om användaren väljer att avsluta
                break
            else:
                print('Ogiltligt svar, försök igen')

    # Metod för att lägga till en ny anteckning
    def add_note(self):
        title = input('Ange titel för din anteckning: ')
        text = input('Ange text för din anteckning: ')
        # Lägger till den nya anteckningen i dictionaryn
        self.notes[title] = text

    # Metod för att ta bort en anteckningen som användaren skriver titeln av
    def remove_note(self, title):
        # Ändrar så att allt blir till småbokstäver så vi inte får problem med att man måste skriva exakt som det står för att ta bort en note
        title_lower = title.lower()
        # Hittar alla titlar som matchar den inmatade titeln (oasvett stor/litenbokstav)
        found_titles = [t for t in self.notes if t.lower() == title_lower]

        # Om matchande titlar hittades
        if found_titles:
            # Loopar genom alla matchande titlar och tar bort dem från dictionaryn
            for found_title in found_titles:
                del self.notes[found_title]
            return True  # Visar att borttagningen var framgångsrik
        else:
            return False  # Visar att ingen matchande anteckning hittades


# Skapar en instans av NoteManager och kallar på huvudmenyn för att starta programmet
note_manager = NoteManager()
note_manager.menu()

