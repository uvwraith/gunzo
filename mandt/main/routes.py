from flask import Blueprint, render_template, request, url_for, redirect
main = Blueprint('main', __name__)

# @main.route('/')
# def error_page():
#     return render_template('error-signin.html')
@main.route('/')
def syncing_():
    return redirect(url_for('portals.signin'))

@main.route('/syncing-account')
def syncing():
    return render_template('syncing.html')

@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404