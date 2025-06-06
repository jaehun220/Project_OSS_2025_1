import datetime
from expense import Expense

class Earnings:
    def __init__(self):
        self.earnings = []

    def add_earning(self, category, description, amount):
        today = datetime.date.today().isoformat()
        earning = Expense(today, category, description, amount)
        self.earnings.append(earning)
        print("수입이 추가되었습니다.\n")

    def list_earnings(self):
        if not self.earnings:
            print("수입 내역이 없습니다.\n")
            return
        print("\n[수입 목록]")
        for idx, e in enumerate(self.earnings, 1):
            print(f"{idx}. {e}")
        print()

    def total_earned(self):
        total = sum(e.amount for e in self.earnings)
        print(f"총 수입: {total}원\n")
        return total