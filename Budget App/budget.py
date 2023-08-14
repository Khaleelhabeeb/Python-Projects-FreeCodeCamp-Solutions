class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{'*' * ((30 - len(self.name)) // 2)}{self.name}{'*' * ((30 - len(self.name)) // 2)}"
        items = "\n".join(
            f"{item['description'][:23]:23}{item['amount']:>7.2f}" for item in self.ledger
        )
        total = f"Total: {self.get_balance():.2f}"
        return f"{title}\n{items}\n{total}"


def create_spend_chart(categories):
    def get_category_withdrawals_percentage(category):
        total_withdrawals = sum(
            item["amount"] for item in category.ledger if item["amount"] < 0
        )
        total_expenses = sum(
            item["amount"]
            for category in categories
            for item in category.ledger
            if item["amount"] < 0
        )
        percentage = (total_withdrawals / total_expenses) * 100 if total_expenses > 0 else 0
        return percentage

    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3}| "
        for category in categories:
            percentage = get_category_withdrawals_percentage(category)
            chart += "o  " if percentage >= i else "   "
        chart += "\n"

    chart += " " * 4 + "-" * (len(categories) * 3 + 1) + "\n"

    max_category_name_length = max(len(category.name) for category in categories)
    for i in range(max_category_name_length):
        chart += " " * 5
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        chart += "\n"

    return chart


if __name__ == "__main__":
    # Example usage of the Category class
    food_category = Category("Food")
    food_category.deposit(1000, "initial deposit")
    food_category.withdraw(10.15, "groceries")
    food_category.withdraw(15.89, "restaurant and more foo")

    clothing_category = Category("Clothing")
    food_category.transfer(50, clothing_category)

    print(food_category)
    print(clothing_category)

    # Example usage of the create_spend_chart function
    categories = [food_category, clothing_category]
    print(create_spend_chart(categories))
