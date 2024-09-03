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


def main():
    SNOWBALL = """I made myself a snowball.
As perfect as could be.
I thought I'd keep it as a pet.
And let it sleep with me.
I made it some pajamas.
And a pillow for its head.
Then last night it ran away,
But first it wet the bed.
"""

    IT = "it"

    # it_count = SNOWBALL.lower().count(IT.lower())
    it_count = len(re.findall(r"\bit\b", SNOWBALL))

    len_poem = len(SNOWBALL) - SNOWBALL.count("\n")

    it_first = SNOWBALL.find(IT)

    I_last = SNOWBALL.rfind("I")

    print(f"{it_count=}")
    print(f"{len_poem=}")
    print(f"{it_first=}")
    print(f"{I_last=}")


if __name__ == "__main__":
    main()
