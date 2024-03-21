import sys
sys.path.insert(0, 'C:/Users/srgee/Questions/mr.cooper Broadband service--app')

from model.users import User

plans = {
    "EntertainmentPlan": {
        "Plan": "EntertainmentPlan",
        "Datalimit": 450,
        "Speed": 300,
        "PlanDuration": 1,
        "Price": 499,
        "isCancellable": 1,
        "isDowngradable": 1,
        "Detuction": 0.15,
    },
    "FamilyPlan": {
        "Plan": "FamilyPlan",
        "Datalimit": "Unlimited",
        "Speed": 500,
        "PlanDuration": 1,
        "Price": 699,
        "isCancellable": 0,
        "isDowngradable": 1,
        "Detuction": 0.25,
    },
    "MusicPlan": {
        "Plan": "MusicPlan",
        "Datalimit": 150,
        "Speed": 150,
        "PlanDuration": 1,
        "Price": 199,
        "isCancellable": 0,
        "isDowngradable": 0,
        "Detuction": 0.10,
    },
    "SportsPlan": {
        "Plan": "SportsPlan",
        "Datalimit": 300,
        "Speed": 200,
        "PlanDuration": 1,
        "Price": 299,
        "isCancellable": 1,
        "isDowngradable": 1,
        "Detuction": 0.10,
    },
}


class Planner(object):


    def viewAllPlans(self):
        table = []
        for _, planDetails in plans.items():
            for attribute in planDetails:
                table.append(planDetails[attribute])
        return table


    def getPlan(self, plan: str) -> dict:
        return plans.get(plan)
