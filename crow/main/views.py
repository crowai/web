from datetime import datetime, timedelta

from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
  predictionDate = datetime.now() + timedelta(hours=1)
  return render_template("main/index.html", predictionDate=predictionDate)
