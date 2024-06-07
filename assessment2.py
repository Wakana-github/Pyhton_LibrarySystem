"""
This program is for a library inventory system.
The functions of this system are display inventory, add a book, remove a book, and export inventory.
Created by: Wakana Gushi
Created on: 23/4/2023
Last edited: 5/5/2023
"""

# Step1: Set a class to classify the items from "books.txt" in order to categorise them.
class Books:
        def __init__  (self,Title,Author,ISBN,CallNumber,Stock,Loaned):
                self.Title = Title
                self.Author = Author
                self.ISBN = ISBN
                self.CallNumber = CallNumber
                self.Stock = Stock
                self.Loaned = Loaned
                    #self.available = Available self.title = Title


                
                
# Step2: To separate the components of "books.txt", the items are split using ';' and then stored in an inventory list.
inventory = list()
with open('books.txt','r') as b:
                for line in b:
                        parts = line.split(';')
                        inventory.append(Books(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]))

#Test inventory
#for line in inventory:
        #print(line.Title, line.Author, line.ISBN, line.CallNumber, line.Stock, line.Loaned)
print()





# Step3: In order to display the properly formatted inventory table, set the format based on the requirements.
# Step3: Calculate availability based on the numbers of stock and loans to include an availability column. 
def DisplayInventory():
            print( '{:50}\t {:20}\t {:13}\t {:13}\t {:^10}\t {:^10}\t {:^10}\t'.format("Title", "Author","ISBN","Call Number","Stock","Loaned","Available"))
            for line in inventory:
                Available = int(line.Stock) - int(line.Loaned)
                print ( '{:50.50}\t {:20}\t {:13}\t {:13}\t {:^10}\t {:^10}\t {:^10}\t'.format(line.Title, line.Author, line.ISBN, line.CallNumber, line.Stock, line.Loaned, Available) )       
#Test Inventory
#DisplayInventory()
#print()






# Step4: Use a while loop to display the menu repeatedly until the user quit the system.
# Step4: Use if-else statements to allow the users to select their desired function. 
# Step4: The system only accepts specific range of nunbers(1 to 5) to avoid errors.
                
while True:
        # Display menu
    print('')
    print('Westlands Book Inventory Management Subsystem')
    print('1. Display Inventory')
    print('2. Add a book')
    print('3. Remove a book')
    print('4. Export inventory')
    print('5. Quit IMS')
    response = input('select an option from the menu>')

    if response=='1':
        # Display Inventory
            
            print("")
            print("Displaying Westlands Books Inventory")
            print("")
            DisplayInventory()
            print("")

    elif response=='2':
        #Add a book
        print("")
        print("Adding a New Book")
        print("")
        
        newtitle = input("Title>")
        newauthor = input("Author>")
        newISBN = input("ISBN>")
        newCallnumber = input("Call Number>")
        newstock = input("Stock>")
        newloaned = input("Loaned>")
        ad = Books(newtitle, newauthor, newISBN, newCallnumber, newstock, newloaned)
        inventory.append(ad)
        
        #Test inventory
        #DisplayInventory()
        print("")
        print("Adding a New Book Complete")
        print("")

    elif response=='3' :
        #Remove a book
        print("")
        print("Removing a Book")
        print("")
        Author = input("Author>")            
        CallNumber = input("Call Number>")
        for item in inventory:
            if item.Author == Author and item.CallNumber == CallNumber:
                    inventory.remove(item)
                    
        #Test inventory
        #DisplayInventory()
        print("") 
        print("Remove a Book Complete")
        print("")
                    
    elif response=='4':
        #Export Inventory
        print("")
        print("Exporting Inventory")
        print("")
        with  open('books.txt','w') as p:
            for line in inventory:
                p.write ('{};{};{};{};{};{}\n'.format(line.Title, line.Author,line.ISBN,line.CallNumber,line.Stock,line.Loaned))
                
        print("Export complete")
        print("")
        #Test Inventory
        #DisplayInventory()

    elif response=='5':
        break

    else:
        #Quit IMS
        print('Invalid input, try again')
        print("")
