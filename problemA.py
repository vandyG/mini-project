# %%
"""
# String /input statement /print out
1. Print a welcome message to the user.
2. Take a string (message) and a letter from the user.
3. Count how many times this letter occurred.
4. Calculate the percentage of the letter in the message.
5. Print the outputs to the user.
"""

# %%
import argparse


# %%
def set_get_letter(input: str) -> str:
    if len(input) > 1:
        raise TypeError("Please provide a single letter as input.")

    return input


# %%
def main():
    print("Welcome User!")

    parser = argparse.ArgumentParser(prog="problemA", description="Problem A")
    parser.add_argument("message", default=None, nargs="?")
    parser.add_argument("letter", default=None, nargs="?", type=set_get_letter)
    parser.add_argument("--match-case", "-c", action="store_true")
    args, unknown = parser.parse_known_args(["--f"])

    if not args.message:
        args.message = input("Please enter a message: ")
    if not args.letter:
        args.letter = set_get_letter(input("Please enter a letter to search: "))
    if not args.match_case:
        match_case = input("Match case? [Y/N]: ")
        if match_case.lower() not in ["y", "n"]:
            raise TypeError("Invalid value for match_case. Please enter 'Y/N'")
        if match_case.lower() == "y":
            args.match_case = True

    if not args.match_case:
        message: str = args.message.lower()  # type: ignore
        letter: str = args.letter.lower()  # type: ignore
    else:
        message: str = args.message  # type: ignore
        letter: str = args.letter  # type: ignore

    print(f"Message: {args.message}")
    print(f"Letter: {args.letter}")
    print(f"Match Case: {args.match_case}")

    count = message.count(letter)
    print(f"Count: {count}")

    percentage = count / len(message)
    print(f"Percentage: {percentage:.2%}")


# %%
if __name__ == "__main__":
    main()
