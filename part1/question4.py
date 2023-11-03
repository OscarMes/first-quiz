from pets_db import get_connection

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

# conn = get_connection()
# c = conn.cursor()




sql_pets_owned_by_nobody = """
            SELECT a.name, a.species, a.age
            FROM animals a
            LEFT JOIN people_animals pa ON a.name = (SELECT p.name FROM animals p WHERE pa.pet_id = p.animal_id)
            WHERE pa.owner_id IS NULL
"""

# c.execute(sql_pets_owned_by_nobody)
# animals = c.fetchall()
# print(animals)

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = """
            SELECT COUNT(*) 
            FROM people_animals pa
            INNER JOIN animals a ON pa.pet_id = a.animal_id
            INNER JOIN people p ON pa.owner_id = p.person_id
            WHERE a.age > p.age

"""

# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """ 
            SELECT P.name AS person_name, A.name AS pet_name, A.species
            FROM people P
            JOIN people_animals PA ON P.person_id = PA.owner_id
            JOIN animals A ON PA.pet_id = A.animal_id
            WHERE P.name = 'bessie'
            AND (
            SELECT COUNT(*)
            FROM people_animals PA2
            WHERE PA2.pet_id = A.animal_id
            ) = 1;
"""

