from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","post"])

def index():
  return(render_template("index.html"))
@app.route("/main",methods=["GET","POST"])

def main():
name = request.form.get("name")
return(render_tempalte("main.html",r=name))

if __name__=="__main__":
  app.run()      
