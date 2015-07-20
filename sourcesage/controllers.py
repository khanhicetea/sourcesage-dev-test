from sourcesage import db, socketio, app
from models import Question, User, Answer
from flask import Flask, Blueprint, render_template, request, session, jsonify
import json
import md5

bp = Blueprint('api', __name__, url_prefix='/api')

def hash_md5(value):
	m = md5.new()
	m.update(value)
	return m.hexdigest()

@bp.route('/signup', methods=['POST'])
def signup():
	data = json.loads(request.data)
	data['password'] = hash_md5(data['password'])
	user = User(**data)
	result = user.save()
	
	return jsonify({'status': 1 if result else 0})