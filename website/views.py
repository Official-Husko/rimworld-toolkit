from flask import Blueprint, render_template, request, flash, redirect, url_for
import os
from .logger import Logger
from time import sleep

views = Blueprint("views", __name__)

@views.route("/")
def blank():
    if os.path.exists("settings.json"):
        return redirect(url_for("views.welcome"))
    else:
        return redirect(url_for("views.setup"))

@views.route("/setup", methods=["GET", "POST"])
def setup():
    if request.method == "POST":
        # TODO: write setup settings to settings.json
        flash("Setup Completed!", category="success")
        sleep(3)
        return redirect(url_for("views.welcome"))
    
    return render_template("setup.html")

@views.route("/welcome")
def welcome():
    # TODO: Show all found projects or just a simple welcome
    return render_template("welcome.html")

@views.route("/project", methods=["GET", "POST"])
def project():
    return render_template("project.html")

@views.route("/export", methods=["GET", "POST"])
def export():
    return render_template("export.html")

@views.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        # TODO: Change or show settings in settings.json
        pass
    return render_template("settings.html")