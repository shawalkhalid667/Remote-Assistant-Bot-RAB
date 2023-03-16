from distutils.log import debug
import sys
import sqlite3
from flask import Flask, redirect, url_for, request, render_template
import intent_management as it

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Sample output to log errors if any
    print('This is error output', file=sys.stderr)
    print('This is standard output', file=sys.stdout)
    return 'Hello, World!'


@app.route('/webhook', methods = ['POST'])
def webhook():
    # Get response from DialogFlow
    req = request.get_json()
    print(dict(req)['queryResult']['queryText'], flush=True)

    # Create a connection to DB and dump the query
    con, cur = connect_db()
    # execute_queries_db("INSERT INTO qna VALUES ('abc', '', 0)", cur, True, con)
    execute_queries_db("INSERT INTO qna (question, answer, status) VALUES ('" + dict(req)['queryResult']['queryText'] + "', '', 0)", cur, True, con)
    con.close()

    # Return sample response to the user
    responseText = "I don't have that response in my database. Let me forward that query to a senior engineer and get back to you! Thank you for your patience. - Webhook"
    res = {"fulfillmentMessages": [{"text": {"text": [responseText]}}]}
    return res


@app.route('/qna', methods = ['POST', 'GET'])
def qna():
    con, cur = connect_db()
    if request.method == 'POST':
        id = request.form['id']
        question = request.form['question']
        answer = str(request.form['answer']).replace("'", "")
        print(answer,question, flush=True)
        execute_queries_db("UPDATE qna SET answer='"+str(answer)+"', status = 1 WHERE id = "+str(id), cur, True, con)
        it.create_intent("remoteassistantbot-xjmv", id, [question], [answer])
        # print(request.json, flush=True)
        # print(request.form['id'], flush=True)
        # print(request.form['question'], flush=True)


    questions = {}
    for row in execute_queries_db("SELECT * FROM qna where status = 0", cur):
        questions[row[0]] = row[1]
    # return str(questions)
    # print(questions)
    return render_template('index.html', questions=questions)


def execute_queries_db(query, cur, commit=False, con=""):
    # Execute Queries - Insert, Update, Delete
    print(query, flush=True)
    query_output = cur.execute(query)
    if commit:
        con.commit()
    print(query_output, flush=True)
    return query_output


def connect_db():
    # Create a connection to SQLite DB
    con = sqlite3.connect('qna_database.db')
    cur = con.cursor()
    return (con, cur)


@app.route('/create_database')
def create_database():
    # Create Database and tables
    con, cur = connect_db()
    execute_queries_db("DROP TABLE qna", cur, True, con)
    execute_queries_db("CREATE TABLE qna (id integer primary key AUTOINCREMENT, question text, answer text, status boolean)", cur, True, con)
    execute_queries_db("INSERT INTO qna (question, answer, status) VALUES ('sample-question','sample-answer', 1)", cur, True, con)
    execute_queries_db("INSERT INTO qna (question, answer, status) VALUES ('sample-question','sample-answer', 1)", cur, True, con)

    con.close()
    return "Database created sucessfully"


if __name__ == "__main__":
    # Set this to false when deployed to production
    app.run(debug=True)
