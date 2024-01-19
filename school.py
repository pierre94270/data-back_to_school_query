# pylint:disable=C0111,C0103
# pylint: disable=missing-docstring, C0103
import sqlite3
import school

conn = sqlite3.connect('data/school.sqlite')
db = conn.cursor()

def students_from_city(db, city):
    """return a list of students from a specific city"""
    
    query="""
        SELECT 
                first_name,
	            last_name 
        FROM students
        WHERE birth_city=  ? 
    """
    
    db.execute(query, (city, ))# , pour créer un tuple
    results = db.fetchall()
    
    #liste.append(i[0]) for i in results2
    return [x for x in results]
    # YOUR CODE HERE
    

#print (students_from_city(db, city))

# To test your code, you can **run it** before running `make`
#   => Uncomment the following lines + run:
#   $ python school.py
#
# import sqlite3
# conn = sqlite3.connect('data/school.sqlite')
# db = conn.cursor()
# print(students_from_city(db, 'Paris'))
