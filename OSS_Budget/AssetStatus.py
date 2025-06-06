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
            
    def show_full_history(self):
        combined = []

        for e in self.budget.expenses:
            combined.append({
                "date": e.date,
                "description": e.description,
                "amount": e.amount,
                "type": "지출",
                "category": e.category,
            })

        for e in self.earnings.earnings:
            combined.append({
                "date": e.date,
                "description": e.description,
                "amount": e.amount,
                "type": "수입",
                "category": e.category,
            })
        combined.sort(key=lambda x: x["date"], reverse=True)
        
        print("| {:<12} | {:<16} | {:>10} | {:<4} | {:<6} |".format("날짜", "내역", "금액", "구분", "분류"))
        print("|" + "-"*16 + "|" + "-"*20 + "|" + "-"*14 + "|" + "-"*8 + "|" + "-"*10 + "|")

        for item in combined:
            print("| {:<14} | {:<18} | {:>10}원 | {:<4} | {:<8} |".format(
                item['date'],
                item['description'],
                item['amount'],
                item['type'],
                item['category']
            ))
        print()
