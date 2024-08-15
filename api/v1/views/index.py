#!/usr/bin/python3
"""
Landing page
"""
from flask import jsonify

from api.v1.views import app_views
from models import storage
from models.engine.db_storage import classes


@app_views.route('/status')
def check_status():
    """
    Check the status of application
    """
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def object_number():
    """
    Retrieves the number of objects by type
    """
    objs = {"Budget": storage.count(classes["Budget"]),
            "Category": storage.count(classes["Category"]),
            "Expense": storage.count(classes["Expense"]),
            "Income": storage.count(classes["Income"]),
            "users": storage.count(classes["User"])}

    return jsonify(objs)
