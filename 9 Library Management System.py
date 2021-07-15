# First of all I will define the menu with all choices
menu = "\nLibrary Management System\n" \
       "==============================\n" \
       "1. Print books info\n" \
       "2. Search for a book\n" \
       "3. Add new book\n" \
       "4. Remove a book\n" \
       "5. Borrow a book\n" \
       "6. Return a book\n" \
       "7. Buy a book from the Library\n" \
       "8. Format The Library Info\n" \
       "9. Exit\n" \
       "=============================="


# define a function that will add the money after sell
def bankAccount(price):
    # Open the file
    bankaccount = open("BankAccount.txt", "a+")
    bankaccount.seek(0)
    # read info
    bank_account = bankaccount.readline()
    # add the money to the account
    bank_account = str(float(bank_account) + float(price))
    # remove the old total and add the new one
    bankaccount.close()
    bankaccount = open("BankAccount.txt", "w+")
    bankaccount.write(bank_account)
    bankaccount.close()


# do the user's order
# number 1
def print_books_info():
    # open the files that we will use
    booksInfo = open("booksInfo.txt", "a+")
    booksInfo.seek(0)
    # store all info inside this value
    books_info = booksInfo.readlines()
    # this choice is about display the info of the book

    # count the number of books and print it
    number_of_books = len(books_info)
    print("\nTotal %d books:" % number_of_books,
          "\n##############################################")
    # read the list as save each info
    counter = 0
    for book in books_info:
        counter += 1
        if book != "\n":
            book = book.split(",")
            serial_number = book[0]
            print("serial#: ", serial_number)
            title = book[1]
            print("title: ", title)
            number_of_authors = book[2].count(":") + 1
            print("number of authors: ", number_of_authors)
            price = book[3]
            print("price: ", price)
            total_copies = int(book[4]) + int(book[5])
            print("total copies: ", total_copies)
            if counter != number_of_books:
                print("##############################################\n")
    booksInfo.close()
    # return True to let the while running
    return True


# number 2
def search_for_book():
    # open the files that we will use
    booksInfo = open("booksInfo.txt", "a+")
    booksInfo.seek(0)
    # store all info inside this value
    books_info = booksInfo.readlines()

    # This choice is about search for a book and display all info about it
    # ask the user which method will be used
    method_search = input("Enter (t) to search by title or (a) to search by author name:").lower()

    # first method
    if method_search == "t":
        # if user put t that mean title method is running
        # ask for the title or part of it
        search_title = input("Enter the title: ").lower()
        # check each book and try to find a mach
        # make a counter and check to know when to print not found
        counter = 0
        check = 0
        for book in books_info:
            # add 1 to counter
            counter += 1
            # take the title for each book and see
            title = book.split(",")
            title = title[1].lower()
            if search_title in title:
                check = 1
                # if the book is found print the info of book
                search_result = book.split(",")
                print("\nMatched records:")
                print("serial#: ", search_result[0],
                      "\n title: ", search_result[1])
                print("authors: ")
                # about the author we will see home many one do we have than print each one separated
                if ":" in search_result[2]:
                    author = search_result[2].split(":")
                    for name in author:
                        print("   -", name)
                else:
                    print("  -", search_result[2])
                print("price: ", search_result[3],
                      "\ncopies in library:", search_result[4],
                      "\nborrowed copies: ", search_result[5],
                      "#########################################\n")
            elif (counter == len(books_info)) and (check == 0):
                print("No matched record found")
    # second method
    elif method_search == "a":
        # if user put a that mean title method is running
        # ask for the author name or part of it
        search_author_name = input("Enter the author name: ").lower()
        # check each book and try to find a mach
        counter = 0
        check = 0
        for book in books_info:
            counter += 1
            # take the author name for each book and see
            author_name = book.split(",")
            author_name = author_name[2].lower()
            if search_author_name in author_name:
                check = 1
                # if the book is found print the info of book
                search_result = book.split(",")
                print("Matched records:")
                print("serial#: ", search_result[0],
                      "\n title: ", search_result[1])
                print("authors: ")
                # about the author we will see home many one do we have than print each one separated
                if ":" in search_result[2]:
                    author = search_result[2].split(":")
                    for name in author:
                        print("   -", name)
                else:
                    print("  -", search_result[2])
                print("price: ", search_result[3],
                      "\ncopies in library:", search_result[4],
                      "\nborrowed copies: ", search_result[5],
                      "#########################################\n")
            elif (counter == len(books_info)) and (check == 0):
                print("No matched record found")
    else:
        print("Invalid input")
    booksInfo.close()
    # return True to let the while running
    return True


