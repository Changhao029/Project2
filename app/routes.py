from sqlalchemy import func

from app import app, db
from flask import render_template, request, flash, redirect, url_for, session, g
from app.forms import RegisterForm, LoginForm, GameTableForm
from app.models import User, GameResult, GameBank
import json
import random

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)
        username = form.username.data
        password = form.password.data
        if form.validate():
            if User.query.filter(User.username == username).first() is None:
                new_user = User(username=username,password=password)
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('login'))
            else:
                flash(" The user name already exists. ")
                return redirect(url_for('register'))
        else:
            flash(" Incorrect user name or password format. ")
            return redirect(url_for('register'))


@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # if g.user:
        #     return render_template('login.html', user=g.user)
        # else:
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        username = form.username.data
        password = form.password.data
        if form.validate():
            user_object = User.query.filter(User.username == username).first()
            if user_object is None:
                flash('invalid username or data')
                return redirect(url_for('login'))
            elif user_object.password != password:
                flash('Incorrect password. Please try again.')
                return redirect(url_for('login'))
            else:
                if request.form.get('remember') == '1':
                    session.permanent = True
                session['username'] = username
                return redirect(url_for('game'))

        else:
            flash('not empty.')
            return redirect(url_for('login'))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == "GET":
        game_bank_obj = GameBank.query.filter(GameBank.id == 1).first()
        # random.seed(g.user.id)
        if g.user:
            random.seed(g.user.id)
            user_flag = g.user
        else:
            random.seed(1)
            user_flag = None
        random_list = random.sample(range(0, 81), 43)
        print(random_list)
        return render_template('game.html', game=game_bank_obj.game.split(','),
                               random_list=random_list, user_flag=user_flag)
    else:
        rows = True
        columns = True
        grids = True
        data_string = request.get_json()
        print(data_string)
        listdata = data_string['game_string'].split(',')
        final_list = list()
        for i in range(0, len(listdata), 9):
            final_list.append(listdata[i:i+9])

        for i in range(len(final_list)):
            temp_col = list()
            for j in range(len(final_list)):
                temp_col.append(final_list[j][i])
            if len(final_list[i]) != len(set(final_list[i])):
                rows = False
            if len(temp_col) != len(set(temp_col)):
                columns = False
        for i in [1, 4, 7]:
            for j in [1, 4, 7]:
                temp_grid = list()
                temp_grid.append(final_list[i-1][j-1])
                temp_grid.append(final_list[i-1][j])
                temp_grid.append(final_list[i-1][j+1])
                temp_grid.append(final_list[i][j-1])
                temp_grid.append(final_list[i][j])
                temp_grid.append(final_list[i][j+1])
                temp_grid.append(final_list[i+1][j-1])
                temp_grid.append(final_list[i+1][j])
                temp_grid.append(final_list[i+1][j+1])
                if len(temp_grid) != len(set(temp_grid)):
                    grids = False
        if rows and columns and grids:
            input_db_data = GameResult(playerId=g.user.id,
                                       start_time=data_string['start_time'],
                                       finish_time=data_string['finish_time'],
                                       time_spent=(data_string['finish_time']-data_string['start_time']))
            db.session.add(input_db_data)
            db.session.commit()
            return "success"
        else:
            return "fail"


@app.route('/rank', methods=['GET', 'POST'])
def rank():
    if request.method == "GET":
        player_best_ranks = db.session.query(GameResult.playerId,
                                             func.min(GameResult.time_spent)).group_by(GameResult.playerId).all()
        print(player_best_ranks)
        rank_dict = dict()
        for i in range(len(player_best_ranks)):
            temp_dict = dict()
            temp_dict["player_name"] = User.query.filter(User.id == player_best_ranks[i][0]).first().username
            temp_dict["best_mark"] = player_best_ranks[i][1]
            rank_dict[i] = temp_dict
        rank_json = json.dumps(rank_dict)
        return rank_json
    else:
        playerId = request.form.get('playerId')
        time_spent = request.form.get('time_spent')
        rank = GameResult(playerId=playerId, time_spent=time_spent)
        db.session.add(rank)
        db.session.commit()
        return ''

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == "GET":
        # game_bank_obj = GameBank.query.filter(GameBank.id == 1).first()
        # # random.seed(g.user.id)
        # random.seed(1)
        # random_list = random.sample(range(0, 81), 43)
        # print(random_list)
        return render_template('upload.html')
    else:
        rows = True
        columns = True
        grids = True
        data_string = request.get_json()
        listdata = data_string['game_string'].split(',')
        final_list = list()
        for i in range(0, len(listdata), 9):
            final_list.append(listdata[i:i+9])

        for i in range(len(final_list)):
            temp_col = list()
            for j in range(len(final_list)):
                temp_col.append(final_list[j][i])
            if len(final_list[i]) != len(set(final_list[i])):
                rows = False
            if len(temp_col) != len(set(temp_col)):
                columns = False
        for i in [1, 4, 7]:
            for j in [1, 4, 7]:
                temp_grid = list()
                temp_grid.append(final_list[i-1][j-1])
                temp_grid.append(final_list[i-1][j])
                temp_grid.append(final_list[i-1][j+1])
                temp_grid.append(final_list[i][j-1])
                temp_grid.append(final_list[i][j])
                temp_grid.append(final_list[i][j+1])
                temp_grid.append(final_list[i+1][j-1])
                temp_grid.append(final_list[i+1][j])
                temp_grid.append(final_list[i+1][j+1])
                if len(temp_grid) != len(set(temp_grid)):
                    grids = False
        if rows and columns and grids:
            input_db_data = GameBank(game=data_string['game_string'],
                uploaderId=g.user.id,
                upload_time=None)
            db.session.add(input_db_data)
            db.session.commit()
            return "success"
        else:
            return "fail"

