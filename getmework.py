from flask import Flask, render_template
import os
import random

basedir = os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)

SQLALCHEMY_DATABASE_URI="sqlite:///" + os.path.join(basedir, "app.db")

items=[ { "id" : random.randint(0,10000), "title" : "I really want to work" , "text" : "I need a job so bad, I am banned from craigs list.  Give me a call"  , "price" : 100*random.randint(0,20), "px" : x, "py" : y,
"longtext" : "<p>Ok long boring text!</p><p>yadda yadda yadda</p>" } for y in range(0,10000,466) for x in range(0,801,400) ]


def find(items,k):
        for x in items:
              if x["id"] == k: return x
              return None

@app.route("/")
def index():
        global items	
        return render_template("index.html",  items = items ) 

@app.route("/product/<int:idx>")

def product(idx):
	global items
	return render_template("product.html", item=find(items,idx)) 

if __name__ == "__main__":
        app.run(host="0.0.0.0", debug=True)

