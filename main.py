print("Python final project")

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print(f"'{self.title}' {self.author} ({self.year})")


class BookManager:
    def __init__(self):
        self.books = []
    # წიგნის დამატება
    def add_book(self):
        print("\nდაამტეთ წიგნი")
        while True:
            try:
                title = input("შეიყვანეთ სათაური: ").strip()
                author = input("შეიყვანეთ ავტორის სახელი და გვარი: ").strip()

                if not title or not author:
                    print("სათაური და ავტორი სახელი და გვარი ცარიელი არ უნდა იყოს\n")
                    continue
                year = input("შეიყვანეთ გამოცემის წელი: ").strip()
                year = int(year)


                # წიგნის დამატება
                new_book = Book(title, author, year)
                self.books.append(new_book)
                print(f"\nწიგნი '{title}' დაემატა სიაში!")
                break

            except ValueError:
                print("\nError: გთხოვთ შეიყვანოთ მხოლოდ ციფრი\n")
            except Exception as e:
                print(f"\nAn unexpected error occurred: {e}\n")
                break


    # დამატებული წიგნების სია
    def display_book_list(self):
        print("\nწიგნების სია:")
        if not self.books:
            print("წიგნების სია ცარიელია.")
            return

        for index, value in enumerate(self.books, 1):
            print(f"{index}. ", end="")
            value.display()




    # სათაურით ძებნა
    def search_books_by_title(self):
        book_title = input("\nშეიყვანეთ სათაური: ").lower().strip()
        founded_books = []

        for book in self.books:
            if book_title in book.title.lower():
                founded_books.append(book)

        if not founded_books:
            print("ამ სათაურით წიგნი არ მოიძებნება. \n სცადეთ ახლიდან.")
            return

        print("\nძიების რეზულტატი:")
        for value in founded_books:
            value.display()


# მომხმარებლის ინტერფეისი
def main():
    print("კეთილი იყო თქვენი მობრძანება ჩვენს ვებსაიტში")
    manager = BookManager()

    while True:
        print("\nმენიუ:")
        print("1. წიგნის დასამატებლად გთხოვთ აირჩიოთ 1-იანი")
        print("2. წიგნების სანახავად გთხოვთ აირჩიოთ 2-იანი")
        print("3. წიგნის მისაძებნად გთოვთ აირჩიოთ 3-იანი")
        print("4. გამოსასვლელად გთხოვთ აირჩიოთ 4-იანი")

        choice = input("აირჩიეთ ციფრი (1-4): ")

        if choice == "1":
            manager.add_book()
        elif choice == "2":
            manager.display_book_list()
        elif choice == "3":
            manager.search_books_by_title()
        elif choice == "4":
            print("\nმადლობას გიხდით ჩვენი საიტით სარგებლობისათვის!")
            break
        else:
            print("გთხოვთ აირჩიოთ ციფრი მხოლოდ 1-4.")


main()

