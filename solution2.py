import sqlite_lib

sqlite_lib.connect('FirstDbSQL.db')

query = """
SELECT year, country, winner, host_country, song_name 
FROM eurovision_winners 
ORDER BY year DESC 
LIMIT 10;
"""

results = sqlite_lib.run_query_select(query)
print(results)
print(f"{'Year':<6} {'Country':<15} {'Winner':<25} {'Host Country':<15} {'Song Name':<30}")
print("="*85)
for row in results:
    year, country, winner, host_country, song_name = row
    print(f"{year:<6} {country:<15} {winner:<25} {host_country:<15} {song_name:<30}")


sqlite_lib.close()
