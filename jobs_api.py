from flask import Blueprint, request
from data import db_session
from data.jobs import Jobs
from flask import jsonify


blueprint = Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    sess = db_session.create_session()
    jobs_list = sess.query(Jobs).all()
    return jsonify({'jobs': [job.to_dict(only=('id', 'team_leader', 'collaborators',
                                               'job', 'work_size', 'start_date',
                                               'end_date', 'is_finished')) for job in jobs_list]})


@blueprint.route('/api/jobs/<id:int>')
def get_jobs_id():
    sess = db_session.create_session()
    jobb = sess.query(Jobs).filter((Jobs.id == id).all())
    if not jobb:
        return jsonify({"error": 'Not found'})
    return jsonify({'jobs': jobb.to_dict(only=('id', 'team_leader', 'collaborators',
                                               'job', 'work_size', 'start_date',
                                               'end_date', 'is_finished'))})

 @blueprint.route('/api/jobs', methods=['POST'])
 def create_jobs():
    if not request.json():
        return make_response(jsonify({'error': 'Bad request'}), 400)
    col = ['team_leader', 'job', 'collaborators', 'work_size', 'is_finished']
    if not all([k in col for k in request.json]):
        return  make_response(jsonify({'error': 'Bad reqqest'}))
    sess = db_session.create_session()
    jobs = Jobs()
    jobs.team_leader = request.json['team_leader']
    jobs.job = request.json['job']
    jobs.collaborators = request.json['collaborators']
    jobs.work_size = request.json['work_size']
    jobs.is_finished = request.json['is_finished']
    sess.add(jobs)
    sess.commit()
    return make_response(jsonify({'jobs.id': jobs.id}), 200)
