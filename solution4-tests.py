import pytest
import sqlite_lib


@pytest.fixture(scope="module")
def setup_db():
    """
    Fixture to connect to the existing database before tests and
    ensure it is closed after tests.
    """
    sqlite_lib.connect('FirstDbSQL.db')
    yield
    sqlite_lib.close()


def test_check_winner_correct(setup_db):
    """
    Test case to verify that check_winner returns the correct song name
    for a given country and year.
    """
    from solution3 import check_winner  # Import from solution3
    result = check_winner('Israel', 2018)
    assert result == 'Toy', f"Expected 'Toy', but got {result}"


def test_check_winner_incorrect(setup_db):
    """
    Test case to verify that check_winner returns 'wrong' for a
    non-existing country or year.
    """
    from solution3 import check_winner  # Import from solution3
    result = check_winner('Israel', 2024)  # Assuming no winner in 2024
    assert result == 'wrong', f"Expected 'wrong', but got {result}"


def test_check_winner_filter_correct(setup_db):
    """
    Test case to verify that check_winner_filter returns the correct song name
    for a given country and year with case-insensitivity.
    """
    from solution3 import check_winner_filter  # Import from solution3
    result = check_winner_filter('israel', 2018)  # Case-insensitive check
    assert result == 'Toy', f"Expected 'Toy', but got {result}"


def test_check_winner_filter_incorrect(setup_db):
    """
    Test case to verify that check_winner_filter returns 'wrong' for a
    non-existing country or year.
    """
    from solution3 import check_winner_filter  # Import from solution3
    result = check_winner_filter('England', 2024)  # Assuming no winner in 2024
    assert result == 'wrong', f"Expected 'wrong', but got {result}"
