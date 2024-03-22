import sys
sys.path.insert(0, 'C:/Users/srgee/Questions/mr.cooper Broadband service-app')
from os import system
from controller.usercontroll import UserAccess
from view.loginview import logIn
from view.signupview import signUp


useraccess = UserAccess()

# Main View
def view(choice=None) -> None:
    system('cls')
    choice = input("1.Log In\n2.Sign Up\n3.Exit\nEnter your choice: ")
    match choice:
        case "1":
            logIn(useraccess=useraccess)
        case "2":
            signUp(useraccess=useraccess)
            choice = input("do you want to LogIn(Yes or No): ").capitalize()
            if choice == "Yes":
                logIn(useraccess=useraccess)
        case "3":
            pass
        case _:
            print("Invalid Operation..")
    
view()
