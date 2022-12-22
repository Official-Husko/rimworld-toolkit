from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .logger import Logger
from time import sleep
import json, random, os

views = Blueprint("views", __name__)

background_list = os.listdir("./website/static/backgrounds")
background = random.choice(background_list)

@views.route("/")
def blank():
    session["background"] = background
    if os.path.exists("settings.json"):
        with open("settings.json", "r") as settings:
            user_settings = json.load(settings)
            session["default_author"] = user_settings["default_author"]
            session["default_author_short"] = user_settings["default_author_short"]
            session["language"] = user_settings["language"]
            session["default_github"] = user_settings["default_github"]
            session["versions"] = user_settings["versions"]
            print(session["versions"])
        return redirect(url_for("views.welcome"))
    else:
        return redirect(url_for("views.setup"))

@views.route("/setup", methods=["GET", "POST"])
def setup():
    session["background"] = background
    if request.method == "POST":
        data = json.loads(str(request.form.to_dict(flat=True)).replace("'", '"'))
        data_example = {
            "versions": data["target-versions"].translate(str.maketrans({"'": "", " ": ""})).split(","),
            "default_author": data["default-author"],
            "default_author_short": data["default-author-short-form"],
            "language": data["language"],
            "default_github": data["default-github-username"]
        }
        settings = open("settings.json", "w")
        json.dump(data_example, settings, indent=6)
        flash("Setup Completed!", category="success")
        sleep(3)
        return redirect(url_for("views.welcome"))
    
    return render_template("setup.html")

@views.route("/welcome")
def welcome():
    session["background"] = background
    try:
        session["default_author"]
    except:
        return redirect(url_for("views.blank"))
    # TODO: Show all found projects or just a simple welcome
    return render_template("welcome.html")

@views.route("/project", methods=["GET", "POST"])
def project():
    session["background"] = background
    return render_template("project.html")

@views.route("/export", methods=["GET", "POST"])
def export():
    session["background"] = background
    return render_template("export.html")

@views.route("/settings", methods=["GET", "POST"])
def settings():
    session["background"] = background
    if request.method == "POST":
        # TODO: Change or show settings in settings.json
        pass
    return render_template("settings.html")