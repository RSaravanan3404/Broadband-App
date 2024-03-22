from os import system
import sys
sys.path.insert(0, 'C:/Users/srgee/Questions/mr.cooper Broadband service-app')
from controller.usercontroll import UserAccess


def planAccess(status: bool, useraccess: UserAccess) -> None:
    '''
    Gives user access to view all the available plans, view the current plan going on, upgrade plan,
    downgrade plan, cancel plan and view transaction details of him/her. 
    '''
    choice = input("1.View All plans\n2.View current plans\n3.Upgrade plan\n\
                   4.Downgrade plan\n5.Cancel plan\n6.View Transactions\n7.Exit\nEnter your choice: ")
    match choice:
        case "1":
            system('cls')
            useraccess.viewAllPlans()

        case "2":
            system('cls')
            useraccess.viewCurrentPlan()
            
        case "3":
            system('cls')
            useraccess.viewCurrentPlan()
            upgradeDuration = input("Enter the number of months You need to upgrade(1 month validity is 28 days. ) Enter only months: ")
            useraccess.upgradePlan(duration=upgradeDuration)

        case "3":
            system('cls')
            useraccess.viewCurrentPlan()
            downgradeDuration = input("Enter the number of months You need to downgrade(1 month validity is 28 days. ) Enter only months: ")
            refund = useraccess.downgradePlan(duration=downgradeDuration)
            if refund:
                print(f"{refund} rupees refunded")

        case "5":
            system('cls')
            useraccess.viewCurrentPlan()
            refund = useraccess.cancelPlan()
            if refund:
                print(f"{refund} rupees refunded")

        case "6":
            system('cls')
            useraccess.viewTransactions()
        
        case "7":
            status = False

        case _:
            system('cls')
            print("Invalid operation.")

    if status:
        planAccess(status=status, useraccess=useraccess)
        