import webbrowser
import subprocess
import os  # 404 Page-hez


def open_github_mark():
    url = "https://github.com/NemodaMark"
    webbrowser.open_new(url)


def open_github_levente():
    url = "https://github.com/HaLTeX1"
    webbrowser.open_new(url)


def open_github_brigi():
    url = "https://github.com/brigii07"
    webbrowser.open_new(url)


def open_fb_mark():
    url = "https://www.facebook.com/nemoda.mark"
    webbrowser.open_new(url)


def open_fb_patrik():
    url = "https://www.facebook.com/profile.php?id=100012008566062"
    webbrowser.open_new(url)


def open_fb_levente():
    url = "https://www.facebook.com/rez.levente.7/"
    webbrowser.open_new(url)


def open_fb_brigi():
    url = "https://www.facebook.com/sz.brigi.b"
    webbrowser.open_new(url)


def open_lnkd_mark():
    url = "https://www.linkedin.com/in/márk-nemoda-869ab3263/"
    webbrowser.open_new(url)


def open_lnkd_levente():
    url = "https://www.linkedin.com/in/réz-levente-157053290/"
    webbrowser.open_new(url)


# LEVELEZÉS
def open_mail_mark(subject):
    email_address = "mark.nemoda@outlook.com"
    webbrowser.open("mailto:" + email_address + "?subject=" + subject)


def open_mail_levente(subject):
    email_address = "info@rezlevente.hu"
    webbrowser.open("mailto:" + email_address + "?subject=" + subject)


def open_mail_brigi(subject):
    email_address = "farkasberta14@gmail.com"
    webbrowser.open("mailto:" + email_address + "?subject=" + subject)


def open_mail_patrik(subject):
    email_address = "patrik.padar@gmail.com"
    webbrowser.open("mailto:" + email_address + "?subject=" + subject)


# INFO MEGNYITÁSA GUI-BÓL
def inftab():
    subprocess.Popen(["python", "gui1.py"])


def notfound():
    filepath = "404.html"
    if os.path.exists(filepath):
        webbrowser.open("file:///" + os.path.abspath(filepath))
    else:
        print("A 404.html fájl nem található.")
