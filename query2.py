from data.jobs import Jobs
from data import db_session
import datetime

db_session.global_init('database/mars_explorer.db')

cap = Jobs()
cap.team_leader = 1
cap.job = 'deployment of residential modules 1 and 2'
cap.work_size = 15
cap.collaborators = '2, 3'
cap.start_date = datetime.datetime.now()
cap.is_finished = False
session = db_session.create_session()
session.add(cap)
session.commit()
