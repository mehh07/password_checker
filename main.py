from utils import evaluate_password

if __name__ == "__main__":
    password = input("Enter your password: ")
    result = evaluate_password(password)

    print(f"\nPassword Strength: {result['rating']}")
    print("Details:")
    for detail in result["reasons"]:
        print(f"• {detail}")
