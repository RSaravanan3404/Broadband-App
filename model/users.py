from __future__ import annotations


class Users:

    _users: list[User] = []

    def getUsers(self):
        return Users._users


    def isExist(self, email: str) -> User:
        for user in Users._users:
            if user.getEmail() == email:
                return user
        return 0
    

    def addUser(self, user: User):
        Users._users.append(user)


class User:

    _no_of_users = 0

    def __init__(self, name, dob) -> None:
        User._no_of_users += 1
        self.name: str = name
        self.dob: str = dob
        self.__age: int = None
        self.__email: str = None
        self.__password: str = None
        self.transactions: list = []
        self.subscription: dict = None
        self.feedbacks = []


    def getInfo(self):
        info = f"Name: {self.name}\nDateOfBirth: {self.dob}\nAge: {self.__age}\nEmail: {self.__email}\
            \nCurrent subscription: {self.subscription.plan if self.subscription else 'Not Subscribed to any plans yet..'}"
        return info
    

    def addFeedback(self, feedback: dict):
        self.feedbacks.append(feedback)
    

    def setSubscription(self, plan):
        self.subscription = plan


    def getSubscription(self):
        return self.subscription


    def viewCurrentPlan(self) -> list[list]:
        table = []
        for planDetails in self.subscription:
            for attribute in planDetails:
                table.append(planDetails[attribute])
        return table


    def setEmail(self, email) -> None:
        self.__email = email


    def getEmail(self) -> str:
        return self.__email


    def setPassword(self, password: str) -> None:
        self.__password = password
    

    def getPassword(self) -> str:
        return self.__password
    
    
    def setAge(self, age: int) -> None:
        self.__age = age


    def getAge(self):
        return self.__age
