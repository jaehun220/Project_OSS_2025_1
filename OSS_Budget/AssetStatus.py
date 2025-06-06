class AssetStatus:
    def __init__(self, budget, earnings):
        self.budget = budget
        self.earnings = earnings

    def check_balance(self):
        total_earned = self.earnings.total_earned()
        total_spent = self.budget.total_spent()

        net_balance = total_earned - total_spent
        if net_balance > 0:
            print(f"이번 달은 {net_balance}원 흑자입니다. 🎉\n")
        elif net_balance < 0:
            print(f"이번 달은 {-net_balance}원 적자입니다. 😢\n")
        else:
            print("이번 달은 수입과 지출이 동일합니다. ⚖️\n")
