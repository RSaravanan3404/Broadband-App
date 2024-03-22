from os import system
import sys
sys.path.insert(0, 'C:/Users/srgee/Questions/mr.cooper Broadband service-app')
from controller.usercontroll import UserAccess
from utilities import plans


def planAccess(status: bool, useraccess: UserAccess) -> None:
    '''
    Gives user access to view all the available plans, view the current plan going on, upgrade plan,
    downgrade plan, cancel plan and view transaction details of him/her. 
    '''
    choice = input("1.View All plans\n2.View current plans\n3.Subscribe\
                   \n4.Upgrade plan\n5.Downgrade plan\n6.Cancel plan\n7.View Transactions\n8.Exit\nEnter your choice: ")
    match choice:
        case "1":
            system('cls')
            useraccess.viewAllPlans()

        case "2":
            system('cls')
            useraccess.viewCurrentPlan()

        case "3":
            system('cls')
            useraccess.viewAllPlans()
            number = 1
            for plan in plans:
                print(f"{number}. {plan}")
                number += 1
            choice = int(input("Enter your choice: "))
            duration = int(input("Enter the plan duration you want to subscribe in months(1 month is 28 days): "))
            plan = plans[choice - 1]
            useraccess.subscribe(planName=plan, duration=duration)
            
        case "4":
            system('cls')
            useraccess.viewCurrentPlan()
            upgradeDuration = int(input("Enter the number of months You need to upgrade(1 month validity is 28 days. ) Enter only months: "))
            useraccess.upgradePlan(duration=upgradeDuration)

        case "5":
            system('cls')
            useraccess.viewCurrentPlan()
            downgradeDuration = int(input("Enter the number of months You need to downgrade(1 month validity is 28 days. ) Enter only months: "))
            refund = useraccess.downgradePlan(duration=downgradeDuration)
            if refund:
                print(f"{refund} rupees refunded")

        case "6":
            system('cls')
            useraccess.viewCurrentPlan()
            refund = useraccess.cancelPlan()
            if refund:
                print(f"{refund} rupees refunded")

        case "7":
            system('cls')
            useraccess.viewTransactions()
        
        case "8":
            status = False

        case _:
            system('cls')
            print("Invalid operation.")

    if status:
        planAccess(status=status, useraccess=useraccess)
        