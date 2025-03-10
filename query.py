from data.users import User
from data import db_session

db_session.global_init('database/mars_explorer.db')

cap = User()
cap.surname = 'Scott'
cap.name = 'Ridley'
cap.age = 21
cap.position = 'captain'
cap.speciality = 'research engineer'
cap.address = 'module_1'
cap.email = 'scott_chief@mars.org'
cap.hashed_password = '228228228'

dungeon_master = User()
dungeon_master.surname = 'Goga'
dungeon_master.name = 'Gogovich'
dungeon_master.age = 350
dungeon_master.position = 'full_master'
dungeon_master.speciality = 'mechanic'
dungeon_master.address = 'module_1488'
dungeon_master.email = 'gachimuchi@email.com'
dungeon_master.hashed_password = 'gachimuchi'

karl_marks = User()
karl_marks.surname = 'Marks'
karl_marks.name = 'Karl'
karl_marks.age = 58
karl_marks.position = 'proletarii'
karl_marks.speciality = 'revolutionary'
karl_marks.address = 'module_1917'
karl_marks.email = 'karl_marks@email.com'
karl_marks.hashed_password = '191719171917'

ernesto_chegevara = User()
ernesto_chegevara.surname = 'Chegevara'
ernesto_chegevara.name = 'Ernesto'
ernesto_chegevara.age = 30
ernesto_chegevara.position = 'proletarii'
ernesto_chegevara.speciality = 'revolutionary'
ernesto_chegevara.address = 'module_1917'
ernesto_chegevara.email = 'chegevara_ernesto@email.com'
ernesto_chegevara.hashed_password = 'ernestochegevaramachine'


session = db_session.create_session()
session.add(cap)
session.add(dungeon_master)
session.add(karl_marks)
session.add(ernesto_chegevara)
session.commit()