import sqlite3

# Connecting to sqlite
# connection database file; will create one if one doesn't exist
connect = sqlite3.connect('patients.db')

# db object
db = connect.cursor()

# line below will search the db file to see if  a table called 'patients' exist it will delete table patient_table if it exists
db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit() ## once use an execute command need to 'commit' it for it to take place
# // commit () --> This method commits the current transaction. If you don't call this method, 
# anything you did since the last call to commit() is not visible from other database connections.

# Creating table, 
table = """ CREATE TABLE patient_table ( 
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL,
            gender CHAR(25) NOT NULL,
            state CHAR(25) NOT NULL,
            country CHAR(25) NOT NULL,
            maritalstatus CHAR(25) NOT NULL,
            status CHAR(25) NOT NULL
        ); """

## 'CREATE TABLE' is the table creation command 
## 'patient_table' is the title of the table 
## whenever writing sql queries MUST need to end in ; [its kinda liek a period]
## 'mrn' 'firstname' 'lastname' 'dob' are the columns 
## 'VARCHAR' 'CHAR' are the dtypes 
## 'NOT NULL' means if you are inserting a new row the values cant be empty

db.execute(table)
connect.commit() # commit the changes, this is annoying but necessary


## note, you may see a .db-journal file, that is a temporary file that is created when you create a database.
## insert data into the table
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, state, country, maritalstatus, status) values('12345', 'Hugh', 'Crain', '01/01/1970', 'M', 'Florida', 'USA', 'Widow', 'Deceased')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, state, country, maritalstatus, status) values('23456', 'Olivia', 'Crain', '02/02/1970', 'F', 'Massachusetts', 'USA', 'Married', 'Deceased')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, state, country, maritalstatus, status) values('34567', 'Steven', 'Crain', '03/03/1980', 'M', 'California', 'USA', 'Divorced', 'Alive')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, state, country, maritalstatus, status) values('45678', 'Shirley', 'Crain', '04/04/1985', 'F', 'Massachusetts', 'USA', 'Married', 'Alive')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, state, country, maritalstatus, status) values('56789', 'Theodora', 'Crain', '05/05/1987', 'F', 'Massachusetts', 'USA', 'Single', 'Alive')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, state, country, maritalstatus, status) values('98765', 'Luke', 'Crain', '06/06/1990', 'M', 'California', 'USA', 'Single', 'Alive')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, state, country, maritalstatus, status) values('87654', 'Eleanor', 'Crain-Vance', '06/06/1990', 'F', 'California', 'USA', 'Widow', 'Deceased')")
## data_variable_name.execute("INSERT INTO table_name(column1,column2,column3,...) values('column1 value','column2 values','...')")

connect.commit()

# close the connection
## connect.close()