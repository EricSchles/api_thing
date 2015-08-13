
from flask import render_template,request,jsonify,redirect,url_for, Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
import datetime
import json

#http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku
###Models
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
db = SQLAlchemy(app)

class Store(db.Model):
    __tablename__ = 'store'

    id = db.Column(db.Integer, primary_key=True)
    date_of_operation = db.Column(db.String(400),nullable=False)
    arrest = db.Column(db.String(400),nullable=False)
    age_group_of_offender = db.Column(db.String(400),nullable=False)
    race_of_offender = db.Column(db.String(400),nullable=False)
    criminal_record = db.Column(db.String(400),nullable=False)
    repeat_offender = db.Column(db.String(400),nullable=False)
    in_posession_of_weapon = db.Column(db.String(400),nullable=False)
    marital_status = db.Column(db.String(400),nullable=False)
    highest_level_of_education = db.Column(db.String(400),nullable=False)
    offenders_sector_of_employment = db.Column(db.String(400),nullable=False)
    vehicle_towed_impounded = db.Column(db.String(400),nullable=False)
    fines = db.Column(db.String(400),nullable=False)
    number_of_charges = db.Column(db.String(400),nullable=False)
    dna_taken = db.Column(db.String(400),nullable=False)
    method_of_payment_for_ads = db.Column(db.String(400),nullable=False)
    website_used_for_posting = db.Column(db.String(400),nullable=False)

    def __init__(self,date_of_operation="",arrest="",age_group_of_offender="",race_of_offender="",
                 criminal_record="",repeat_offender="",in_possession_of_weapon="",marital_status="",
                 highest_level_of_education="",offenders_sector_of_employment="",vehicle_towed_impounded="",
                 fines="",number_of_charges="",dna_taken="",method_of_payment_for_ads="",website_used_for_posting=""):
        self.date_of_operation= date_of_operation
        self.arrest=arrest
        self.age_group_of_offender=age_group_of_offender
        self.race_of_offender=race_of_offender
        self.criminal_record=criminal_record
        self.repeat_offender=repeat_offender
        self.in_possession_of_weapon=in_possession_of_weapon
        self.marital_status=marital_status
        self.highest_level_of_education=highest_level_of_education
        self.offenders_sector_of_employment=offenders_sector_of_employment
        self.vehicle_towed_impounded=vehicle_towed_impounded
        self.fines=fines
        self.number_of_charges=number_of_charges
        self.dna_taken=dna_taken
        self.method_of_payment_for_ads=method_of_payment_for_ads
        self.website_used_for_posting=website_used_for_posting

###Controller

@app.route("/html_view",methods=["GET","POST"])
def html_view():
    return render_template("index.html",data=Store.query.all())

@app.route("/receive_json/<data>",methods=["POST"])
def receive_json(data):
    
    
    data = json.loads(data)
    store = Store(date_of_operation=data["date_of_operation"],
                  arrest=data["arrest"],
                  age_group_of_offender=data["age_group_of_offender"],
                  race_of_offender=data["race_of_offender"],
                  criminal_record=data["criminal_record"],
                  repeat_offender=data["repeat_offender"],
                  in_possession_of_weapon=data["in_possession_of_weapon"],
                  marital_status=data["marital_status"],
                  highest_level_of_education=data["highest_level_of_education"],
                  offenders_sector_of_employment=data["offenders_sector_of_employment"],
                  vehicle_towed_impounded=data["vehicle_towed_impounded"],
                  fines=data["fines"],
                  number_of_charges=data["number_of_charges"],
                  dna_taken=data["dna_taken"],
                  method_of_payment_for_ads=data["method_of_payment_for_ads"],
                  website_used_for_posting=data["website_used_for_posting"])
    db.session.add(store)
    db.session.commit()
    return "success"

@app.route("/json_view",methods=["GET","POST"])
def json_view():
    data = Store.query.all()
    json_list = []
    for datum in data:
        elem = {}
        elem["date_of_operation"]= datum.date_of_operation
        elem["arrest"]=datum.arrest
        elem["age_group_of_offender"]=datum.age_group_of_offender
        elem["race_of_offender"]=datum.race_of_offender
        elem["criminal_record"]=datum.criminal_record
        elem["repeat_offender"]=datum.repeat_offender
        elem["in_possession_of_weapon"]=datum.in_possession_of_weapon
        elem["marital_status"]=datum.marital_status
        elem["highest_level_of_education"]=datum.highest_level_of_education
        elem["offenders_sector_of_employment"]=datum.offenders_sector_of_employment
        elem["vehicle_towed_impounded"]=datum.vehicle_towed_impounded
        elem["fines"]=datum.fines
        elem["number_of_charges"]=datum.number_of_charges
        elem["dna_taken"]=datum.dna_taken
        elem["method_of_payment_for_ads"]=datum.method_of_payment_for_ads
        elem["website_used_for_posting"]=datum.website_used_for_posting
        json_list.append(elem)
    return json.dumps(json_list)


if __name__ =='__main__':
    app.run(debug=True)    
