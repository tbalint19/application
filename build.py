from models import *

db.connect()
db.drop_tables([School, City, Applicant], safe=True)  # for testing
db.create_tables([School, City, Applicant], safe=True)