# number 3
def add_new_book():
    # open the files that we will use
    booksInfo = open("booksInfo.txt", "a+")
    booksInfo.seek(0)
    # store all info inside this value
    books_info = booksInfo.readlines()

    # This choice will allow you to add a new book
    # ask for a serial number
    serial_number = input("Enter serial number made from 5 digit: ")
    # ask for the title of the book
    title = input("Enter book title: ")
    # ask for author name or names and set a counter
    author = ""
    counter = 1
    author_names = ""
    # check6 is one of the check steps
    check6 = False
    while author != "q" and author != "Q":
        author = input("Enter name of author %d or q to stop:" % counter)
        # if user put q it will stop here
        if author == "q" or author == "Q":
            break
        # check if it is a space
        if author == "" or author.isspace():
            check6 = True
        # make the correct format
        if counter > 1:
            author_names += ":" + author
        else:
            author_names = author
        counter += 1
    # ask for the price
    price = input("Enter book price: ")
    # ask for the number of books
    number_of_books = input("Enter number of book copies: ")
    print()

    # make a value call check to see where is the problems
    check = True
    # check serial number
    # [1] is check for number of digit
    if len(serial_number) != 5:
        print("Error: serial number must be 5 digit")
        check = False
    # [2] is check is digit
    elif not serial_number.isdigit():
        print("Error: serial number must be only digit")
        check = False
    # [3] check repeated
    else:
        for book in books_info:
            book = book.split(",")
            book = book[0]
            if serial_number in book:
                print("Error: serial number is already used")
                check = False

    # check the title
    # [4] check empty title
    if title == "" or title.isspace():
        print("Error: Title should not be empty")
        check = False

    # check author
    # [5] no author
    if len(author_names) < 1:
        print("Error: you must put at lest 1 author name")
        check = False
    # [6] check one of the author name is empty
    if check6:
        print("Error: names of all authors should not be empty")
        check = False

    # check the price
    # [7] check if the price is digit
    price1 = price.replace(".", "")
    if not price1.isdigit():
        print("Error: price should be a valid float number")
        check = False

    # [8] check the number of copies
    if (not number_of_books.isdigit()) or (int(number_of_books) <= 0):
        print("Error: number of copies should be a valid int number")
        check = False
    # print if every things are OK or not
    if check:
        new_book = "\n" + serial_number + "," + title + "," + author_names + "," + price + "," + number_of_books + "," + "0"
        booksInfo.write(new_book)
        booksInfo.seek(0)
        books_info = booksInfo.readlines()
        print("New book was added successfully")
    else:
        print("New book was not added successfully")
    booksInfo.close()
    # return True to let the while running
    return True


# number 4
def remove_book():
    # open the files that we will use
    booksInfo = open("booksInfo.txt", "a+")
    booksInfo.seek(0)
    # store all info inside this value
    books_info = booksInfo.readlines()

    # this choice for remove a book from the file
    # first of all the user must enter the serial number for the book
    serial_number = input("Enter book serial number to remove: ")
    # check if the book is exist and print it
    for book in books_info:
        book = book.split(",")
        if serial_number == book[0]:
            # if the book is found so print the info of book
            print("serial#: ", serial_number)
            title = book[1]
            print("title: ", title)
            print("authors: ")
            # about the author we will see home many one do we have than print each one separated
            if ":" in book[2]:
                author = book[2].split(":")
                for name in author:
                    print("   -", name)
            else:
                print("  -", book[2])
            price = book[3]
            print("price: ", price)
            total_copies = int(book[4]) + int(book[5])
            print("total copies: ", total_copies)
            print("##############################################\n")
            # after that we have to make sure and ask the user if he want to delete the book
            make_sure = input("Deleting the book .. Are you sure (yes/no): ").lower()
            if make_sure == "yes":
                # if there are no books are  borrowed books so Continu
                if int(book[5]) == 0:
                    # open the file for write
                    booksInfo.close()
                    booksInfo = open("booksInfo.txt", "w+")
                    # delete the book that have the same serial number
                    for book1 in books_info:
                        if serial_number in book1:
                            print("Book was removed successfully")
                            pass
                        else:
                            booksInfo.write(book1)
                    # open the file as a+
                    booksInfo.close()
                    booksInfo = open("booksInfo.txt", "a+")
                    booksInfo.seek(0)
                    books_info = booksInfo.readlines()
                else:
                    print("Book cannot be removed: borrowed copies must be 0")
            elif make_sure == "no":
                print("operation is cancelled")
    booksInfo.close()
    # return True to let the while running
    return True


