
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil
import sys
import subprocess
import string
import random
import json
import re
import time
import argparse
import zipfile
from io import BytesIO

from concurrent.futures import ThreadPoolExecutor, as_completed

from utils.decorators import MessageDecorator
from utils.provider import APIProvider

try:
    import requests
    from colorama import Fore, Style
except ImportError:
    print("\tSome dependencies could not be imported (possibly not installed)")
    print(
        "Type `pip3 install -r requirements.txt` to "
        " install all required packages")
    sys.exit(1)


def readisdc():
    with open("isdcodes.json") as file:
        isdcodes = json.load(file)
    return isdcodes


def get_version():
    try:
        return open(".version", "r").read().strip()
    except Exception:
        return '1.0'


def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def bann_text():
    clr()
    logo = """
   ████████ █████                 ██
   ▒▒▒██▒▒▒ ██▒▒██                ██
      ██    ██  ██        ██   ██ ██
      ██    █████▒  ████  ███ ███ █████
      ██    ██▒▒██ ██  ██ ██▒█▒██ ██▒▒██
      ██    ██  ██ ██  ██ ██ ▒ ██ ██  ██
      ██    █████▒ ▒████▒ ██   ██ █████▒
      ▒▒    ▒▒▒▒▒   ▒▒▒▒  ▒▒   ▒▒ ▒▒▒▒▒
                                         """
    if ASCII_MODE:
        logo = ""
    version = "Version: "+__VERSION__
    contributors = "Contributors: "+" ".join(__CONTRIBUTORS__)
    print(random.choice(ALL_COLORS) + logo + RESET_ALL)
    mesgdcrt.SuccessMessage(version)
    mesgdcrt.SectionMessage(contributors)
    print()


def check_intr():
    try:
        requests.get("https://motherfuckingwebsite.com")
    except Exception:
        bann_text()
        mesgdcrt.FailureMessage("Poor internet connection detected")
        sys.exit(2)


def format_phone(num):
    num = [n for n in num if n in string.digits]
    return ''.join(num).strip()


def do_zip_update():
    success = False
    if DEBUG_MODE:
        zip_url = "https://github.com/TheSpeedX/TBomb/archive/dev.zip"
        dir_name = "TBomb-dev"
    else:
        zip_url = "https://github.com/TheSpeedX/TBomb/archive/master.zip"
        dir_name = "TBomb-master"
    print(ALL_COLORS[0]+"Downloading ZIP ... "+RESET_ALL)
    response = requests.get(zip_url)
    if response.status_code == 200:
        zip_content = response.content
        try:
            with zipfile.ZipFile(BytesIO(zip_content)) as zip_file:
                for member in zip_file.namelist():
                    filename = os.path.split(member)
                    if not filename[1]:
                        continue
                    new_filename = os.path.join(
                        filename[0].replace(dir_name, "."),
                        filename[1])
                    source = zip_file.open(member)
                    target = open(new_filename, "wb")
                    with source, target:
                        shutil.copyfileobj(source, target)
            success = True
        except Exception:
            mesgdcrt.FailureMessage("Error occured while extracting !!")
    if success:
        mesgdcrt.SuccessMessage("TBomb was updated to the latest version")
        mesgdcrt.GeneralMessage(
            "Please run the script again to load the latest version")
    else:
        mesgdcrt.FailureMessage("Unable to update TBomb.")
        mesgdcrt.WarningMessage(
            "Grab The Latest one From https://github.com/TheSpeedX/TBomb.git")

    sys.exit()


