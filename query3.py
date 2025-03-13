from data.users import User
from data import db_session

db_session.global_init(input())
session = db_session.create_session()
users = (session.query(User).filter(User.speciality.notlike('%engineer%'), User.position.notlike('%engineer%')),
         User.address.notlike('module_1').all())
for user in users:
    print(user.id)