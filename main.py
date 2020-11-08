from flask import Flask, render_template, request, jsonify
import mysql.connector
import operator
import json
import pandas as pd


app = Flask(__name__)
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="name",
#   password="1234",
#   database = "suspects"
# )
#
# mycursor = mydb.cursor()

BASEURLS = ["https://gw.hackathon.vtb.ru"]
#
# @app.route('/')
# def index():
#     getIdDB(2, 'customers')
#     return render_template("index.html")

@app.route('/v1/adv/', methods= ["GET"])
def getAdv():
    value = getIdDB(2,2)
    return render_template("index.html", value = value)\


@app.route('/db')
@app.route('/db/page/<int:page>')
def dbInit(page = 1):

    mydb = getAccessToDB("name", "1234", "suspects")
    mycursor = mydb.cursor()
    df = pd.read_sql_query("SELECT * from suspects where suspect_id between %d and %d" % (page*15-15, page*15), mydb)

    print(df.items)
    # sql = "select * from suspects where suspect_id between '%d' and '%d' values (%d,%d))"
    # mycursor.execute(sql, (page*15-15), (page*15))
    # r = [dict((mycursor.description[i][0], value)
    #           for i, value in enumerate(row)) for row in mycursor.fetchall()]
    # mycursor.close()
    return render_template("index.html", database = df.to_html(classes='data'), titles=df.columns.values,page = page)




def getIdDB(id, tablename):
    pass


def getAccessToDB(log, password, db):
    con = mysql.connector.connect(
        host="localhost",
        user=log,
        password=password,
        database=db
    )
    return con

if __name__ == '__main__':
    app.run(debug=True, port=5000)