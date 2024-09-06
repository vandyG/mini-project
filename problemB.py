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

import random
import re
from textwrap import dedent
from typing import Dict, Generator, List

from rich import print


def count_stats(search: List[str], string: str) -> Dict[str, List[re.Match]]:
    """Find all word/substring matches for each search term in the input string.

    Args:
        search (List[str]): List of items to search.
        string (str): The string to search in.

    Returns:
        Dict[str, List]: List of Match objects for each search term.
    """
    matches = {}

    for term in search:
        pattern = re.compile(r"(\b" + term + r"\b)|(" + term + r")", flags=re.I)
        curr_matches = list(pattern.finditer(string))

        matches[term] = curr_matches

    return matches


def pretty_print(search: List[str], string: str) -> Generator:
    """Highlight the matched terms in the string.

    Args:
        search (List[str]): List of search terms.
        string (str): Input string.

    Yields:
        Generator: Output string with the search term highlighted.
    """
    colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]

    for term in search:
        input = string
        substring_pattern = re.compile(term, re.I)
        color = random.choice(colors)

        input = re.sub(
            substring_pattern,
            lambda match: f"[bold {color}]{match.group(0)}[/bold {color}]",
            input,  # noqa: B023
        )

        yield input


def main():
    """Main funciton."""
    SNOWBALL = dedent("""
        I made myself a snowball.
        As perfect as could be.
        I thought I'd keep it as a pet.
        And let it sleep with me.
        I made it some pajamas.
        And a pillow for its head.
        Then last night it ran away,
        But first it wet the bed.
    """)

    search_terms = ["it", "i"]

    matches = count_stats(search_terms, SNOWBALL)

    for match_term, match_list in matches.items():
        just_words = [match for match in match_list if match.group(1)]
        just_non_words = [match for match in match_list if not match.group(1)]
        count = len(match_list)
        word_count = len(just_words)

        def min_func(match):
            return match.start()

        first_substring = min(match_list, key=min_func)
        first_word = min(just_words, key=min_func)
        first_non_word = min(just_non_words, key=min_func)

        print(f"Total [bold]'{match_term}'[/bold] substrings: {count}")
        print(f"Total [bold]'{match_term}'[/bold] words: {word_count}")
        print(f"First [bold]'{match_term}'[/bold] substrings: {first_substring}")
        print(f"First [bold]'{match_term}'[/bold] word: {first_word}")
        print(f"First [bold]'{match_term}'[/bold] non-word substring: {first_non_word}")
        print(next(pretty_print(search_terms, SNOWBALL)))
        print("---")

    pretty_print(search_terms, SNOWBALL)

    len_poem = len(SNOWBALL) - SNOWBALL.count("\n")

    print(f"Number of characters in poem: {len_poem}")


if __name__ == "__main__":
    main()
