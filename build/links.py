import webbrowser
import subprocess
import os  # 404 Page-hez


def open_github_mark():
    url = "https://github.com/NemodaMark"
    print("Külső hivatkozás megnyitása:", url)
    webbrowser.open_new(url)


def open_github_levente():
    url = "https://github.com/HaLTeX1"
    print("Külső hivatkozás megnyitása:", url)
    webbrowser.open_new(url)


def open_github_brigi():
    url = "https://github.com/brigii07"
    print("Külső hivatkozás megnyitása:", url)
    webbrowser.open_new(url)


def open_fb_mark():
    url = "https://www.facebook.com/nemoda.mark"
    print("Külső hivatkozás megnyitása:", url)
    webbrowser.open_new(url)


def open_fb_patrik():
    url = "https://www.facebook.com/profile.php?id=100012008566062"
    print("Külső hivatkozás megnyitása:", url)
    webbrowser.open_new(url)


def open_fb_levente():
    url = "https://www.facebook.com/rez.levente.7/"
    print("Külső hivatkozás megnyitása:", url)
    webbrowser.open_new(url)


def open_fb_brigi():
    url = "https://www.facebook.com/sz.brigi.b"
    print("Külső hivatkozás megnyitása:", url)
    webbrowser.open_new(url)


def open_lnkd_mark():
    url = "https://www.linkedin.com/in/márk-nemoda-869ab3263/"
    print("Külső hivatkozás megnyitása:", url)
    webbrowser.open_new(url)


def open_lnkd_levente():
    url = "https://www.linkedin.com/in/réz-levente-157053290/"
    print("Külső hivatkozás megnyitása:", url)
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
        print(f"A {filepath} fájl nem található.")