# number 5
def borrow_book():
    # open the files that we will use
    booksInfo = open("booksInfo.txt", "a+")
    booksInfo.seek(0)
    # store all info inside this value
    books_info = booksInfo.readlines()

    borrowedInfo = open("borrowedInfo.txt", "a+")
    borrowedInfo.seek(0)
    # store all info inside this value
    borrowed_info = borrowedInfo.readlines()

    # this part is about borrow a book
    # first take the serial number of the book
    serial_number = input("Enter book serial number to borrow:  ")
    if (serial_number.isdigit()) and (len(serial_number) == 5):
        # check if the book is exist
        check_book = False
        # check each book
        counter_1 = 0
        for book in books_info:
            book = book.split(",")
            if int(serial_number) == int(book[0]):
                # if the serial number is found stop
                check_book = True
                break
            else:
                counter_1 += 1
        # check if the serial number is found and check if there are any copy
        if not check_book:
            print("Error: no matched serial number")
        elif int(book[-2]) <= 0:
            print("Error: no available copies in the library")
        else:
            # if every thing is OK ask for id
            id_number = input("Enter user ID: ")
            # check how many book have been borrow by this id
            counter = 0
            for ID in borrowed_info:
                ID = ID.split(",")
                ID = ID[1]
                if int(id_number) == int(ID):
                    counter += 1
            if counter >= 3:
                print("Error: user cannot borrow more than 3 books")
            else:
                check = True
                for ID in borrowed_info:
                    ID = ID.split(",")
                    if int(ID[0]) == int(serial_number):
                        if int(id_number) == int(ID[1]):
                            check = False
                            print("You can not borrow more than 1 cope for the same book")
                if check:
                    # add the serial number and the id number to the file
                    new_borrow = "\n" + serial_number + "," + id_number
                    borrowed_info.append(new_borrow)
                    borrowedInfo.close()
                    borrowedInfo = open("borrowedInfo.txt", "w+")
                    for line in borrowed_info:
                        borrowedInfo.write(line)
                    # add the borrow book by 1 and minus the number of book by 1
                    book[-1] = str(int(book[-1]) + 1)
                    book[-2] = str(int(book[-2]) - 1)
                    # change the info of the books
                    # change form list into string
                    new_book = ""
                    for info in book:
                        if new_book == "":
                            new_book = info
                        else:
                            new_book += "," + info
                    new_book = new_book + "\n"
                    # change information
                    books_info[counter_1] = new_book
                    # rewrite information
                    booksInfo.close()
                    booksInfo = open("booksInfo.txt", "w+")
                    for line in books_info:
                        if line != "":
                            booksInfo.write(str(line))
                    booksInfo.close()
                    booksInfo = open("booksInfo.txt", "a+")
                    booksInfo.seek(0)
                    books_info = booksInfo.readlines()
                    print("Book was borrowed successfully")

                    borrowedInfo.close()
                    borrowedInfo = open("borrowedInfo.txt", "a+")
                    borrowedInfo.seek(0)
                    borrowed_info = borrowedInfo.readlines()
    else:
        print("Error: serial number should be 5 digits")
    booksInfo.close()
    borrowedInfo.close()
    # return True to let the while running
    return True


# number 6
def return_book():
    # open the files that we will use
    booksInfo = open("booksInfo.txt", "a+")
    booksInfo.seek(0)
    # store all info inside this value
    books_info = booksInfo.readlines()

    # open the files that we will use
    borrowedInfo = open("borrowedInfo.txt", "a+")
    borrowedInfo.seek(0)
    # store all info inside this value
    borrowed_info = borrowedInfo.readlines()

    # this one is about return a borrow book
    # first of all i need to know the serial number of the book
    serial_number = input("Enter book serial number to return: ")
    id_number = input("Enter user ID: ")
    # make sure that the serial number is existing
    check = False  # this is a ticket for pass the processes
    counter = 0
    for borrow in borrowed_info:
        borrow = borrow.split(",")
        if (int(serial_number) == int(borrow[0])) and (int(id_number) == int(borrow[1])):
            # if the book is found change check to true
            check = True
            break
        else:
            counter += 1
    if check:
        # if the borrow in there so delete it
        borrowed_info.pop(counter)
        borrowedInfo.close()
        borrowedInfo = open("borrowedInfo.txt", "w+")
        for line in borrowed_info:
            borrowedInfo.write(str(line))
        borrowedInfo.close()
        borrowedInfo = open("borrowedInfo.txt", "a+")
        borrowedInfo.seek(0)
        borrowed_info = borrowedInfo.readlines()

        # add 1 to the available books and -1 to the borrow books
        counter = 0
        for book in books_info:
            book = book.split(",")
            if int(serial_number) == int(book[0]):
                break
            else:
                counter += 1
        book[-1] = str(int(book[-1]) - 1)
        book[-2] = str(int(book[-2]) + 1)
        new_book = ""
        for info in book:
            if new_book == "":
                new_book = info
            else:
                new_book += "," + info
        new_book = new_book + "\n"
        # change information
        books_info[counter] = new_book
        # rewrite information
        booksInfo.close()
        booksInfo = open("booksInfo.txt", "w+")
        for line in books_info:
            if line != "":
                booksInfo.write(str(line))
        booksInfo.close()
        booksInfo = open("booksInfo.txt", "a+")
        booksInfo.seek(0)
        books_info = booksInfo.readlines()
        print("Book was returned successfully")
    else:
        # if there is no mach print error
        print("Error: no matched record found in borrowedInfo.txt")
    booksInfo.close()
    borrowedInfo.close()
    # return True to let the while running
    return True


# number 7
def buy_book():
    # open the files that we will use
    booksInfo = open("booksInfo.txt", "a+")
    booksInfo.seek(0)
    bookSold = open("booksold.txt", "a+")
    bookSold.seek(0)
    # store all info inside this value
    books_info = booksInfo.readlines()
    book_sold = bookSold.readlines()
    # Take the serial number of the book and check if it is there
    serial_number = int(input("Enter the serial number of the book: "))
    available = False
    counter = 0
    for book in books_info:
        book = book.split(",")
        if serial_number == int(book[0]):
            if int(book[-2]) > 0:
                available = True
                # Print the info of the book
                print("serial#: ", serial_number)
                print("title: ", book[1])
                print("authors: ")
                # about the author we will see home many one do we have than print each one separated
                if ":" in book[2]:
                    author = book[2].split(":")
                    for name in author:
                        print("   -", name)
                else:
                    print("  -", book[2])
                    price = float(book[3])
                print("price: ", price)
                print("number of available copies: ", book[4])
                print("##############################################\n")
                # if there are a copies ask the user for the number of copies that he want
                number_of_sold_book = int(input("Enter the number of copies that you want to take: "))
                # Take the user's ID
                id_number = input("Enter your ID number")  # i don't know why I am taking it but I might use it later
                # Check if there are enough books
                if int(book[-2]) >= number_of_sold_book:
                    # add the money to the bank account
                    bankAccount(price * number_of_sold_book)
                    # if yes write the sold information
                    sold_info = "\n" + str(book[0]) + "," + id_number
                    bookSold.write(sold_info)
                    book[-2] = str(int(book[-2]) - number_of_sold_book)
                    # change the info of the books
                    # change form list into string
                    new_book = ""
                    for info in book:
                        if new_book == "":
                            new_book = info
                        else:
                            new_book += "," + info
                    # new_book = new_book + "\n"
                    books_info[counter] = new_book
                    booksInfo.close()
                    booksInfo = open("booksInfo.txt", "w+")
                    for line in books_info:
                        if line != "":
                            booksInfo.write(str(line))
                    print("Thank You For Buying From Our Store")
                else:
                    # if there are no enough books print this
                    print("There are {} books only".format(book[-2]))
                    available = True
                    break
            else:
                # If there are NO books print this
                print("There are {} books only".format(book[-2]))
                available = True
                break
        else:
            counter += 1
    if not available:
        print("The book is not found")
    booksInfo.close()
    bookSold.close()


# number 8
def format_library_info():
    # Ask for the password before delete all information
    password = int(input("Enter The Password: "))
    # if the password is correct delete
    if password == 202036900:
        # Delete all information
        booksInfo = open("booksInfo.txt", "w")
        borrowedInfo = open("borrowedInfo.txt", "w")
        booksInfo.close()
        borrowedInfo.close()
        print("Delete has done successfully")
    else:
        # print error
        print("Error:Incorrect Password")
    # return True to let the while running
    return True


# number 9
def exit_program():
    print("❤" * 32)
    print("☺ Thanks for using our Library Management System ☺")
    print("❤" * 32)
    # return False to let the while stop


# define a main function
def main():
    # make run = true to keep going
    run = True
    while run:
        # print the menu every time
        print(menu)
        # ask the user to choose a number from the menu
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print_books_info()
        elif choice == 2:
            search_for_book()
        elif choice == 3:
            add_new_book()
        elif choice == 4:
            remove_book()
        elif choice == 5:
            borrow_book()
        elif choice == 6:
            return_book()
        elif choice == 7:
            buy_book()
        elif choice == 8:
            format_library_info()
        elif choice == 9:
            exit_program()
            run = False
        else:
            print("Invalid input")


main()
