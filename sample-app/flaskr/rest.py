import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask.json import jsonify
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('rest', __name__, url_prefix='/rest')

@bp.route('/users', methods=('GET',))
def register():
    db = get_db()
    users = db.execute(
        'SELECT * FROM user'
    ).fetchall()
    userlist = []
    for user in users:
        userdic = {"id" : user['id'], "username" : user["username"], "password" : user["password"]}
        userlist.append(userdic)
    return jsonify(userlist)