def do_git_update():
    success = False
    try:
        print(ALL_COLORS[0]+"UPDATING "+RESET_ALL, end='')
        process = subprocess.Popen("git checkout . && git pull ",
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        while process:
            print(ALL_COLORS[0]+'.'+RESET_ALL, end='')
            time.sleep(1)
            returncode = process.poll()
            if returncode is not None:
                break
        success = not process.returncode
    except Exception:
        success = False
    print("\n")

    if success:
        mesgdcrt.SuccessMessage("TBomb was updated to the latest version")
        mesgdcrt.GeneralMessage(
            "Please run the script again to load the latest version")
    else:
        mesgdcrt.FailureMessage("Unable to update TBomb.")
        mesgdcrt.WarningMessage("Make Sure To Install 'git' ")
        mesgdcrt.GeneralMessage("Then run command:")
        print(
            "git checkout . && "
            "git pull https://github.com/TheSpeedX/TBomb.git HEAD")
    sys.exit()


def update():
    if shutil.which('git'):
        do_git_update()
    else:
        do_zip_update()


def check_for_updates():
    if DEBUG_MODE:
        mesgdcrt.WarningMessage(
            "DEBUG MODE Enabled! Auto-Update check is disabled.")
        return
    mesgdcrt.SectionMessage("Checking for updates")
    fver = requests.get(
        "https://raw.githubusercontent.com/TheSpeedX/TBomb/master/.version"
    ).text.strip()
    if fver != __VERSION__:
        mesgdcrt.WarningMessage("An update is available")
        mesgdcrt.GeneralMessage("Starting update...")
        update()
    else:
        mesgdcrt.SuccessMessage("TBomb is up-to-date")
        mesgdcrt.GeneralMessage("Starting TBomb")


def notifyen():
    try:
        if DEBUG_MODE:
            url = "https://github.com/TheSpeedX/TBomb/raw/dev/.notify"
        else:
            url = "https://github.com/TheSpeedX/TBomb/raw/master/.notify"
        noti = requests.get(url).text.upper()
        if len(noti) > 10:
            mesgdcrt.SectionMessage("NOTIFICATION: " + noti)
            print()
    except Exception:
        pass


def get_phone_info():
    while True:
        target = ""
        cc = input(mesgdcrt.CommandMessage(
            "Enter your country code (Without +): "))
        cc = format_phone(cc)
        if not country_codes.get(cc, False):
            mesgdcrt.WarningMessage(
                "The country code ({cc}) that you have entered"
                " is invalid or unsupported".format(cc=cc))
            continue
        target = input(mesgdcrt.CommandMessage(
            "Enter the target number: +" + cc + " "))
        target = format_phone(target)
        if ((len(target) <= 6) or (len(target) >= 12)):
            mesgdcrt.WarningMessage(
                "The phone number ({target})".format(target=target) +
                "that you have entered is invalid")
            continue
        return (cc, target)


def get_mail_info():
    mail_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    while True:
        target = input(mesgdcrt.CommandMessage("Enter target mail: "))
        if not re.search(mail_regex, target, re.IGNORECASE):
            mesgdcrt.WarningMessage(
                "The mail ({target})".format(target=target) +
                " that you have entered is invalid")
            continue
        return target


def pretty_print(cc, target, success, failed):
    requested = success+failed
    mesgdcrt.SectionMessage("Bombing is in progress - Please be patient")
    mesgdcrt.GeneralMessage(
        "Please stay connected to the internet during bombing")
    mesgdcrt.GeneralMessage("Target       : " + cc + " " + target)
    mesgdcrt.GeneralMessage("Sent         : " + str(requested))
    mesgdcrt.GeneralMessage("Successful   : " + str(success))
    mesgdcrt.GeneralMessage("Failed       : " + str(failed))
    mesgdcrt.WarningMessage(
        "This tool was made for fun and research purposes only")
    mesgdcrt.SuccessMessage("TBomb was created by SpeedX")


def workernode(mode, cc, target, count, delay, max_threads):

    api = APIProvider(cc, target, mode, delay=delay)
    clr()
    mesgdcrt.SectionMessage("Gearing up the Bomber - Please be patient")
    mesgdcrt.GeneralMessage(
        "Please stay connected to the internet during bombing")
    mesgdcrt.GeneralMessage("API Version   : " + api.api_version)
    mesgdcrt.GeneralMessage("Target        : " + cc + target)
    mesgdcrt.GeneralMessage("Amount        : " + str(count))
    mesgdcrt.GeneralMessage("Threads       : " + str(max_threads) + " threads")
    mesgdcrt.GeneralMessage("Delay         : " + str(delay) +
                            " seconds")
    mesgdcrt.WarningMessage(
        "This tool was made for fun and research purposes only")
    print()
    input(mesgdcrt.CommandMessage(
        "Press [CTRL+Z] to suspend the bomber or [ENTER] to resume it"))

    if len(APIProvider.api_providers) == 0:
        mesgdcrt.FailureMessage("Your country/target is not supported yet")
        mesgdcrt.GeneralMessage("Feel free to reach out to us")
        input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
        bann_text()
        sys.exit()

    success, failed = 0, 0
    while success < count:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            jobs = []
            for i in range(count-success):
                jobs.append(executor.submit(api.hit))

            for job in as_completed(jobs):
                result = job.result()
                if result is None:
                    mesgdcrt.FailureMessage(
                        "Bombing limit for your target has been reached")
                    mesgdcrt.GeneralMessage("Try Again Later !!")
                    input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
                    bann_text()
                    sys.exit()
                if result:
                    success += 1
                else:
                    failed += 1
                clr()
                pretty_print(cc, target, success, failed)
    print("\n")
    mesgdcrt.SuccessMessage("Bombing completed!")
    time.sleep(1.5)
    bann_text()
    sys.exit()


def selectnode(mode="sms"):
    mode = mode.lower().strip()
    try:
