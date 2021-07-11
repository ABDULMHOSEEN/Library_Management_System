# open the files that we will use
booksInfo = open("booksInfo.txt", "a+")
booksInfo.seek(0)
borrowedInfo = open("borrowedInfo.txt", "a+")
borrowedInfo.seek(0)
# store all info inside this value
books_info = booksInfo.readlines()
borrowed_info = borrowedInfo.readlines()
# First of all I will define the menu with all choices
menu = "\nLibrary Management System\n" \
       "==============================\n" \
       "1. Print books info\n" \
       "2. Search a book\n" \
       "3. Add new book\n" \
       "4. Remove a book\n" \
       "5. Borrow a book\n" \
       "6. Return a book\n" \
       "7. Exit\n" \
       "=============================="
# set choice to zero to use it in while than ask user to change it
choice = 0
# use the while loop to make the program take an input from the user until number 7 is entered which is the exit choice
running = True
while running:
    # print the menu every time
    print(menu)
    # ask the user to choose a number from the menu
    choice = int(input("Enter your choice: "))

    # do the user's order

    # number 1
    if choice == 1:
        # this choice is about display the info of the book

        # count the number of books and print it
        number_of_books = len(books_info)
        print("\nTotal %d books:" % number_of_books,
              "\n##############################################")
        # read the list as save each info
        for book in books_info:
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
                print("##############################################\n")

    # number 2
    if choice == 2:
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

    # number 3
    if choice == 3:
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
            print("New book was added successfully\n")
        else:
            print("New book was not added successfully\n")

    # number 4
    if choice == 4:
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

    # number 5
    if choice == 5:
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
            if check_book == False:
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

    # number 6
    if choice == 6:
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

    if choice == 7:
        print("❤"*32)
        print("☺ Thanks for using our Library Management System ☺")
        print("❤" * 32)
        running = False
    if str(choice) not in "1234567":
        print("Invalid input")
booksInfo.close()
borrowedInfo.close()
