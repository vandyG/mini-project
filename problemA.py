"""# String /input statement /print out
1. Print a welcome message to the user.
2. Take a string (message) and a letter from the user.
3. Count how many times this letter occurred.
4. Calculate the percentage of the letter in the message.
5. Print the outputs to the user.
"""

import argparse


def main():
    print("Welcome User!")

    parser = argparse.ArgumentParser(prog="Problem A", description="Problem A")
    parser.add_argument("message")
    parser.add_argument("letter")
    args = parser.parse_args()

    message: str = args.message.lower()  # type: ignore
    letter: str = args.letter.lower()  # type: ignore

    count = message.count(letter)
    print(f"Count: {count}")

    percentage = count / len(message)
    print(f"Percentage: {percentage:.2%}")


if __name__ == "__main__":
    main()
