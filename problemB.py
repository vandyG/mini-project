"""snowball is one of the most famous poems in literature. It says.

I made myself a snowball.
As perfect as could be.
I thought I'd keep it as a pet.
And let it sleep with me.
I made it some pajamas.
And a pillow for its head.
Then last night it ran away,
But first it wet the bed.

1. How many the word it does the poem have? --> Store the output in a variable called
it_count (check the different scenarios)
2. How many characters in the poem, including the spaces and punctuations? --> Store the
output in a variable called len_poem
3. Where is the first occurrence for the word it? --> Store the output in a variable called
it_first (check the different scenarios)
4. Where is the last occurrence for the word I? --> Store the output in a variable called
I_last (check the different scenarios)

"""

import re

from pygments import highlight
from rich import print


def main():
    SNOWBALL = """I made myself a snowball.
As perfect as could be.
I thought I'd keep it as a pet.
And let it sleep with me.
I made it some pajamas.
And a pillow for its head.
Then last night it ran away,
But first it wet the bed."""

    IT = "it"

    # it_count = SNOWBALL.lower().count(IT.lower())
    it_word_pattern = re.compile(r"(\bit\b)|(it)", flags=re.I)
    # it_substring_pattern = re.compile(r"\Bit\B", flags=re.I)

    SNOWBALL_OUTPUT = ""
    prevend = 0
    it_word_count = 0
    it_count = 0
    it_word_first = None
    it_substring_first = None
    it_not_word_substring_first = None

    it_word_iter = it_word_pattern.finditer(SNOWBALL)

    for word in it_word_iter:
        it_count += 1
        start = word.start()
        end = word.end()

        if word.group(1):
            highlighted_word = f"[bold red]{word.group(1)}[/bold red]"
            it_word_count += 1

            if it_word_count == 1:
                it_word_first = (start, end)

        else:
            highlighted_word = f"[bold blue]{word.group(0)}[/bold blue]"

        if it_count == 1:
            it_substring_first = (start, end)

        if it_count - it_word_count == 1:
            it_not_word_substring_first = (start, end)

        SNOWBALL_OUTPUT = SNOWBALL_OUTPUT + SNOWBALL[prevend:start] + highlighted_word
        prevend = end

    SNOWBALL_OUTPUT = SNOWBALL_OUTPUT + SNOWBALL[prevend:]
    print(SNOWBALL_OUTPUT)
    print(f"Total 'it' substrings = {it_count}")
    print(f"Total 'it' words = {it_word_count}")

    len_poem = len(SNOWBALL) - SNOWBALL.count("\n")

    # it_first = SNOWBALL.find(IT)

    # I_last = SNOWBALL.rfind("I")

    # print(f"{it_count=}")
    print(f"{it_count=}")
    print(f"{it_word_count=}")
    print(f"{len_poem=}")
    print(f"{it_word_first=}")
    print(f"{it_substring_first=}")
    print(f"{it_not_word_substring_first=}")
    # print(f"{it_first=}")
    # print(f"{I_last=}")


if __name__ == "__main__":
    main()
