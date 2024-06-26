import sys
sys.path.insert(0, 'C:/Users/srgee/Questions/mr.cooper Broadband service-app')
from model.feedbacksandratings import FeedBackAndRatings
from model.users import Users, User
from model.transactions import Transactions
from model.plans import Planner, plans
from model.utilities import calculateAge, printTable, planAttributes, transactionAttributes, feedbackAttributes


class UserAccess(object):

    
    def __init__(self) -> None:
        self.user: User = None
        self.users: Users = Users()
        self.planner: Planner = Planner()
        self.feebacks: FeedBackAndRatings = FeedBackAndRatings()
        self.transactions: Transactions = Transactions()

    # user stuffs
    def setUser(self, user: User) -> None:
        self.user = user


    def isExist(self, email: str) -> User:
        return self.users.isExist(email=email)


    def logIn(self, user: User, password: str) -> bool:
        if password == user.getPassword():
            self.setUser(user=user)
            return True
        return False
    
    
    def signUp(self, email: str, name: str, dob: str, password: str) -> bool:
        user = User(name, dob)
        age = calculateAge(dob=dob)
        user.setAge(age=age)
        user.setEmail(email=email)
        user.setPassword(password=password)
        # Adding a new user to the users 
        self.users.addUser(user=user)
        return True
    

    def viewProfile(self) -> None:
        print(self.user.getInfo())


    def editProfile(self, name: str, dob: str, password: str) -> bool:
        if name:
            self.user.name = name
        if dob:
            self.user.dob = dob
            age = calculateAge(dob=dob)
            self.user.setAge(age=age)
        if password:
            self.user.setPassword(password=password)
        return True
    

    # plans and stuffs
    

    def viewAllPlans(self) -> None:
        table = self.planner.viewAllPlans()
        printTable(head=planAttributes, table=table)


    def viewCurrentPlan(self) -> None:
        table = self.user.viewCurrentPlan()
        if table:
            printTable(head=planAttributes, table=table)
        else:
            print("Not subscribed to any plans yet.")


    def subscribe(self, planName: str, duration: int) -> bool:
        if self.user.getSubscription() is None:
            plan = self.planner.getPlan(plan=planName)
            price = plan.get("Price")
            duration = plan["PlanDuration"] = duration
            total = price * duration
            print("Total amount:", total)

            # transaction
            amount_paid = int(input("Pay the specified amount: "))
            type = "subscribed to " + plan.get("Plan")
            self.transactions.addTransction(user=self.user, type=type, amount=amount_paid)

            if amount_paid >= total:
                self.user.setSubscription(plan=plan)
            return True
        print("Already there is a subscription going on..")
        return False
    

    def upgradePlan(self, duration: int) -> None:
        plan = self.user.getSubscription()
        if plan:
            planname = self.user.getSubscription().get("Plan")
            price = plans.get(planname).get("Price")
            total = price * duration
            duration += plan.get("PlanDuration")
            print("Total amount:", total)

            # transaction
            amount_paid = int(input("Pay the specified amount: "))
            type = f"upgraded {plan.get('Plan')} to {duration} months."
            self.transactions.addTransction(user=self.user, type=type, amount=amount_paid)
            
            plan["Duration"] = duration
            plan["Price"] = price * duration
            plan["Datalimit"] *= duration
            return True
        print("You have'nt subscribed to any plans yet.")


    def downgradePlan(self, duration: int) -> int:
        plan = self.user.getSubscription()
        if plan:
            current_duration = plan.get("PlanDuration")
            if plan.get("isDowngradable") and current_duration > duration:
                detuction = plan.get("Detuction")
                price = plan.get("Price") // duration
                refund = price - (price * detuction)
                return refund
            print("Cannot downgrade this plan.")
            return
        print("You have'nt subscribed to any plans yet.")


    def cancelPlan(self) -> int:
        plan = self.user.getSubscription()
        if plan.get("isCancellable"):
            duration = plan.get("PlanDuration")
            price = plan.get("Price")
            total = price * duration
            detuction = plan.get("Detuction")
            refund = total - total * detuction
            self.user.setSubscription(None)
            return refund
        print("This plan does'nt have cancel option")
        return

    
    # transaction
    def viewTransactions(self) -> None:
        table = self.transactions.getTransactionDetails(user=self.user)
        if table:
            printTable(head=transactionAttributes, table=table)
        else:
            print("No transactions so far")


    # Feedback and ratings
    def viewAllFeedbacks(self) -> None:
        table = self.feebacks.viewAllFeedbacks()
        if table:
            printTable(head=feedbackAttributes, table=table)
        else:
            print("Feedbak is empty leave your feedback")


    def viewYourFeedback(self) -> None:
        table = self.feebacks.viewYourFeedbacks(user=self.user)
        if table:
            printTable(head=feedbackAttributes, table=table)
        else:
            print("You have'nt left any feedbacks")


    def leaveFeedback(self, rating: int, feedback: str) -> None:
        self.feebacks.newFeedback(user=self.user, rating=rating, feedback=feedback)
