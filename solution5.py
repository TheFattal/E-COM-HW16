import solution3
import sqlite_lib


def update_genre(country, year, new_genre):
    """
    Updates the genre of the winning song for the given country and year if it exists.

    :param country: The country to check
    :param year: The year of the contest
    :param new_genre: The new genre to set for the winning song
    """
    winner = solution3.check_winner(country, year)

    if winner == "wrong":
        print("wrong")
        return

    # Check if the genre already exists in the table
    query_existing_genre = f"""
    SELECT DISTINCT genre FROM eurovision_winners WHERE genre = '{new_genre}';
    """
    existing_genres = sqlite_lib.run_query_select(query_existing_genre)

    if existing_genres:
        print("enter different genre")
        return

    # Update the genre for the winning song
    query_update_genre = f"""
    UPDATE eurovision_winners
    SET genre = '{new_genre}'
    WHERE country = '{country}' AND year = {year};
    """
    sqlite_lib.run_query_select(query_update_genre)

    print("done")


def main():
    # Connect to the database
    sqlite_lib.connect('FirstDbSQL.db')

    try:
        # Get user input
        country = input("Enter country: ").strip()
        year = int(input("Enter year: ").strip())
        new_genre = input("Change genre to: ").strip()

        # Call the function with user inputs
        update_genre(country, year, new_genre)

    except ValueError as ve:
        print(f"Error with input values: {ve}")

    # Close the database connection
    sqlite_lib.close()


if __name__ == "__main__":
    main()
