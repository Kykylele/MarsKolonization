from flask import Blueprint
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


@blueprint.route('/api/jobs/<int:id>')
def get_jobs_id(id):
    sess = db_session.create_session()
    jobb = sess.query(Jobs).filter(Jobs.id == id).first()
    if not jobb:
        return jsonify({"error": 'Not found'})
    return jsonify({'jobs': jobb.to_dict(only=('id', 'team_leader', 'collaborators',
                                               'job', 'work_size', 'start_date',
                                               'end_date', 'is_finished'))})
