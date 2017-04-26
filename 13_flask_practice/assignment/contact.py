from flask import Flask, render_template, request
import sqlite3 as lite
app = Flask(__name__)


@app.route('/')
def index():
    conn = lite.connect("members.db")
    conn.row_factory = lite.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM members")

    rows = cur.fetchall();
    return render_template('index.html', rows = rows)


@app.route('/new_member')
def new_member():
    return render_template('new_member.html')

@app.route('/add_proccess', methods= ['POST', 'GET'])
def add_proccess():
    if request.method == 'POST':
        try:
            name = request.form['name']
            age = request.form['age']
            email = request.form['email']
            phone = request.form['phone']

            with lite.connect("members.db") as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO members (name, age, email, phone) VALUES (?,?,?,?)",(name, age, email, phone))
                conn.commit()
                msg = "성공적으로 저장되었습니다!"
        except:
            conn.rollback()
            msg = "에러발생!"

        finally:
            return render_template("result.html", msg = msg)
            conn.close()

if __name__=='__main__':
    app.run(host='0.0.0.0')
