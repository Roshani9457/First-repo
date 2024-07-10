list=[('Higgler','coppard','Romance'),('Signalman','Charles Dickens','Suspens'),('Train to Pakistan','Khushwant Singh','Romance')]
#created list of books using tuple
def add_book(title,author,genre):           #created function add_book with parameter title,author,genre     
    return title,author,genre            #return title,author,genre

def add_to_library(tuple):                 #created function add_to_libray with parameter tuple
    list.append(tuple)               #added tuple to list
    myset = set(list)               #convert list to set to remove duplicate
    return myset               #return myset

def remove_from_library(title,author,genre):       #created function remove_from_library with parameter title,author,genre 
    list.remove((title,author,genre))           #remove title,author,genre  from list
    return list                              #return list

def search_book(title_author):             #created function search_book with parameter title_author
    x=title_author                        #store title_author in x
    output=[]                            #created empty list
    for i in list:                        #for used to take single tuple from list and store in i
        if x in i:                    #if check x is present in i or not
            output.append(i)             #i is added in output
    return output                     #return output

def list_books():                     #created function list_books
    print(list)                    #print list

def categorize_books(genre):                 #create function categorize_books with parameter genre
    x=genre                      #store genre in x
    output=[]                   #ceated empty list
    for i in list:              #for used to take single tuple from list and store in i
        if x in i:               #if check x is present in i or not
            output.append(i)         #i is added in output
    dict={                     #ceated dictionary
        genre:output
    }
    print(dict)               #print dictionary

while (next != 'no'):                #use while loop with condition next not equal to no
    ch=input("Enter choice(add,add to library,remove,search,list,categorize) book:")       #take choice from user
    if(ch == 'add book'):            #if check choice is equal to add book or not
        title=input('Enter title of book:')
        author=input('Enter author of book:')
        genre=input('Enter genre of book:')
        print('added book:',add_book(title,author,genre))
    elif (ch == 'add to library'):             #elif check choice is equal to add to library or not
        title=input('Enter title of book:')
        author=input('Enter author of book:')
        genre=input('Enter genre of book:')
        tuple=title,author,genre
        print('added book to library:',add_to_library(tuple))
    elif (ch == 'remove book'):                #elif check choice is equal to remove book or not
        title=input('Enter title of book:')
        author=input('Enter author of book:')
        genre=input('Enter genre of book:')
        print('After remove:',remove_from_library(title,author,genre))
    elif (ch == 'search book'):                #if check choice is equal to search book or not
        title_author=input('Enter title or author of book:')
        print('Book found:',search_book(title_author))
    elif (ch == 'list book'):                   #if check choice is equal to list book or not
        list_books()
    elif (ch == 'categorize book'):             #if check choice is equal to categorize book or not
        genre=input('Enter genre og book:')
        categorize_books(genre)
    else :
        print('invalid choice')
    next=input('If you want to continue then yes else no:')           #take input from user 