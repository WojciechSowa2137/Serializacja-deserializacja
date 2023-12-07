import json

from marshmallow import Schema, fields
from pprint import pprint
from datetime import date


class StudentSchema(Schema):
    id = fields.UUID()
    name = fields.Str()
    surname = fields.Str()
    mail = fields.Email()
    birth = fields.Date()

class Student:
    def __init__(self, id, name, surname, mail, birth):
        self.id = id
        self.name = name
        self.surname = surname
        self.mail = mail
        self.birth = birth


student = Student(0,"Maciek","Kowlaski","2137@gmail.com",date.today())
schema = StudentSchema()
result = schema.dump(student)
pprint(result)

schema_filter = StudentSchema(exclude=("id","mail"))
result_filter = schema_filter.dump(student)

with open(f"{result_filter['name']}_{result_filter['surname']}.json", "w") as f:
    json.dump(result_filter,f)
f.close()



