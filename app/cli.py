import argparse
import getpass
import sys
from app.analyzer import analyze_password


def main():
    parser = argparse.ArgumentParser(description="Password Sentinel CLI")
    parser.add_argument("--password", help="Password as plain text (not recommended)")
    args = parser.parse_args()

    if args.password:
        password = args.password
    else:
        try:
            password = getpass.getpass("Enter password: ")
        except Exception:
            print("Error reading password")
            sys.exit(1)

    if not password:
        print("Error: Password cannot be empty")
        sys.exit(1)

    result = analyze_password(password)

    print("\nPassword Strength Analysis")
    print("-" * 26)
    print(f"Score: {result['score']} / 100")
    print(f"Rating: {result['rating']}\n")

    print("Details:")
    for line in result["details"]:
        print(f"- {line}")

    if result["recommendations"]:
        print("\nRecommendations:")
        for rec in result["recommendations"]:
            print(f"- {rec}")


if __name__ == "__main__":
    main()
