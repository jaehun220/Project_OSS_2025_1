from budget import Budget
from earnings import Earnings
from AssetStatus import AssetStatus

def main():
    budget = Budget()
    earnings = Earnings()
    tracker = AssetStatus(budget, earnings)

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 수입 추가")
        print("5. 수입 목록 보기")
        print("6. 총 수입 보기")
        print("7. 수입/지출 내역 확인")
        print("8. 잔액 확인 (흑자/적자)")
        print("9. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            category = input("카테고리 (예: 급여, 부수입 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            earnings.add_earning(category, description, amount)

        elif choice == "5":
            earnings.list_earnings()

        elif choice == "6":
            earnings.total_earned()

        elif choice == "7":
            tracker.show_full_history()
            
        elif choice == "8":
            tracker.check_balance()

        elif choice == "9":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
