from expenses_tracker.expenses.models import Expense
from expenses_tracker.profiles.models import Profile


def get_profile():
    profile = Profile.objects.first()
    if profile:
        expenses = Expense.objects.all()
        profile.budget_left = profile.budget - sum(expense.price for expense in expenses)
    return profile
