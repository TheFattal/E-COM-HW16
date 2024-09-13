import sqlite_lib
import pytest


@pytest.fixture
def before_after_operations_db():
    # BEFORE
    sqlite_lib.connect('FirstDbSQL.db')

    yield  # test_get_years

    # AFTER
    sqlite_lib.close()


def test_get_years(before_after_operations_db):

    # BEFORE
    # sqlite_lib.connect('hw.db')

    # Act
    result = sqlite_lib.run_query_select('''
        SELECT YEAR FROM eurovision_winners ew
        LIMIT 1
    ''')

    # Assert
    assert result == [(1956,)]

    # AFTER
    # sqlite_lib.close()


def test_db_table_euro_68(before_after_operations_db):
    # Act
    actual = sqlite_lib.run_query_select('''
        SELECT COUNT(*) songs_count FROM eurovision_winners ew
    ''')

    # Assert
    expected = [(68,)]
    assert actual == expected


def test_db_table_songs_68(before_after_operations_db):
    # Act
    actual = sqlite_lib.run_query_select('''
        SELECT COUNT(*) songs_count FROM song_details sd
    ''')

    # Assert
    expected = [(68,)]
    assert actual == expected
