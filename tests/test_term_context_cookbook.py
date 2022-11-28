import pytest
import term_context_cookbook


@pytest.mark.parametrize(
    "input_file, expected_char_data",
    [
        ("tests/test_input/simple.txt", ["t", "e", "s", "t"]),
        (
            "tests/test_input/with_spaces.txt",
            ["o", "n", "e", " ", "t", "w", "o", " ", "t", "h", "r", "e", "e"],
        ),
        (
            "tests/test_input/with_newlines.txt",
            ["o", "n", "e", " ", "t", "w", "o", " ", "t", "h", "r", "e", "e"],
        ),
    ],
    ids=["simple", "with_spaces", "with_newlines"],
)
def test_read_file_gets_char_data(input_file, expected_char_data):
    # Given char_data is empty and input file is set
    term_context_cookbook.char_data = []
    term_context_cookbook.input_file = input_file

    # When read_file is called
    term_context_cookbook.read_file()

    # Then char_data should contain the characters in the input file
    assert term_context_cookbook.char_data == expected_char_data


@pytest.mark.parametrize(
    "char_data,expected_words",
    [
        (["o", "n", "e"], ["one"]),
        (
            ["o", "n", "e", " ", "t", "w", "o", " ", "t", "h", "r", "e", "e"],
            ["one", "two", "three"],
        ),
    ],
    ids=["one word", "three words"],
)
def test_group_char_data_into_words_forms_words(char_data, expected_words):
    # Given words is empty and char_data contains these characters
    term_context_cookbook.words = []
    term_context_cookbook.char_data = char_data

    # When group_char_data_into_words is called
    term_context_cookbook.group_char_data_into_words()

    # Then words should contain words formed from the characters
    assert term_context_cookbook.words == expected_words


@pytest.mark.parametrize(
    "words,term,expected_contexts",
    [
        (
            ["one", "two", "three", "four", "five", "two"],
            "three",
            [["one", "two", "three", "four", "five"]],
        ),
        (
            ["one", "two", "three", "four", "five", "two"],
            "one",
            [["one", "two", "three"]],
        ),
        (
            ["one", "two", "three", "four", "five", "two"],
            "five",
            [["three", "four", "five", "two"]],
        ),
        (
            ["one", "two", "three", "four", "five", "two"],
            "two",
            [["one", "two", "three", "four"], ["four", "five", "two"]],
        ),
        (["one", "two", "three"], "two", [["one", "two", "three"]]),
    ],
    ids=[
        "one simple context",
        "one context with start constraint",
        "one context with end constraint",
        "two contexts with constraints",
        "one context with double-sided constraint",
    ],
)
def test_gather_contexts_from_words_handles_constraints(words, term, expected_contexts):
    # Given contexts is empty and words contains the term
    term_context_cookbook.contexts = []
    term_context_cookbook.words = words
    term_context_cookbook.term = term

    # When gather_contexts_from_words is called
    term_context_cookbook.gather_contexts_from_words()

    # Then contexts should contain the term and up to two words before and two words after it
    assert term_context_cookbook.contexts == expected_contexts


def test_print_contexts_displays_input(capsys):
    # Given input file is with_spaces.txt and term is two
    term_context_cookbook.contexts = []
    term_context_cookbook.input_file = "with_spaces.txt"
    term_context_cookbook.term = "two"

    # When print_contexts is called
    term_context_cookbook.print_contexts()
    out, err = capsys.readouterr()

    # Then the output should contain the input file and term
    assert "with_spaces.txt" in out
    assert "two" in out


@pytest.mark.parametrize(
    "term,contexts,expected_output",
    [
        (
            "three",
            [["one", "two", "three", "four", "five"]],
            "- one two _three_ four five",
        ),
        (
            "two",
            [["one", "two", "three", "four"], ["four", "five", "two"]],
            "- one _two_ three four \n- four five _two_",
        ),
    ],
    ids=["one simple context", "two contexts with constraints"],
)
def test_print_contexts_displays_contexts(term, contexts, expected_output, capsys):
    # Given the term and contexts
    term_context_cookbook.input_file = ""
    term_context_cookbook.term = term
    term_context_cookbook.contexts = contexts

    # When print_contexts is called
    term_context_cookbook.print_contexts()
    out, err = capsys.readouterr()

    # Then the output should contain the expected output
    assert expected_output in out
