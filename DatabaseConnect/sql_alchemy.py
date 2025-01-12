from sqlalchemy import ForeignKey, create_engine, MetaData, Table, Column, Integer, String, text
engine = create_engine("mysql+mysqlconnector://root:Alhadi%40737@localhost/testdb", echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String(20)), 
   Column('lastname', String(20)), 
)

addresses = Table(
   'addresses', meta, 
   Column('id', Integer, primary_key = True), 
   Column('st_id', Integer, ForeignKey('students.id')), 
   Column('postal_add', String(20)), 
   Column('email_add', String(20)))

meta.create_all(engine, [students, addresses])

ins = students.insert()
ins = students.insert().values(name = 'Ravi', lastname = 'Kapoor')
conn = engine.connect()
result = conn.execute(ins)

# To insert set of parameters
conn.execute(students.insert(), [
   {'name':'Rajiv', 'lastname' : 'Khanna'},
   {'name':'Komal','lastname' : 'Bhandari'},
   {'name':'Abdul','lastname' : 'Sattar'},
   {'name':'Priya','lastname' : 'Rajhans'},
])


# Read the data
s = students.select()
result = conn.execute(s)
for row in result:
   print (row)


# Where 
s = students.select().where(students.c.id>2)
result = conn.execute(s)
for row in result:
   print (row)

# Using text query
t = text("SELECT * FROM students")
result = conn.execute(t)
for row in result:
   print (row)


stmt = students.update().where(students.c.lastname == 'Khanna').values(lastname = 'Kapoor')
result = conn.execute(stmt)

stmt = students.delete()
result = conn.execute(stmt)
