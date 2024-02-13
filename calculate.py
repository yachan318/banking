def calculate_interest(start_deposit, interest_rate, investment_term, interest_paid):
    # Convert interest rate to decimal
    interest_rate_decimal = interest_rate / 100

    # Convert investment term to months
    if "year" in investment_term.lower():
        investment_term_months = int(investment_term.split()[0]) * 12
    elif "month" in investment_term.lower():
        investment_term_months = int(investment_term.split()[0])
    else:
        raise ValueError("Invalid investment term. Please specify years or months.")

    # Calculate interest based on interest paid frequency
    if "monthly" in interest_paid.lower():
        interest_frequency = 12
    elif "quarterly" in interest_paid.lower():
        interest_frequency = 4
    elif "annually" in interest_paid.lower():
        interest_frequency = 1
    elif "maturity" in interest_paid.lower():
        interest_frequency = investment_term_months
    else:
        raise ValueError("Invalid interest paid frequency. Please specify Monthly, Quarterly, Annually, or At Maturity.")

    # Calculate final balance
    final_balance = start_deposit * ((1 + interest_rate_decimal / interest_frequency) ** (investment_term_months))

    return final_balance


def main():
    print("Welcome to the Term Deposit Calculator!")
    print("Please provide the following inputs:")

    start_deposit = float(input("Start deposit amount ($): "))
    interest_rate = float(input("Interest rate (%): "))
    investment_term = input("Investment term (e.g., 3 years or 36 months): ")
    interest_paid = input("Interest paid (Monthly, Quarterly, Annually, At Maturity): ")

    try:
        final_balance = calculate_interest(start_deposit, interest_rate, investment_term, interest_paid)
        print(f"Final balance: ${final_balance:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
