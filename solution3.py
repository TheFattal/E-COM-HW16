import sqlite_lib


def check_winner(country, year):
    """
    Retrieves the song name from the eurovision_winners table
    based on the specified country and year.
    """
    query = f"SELECT song_name FROM eurovision_winners WHERE country = '{country}' AND year = {year};"
    result = sqlite_lib.run_query_select(query)
    if result:
        return result[0][0]  # result is a list of tuples like [(song_name,)]
    else:
        return "wrong"


def check_winner_filter(country, year):
    """
    Retrieves the song name from the eurovision_winners table
    and filters the results in Python based on the specified country and year.
    """
    query = "SELECT year, country, song_name FROM eurovision_winners;"
    result_sql = sqlite_lib.run_query_select(query)
    # Filter results in Python
    result = list(filter(lambda row: row[1].lower() == country.lower() and row[0] == year, result_sql))
    if result:
        return result[0][2]  # result is a list of tuples like [(year, country, song_name)]
    else:
        return "wrong"


def main():
    """
    Main function to interact with the user and perform queries.
    """
    try:
        # Establish database connection
        sqlite_lib.connect('FirstDbSQL.db')

        # Example test for check_winner_filter function
        print(check_winner_filter('israel', 2018))

        # Get user input
        country = input('Enter country please: ').strip()
        year = int(input('Enter year please: '))

        # Perform query
        result = check_winner(country, year)
        print(result)

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Ensure database connection is closed
        sqlite_lib.close()


if __name__ == "__main__":
    main()
