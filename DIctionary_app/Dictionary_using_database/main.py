import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter the word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if(results):
    for result in results:
        output = results[0]
    if(type(output) == tuple):
        for items in output:
            print(items)
    else:
        print(output)
else:
    print("No results found!")