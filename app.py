import os, secrets, requests
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash
app=Flask(__name__)
app.secret_key=os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)
LOGIN_CODE=os.environ.get("APP_LOGIN_CODE","change-this-demo-code")
ISS_API="https://api.wheretheiss.at/v1/satellites/25544"
def login_required(fn):
    @wraps(fn)
    def wrapped(*a,**kw):
        if not session.get("authenticated"): return redirect(url_for("login"))
        return fn(*a,**kw)
    return wrapped
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        if secrets.compare_digest(request.form.get("login_code",""),LOGIN_CODE):
            session.clear(); session["authenticated"]=True
            return redirect(url_for("dashboard"))
        flash("Incorrect demo code.")
    return render_template("login.html")
@app.get("/logout")
def logout():
    session.clear(); return redirect(url_for("login"))
@app.get("/")
@login_required
def dashboard():
    iss=None; error=None
    try:
        r=requests.get(ISS_API,timeout=8); r.raise_for_status(); d=r.json()
        iss={k:round(float(d[src]),4 if k in ("latitude","longitude") else 2) for k,src in
             [("latitude","latitude"),("longitude","longitude"),("altitude_km","altitude"),("velocity_kmh","velocity")]}
    except (requests.RequestException,KeyError,TypeError,ValueError):
        error="ISS public data is temporarily unavailable."
    return render_template("dashboard.html",iss=iss,error=error)
if __name__=="__main__": app.run(host="127.0.0.1",port=5000,debug=False)
