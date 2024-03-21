import sys
sys.path.insert(0, 'C:/Users/srgee/Questions/mr.cooper Broadband service-app')

from model.users import User

class FeedBackAndRatings:

    _feedbacksAndRatings: list[dict] = []

    def getFeedbacksAndRatings(self):
        return FeedBackAndRatings._feedbacksAndRatings


    def newFeedback(self, user: User, rating: int, feedback: str):
        FeedBackAndRatings._feedbacksAndRatings.append({
                                        "User": user, 
                                        "Rating": rating, 
                                        "Feedback": feedback,
                                    })
        

    def viewAllFeedbacks(self):
        table = []
        for feedback in FeedBackAndRatings._feedbacksAndRatings:
            rating = feedback["Rating"]
            if rating > 2:
                user_name = feedback["User"].name
                feedback = feedback["Feedback"]
                table.append([user_name, rating, feedback])

        return table
    
    
    def viewYourFeedbacks(self, user: User):

        table = []
        for feedback in FeedBackAndRatings._feedbacksAndRatings:
            user_name = feedback["User"].name 
            if user_name == user.name:
                rating = feedback["Rating"]
                feedback = feedback["Feedback"]
                table.append([user_name, rating, feedback])

        return table
    
