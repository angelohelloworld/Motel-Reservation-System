from menu import Menu

def main():
    menu = Menu()
    action = 0
    
    while action != 4:
        print("\n***Casa de Motel INN***\n")
        
        print("What would you like to do?")
        print("[1] View rooms")
        print("[2] Book a room")
        print("[3] Manage booking")
        print("[4] Exit")
        
        action = int(input())
	
        if action == 1:
            menu.view_rooms()
        elif action == 2:
            menu.book_room()
        elif action == 3:
            menu.manage_booking()
        elif action == 4:
            exit()
	
main()