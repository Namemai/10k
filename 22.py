# -*- coding: utf-8 -*- 
import DRAGON
from DRAGON import *
from dkbot.ttypes import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from humanfriendly import format_timespan, format_size, format_number, format_length
from time import sleep
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse
from datetime import timedelta, date
from datetime import datetime
from gtts import gTTS
import html5lib,shutil
import wikipedia,goslate
import ffmpy
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
#import pyimgflip

cl = LineClient()
cl.log("Auth Token : " + str(cl.authToken))
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))

ki = LineClient()
ki.log("Auth Token : " + str(ki.authToken))
ki.log("Channel Access Token : " + str(channel.channelAccessToken))

kk = LineClient()
kk.log("Auth Token : " + str(kk.authToken))
kk.log("Channel Access Token : " + str(channel.channelAccessToken))

kc = LineClient()
kc.log("Auth Token : " + str(kc.authToken))
kc.log("Channel Access Token : " + str(channel.channelAccessToken))

kb = LineClient()
kb.log("Auth Token : " + str(kb.authToken))
kb.log("Channel Access Token : " + str(channel.channelAccessToken))

kd = LineClient()
kd.log("Auth Token : " + str(kd.authToken))
kd.log("Channel Access Token : " + str(channel.channelAccessToken))

ke = LineClient()
ke.log("Auth Token : " + str(ke.authToken))
ke.log("Channel Access Token : " + str(channel.channelAccessToken))

kf = LineClient()
kf.log("Auth Token : " + str(kf.authToken))
kf.log("Channel Access Token : " + str(channel.channelAccessToken))

k8 = LineClient()
k8.log("Auth Token : " + str(k8.authToken))
k8.log("Channel Access Token : " + str(channel.channelAccessToken))

k9 = LineClient()
k9.log("Auth Token : " + str(k9.authToken))
k9.log("Channel Access Token : " + str(channel.channelAccessToken))

k10 = LineClient()
k10.log("Auth Token : " + str(k10.authToken))
k10.log("Channel Access Token : " + str(channel.channelAccessToken))

k11 = LineClient()
k11.log("Auth Token : " + str(k11.authToken))
k11.log("Channel Access Token : " + str(channel.channelAccessToken))

k12 = LineClient()
k12.log("Auth Token : " + str(k12.authToken))
k12.log("Channel Access Token : " + str(channel.channelAccessToken))

k13 = LineClient()
k13.log("Auth Token : " + str(k13.authToken))
k13.log("Channel Access Token : " + str(channel.channelAccessToken))

k14 = LineClient()
k14.log("Auth Token : " + str(k14.authToken))
k14.log("Channel Access Token : " + str(channel.channelAccessToken))

k15 = LineClient()
k15.log("Auth Token : " + str(k15.authToken))
k15.log("Channel Access Token : " + str(channel.channelAccessToken))

k16 = LineClient()
k16.log("Auth Token : " + str(k16.authToken))
k16.log("Channel Access Token : " + str(channel.channelAccessToken))

k17 = LineClient()
k17.log("Auth Token : " + str(k17.authToken))
k17.log("Channel Access Token : " + str(channel.channelAccessToken))

k18 = LineClient()
k18.log("Auth Token : " + str(k18.authToken))
k18.log("Channel Access Token : " + str(channel.channelAccessToken))

k19 = LineClient()
k19.log("Auth Token : " + str(k19.authToken))
k19.log("Channel Access Token : " + str(channel.channelAccessToken))

k20 = LineClient()
k20.log("Auth Token : " + str(k20.authToken))
k20.log("Channel Access Token : " + str(channel.channelAccessToken))

kj = LineClient()
kj.log("Auth Token : " + str(kj.authToken))
kj.log("Channel Access Token : " + str(channel.channelAccessToken))

sw = LineClient()
sw.log("Auth Token : " + str(sw.authToken))
sw.log("Channel Access Token : " + str(channel.channelAccessToken))
print("\nBY: SELFBOT-BY:MAI\n")

poll = LinePoll(cl)
call = cl
creator = ["uc66e45201d1612eb4ce7b3a86bac4685"]
owner = ["uc66e45201d1612eb4ce7b3a86bac4685"]
admin = ["uc66e45201d1612eb4ce7b3a86bac4685"]
staff = ["uc66e45201d1612eb4ce7b3a86bac4685"]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kb.getProfile().mid
Emid = kd.getProfile().mid
Fmid = ke.getProfile().mid
Gmid = kf.getProfile().mid
mid8 = k8.getProfile().mid
mid9 = k9.getProfile().mid
mid10 = k10.getProfile().mid
mid11 = k11.getProfile().mid
mid12 = k12.getProfile().mid
mid13 = k13.getProfile().mid
mid14 = k14.getProfile().mid
mid15 = k15.getProfile().mid
mid16 = k16.getProfile().mid
mid17 = k17.getProfile().mid
mid18 = k18.getProfile().mid
mid19 = k19.getProfile().mid
mid20 = k20.getProfile().mid
Jmid = kj.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [cl,ki,kk,kc,kb,kd,ke,kf,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20,kj,sw]
ABC = [cl,ki,kk,kc,kb,kd,ke,kf,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20,kj,sw]
GHOST = [kj,sw]
Bots = [mid,Amid,Bmid,Dmid,Emid,Fmid,Gmid,mid8,mid9,mid10,mid11,mid12,mid13,mid14,mid15,mid16,mid17,mid18,mid19,mid20,Jmid,Zmid]
Saints = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectantijs = []
protectinvite = []
protectcancel = []
ghost = []
welcome = []
left = []
msg_dict = {}
msg_dict1 = {}

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = kb.getProfile().displayName
responsename5 = kd.getProfile().displayName
responsename6 = ke.getProfile().displayName
responsename7 = kf.getProfile().displayName
responsename1 = k8.getProfile().displayName
responsename2 = k9.getProfile().displayName
responsename3 = k10.getProfile().displayName
responsename4 = k11.getProfile().displayName
responsename5 = k12.getProfile().displayName
responsename6 = k13.getProfile().displayName
responsename7 = k14.getProfile().displayName
responsename1 = k15.getProfile().displayName
responsename2 = k16.getProfile().displayName
responsename3 = k17.getProfile().displayName
responsename4 = k18.getProfile().displayName
responsename5 = k19.getProfile().displayName
responsename6 = k20.getProfile().displayName
responsename8 = kj.getProfile().displayName
responsename9 = sw.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "SpamInvite":False,
    "changeCover":False,
    "changeVideo":False,
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userMention":{},
    "timeRestart": {},
    "server": {},
    "simiSimi":{},
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
}

wait = {
    "Limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":False,
    "contact":False,
    "invite":False,
    'autoJoin':False,
    'autoAdd':False,
    'autoBlock':True,
    'Timeline':False,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "mentionKick":False,
    "welcomeOn":False,
    "likeOn":True,
    "stickerOn":False,
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
            "displayName": "",
            "coverId": "",
            "pictureStatus": "",
            "statusMessage": ""
            },
    "unsend":False,
    "mention":"BY:MAI",
    "Respontag":"BY:MAI",
    "welcome":"BY:MAI",
    "leave":"Slamat tinggal sobat\nsmoga ktmu di lain hari nanti",
    "comment":"BY:MAI",
    "message":"Auto block ]\n ผมบล็อกคุนไว้แล้วกรุนารอผมมา 😭",
}
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

coverId = {}


lineProfile = cl.getProfile()
backup = cl.getProfile()
backup.displayName = lineProfile.displayName
backup.statusMessage = lineProfile.statusMessage
backup.pictureStatus = lineProfile.pictureStatus


with open('creator.json', 'r') as fp:
     creator = json.load(fp)
with open('owner.json', 'r') as fp:
     owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
Setmain = json.load(Setbot)
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

mulai = time.time()

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "「 Daftar Member 」\n\n1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "「✭」{}. ".format(str(no))
            else:
                textx += "\n「 Total {} Member 」".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
           
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "「 Auto Welcome 」\nɦαℓℓσ.......  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+" Di "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "「 Respon Leave 」\nBaper Ya Kak ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        ki.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

#message.createdTime -> 00:00:00
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict1[msg_id]

def atend1():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

#message.createdTime -> 00:00:00
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "🇹🇭❂͜͡➣      「 🤖 คำสั่ง 🤖 」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "คำสั่ง\n" + \
                  "🇹🇭❂͜͡➣ " + key + "คำสั่ง1\n" + \
                  "🇹🇭❂͜͡➣ " + key + "คำสั่ง2\n" + \
                  "🇹🇭❂͜͡➣ " + key + "คำสั่ง3\n" + \
                  "🇹🇭❂͜͡➣ " + key + "!mai\n" + \
                  "🇹🇭❂͜͡➣ " + key + "คท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เช็ค\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ข้อมูล\n" + \
                  "🇹🇭❂͜͡➣ " + key + "รีบอท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ออน\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ผส\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Sp\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Spb\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ประกาศ:「ข้อความ」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ตั้งบอทคท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ตั้งเชลคท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ตั้งแอดมินคท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ลบบอทคท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ลบเชลคท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ลบแอดมินคท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ปิดข้อความ\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เชคบอท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "คิกมา\n" + \
                  "🇹🇭❂͜͡➣ " + key + "คิกออก\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ผีมา\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ผีออก\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เชิญผี\n" + \
                  "🇹🇭         🤖 คำสั่งบอท 🤖\n" + \
                  "🇹🇭❂͜͡➣ " + key + "บอท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เชิญบอท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เชคดำ\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ล้างดำ\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ตั้งแอดมิน @\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ลบแอดมิน @\n" + \
                  "🇹🇭❂͜͡➣ " + key + "รูป1-20\n" + \
                  "🇹🇭❂͜͡➣ " + key + "protectkick on\off\n" + \
                  "🇹🇭❂͜͡➣ " + key + "protectjoin on\off\n" + \
                  "🇹🇭❂͜͡➣ " + key + "protectinvite on\off\n" + \
                  "🇹🇭❂͜͡➣ " + key + "protecturl on\off\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Ghost on\off\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Allpro on\off\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Antijs on\n" + \
                  "🇹🇭❂͜͡➣ BY:MAI"

    return helpMessage

def help1():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "🇹🇭❂͜͡➣      「 🤖 คำสั่ง1 🤖 」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "แทค\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ข้อมูลกลุ่ม\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เปิดลิ้ง\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ปิดลิ้ง\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ลิ้งกลุ่ม\n" + \
                  "🇹🇭❂͜͡➣ " + key + "กลุ่ม\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ข้อมูลกลุ่ม「ลำดับ」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ลบแชท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ไอดี「@」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ขโมย「@」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ปก「@」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ก็อป「@」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "คืนร่าง\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ลบรัน\n" + \
                  "🇹🇭❂͜͡➣ " + key + "sᴘᴀᴍᴄᴀʟʟᴛᴏ 「จำนวน」 「@」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "แทค「จำนวน」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "แทค「@」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "รัวคอล「จำนวน」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "รัวคอล\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เปลี่ยนชื่อ「ชื่อ」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เปลี่ยนรูป「ส่งรูป」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "รูปวิดีโอ 「ส่งวิดีโอ」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เปลี่ยนรูปกลุ่ม\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ของขวัญ:「ไอดี」「จำนวน」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "แสปม:「ไอดี」「จำนวน」\n" + \
                  "🇹🇭❂͜͡➣ BY:MAI"
                  
    return helpMessage1

def help2():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2= "      「 🤖 คำสั่ง2 🤖 」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ᴡᴇʟᴄᴏᴍᴇ「ᴏɴ/ᴏғғ」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เปิดเชิญ\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เปิดเชิญ\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เปิดสติกเกอร์\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ปิดสติกเกอร์\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เปิดยกเลิก\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ปิดยกเลิก\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เปิดคนแอบ\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ปิดคนแอบ\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เปิดแทค\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ปิดแทค\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เปิดเชคโพส\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ปิดเชคโพส\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เปิดคท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ปิดคท\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เปิดเข้ากลุ่ม\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ปิดเข้ากลุ่ม\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เปิดคนแอด\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ปิดคนแอด\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เปิดคนออก\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ปิดคนออก\n" + \
                  "🇹🇭❂͜͡➣ " + key + "เปิดมุดลิ้ง\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ปิดมุดลิ้ง\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ข้อความคนแอบ\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ข้อความแสปม\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ข้อความคนแอด\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ข้อความคนแทค\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ข้อความคนออก\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ข้อความคนเข้า\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ตั้งคนแอบ「ข้อความ」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ตั้งแสปม「ข้อความ」」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ตั้งคนแอด「ข้อความ」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ตั้งแทค「ข้อความ」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ตั้งคนออก「ข้อความ」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ตั้งคนเข้า「ข้อความ」\n" + \
                  "🇹🇭❂͜͡➣ BY:MAI"

    return helpMessage2

def help3():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "      「 MUSIK 」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Musik「Nama Penyanyi」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Listmp3\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Addmp3「Teks」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Dellmp3「Teks」\n" + \
                  "🇹🇭❂͜͡➣   「 VIDEO 」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Listvideo\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Addvideo「Teks」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Dellvideo「Teks」\n" + \
                  "🇹🇭❂͜͡➣   「 GAMBAR 」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Listimage\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Addimg「Teks」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Dellimg「Teks」\n" + \
                  "🇹🇭❂͜͡➣   「 STICKER 」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Liststicker\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Addsticker「Teks」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Dellsticker「Teks」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Kode wilayah\n" + \
                  "🇹🇭❂͜͡➣   「 MEDIA LAIN 」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "ยูทูป「ชื่อคลิป」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Lihat 「Kode wilayah cctv」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-fs「Query」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-line「ID Line」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-apk「Query」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-gif「Query」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-xxx「Query」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-anime「Query」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-mimpi「Query」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-audio「Query」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-mp3「Query」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-video「Query」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-bintang「Zodiak」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-zodiak「Zodiak」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-sholat「Nama Kota」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-cuaca「Nama Kota」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-lokasi「Nama Kota」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-lirik「Judul Lagu」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-instagram「User Name」\n" + \
                  "🇹🇭❂͜͡➣ " + key + "Get-date「tgl-bln-thn」\n" + \
                  "🇹🇭❂͜͡➣ BY:MAI"

    return helpMessage3

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return

        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventJoinByTicket = False
                            cl.updateGroup(X)
                            Ti = cl.reissueGroupTicket(op.param1)
                            kj.acceptGroupInvitationByTicket(op.param1,Ti)
                            kj.sendMessage(op.param1,"wah kiker mainan qr minta di cipok")
                            kj.kickoutFromGroup(op.param1,[op.param2])
                            wait["blacklist"][op.param2] = True
                            X = kj.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            kj.updateGroup(X)
                            kj.leaveGroup(op.param1)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)
                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kk.updateGroup(X)
                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.updateGroup(X)
                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if kb.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            kb.reissueGroupTicket(op.param1)
                                            X = kb.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            cl.updateGroup(X)
                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if kd.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                kd.reissueGroupTicket(op.param1)
                                                X = kd.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                kd.updateGroup(X)
                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        try:
                                            if ke.getGroup(op.param1).preventedJoinByTicket == False:
                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    ke.reissueGroupTicket(op.param1)
                                                    X = ke.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    ke.updateGroup(X)
                                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)            
                                        except:
                                            try:
                                                if kf.getGroup(op.param1).preventedJoinByTicket == False:
                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                        kf.reissueGroupTicket(op.param1)
                                                        X = kf.getGroup(op.param1)
                                                        X.preventedJoinByTicket = True
                                                        kf.updateGroup(X)
                                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)           
                                            except:
                                                try:
                                                    if k20.getGroup(op.param1).preventedJoinByTicket == False:
                                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                            k20.reissueGroupTicket(op.param1)
                                                            X = k20.getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            k20.updateGroup(X)
                                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)          
                                                except:
                                                    try:
                                                        if sw.getGroup(op.param1).preventedJoinByTicket == False:
                                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                sw.reissueGroupTicket(op.param1)
                                                                X = sw.getGroup(op.param1)
                                                                X.preventedJoinByTicket = True
                                                                sw.updateGroup(X)
                                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)             
                                                    except:
                                                        pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
                        kd.leaveGroup(op.param1)
                    else:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)           
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
                        kf.leaveGroup(op.param1)
                    else:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
            if mid8 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k8.acceptGroupInvitation(op.param1)
                        ginfo = k8.getGroup(op.param1)
                    else:
                        k8.acceptGroupInvitation(op.param1)
                        ginfo = k8.getGroup(op.param1)
            if mid9 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k9.acceptGroupInvitation(op.param1)
                        ginfo = k9.getGroup(op.param1)
                        k9.leaveGroup(op.param1)
                    else:
                        k9.acceptGroupInvitation(op.param1)
                        ginfo = k9.getGroup(op.param1)
            if mid10 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k10.acceptGroupInvitation(op.param1)
                        ginfo = k10.getGroup(op.param1)
                        k10.leaveGroup(op.param1)
                    else:
                        k10.acceptGroupInvitation(op.param1)
                        ginfo = k10.getGroup(op.param1)
            if mid11 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k11.acceptGroupInvitation(op.param1)
                        ginfo = k11.getGroup(op.param1)
                        k11.leaveGroup(op.param1)
                    else:
                        k11.acceptGroupInvitation(op.param1)
                        ginfo = k11.getGroup(op.param1)
            if mid12 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k12.acceptGroupInvitation(op.param1)
                        ginfo = k12.getGroup(op.param1)
                        k12.leaveGroup(op.param1)
                    else:
                        k12.acceptGroupInvitation(op.param1)
                        ginfo = k12.getGroup(op.param1)
            if mid13 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k13.acceptGroupInvitation(op.param1)
                        ginfo = k13.getGroup(op.param1)
                        k13.leaveGroup(op.param1)
                    else:
                        k13.acceptGroupInvitation(op.param1)
                        ginfo = k13.getGroup(op.param1)
            if mid14 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k14.acceptGroupInvitation(op.param1)
                        ginfo = k14.getGroup(op.param1)
                        k14.leaveGroup(op.param1)
                    else:
                        k14.acceptGroupInvitation(op.param1)
                        ginfo = k14.getGroup(op.param1)           
            if mid15 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k15.acceptGroupInvitation(op.param1)
                        ginfo = k15.getGroup(op.param1)
                        k15.leaveGroup(op.param1)
                    else:
                        k15.acceptGroupInvitation(op.param1)
                        ginfo = k15.getGroup(op.param1)
            if mid16 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k16.acceptGroupInvitation(op.param1)
                        ginfo = k16.getGroup(op.param1)
                        k16.leaveGroup(op.param1)
                    else:
                        k16.acceptGroupInvitation(op.param1)
                        ginfo = k16.getGroup(op.param1)
            if mid17 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k17.acceptGroupInvitation(op.param1)
                        ginfo = k17.getGroup(op.param1)
                        k17.leaveGroup(op.param1)
                    else:
                        k17.acceptGroupInvitation(op.param1)
                        ginfo = k17.getGroup(op.param1)
            if mid18 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k18.acceptGroupInvitation(op.param1)
                        ginfo = k18.getGroup(op.param1)
                        k18.leaveGroup(op.param1)
                    else:
                        k18.acceptGroupInvitation(op.param1)
                        ginfo = k18.getGroup(op.param1)
            if mid19 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k19.acceptGroupInvitation(op.param1)
                        ginfo = k19.getGroup(op.param1)
                        k19.leaveGroup(op.param1)
                    else:
                        k19.acceptGroupInvitation(op.param1)
                        ginfo = k19.getGroup(op.param1)
            if mid20 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k20.acceptGroupInvitation(op.param1)
                        ginfo = k20.getGroup(op.param1)
                        k20.leaveGroup(op.param1)
                    else:
                        k20.acceptGroupInvitation(op.param1)
                        ginfo = k20.getGroup(op.param1)                       

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                ki.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    kk.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        kc.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = kb.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            kb.cancelGroupInvitation(op.param1,[_mid])
                                    except:
                                        try:
                                            group = kd.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                kd.cancelGroupInvitation(op.param1,[_mid])
                                        except:
                                            try:
                                                group = kd.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for _mid in gMembMids:
                                                    kd.cancelGroupInvitation(op.param1,[_mid])
                                            except:
                                                pass

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                    
        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                    
        if op.type == 13:
            if op.param3 in wait["blacklist"]:
                    try:
                        random.choice(ABC).cancelGroupInvitation(op.param1,[op.param3])
                    except:
                        pass
 
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)
                
        if op.type == 17:
            if op.param1 in left:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leftMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)
                sendMention(to, "ãAuto Mentionã\nâ«@!", [sender])
                cl.sendContact(to, sender)    
                
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k18.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            k8.kickoutFromGroup(op.param1,[op.param2])          
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                kb.kickoutFromGroup(op.param1,[op.param2])         
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                               try:
                                                   if op.param3 not in wait["blacklist"]:
                                                       ke.kickoutFromGroup(op.param1,[op.param2])      
                                               except:
                                                  try:
                                                      if op.param3 not in wait["blacklist"]:
                                                          kf.kickoutFromGroup(op.param1,[op.param2]) 
                                                  except:
                                                     try:
                                                         if op.param3 not in wait["blacklist"]:
                                                             k9.kickoutFromGroup(op.param1,[op.param2])        
                                                     except:
                                                        try:
                                                            if op.param3 not in wait["blacklist"]:
                                                                k10.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                if op.param3 not in wait["blacklist"]:
                                                                    k11.kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                               try:
                                                                   if op.param3 not in wait["blacklist"]:
                                                                       k12.kickoutFromGroup(op.param1,[op.param2])
                                                               except:
                                                                  try:
                                                                      if op.param3 not in wait["blacklist"]:
                                                                          k13.kickoutFromGroup(op.param1,[op.param2])  
                                                                  except:
                                                                     try:
                                                                         if op.param3 not in wait["blacklist"]:
                                                                             k14.kickoutFromGroup(op.param1,[op.param2])
                                                                     except:
                                                                        try:
                                                                            if op.param3 not in wait["blacklist"]:
                                                                                k15.kickoutFromGroup(op.param1,[op.param2])  
                                                                        except:
                                                                           try:
                                                                               if op.param3 not in wait["blacklist"]:
                                                                                    k16.kickoutFromGroup(op.param1,[op.param2])        
                                                                           except:
                                                                               pass  
                return

        if op.type == 5:
              if wait["autoAdd"] == True:
                  cl.findAndAddContactsByMid(op.param1)
                  sendMention(op.param1, op.param1, "Haii ", ", terimakasih sudah add saya")
                  cl.sendText(op.param1, wait["message"])
                  cl.sendContact(op.param1, "uc66e45201d1612eb4ce7b3a86bac4685")

        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if wait["autoBlock"] == True:
                cl.sendText(op.param1, wait["message"])
                cl.sendContact(op.param1, "uc66e45201d1612eb4ce7b3a86bac4685")
                cl.blockContact(op.param1)

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                	pass

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                ki.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    kk.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        kc.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = kb.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            kb.cancelGroupInvitation(op.param1,[_mid])
                                    except:
                                        try:
                                            group = k8.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                k8.cancelGroupInvitation(op.param1,[_mid])
                                        except:
                                            try:
                                                group = k9.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for _mid in gMembMids:
                                                    k9.cancelGroupInvitation(op.param1,[_mid])
                                            except:
                                                pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
                
        if op.type == 19:
            if op.param1 in ผี:
                try:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        sw.sendMessage(op.param1,"Wah kiker tempe mai kick orang minta di hajar")
                        sw.leaveGroup(op.param1)
                        kj.leaveGroup(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                except:
                    try:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            G = ki.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            ki.updateGroup(G)
                            invsend = 0
                            Ticket = ki.reissueGroupTicket(op.param1)
                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                            random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                            wait["blacklist"][op.param2] = True
                            sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                            sw.leaveGroup(op.param1)
                            kj.leaveGroup(op.param1)
                            X = ki.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            ki.updateGroup(X)
                    except:
                        try:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                G = kk.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                kk.updateGroup(G)
                                invsend = 0
                                Ticket = kk.reissueGroupTicket(op.param1)
                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True
                                sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                                sw.leaveGroup(op.param1)
                                kj.leaveGroup(op.param1)
                                X = kk.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                kk.updateGroup(X)
                        except:
                            try:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kc.updateGroup(G)
                                    invsend = 0
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                    wait["blacklist"][op.param2] = True
                                    sw.sendMessage(op.param1,"Wah kiker tempe mai kick orang minta di hajar")
                                    sw.leaveGroup(op.param1)
                                    kj.leaveGroup(op.param1)
                                    X = kc.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kc.updateGroup(X)
                            except:
                                try:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        G = kb.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        kb.updateGroup(G)
                                        invsend = 0
                                        Ticket = kb.reissueGroupTicket(op.param1)
                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                        wait["blacklist"][op.param2] = True
                                        sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                                        sw.leaveGroup(op.param1)
                                        kj.leaveGroup(op.param1)
                                        X = kb.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kb.updateGroup(X)
                                except:
                                    try:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            G = kd.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kd.updateGroup(G)
                                            invsend = 0
                                            Ticket = kd.reissueGroupTicket(op.param1)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                            wait["blacklist"][op.param2] = True
                                            sw.sendMessage(op.param1,"Terdeteksi Kicker,Maaf anda melangar")
                                            sw.leaveGroup(op.param1)
                                            kj.leaveGroup(op.param1)
                                            X = kd.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            kd.updateGroup(X)
                                    except:
                                        try:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                G = ke.getGroup(op.param1)
                                                G.preventedJoinByTicket = False
                                                ke.updateGroup(G)
                                                invsend = 0
                                                Ticket = ke.reissueGroupTicket(op.param1)
                                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                wait["blacklist"][op.param2] = True
                                                sw.sendMessage(op.param1,"Terdeteksi kicker\nMaaf anda mepanggar")
                                                sw.leaveGroup(op.param1)
                                                kj.leaveGroup(op.param1)
                                                X = ke.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                ke.updateGroup(X)
                                        except:
                                            try:
                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    G = kf.getGroup(op.param1)
                                                    G.preventedJoinByTicket = False
                                                    kf.updateGroup(G)
                                                    invsend = 0
                                                    Ticket = kf.reissueGroupTicket(op.param1)
                                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                    wait["blacklist"][op.param2] = True
                                                    sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                                                    sw.leaveGroup(op.param1)
                                                    kj.leaveGroup(op.param1)
                                                    X = kf.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    kf.updateGroup(X)      
                                            except:
                                                try:
                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                        G = ki.getGroup(op.param1)
                                                        G.preventedJoinByTicket = False
                                                        ki.updateGroup(G)
                                                        invsend = 0
                                                        Ticket = ki.reissueGroupTicket(op.param1)
                                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                        wait["blacklist"][op.param2] = True
                                                        sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                                                        sw.leaveGroup(op.param1)
                                                        kj.leaveGroup(op.param1)
                                                        X = ki.getGroup(op.param1)
                                                        X.preventedJoinByTicket = True
                                                        ki.updateGroup(X)  
                                                except:
                                                    try:
                                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                            G = k8.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            k8.updateGroup(G)
                                                            invsend = 0
                                                            Ticket = k8.reissueGroupTicket(op.param1)
                                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                            wait["blacklist"][op.param2] = True
                                                            sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                                                            sw.leaveGroup(op.param1)
                                                            kj.leaveGroup(op.param1)
                                                            X = kh.getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            kh.updateGroup(X)     
                                                    except:
                                                        pass
                  
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sw.acceptGroupInvitation(op.param1)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        cl.findAndAddContactsByMid(op.param1,[Zmid])
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass
                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                else:
                    pass
            except:
                pass
                
        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                    except:
                        pass
         
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            ki.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            ki.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.inviteIntoGroup(op.param1,[op.param3])
                                                    cl.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                                        k8.inviteIntoGroup(op.param1,[op.param3])
                                                        cl.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                                            k9.inviteIntoGroup(op.param1,[op.param3])
                                                            cl.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kk.updateGroup(G)
                                            Ticket = kk.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                                ki.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                                    k8.inviteIntoGroup(op.param1,[op.param3])
                                                    ki.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k9.kickoutFromGroup(op.param1,[op.param2])
                                                        k9.inviteIntoGroup(op.param1,[op.param3])
                                                        ki.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k10.kickoutFromGroup(op.param1,[op.param2])
                                                            k10.inviteIntoGroup(op.param1,[op.param3])
                                                            ki.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kd.kickoutFromGroup(op.param1,[op.param2])
                                kd.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                    kk.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kc.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kc.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kc.updateGroup(G)
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k8.kickoutFromGroup(op.param1,[op.param2])
                                                k8.inviteIntoGroup(op.param1,[op.param3])
                                                kk.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k9.kickoutFromGroup(op.param1,[op.param2])
                                                    k9.inviteIntoGroup(op.param1,[op.param3])
                                                    kk.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k10.kickoutFromGroup(op.param1,[op.param2])
                                                        k10.inviteIntoGroup(op.param1,[op.param3])
                                                        kk.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k11.kickoutFromGroup(op.param1,[op.param2])
                                                            k11.inviteIntoGroup(op.param1,[op.param3])
                                                            kk.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kd.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                    kf.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                        k8.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kb.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            kb.updateGroup(G)
                                            Ticket = kb.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kb.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kb.updateGroup(G)
                                            Ticket = kb.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k9.kickoutFromGroup(op.param1,[op.param2])
                                                k9.inviteIntoGroup(op.param1,[op.param3])
                                                kc.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k10.kickoutFromGroup(op.param1,[op.param2])
                                                    k10.inviteIntoGroup(op.param1,[op.param3])
                                                    kc.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k11.kickoutFromGroup(op.param1,[op.param2])
                                                        k11.inviteIntoGroup(op.param1,[op.param3])
                                                        kc.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k12.kickoutFromGroup(op.param1,[op.param2])
                                                            k12.inviteIntoGroup(op.param1,[op.param3])
                                                            kc.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        kd.inviteIntoGroup(op.param1,[op.param3])
                        kb.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            kb.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kf.kickoutFromGroup(op.param1,[op.param2])
                                kf.inviteIntoGroup(op.param1,[op.param3])
                                kb.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                    k8.inviteIntoGroup(op.param1,[op.param3])
                                    kb.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k9.kickoutFromGroup(op.param1,[op.param2])
                                        k9.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kd.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.updateGroup(G)
                                            Ticket = kd.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kd.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kd.updateGroup(G)
                                            Ticket = kd.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k10.kickoutFromGroup(op.param1,[op.param2])
                                                k10.inviteIntoGroup(op.param1,[op.param3])
                                                kb.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k11.kickoutFromGroup(op.param1,[op.param2])
                                                    k11.inviteIntoGroup(op.param1,[op.param3])
                                                    kb.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k12.kickoutFromGroup(op.param1,[op.param2])
                                                        k12.inviteIntoGroup(op.param1,[op.param3])
                                                        kb.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k13.kickoutFromGroup(op.param1,[op.param2])
                                                            k13.inviteIntoGroup(op.param1,[op.param3])
                                                            kb.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass
                return

            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kd.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k9.kickoutFromGroup(op.param1,[op.param2])
                            k9.inviteIntoGroup(op.param1,[op.param3])
                            kd.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kf.kickoutFromGroup(op.param1,[op.param2])
                                kf.inviteIntoGroup(op.param1,[op.param3])
                                kd.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                    k8.inviteIntoGroup(op.param1,[op.param3])
                                    kd.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k10.kickoutFromGroup(op.param1,[op.param2])
                                        k10.inviteIntoGroup(op.param1,[op.param3])
                                        kd.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = ke.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.updateGroup(G)
                                            Ticket = ke.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = ke.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            ke.updateGroup(G)
                                            Ticket = ke.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k11.kickoutFromGroup(op.param1,[op.param2])
                                                k11.inviteIntoGroup(op.param1,[op.param3])
                                                kd.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k12.kickoutFromGroup(op.param1,[op.param2])
                                                    k12.inviteIntoGroup(op.param1,[op.param3])
                                                    kd.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k13.kickoutFromGroup(op.param1,[op.param2])
                                                        k13.inviteIntoGroup(op.param1,[op.param3])
                                                        kd.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k14.kickoutFromGroup(op.param1,[op.param2])
                                                            k14.inviteIntoGroup(op.param1,[op.param3])
                                                            kd.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass
                return

            if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                        kf.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k8.kickoutFromGroup(op.param1,[op.param2])
                            k8.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k9.kickoutFromGroup(op.param1,[op.param2])
                                k9.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k10.kickoutFromGroup(op.param1,[op.param2])
                                    k10.inviteIntoGroup(op.param1,[op.param3])
                                    ke.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k11.kickoutFromGroup(op.param1,[op.param2])
                                        k11.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kf.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            kf.updateGroup(G)
                                            Ticket = kf.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kf.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kf.updateGroup(G)
                                            Ticket = kf.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k12.kickoutFromGroup(op.param1,[op.param2])
                                                k12.inviteIntoGroup(op.param1,[op.param3])
                                                ke.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k13.kickoutFromGroup(op.param1,[op.param2])
                                                    k13.inviteIntoGroup(op.param1,[op.param3])
                                                    ke.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k14.kickoutFromGroup(op.param1,[op.param2])
                                                        k14.inviteIntoGroup(op.param1,[op.param3])
                                                        ke.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k15.kickoutFromGroup(op.param1,[op.param2])
                                                            k15.inviteIntoGroup(op.param1,[op.param3])
                                                            ke.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass
                return

            if mid8 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k8.kickoutFromGroup(op.param1,[op.param2])
                        k8.inviteIntoGroup(op.param1,[op.param3])
                        kf.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k9.kickoutFromGroup(op.param1,[op.param2])
                            k9.inviteIntoGroup(op.param1,[op.param3])
                            kf.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k10.kickoutFromGroup(op.param1,[op.param2])
                                k10.inviteIntoGroup(op.param1,[op.param3])
                                kf.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k11.kickoutFromGroup(op.param1,[op.param2])
                                    k11.inviteIntoGroup(op.param1,[op.param3])
                                    kf.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k12.kickoutFromGroup(op.param1,[op.param2])
                                        k12.inviteIntoGroup(op.param1,[op.param3])
                                        kf.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k8.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k8.kickoutFromGroup(op.param1,[op.param2])
                                            k8.updateGroup(G)
                                            Ticket = k8.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k8.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k8.updateGroup(G)
                                            Ticket = k8.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k13.kickoutFromGroup(op.param1,[op.param2])
                                                k13.inviteIntoGroup(op.param1,[op.param3])
                                                kf.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k14.kickoutFromGroup(op.param1,[op.param2])
                                                    k14.inviteIntoGroup(op.param1,[op.param3])
                                                    kf.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k15.kickoutFromGroup(op.param1,[op.param2])
                                                        k15.inviteIntoGroup(op.param1,[op.param3])
                                                        kf.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k16.kickoutFromGroup(op.param1,[op.param2])
                                                            k16.inviteIntoGroup(op.param1,[op.param3])
                                                            kf.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass                                    
                return

            if mid9 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k9.kickoutFromGroup(op.param1,[op.param2])
                        k9.inviteIntoGroup(op.param1,[op.param3])
                        k8.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k10.kickoutFromGroup(op.param1,[op.param2])
                            k10.inviteIntoGroup(op.param1,[op.param3])
                            k8.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k11.kickoutFromGroup(op.param1,[op.param2])
                                k11.inviteIntoGroup(op.param1,[op.param3])
                                k8.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k12.kickoutFromGroup(op.param1,[op.param2])
                                    k12.inviteIntoGroup(op.param1,[op.param3])
                                    k8.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k13.kickoutFromGroup(op.param1,[op.param2])
                                        k13.inviteIntoGroup(op.param1,[op.param3])
                                        k8.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k9.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                            k9.updateGroup(G)
                                            Ticket = k9.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k9.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k9.updateGroup(G)
                                            Ticket = k9.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k14.kickoutFromGroup(op.param1,[op.param2])
                                                k14.inviteIntoGroup(op.param1,[op.param3])
                                                k8.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k15.kickoutFromGroup(op.param1,[op.param2])
                                                    k15.inviteIntoGroup(op.param1,[op.param3])
                                                    k8.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k16.kickoutFromGroup(op.param1,[op.param2])
                                                        k16.inviteIntoGroup(op.param1,[op.param3])
                                                        k8.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k17.kickoutFromGroup(op.param1,[op.param2])
                                                            k17.inviteIntoGroup(op.param1,[op.param3])
                                                            k8.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass
                return

            if mid10 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k10.kickoutFromGroup(op.param1,[op.param2])
                        k10.inviteIntoGroup(op.param1,[op.param3])
                        k9.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k11.kickoutFromGroup(op.param1,[op.param2])
                            k11.inviteIntoGroup(op.param1,[op.param3])
                            k9.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k12.kickoutFromGroup(op.param1,[op.param2])
                                k12.inviteIntoGroup(op.param1,[op.param3])
                                k9.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k13.kickoutFromGroup(op.param1,[op.param2])
                                    k13.inviteIntoGroup(op.param1,[op.param3])
                                    k9.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k14.kickoutFromGroup(op.param1,[op.param2])
                                        k14.inviteIntoGroup(op.param1,[op.param3])
                                        k9.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k10.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k10.kickoutFromGroup(op.param1,[op.param2])
                                            k10.updateGroup(G)
                                            Ticket = k10.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k10.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k10.updateGroup(G)
                                            Ticket = k10.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k15.kickoutFromGroup(op.param1,[op.param2])
                                                k15.inviteIntoGroup(op.param1,[op.param3])
                                                k9.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k16.kickoutFromGroup(op.param1,[op.param2])
                                                    k16.inviteIntoGroup(op.param1,[op.param3])
                                                    k9.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k17.kickoutFromGroup(op.param1,[op.param2])
                                                        k17.inviteIntoGroup(op.param1,[op.param3])
                                                        k9.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k18.kickoutFromGroup(op.param1,[op.param2])
                                                            k18.inviteIntoGroup(op.param1,[op.param3])
                                                            k9.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid11 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k11.kickoutFromGroup(op.param1,[op.param2])
                        k11.inviteIntoGroup(op.param1,[op.param3])
                        k10.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k12.kickoutFromGroup(op.param1,[op.param2])
                            k12.inviteIntoGroup(op.param1,[op.param3])
                            k10.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k13.kickoutFromGroup(op.param1,[op.param2])
                                k13.inviteIntoGroup(op.param1,[op.param3])
                                k10.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k14.kickoutFromGroup(op.param1,[op.param2])
                                    k14.inviteIntoGroup(op.param1,[op.param3])
                                    k10.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k15.kickoutFromGroup(op.param1,[op.param2])
                                        k15.inviteIntoGroup(op.param1,[op.param3])
                                        k10.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k11.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k11.kickoutFromGroup(op.param1,[op.param2])
                                            k11.updateGroup(G)
                                            Ticket = k11.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k11.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k11.updateGroup(G)
                                            Ticket = k11.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k16.kickoutFromGroup(op.param1,[op.param2])
                                                k16.inviteIntoGroup(op.param1,[op.param3])
                                                k10.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k17.kickoutFromGroup(op.param1,[op.param2])
                                                    k17.inviteIntoGroup(op.param1,[op.param3])
                                                    k10.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k18.kickoutFromGroup(op.param1,[op.param2])
                                                        k18.inviteIntoGroup(op.param1,[op.param3])
                                                        k10.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k19.kickoutFromGroup(op.param1,[op.param2])
                                                            k19.inviteIntoGroup(op.param1,[op.param3])
                                                            k10.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid12 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k12.kickoutFromGroup(op.param1,[op.param2])
                        k12.inviteIntoGroup(op.param1,[op.param3])
                        k11.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k13.kickoutFromGroup(op.param1,[op.param2])
                            k13.inviteIntoGroup(op.param1,[op.param3])
                            k11.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k14.kickoutFromGroup(op.param1,[op.param2])
                                k14.inviteIntoGroup(op.param1,[op.param3])
                                k11.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k15.kickoutFromGroup(op.param1,[op.param2])
                                    k15.inviteIntoGroup(op.param1,[op.param3])
                                    k11.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k16.kickoutFromGroup(op.param1,[op.param2])
                                        k16.inviteIntoGroup(op.param1,[op.param3])
                                        k11.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k12.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k12.kickoutFromGroup(op.param1,[op.param2])
                                            k12.updateGroup(G)
                                            Ticket = k12.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k12.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k12.updateGroup(G)
                                            Ticket = k12.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k17.kickoutFromGroup(op.param1,[op.param2])
                                                k17.inviteIntoGroup(op.param1,[op.param3])
                                                k11.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k18.kickoutFromGroup(op.param1,[op.param2])
                                                    k18.inviteIntoGroup(op.param1,[op.param3])
                                                    k11.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k19.kickoutFromGroup(op.param1,[op.param2])
                                                        k19.inviteIntoGroup(op.param1,[op.param3])
                                                        k11.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k20.kickoutFromGroup(op.param1,[op.param2])
                                                            k20.inviteIntoGroup(op.param1,[op.param3])
                                                            k11.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid13 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k13.kickoutFromGroup(op.param1,[op.param2])
                        k13.inviteIntoGroup(op.param1,[op.param3])
                        k12.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k14.kickoutFromGroup(op.param1,[op.param2])
                            k14.inviteIntoGroup(op.param1,[op.param3])
                            k12.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k15.kickoutFromGroup(op.param1,[op.param2])
                                k15.inviteIntoGroup(op.param1,[op.param3])
                                k12.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k16.kickoutFromGroup(op.param1,[op.param2])
                                    k16.inviteIntoGroup(op.param1,[op.param3])
                                    k12.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k17.kickoutFromGroup(op.param1,[op.param2])
                                        k17.inviteIntoGroup(op.param1,[op.param3])
                                        k12.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k13.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k13.kickoutFromGroup(op.param1,[op.param2])
                                            k13.updateGroup(G)
                                            Ticket = k13.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k13.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k13.updateGroup(G)
                                            Ticket = k13.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k18.kickoutFromGroup(op.param1,[op.param2])
                                                k18.inviteIntoGroup(op.param1,[op.param3])
                                                k12.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k19.kickoutFromGroup(op.param1,[op.param2])
                                                    k19.inviteIntoGroup(op.param1,[op.param3])
                                                    k12.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k20.kickoutFromGroup(op.param1,[op.param2])
                                                        k20.inviteIntoGroup(op.param1,[op.param3])
                                                        k12.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                                            k12.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid14 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k14.kickoutFromGroup(op.param1,[op.param2])
                        k14.inviteIntoGroup(op.param1,[op.param3])
                        k13.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k15.kickoutFromGroup(op.param1,[op.param2])
                            k15.inviteIntoGroup(op.param1,[op.param3])
                            k13.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k16.kickoutFromGroup(op.param1,[op.param2])
                                k16.inviteIntoGroup(op.param1,[op.param3])
                                k13.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k17.kickoutFromGroup(op.param1,[op.param2])
                                    k17.inviteIntoGroup(op.param1,[op.param3])
                                    k13.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k18.kickoutFromGroup(op.param1,[op.param2])
                                        k18.inviteIntoGroup(op.param1,[op.param3])
                                        k13.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k14.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k14.kickoutFromGroup(op.param1,[op.param2])
                                            k14.updateGroup(G)
                                            Ticket = k14.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k14.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k14.updateGroup(G)
                                            Ticket = k14.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k19.kickoutFromGroup(op.param1,[op.param2])
                                                k19.inviteIntoGroup(op.param1,[op.param3])
                                                k13.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k20.kickoutFromGroup(op.param1,[op.param2])
                                                    k20.inviteIntoGroup(op.param1,[op.param3])
                                                    k13.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                                        k13.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                                            k13.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid15 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k15.kickoutFromGroup(op.param1,[op.param2])
                        k15.inviteIntoGroup(op.param1,[op.param3])
                        k14.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k16.kickoutFromGroup(op.param1,[op.param2])
                            k16.inviteIntoGroup(op.param1,[op.param3])
                            k14.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k17.kickoutFromGroup(op.param1,[op.param2])
                                k17.inviteIntoGroup(op.param1,[op.param3])
                                k14.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k18.kickoutFromGroup(op.param1,[op.param2])
                                    k18.inviteIntoGroup(op.param1,[op.param3])
                                    k14.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k19.kickoutFromGroup(op.param1,[op.param2])
                                        k19.inviteIntoGroup(op.param1,[op.param3])
                                        k14.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k15.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k15.kickoutFromGroup(op.param1,[op.param2])
                                            k15.updateGroup(G)
                                            Ticket = k15.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k15.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k15.updateGroup(G)
                                            Ticket = k15.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k20.kickoutFromGroup(op.param1,[op.param2])
                                                k20.inviteIntoGroup(op.param1,[op.param3])
                                                k14.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                                    k14.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                                        k14.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                                            k14.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass 
                return

            if mid16 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k16.kickoutFromGroup(op.param1,[op.param2])
                        k16.inviteIntoGroup(op.param1,[op.param3])
                        k15.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k17.kickoutFromGroup(op.param1,[op.param2])
                            k17.inviteIntoGroup(op.param1,[op.param3])
                            k15.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k18.kickoutFromGroup(op.param1,[op.param2])
                                k18.inviteIntoGroup(op.param1,[op.param3])
                                k15.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k19.kickoutFromGroup(op.param1,[op.param2])
                                    k19.inviteIntoGroup(op.param1,[op.param3])
                                    k15.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k20.kickoutFromGroup(op.param1,[op.param2])
                                        k20.inviteIntoGroup(op.param1,[op.param3])
                                        k15.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k16.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k16.kickoutFromGroup(op.param1,[op.param2])
                                            k16.updateGroup(G)
                                            Ticket = k16.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k16.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k16.updateGroup(G)
                                            Ticket = k16.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                                cl.inviteIntoGroup(op.param1,[op.param3])
                                                k15.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                    k15.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                        k15.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                                            k15.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid17 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k17.kickoutFromGroup(op.param1,[op.param2])
                        k17.inviteIntoGroup(op.param1,[op.param3])
                        k16.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k18.kickoutFromGroup(op.param1,[op.param2])
                            k18.inviteIntoGroup(op.param1,[op.param3])
                            k16.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k19.kickoutFromGroup(op.param1,[op.param2])
                                k19.inviteIntoGroup(op.param1,[op.param3])
                                k16.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k20.kickoutFromGroup(op.param1,[op.param2])
                                    k20.inviteIntoGroup(op.param1,[op.param3])
                                    k16.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        k16.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k17.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k17.kickoutFromGroup(op.param1,[op.param2])
                                            k17.updateGroup(G)
                                            Ticket = k17.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k17.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k17.updateGroup(G)
                                            Ticket = k17.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                k16.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                    k16.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                        k16.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                            k16.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid18 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k18.kickoutFromGroup(op.param1,[op.param2])
                        k18.inviteIntoGroup(op.param1,[op.param3])
                        k17.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k19.kickoutFromGroup(op.param1,[op.param2])
                            k19.inviteIntoGroup(op.param1,[op.param3])
                            k17.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k20.kickoutFromGroup(op.param1,[op.param2])
                                k20.inviteIntoGroup(op.param1,[op.param3])
                                k17.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                    k17.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        k17.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k18.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k18.kickoutFromGroup(op.param1,[op.param2])
                                            k18.updateGroup(G)
                                            Ticket = k18.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k18.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k18.updateGroup(G)
                                            Ticket = k18.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                k17.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                                    k17.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                                        k17.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                                            kd.inviteIntoGroup(op.param1,[op.param3])
                                                            k17.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid19 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k19.kickoutFromGroup(op.param1,[op.param2])
                        k19.inviteIntoGroup(op.param1,[op.param3])
                        k18.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k20.kickoutFromGroup(op.param1,[op.param2])
                            k20.inviteIntoGroup(op.param1,[op.param3])
                            k18.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                k18.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    k18.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        k18.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k19.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k19.kickoutFromGroup(op.param1,[op.param2])
                                            k19.updateGroup(G)
                                            Ticket = k19.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k19.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k19.updateGroup(G)
                                            Ticket = k19.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kb.kickoutFromGroup(op.param1,[op.param2])
                                                kb.inviteIntoGroup(op.param1,[op.param3])
                                                k18.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                                    k18.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                                        k18.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                                            k18.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if mid20 in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k10.kickoutFromGroup(op.param1,[op.param2])
                        k10.inviteIntoGroup(op.param1,[op.param3])
                        k9.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k20.kickoutFromGroup(op.param1,[op.param2])
                            k20.inviteIntoGroup(op.param1,[op.param3])
                            k19.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                k19.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    k19.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        k19.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = k20.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k20.kickoutFromGroup(op.param1,[op.param2])
                                            k20.updateGroup(G)
                                            Ticket = k20.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = k20.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            k20.updateGroup(G)
                                            Ticket = k20.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                                kc.inviteIntoGroup(op.param1,[op.param3])
                                                k19.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                                    k19.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                                        k19.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                                            k19.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if Gmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                        kf.inviteIntoGroup(op.param1,[op.param3])
                        k20.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            k20.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                k20.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    k20.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        k20.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kf.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            kf.updateGroup(G)
                                            Ticket = kf.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kf.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kf.updateGroup(G)
                                            Ticket = kf.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                                k20.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                    k20.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                                        k20.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k8.kickoutFromGroup(op.param1,[op.param2])
                                                            k8.inviteIntoGroup(op.param1,[op.param3])
                                                            k20.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass 
                return

            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k12.kickoutFromGroup(op.param1,[op.param2])
                        k12.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k13.kickoutFromGroup(op.param1,[op.param2])
                            k13.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k14.kickoutFromGroup(op.param1,[op.param2])
                                k14.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k15.kickoutFromGroup(op.param1,[op.param2])
                                    k15.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k16.kickoutFromGroup(op.param1,[op.param2])
                                        k16.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.updateGroup(G)
                                            Ticket = kk.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kk.updateGroup(G)
                                            Ticket = kk.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                k17.kickoutFromGroup(op.param1,[op.param2])
                                                k17.inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k18.kickoutFromGroup(op.param1,[op.param2])
                                                    k18.inviteIntoGroup(op.param1,[op.param3])
                                                    cl.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k19.kickoutFromGroup(op.param1,[op.param2])
                                                        k19.inviteIntoGroup(op.param1,[op.param3])
                                                        cl.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            k20.kickoutFromGroup(op.param1,[op.param2])
                                                            k20.inviteIntoGroup(op.param1,[op.param3])
                                                            cl.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass                                                        
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.findAndAddContactsByMid(op.param1,admin)
                                                ke.inviteIntoGroup(op.param1,admin)
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.findAndAddContactsByMid(op.param1,admin)
                                                    kf.inviteIntoGroup(op.param1,admin)
                                                except:
                                                    try:
                                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                                        k8.findAndAddContactsByMid(op.param1,admin)
                                                        k8.inviteIntoGroup(op.param1,admin)  
                                                    except:
                                                        try:
                                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                                            k9.findAndAddContactsByMid(op.param1,admin)
                                                            k9.inviteIntoGroup(op.param1,admin)  
                                                        except:
                                                            pass

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k10.kickoutFromGroup(op.param1,[op.param2])
                        k10.findAndAddContactsByMid(op.param1,admin)
                        k10.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            k11.kickoutFromGroup(op.param1,[op.param2])
                            k11.findAndAddContactsByMid(op.param1,admin)
                            k11.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                k12.kickoutFromGroup(op.param1,[op.param2])
                                k12.findAndAddContactsByMid(op.param1,admin)
                                k12.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    k13.kickoutFromGroup(op.param1,[op.param2])
                                    k13.findAndAddContactsByMid(op.param1,admin)
                                    k13.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        k14.kickoutFromGroup(op.param1,[op.param2])
                                        k14.findAndAddContactsByMid(op.param1,admin)
                                        k14.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            k15.kickoutFromGroup(op.param1,[op.param2])
                                            k15.findAndAddContactsByMid(op.param1,admin)
                                            k15.nviteIntoGroup(op.param1,admin)
                                        except:
                                            try:
                                                k16.kickoutFromGroup(op.param1,[op.param2])
                                                k16.findAndAddContactsByMid(op.param1,admin)
                                                k16.inviteIntoGroup(op.param1,admin)
                                            except:
                                                 try:
                                                     k17.kickoutFromGroup(op.param1,[op.param2])
                                                     k17.findAndAddContactsByMid(op.param1,admin)
                                                     k17.inviteIntoGroup(op.param1,admin)
                                                 except:
                                                     try:
                                                         k18.kickoutFromGroup(op.param1,[op.param2])
                                                         k18.findAndAddContactsByMid(op.param1,admin)
                                                         k18.inviteIntoGroup(op.param1,admin)  
                                                     except:
                                                        try:
                                                            k19.kickoutFromGroup(op.param1,[op.param2])
                                                            k19.findAndAddContactsByMid(op.param1,admin)
                                                            k19.inviteIntoGroup(op.param1,admin)  
                                                        except:
                                                            pass
                                                           
            
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k20.kickoutFromGroup(op.param1,[op.param2])
                                                       k20.findAndAddContactsByMid(op.param1,admin)
                                                       k20.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k8.kickoutFromGroup(op.param1,[op.param2])
                                                           k8.findAndAddContactsByMid(op.param1,admin)
                                                           k8.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass          

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k9.kickoutFromGroup(op.param1,[op.param2])
                        k9.findAndAddContactsByMid(op.param1,admin)
                        k9.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            k10.kickoutFromGroup(op.param1,[op.param2])
                            k10.findAndAddContactsByMid(op.param1,admin)
                            k10.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                k11.kickoutFromGroup(op.param1,[op.param2])
                                k11.findAndAddContactsByMid(op.param1,admin)
                                k11.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    k12.kickoutFromGroup(op.param1,[op.param2])
                                    k12.findAndAddContactsByMid(op.param1,admin)
                                    k12.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        k13.kickoutFromGroup(op.param1,[op.param2])
                                        k13.findAndAddContactsByMid(op.param1,admin)
                                        k13.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            k14.kickoutFromGroup(op.param1,[op.param2])
                                            k14.findAndAddContactsByMid(op.param1,admin)
                                            k14.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               k15.kickoutFromGroup(op.param1,[op.param2])
                                               k15.findAndAddContactsByMid(op.param1,admin)
                                               k15.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   k16.kickoutFromGroup(op.param1,[op.param2])
                                                   k16.findAndAddContactsByMid(op.param1,admin)
                                                   k16.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k17.kickoutFromGroup(op.param1,[op.param2])
                                                       k17.findAndAddContactsByMid(op.param1,admin)
                                                       k17.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k18.kickoutFromGroup(op.param1,[op.param2])
                                                           k18.findAndAddContactsByMid(op.param1,admin)
                                                           k18.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass
                                                           
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k19.kickoutFromGroup(op.param1,[op.param2])
                                                       k19.findAndAddContactsByMid(op.param1,admin)
                                                       k19.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k20.kickoutFromGroup(op.param1,[op.param2])
                                                           k20.findAndAddContactsByMid(op.param1,admin)
                                                           k20.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass       
                                                           
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k8.kickoutFromGroup(op.param1,[op.param2])
                                                       k8.findAndAddContactsByMid(op.param1,admin)
                                                       k8.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k9.kickoutFromGroup(op.param1,[op.param2])
                                                           k9.findAndAddContactsByMid(op.param1,admin)
                                                           k9.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass         

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k10.kickoutFromGroup(op.param1,[op.param2])
                                                       k10.findAndAddContactsByMid(op.param1,admin)
                                                       k10.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k11.kickoutFromGroup(op.param1,[op.param2])
                                                           k11.findAndAddContactsByMid(op.param1,admin)
                                                           k11.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass
                                                           
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k13.kickoutFromGroup(op.param1,[op.param2])
                                                       k13.findAndAddContactsByMid(op.param1,admin)
                                                       k13.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k14.kickoutFromGroup(op.param1,[op.param2])
                                                           k14.findAndAddContactsByMid(op.param1,admin)
                                                           k14.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass          

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k15.kickoutFromGroup(op.param1,[op.param2])
                                                       k15.findAndAddContactsByMid(op.param1,admin)
                                                       k15.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k16.kickoutFromGroup(op.param1,[op.param2])
                                                           k16.findAndAddContactsByMid(op.param1,admin)
                                                           k16.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass          

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k17.kickoutFromGroup(op.param1,[op.param2])
                                                       k17.findAndAddContactsByMid(op.param1,admin)
                                                       k17.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k18.kickoutFromGroup(op.param1,[op.param2])
                                                           k18.findAndAddContactsByMid(op.param1,admin)
                                                           k18.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass
                                                           
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       k19.kickoutFromGroup(op.param1,[op.param2])
                                                       k19.findAndAddContactsByMid(op.param1,admin)
                                                       k19.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           k20.kickoutFromGroup(op.param1,[op.param2])
                                                           k20.findAndAddContactsByMid(op.param1,admin)
                                                           k20.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass           
                                
                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["RAreadPoint"]:
                   if op.param2 in Setmain["RAreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["RAreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if wait["autoBlock"] == True:
                cl.blockContact(op.param1)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Mai 」\n• : "
                                ret_ = ": {}".format(str(ginfo.name))
                                ret_ += "\n : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += ""
                                ret_ += "\nผู้สร้างบอท :  line.me/ti/p/~mai06555mai" 
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Mai  」\n"
                                ret_ += "•: {}".format(str(ryan.displayName))
                                ret_ += "\n•: {}".format(str(ginfo.name))
                                ret_ += "\n•: {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n•: {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\n"
                                ret_ += "\nผู้สร้างบอท :  line.me/ti/p/~mai06555mai" 
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Mai 」\n"
                                ret_ += "• : {}".format(str(ryan.displayName))
                                ret_ += "\n•: {}".format(str(ginfo.name))
                                ret_ += "\n• : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "\n"
                                ret_ += "\nผู้สร้างบอท :  line.me/ti/p/~mai06555mai" 
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 55:
            try:
                if op.param1 in Setmain["ARreadPoint"]:
                   if op.param2 in Setmain["ARreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ARreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        sider = cl.getContact(op.param2).picturePath
                        image = 'http://dl.profile.line.naver.jp'+sider
                        cl.sendImageWithURL(op.param1, image)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                   if msg._from in wait["blacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = cl.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           saints = cl.getContact(msg._from)
                           sendMention(msg.to, saints.mid, "", wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"25628787","STKPKGID":"1818607","STKVER":"1"}, contentType=7)
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendImageWithURL(msg.to,image)
                           rnd = ["yg nge tag semoga masuk surga amin"]
                           p = random.choice(rnd)
                           lang = 'id'
                           tts = gTTS(text=p, lang=lang)
                           tts.save("hasil.mp3")
                           cl.sendAudio(msg.to,"hasil.mp3")
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"25628787","STKPKGID":"1818607","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in admin:
                           saints = cl.getContact(msg._from)
                           sendMention(msg.to, saints.mid, "", wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"PRDID":"a0768339-c2d3-4189-9653-2909e9bb6f58","PRDTYPE":"THEME","MSGTPL":"6"}, contentType=9)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["mentionKick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in admin:
                           cl.sendMessage(msg.to, "Ngetag lagi\nCipok nich")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
#SPAMINVITE
               if op.type == 25:
                 if settings['SpamInvite'] == True:
                   msg = op.message
                   man = msg._from
                   send = msg.to
                   if msg.contentType == 13:
                       if msg._from in admin:
                           korban = msg.contentMetadata["displayName"]
                           invite = msg.contentMetadata["mid"]
                           groups = cl.getGroup(send)
                           pending = groups.invitee
                           targets = []
                           for x in groups.members:
                               if korban in x.displayName:
                                   cl.sendText(send, korban + " Sudah Berada DiGrup Ini")
                               else:
                                   targets.append(invite)
                           if targets == []:
                               pass
                           else:
                               for target in targets:
                                   try:
                                       cl.findAndAddContactsByMid(target)
                                       cl.createGroup("mai",[target]) 
                                       cl.sendText(send,"แสปมกลุ่ม " + korban + "\nเสร็จแล้ว...")
                                       settings['SpamInvite'] = False
                                   except:             
                                        cl.sendText(send, 'Contact error')
                                        settings['SpamInvite'] = False
                                        break
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 16:
                    if wait["Timeline"] == True:
                            ret_ = "「Mai」"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(sender)
                                auth = "\n• ✡༎⎑  ༓ᴘᴇɴᴜʟɪs : {}".format(str(contact.displayName))
                            else:
                                auth = "\n• ✡༎⎑  ༓ᴘᴇɴᴜʟɪs : {}".format(str(msg.contentMetadata["serviceName"]))
                            ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n• ✡༎⎑  ༓sᴛɪᴄᴋᴇʀ : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• ✡༎⎑  ༓ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n• ✡༎⎑  ༓Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• ✡༎⎑  ༓Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n• ✡༎⎑  ༓Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• ✡༎⎑  ༓Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• ✡༎⎑  ༓Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                text = "\n• ✡༎⎑  ༓Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n• ✡༎⎑  ༓Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += text
                            cl.sendMessage(to, str(ret_))
                            cl.like(url[25:58], url[66:], likeType=1005)
                            cl.comment(url[25:58], url[66:], wait["message"])
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 sᴛɪᴄᴋᴇʀ ɪɴғᴏ 」"
                   ret_ += "\n• ✡༎⎑  ༓sᴛɪᴄᴋᴇʀ ɪᴅ: {}".format(stk_id)
                   ret_ += "\n• ✡༎⎑  ༓sᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ : {}".format(stk_ver)
                   ret_ += "\n• ✡༎⎑  ༓sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇ : {}".format(pkg_id)
                   ret_ += "\n• ✡༎⎑  ༓sᴛɪᴄᴋᴇʀ ᴜʀʟ: line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                if wait["stickerOn"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        r = s.get("https://store.line.me/stickershop/product/{}/id".format(urllib.parse.quote(pkg_id)))
                        soup = BeautifulSoup(r.content, 'html5lib')
                        data = soup.select("[class~=mdBtn01Txt]")[0].text
                        if data == 'Lihat Produk Lain':
                            ret_ = "「 sᴛɪᴄᴋᴇʀ ɪɴғᴏ 」"
                            ret_ += "\n• ✡༎⎑  ༓sᴛɪᴄᴋᴇʀ ɪᴅ : {}".format(stk_id)
                            ret_ += "\n• ✡༎⎑  ༓sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇ : {}".format(pkg_id)
                            ret_ += "\n•✡༎⎑  ༓  : {}".format(stk_ver)
                            ret_ += "\n• sᴛɪᴄᴋᴇʀ ᴜʀʟ : line://shop/detail/{}".format(pkg_id)
                            cl.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = cl.downloadFileURL(data)
                               cl.sendImage(msg.to,path)
                        else:
                            ret_ = "「 sᴛɪᴄᴋᴇʀ ɪɴғᴏ 」"
                            ret_ += "\n• ✡༎⎑  ༓PRICE : "+soup.findAll('p', attrs={'class':'mdCMN08Price'})[0].text
                            ret_ += "\n• ✡༎⎑  ༓AUTHOR : "+soup.select("a[href*=/stickershop/author]")[0].text
                            ret_ += "\n• ✡༎⎑  ༓sᴛɪᴄᴋᴇʀ ɪᴅ : {}".format(str(stk_id))
                            ret_ += "\n• ✡༎⎑  ༓sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇ : {}".format(str(pkg_id))
                            ret_ += "\n• ✡༎⎑  ༓sᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ : {}".format(str(stk_ver))
                            ret_ += "\n• ✡༎⎑  ༓sᴛɪᴄᴋᴇʀ ᴜʀʟ : line://shop/detail/{}".format(str(pkg_id))
                            ret_ += "\n• ✡༎⎑  ༓DESCRIPTION :\n"+soup.findAll('p', attrs={'class':'mdCMN08Desc'})[0].text
                            cl.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = cl.downloadFileURL(data)
                               cl.sendImage(msg.to,path)
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to," 「 Contact Info 」\n「✭」 Nama : " + msg.contentMetadata["displayName"] + "\n「✭」 MID : " + msg.contentMetadata["mid"] + "\n「✭」 Status Msg : " + contact.statusMessage + "\n「✭」 Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            cl.sendMessage(msg.to, "「Dia」")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  cl.findAndAddContactsByMid(target)
                                  cl.inviteIntoGroup(msg.to,[target])
                                  ryan = cl.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  "「 Sukses Invite 」\nNama "
                                  ret_ = "「Ketik Invite off jika sudah done」"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  cl.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  cl.sendText(msg.to,"Anda terkena limit")
                                  wait["invite"] = False
                                  break
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan anggota bot saints")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if wait["Addimage"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        images[wait["Addimage"]["name"]] = str(path)
                        f = codecs.open("image.json","w","utf-8")
                        json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan gambar {}".format(str(wait["Addimage"]["name"])))
                        wait["Addimage"]["status"] = False                
                        wait["Addimage"]["name"] = ""
               if msg.contentType == 2:
                 if msg._from in admin:
                    if wait["Addvideo"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        videos[wait["Addvideo"]["name"]] = str(path)
                        f = codecs.open("video.json","w","utf-8")
                        json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan video {}".format(str(wait["Addvideo"]["name"])))
                        wait["Addvideo"]["status"] = False                
                        wait["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                 if msg._from in admin:
                    if wait["Addsticker"]["status"] == True:
                        stickers[wait["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                        f = codecs.open("sticker.json","w","utf-8")
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan sticker {}".format(str(wait["Addsticker"]["name"])))
                        wait["Addsticker"]["status"] = False                
                        wait["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                 if msg._from in admin:
                    if wait["Addaudio"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        audios[wait["Addaudio"]["name"]] = str(path)
                        f = codecs.open("audio.json","w","utf-8")
                        json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan mp3 {}".format(str(wait["Addaudio"]["name"])))
                        wait["Addaudio"]["status"] = False                
                        wait["Addaudio"]["name"] = ""
               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["ARfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["ARfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["ARfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["ARfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["ARfoto"]:
                            path = kb.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Dmid]
                            kb.updateProfilePicture(path)
                            kb.sendMessage(msg.to,"Foto berhasil dirubah") 
                        elif Emid in Setmain["ARfoto"]:
                            path = kd.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Emid]
                            kd.updateProfilePicture(path)
                            kd.sendMessage(msg.to,"Foto berhasil dirubah")   
                        elif Fmid in Setmain["ARfoto"]:
                            path = ke.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Fmid]
                            ke.updateProfilePicture(path)
                            ke.sendMessage(msg.to,"Foto berhasil dirubah")     
                        elif Gmid in Setmain["ARfoto"]:
                            path = kf.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Gmid]
                            kf.updateProfilePicture(path)
                            kf.sendMessage(msg.to,"Foto berhasil dirubah")       
                        elif Hmid in Setmain["ARfoto"]:
                            path = kg.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Hmid]
                            kg.updateProfilePicture(path)
                            kg.sendMessage(msg.to,"Foto berhasil dirubah")        
                        elif Imid in Setmain["ARfoto"]:
                            path = kh.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Imid]
                            kh.updateProfilePicture(path)
                            kh.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Jmid in Setmain["ARfoto"]:
                            path = kh.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Jmid]
                            kj.updateProfilePicture(path)
                            kj.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Zmid in Setmain["ARfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = kb.downloadObjectMsg(msg_id)
                     path5 = kd.downloadObjectMsg(msg_id)
                     path6 = ke.downloadObjectMsg(msg_id)
                     path7 = kf.downloadObjectMsg(msg_id)
                     path8 = k8.downloadObjectMsg(msg_id)
                     path9 = k9.downloadObjectMsg(msg_id)
                     path10 = k10.downloadObjectMsg(msg_id)
                     path11 = k11.downloadObjectMsg(msg_id)
                     path12 = k12.downloadObjectMsg(msg_id)
                     path13 = k13.downloadObjectMsg(msg_id)
                     path14 = k14.downloadObjectMsg(msg_id)
                     path15 = k15.downloadObjectMsg(msg_id)
                     path16 = k16.downloadObjectMsg(msg_id)
                     path17 = k17.downloadObjectMsg(msg_id)
                     path18 = k18.downloadObjectMsg(msg_id)
                     path19 = k19.downloadObjectMsg(msg_id)
                     path20 = k20.downloadObjectMsg(msg_id)
                     path21 = kj.downloadObjectMsg(msg_id)
                     path22 = sw.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kb.updateProfilePicture(path3)
                     kb.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kd.updateProfilePicture(path3)
                     kd.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     ke.updateProfilePicture(path3)
                     ke.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kf.updateProfilePicture(path3)
                     kf.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kj.updateProfilePicture(path3)
                     kj.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     sw.updateProfilePicture(path3)
                     sw.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
               if msg.contentType == 2:
                   if msg._from in admin:
                       if mid in Setmain["ARvideo"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["ARvideo"][mid]
                            cl.updateProfileVideoPicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah jadi video")

               if msg.contentType == 0:
                 if Setmain["autoRead"] == True:
                     cl.sendChatChecked(msg.to, msg_id)
                 if text is None:
                     return
                 else:
                        for sticker in stickers:
                         if msg._from in admin:
                           if text.lower() == sticker:
                              sid = stickers[text.lower()]["STKID"]
                              spkg = stickers[text.lower()]["STKPKGID"]
                              cl.sendSticker(to, spkg, sid)
                        for image in images:
                         if msg._from in admin:
                           if text.lower() == image:
                              cl.sendImage(msg.to, images[image])
                        for audio in audios:
                         if msg._from in admin:
                           if text.lower() == audio:
                              cl.sendAudio(msg.to, audios[audio])
                        for video in videos:
                         if msg._from in admin:
                           if text.lower() == video:
                              cl.sendVideo(msg.to, videos[video])
                        cmd = command(text)
                        if cmd == "เปิดบอท":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendText(msg.to, "เปิดระบบทำงานของบอทแล้วคัฟเจ้านายสุดหล่อ")
                                
                        elif cmd == "ปิดบอท":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendText(msg.to, "เปิดระบบทำงานของบอทแล้วคัฟเจ้านายสุดหล่อ")
                                            
                        elif cmd == "คำสั่ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage = help()
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「My Name 'S」\n• User : "
                                ret_ = str(helpMessage)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "คำสั่ง1":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage1 = help1()
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「MY Name 'S」\n• User : "
                                ret_ = str(helpMessage1)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "คำสั่ง2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage2 = help2()
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「MY Nme 'S」\n• User : "
                                ret_ = str(helpMessage2)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "คำสั่ง3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage3 = help3()
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「MY Name 'S」\n• User : "
                                ret_ = str(helpMessage3)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "เชค":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "\n   「 Mai 」\n"
                                if wait["stickerOn"] == True: md+="「🇹🇭」 Sticker「ON」📲\n"
                                else: md+="「🇹🇭」 Sticker「OFF」📵\n"
                                if wait["contact"] == True: md+="「🇹🇭」 Contact「ON」📲\n"
                                else: md+="「🇹🇭」 Contact「OFF」📵\n"
                                if wait["talkban"] == True: md+="「🇹🇭」 Talkban「ON」📲\n"
                                else: md+="「🇹🇭」 Talkban「OFF」📵\n"
                                if wait["unsend"] == True: md+="「🇹🇭」 Unsend「ON」📲\n"
                                else: md+="「🇹🇭」 Unsend「OFF」📵\n"
                                if settings["SpamInvite"] == True: md+="「🇹🇭」 Spaminvite「ON」📲\n"
                                else: md+="「🇹🇭」 Spaminvite「OFF」📵\n"
                                if wait["detectMention"] == True: md+="「🇹🇭」 Respon「ON」📲\n"
                                else: md+="「🇹🇭」 Respon「OFF」📵\n"
                                if wait["Timeline"] == True: md+="「🇹🇭」 Timeline「ON」📲\n"
                                else: md+="「🇹🇭」 Timeline「OFF」📵\n"
                                if wait["autoJoin"] == True: md+="「🇹🇭」 Autojoin「ON」📲\n"
                                else: md+="「🇹🇭」 Autojoin「OFF」📵\n"
                                if wait["autoAdd"] == True: md+="「🇹🇭」 Autoadd「ON」📲\n"
                                else: md+="「🇹🇭」 Autoadd「OFF」📵\n"
                                if settings["autoJoinTicket"] == True: md+="「🇹🇭」 Jointicket「ON」📲\n"
                                else: md+="「🇹🇭」 Jointicket「OFF」📵\n"
                                if msg.to in welcome: md+="「🇹🇭」 Welcome「ON」📲\n"
                                else: md+="「🇹🇭」 Welcome「OFF」📵\n"
                                if wait["autoLeave"] == True: md+="「🇹🇭」 Autoleave「ON」📲\n"
                                else: md+="「🇹🇭」 Autoleave「OFF」📵\n"
                                if msg.to in protectqr: md+="「🇹🇭」Protecturl「ON」📲\n"
                                else: md+="「🇹🇭」Protecturl「OFF」📵\n"
                                if msg.to in protectjoin: md+="「🇹🇭」Protectjoin「ON」📲\n"
                                else: md+="「🇹🇭」Protectjoin「OFF」📵\n"
                                if msg.to in protectjoin: md+="「🇹🇭」Protectinvite「ON」📲\n"
                                else: md+="「🇹🇭」Protectinvite「OFF」📵\n"
                                if msg.to in protectkick: md+="「🇹🇭」Protectkick「ON」📲\n"
                                else: md+="「🇹🇭」Protectkick「OFF」📵\n"
                                if msg.to in protectcancel: md+="「🇹🇭」Protectcancel「ON」📲\n"
                                else: md+="「🇹🇭」Protectcancel「OFF」📵\n"
                                if msg.to in protectantijs: md+="「🇹🇭」Antijs「ON」📲\n"
                                else: md+="「🇹🇭」Antijs「OFF」📵\n"  
                                if msg.to in ghost: md+="「🇹🇭」Ghost「ON」📲\n"
                                else: md+="「🇹🇭」Ghost「OFF」📵\n"
                                ginfo = cl.getGroup(msg.to)
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 BY:MAI  」\n• User : "
                                ret_ = "• Group : {}\n".format(str(ginfo.name))
                                ret_ += str(md)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + "\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                
                        elif cmd == "ผส" or text.lower() == 'creator':
                            if msg._from in admin:
                                cl.sendText(msg.to,"「CREATOR BOT\nPelindung Room Kita」") 
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd.startswith('ข้อมูล'):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            try:
                                arr = []
                                today = datetime.today()
                                thn = 2018 
                                bln = 12     #isi bulannya yg sewa
                                hr = 17    #isi tanggalnya yg sewa
                                future = datetime(thn, bln, hr)
                                days = (str(future - today))
                                comma = days.find(",")
                                days = days[:comma]
                                contact = cl.getContact(mid)
                                favoritelist = cl.getFavoriteMids()
                                grouplist = cl.getGroupIdsJoined()
                                contactlist = cl.getAllContactIds()
                                blockedlist = cl.getBlockedContactIds()
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                start = time.time()
                                #cl.sendText("u6bca85cef34fc8ec0e2b459e179e3708", '.')
                                elapsed_time = time.time() - start
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 sᴇʟғʙᴏᴛ 」\n• ✡༎⎑  ༓ᴜsᴇʀ : "
                                ret_ = "• ✡༎⎑  ༓ɢʀᴏᴜᴘ : {} ɢʀᴏᴜᴘ".format(str(len(grouplist)))
                                ret_ += "\n• ✡༎⎑  ༓ғʀɪᴇɴᴅ : {} ғʀɪᴇɴᴅ".format(str(len(contactlist)))
                                ret_ += "\n• ✡༎⎑  ༓ʙʟᴏᴄᴋᴇᴅ : {} ʙʟᴏᴄᴋᴇᴅ".format(str(len(blockedlist)))
                                ret_ += "\n• ✡༎⎑  ༓ғᴀᴠᴏʀɪᴛᴇ : {} ғᴀᴠᴏʀɪᴛᴇ".format(str(len(favoritelist)))
                                ret_ += "\n• ✡༎⎑  ༓ᴠᴇʀsɪᴏɴ : 「 sᴇʟғʙᴏᴛ ᴏɴʟʏ 」"
                                ret_ += "\n• ✡༎⎑  ༓ᴇxᴘɪʀᴇᴅ : {} - {} - {}".format(str(hr), str(bln), str(thn))
                                ret_ += "\n• ✡༎⎑  ༓ɪɴ ᴅᴀʏs : {} ᴀɢᴀɪɴ".format(days)
                                ret_ += "\n「 sᴘᴇᴇᴅ ʀᴇsᴘᴏɴ 」\n• ✡༎⎑  ༓{} ᴅᴇᴛɪᴋ".format(str(elapsed_time))
                                ret_ += "\n「 sᴇʟғʙᴏᴛ ʀᴜɴᴛɪᴍᴇ 」\n• ✡༎⎑  ༓{}".format(str(bot))
                                ret_ += "\n"
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                #cl.sendContact(to, "")
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd == "มี" or text.lower() == 'aim':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 User Selfbot 」\n", "")
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)


                        elif cmd.startswith("ไอดี "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("ขโมย " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               a = channel.getProfileCoverURL(mid=key1)
                               cl.sendMessage(msg.to, "「 Contact Info 」\n• Nama : "+str(mi.displayName)+"\n• Mid : " +key1+"\n• Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                                   cl.sendImageWithURL(receiver, a)
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))
                                   cl.sendImageWithURL(receiver, a)

                        elif ("ปก " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    cl.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
#CLONE
                        elif cmd.startswith("ก็อป "):
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    cl.cloneContactProfile(ls)
                                    cl.sendContact(to, sender)
                                    cl.sendMessage(to, "➧ Berhasil clone profile")

                        elif cmd == "คืนร่าง":
                            try:
                                lineProfile = cl.getProfile()
                                lineProfile.displayName = str(wait["myProfile"]["displayName"])
                                lineProfile.statusMessage = str(wait["myProfile"]["statusMessage"])
                                lineProfile.pictureStatus = str(wait["myProfile"]["pictureStatus"])
                                cl.updateProfileAttribute(8, lineProfile.pictureStatus)
                                cl.updateProfile(lineProfile)
                                coverId = str(wait["myProfile"]["coverId"])
                                cl.updateProfileCoverById(coverId)
                                cl.sendMessage(to, "")
                            except Exception as e:
                                cl.sendMessage(to, "กลับแล้วงับ")

                        elif cmd == "backupprofile":
                            try:
                                profile = cl.getProfile()
                                wait["myProfile"]["displayName"] = str(profile.displayName)
                                wait["myProfile"]["statusMessage"] = str(profile.statusMessage)
                                wait["myProfile"]["pictureStatus"] = str(profile.pictureStatus)
#                                coverId = ririn.getProfileDetail()["result"]["objectId"]
#                                wait["myProfile"]["coverId"] = str(coverId)
                                cl.sendMessage(to, "ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs")
                            except Exception as e:
                                cl.sendMessage(to, "ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ ғᴀɪʟᴇᴅ")

                        elif ("สติกเกอร์: " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    query = msg.text.replace("Sticker: ", "")
                                    query = int(query)
                                    if type(query) == int:
                                        cl.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        cl.sendText(receiver, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        cl.sendText(receiver, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    cl.sendText(receiver, str(e))

                        elif "/ti/g/" in msg.text.lower():
                           if msg._from in admin:
                             if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                    if l not in n_links:
                                       n_links.append(l)
                                 for ticket_id in n_links:
                                    group = cl.findGroupByTicket(ticket_id)
                                    cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                    
                        elif cmd == "ลบรัน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                  cl.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  cl.sendMessage(to, "Tidak ada undangan yang tertunda")

                        elif text.lower() == "ลบแชท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   kb.removeAllMessages(op.param2)
                                   kd.removeAllMessages(op.param2) 
                                   ke.removeAllMessages(op.param2)
                                   kf.removeAllMessages(op.param2)
                                   k8.removeAllMessages(op.param2)
                                   kj.removeAllMessages(op.param2)
                                   sw.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "ลบแชทคิก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   kb.removeAllMessages(op.param2)
                                   kd.removeAllMessages(op.param2)
                                   ke.removeAllMessages(op.param2)
                                   kf.removeAllMessages(op.param2)
                                   k8.removeAllMessages(op.param2)
                                   k9.removeAllMessages(op.param2)
                                   k10.removeAllMessages(op.param2)
                                   k11.removeAllMessages(op.param2)
                                   k12.removeAllMessages(op.param2)
                                   k13.removeAllMessages(op.param2)
                                   k14.removeAllMessages(op.param2)
                                   k15.removeAllMessages(op.param2)
                                   k16.removeAllMessages(op.param2)
                                   k17.removeAllMessages(op.param2)
                                   k18.removeAllMessages(op.param2)
                                   k19.removeAllMessages(op.param2)
                                   k20.removeAllMessages(op.param2)
                                   kj.removeAllMessages(op.param2)
                                   sw.removeAllMessages(op.param2)
                                   ki.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   kk.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   kc.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   kb.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   kd.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   ke.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   kf.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k8.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k9.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k10.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k11.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k12.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k13.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k14.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k15.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k16.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k17.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k18.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k19.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                                   k20.sendMessage(msg.to,"ลบข้อความในแชททั้งหมดเรียบร้อย...")
                               except:
                                   pass

                        elif cmd.startswith("ประกาศ "):
                           if msg._from in admin:
                             sep = text.split(" ")
                             bc = text.replace(sep[0] + " ","")
                             saya = cl.getGroupIdsJoined()
                             for group in saya:
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 ประกาศกลุ่ม 」\nประกาศ โดย "
                                ret_ = "{}".format(str(bc))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(group, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd.startswith("ออกกลุ่ม: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    kk.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    kb.leaveGroup(i)
                                    kd.leaveGroup(i)
                                    ke.leaveGroup(i)
                                    kf.leaveGroup(i)
                                    k8.leaveGroup(i)
                                    k9.leaveGroup(i)
                                    k10.leaveGroup(i)
                                    k11.leaveGroup(i)
                                    k12.leaveGroup(i)
                                    k13.leaveGroup(i)
                                    k14.leaveGroup(i)
                                    k15.leaveGroup(i)
                                    k16.leaveGroup(i)
                                    k17.leaveGroup(i)
                                    k18.leaveGroup(i)
                                    k19.leaveGroup(i)
                                    k20.leaveGroup(i)
                                    k20.sendMessage(msg.to,"บอทออกแล้ว กลุ่ม " +str(ginfo.name))

                                
                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Setkey 」\nSetkey saat ini「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "「 Change Setkey 」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "「 Resetkey 」\nSetkey mu telah direset")

                        elif cmd == "รีบอท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 รีบูสระบบบอท 」\nUser ", "\nกรุณาทำการล็อคอินอีกครั้ง...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "ออน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 เวลาทำงานของบอท 」\n• ชื่อผู้ใช้ : "
                                ret_ = "• {}".format(str(bot))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "ข้อมูลกลุ่ม":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "「 ข้อมูลกลุ่ม 」\n「✭」 ❂➣ ชื่อกลุ่ม : {}".format(G.name)+ "\n「✭」 ไอดีกลุ่ม : {}".format(G.id)+ "\n「✭」 Pembuat : {}".format(G.creator.displayName)+ "\n「✭」 Waktu Dibuat : {}".format(str(timeCreated))+ "\n「✭」 Jumlah Member : {}".format(str(len(G.members)))+ "\n「✭」 Jumlah Pending : {}".format(gPending)+ "\n「✭」 Group Qr : {}".format(gQr)+ "\n「✭」 Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("ข้อมูลกลุ่ม "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "「 Group Info 」"
                                ret_ += "\n「🇹🇭」  ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(G.name)
                                ret_ += "\n「🇹🇭」 ID Group : {}".format(G.id)
                                ret_ += "\n「🇹🇭」 Pembuat : {}".format(gCreator)
                                ret_ += "\n「🇹🇭」 Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n「🇹🇭」 Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n「🇹🇭」 Jumlah Pending : {}".format(gPending)
                                ret_ += "\n「🇹🇭」 Group Qr : {}".format(gQr)
                                ret_ += "\n「🇹🇭」 Group Ticket : {}".format(gTicket)
                                ret_ += "\n「🇹🇭」 Picture Url : http://dl.profile.line-cdn.net/{}".format(G.pictureStatus)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except:
                                pass
#Spamcallto
                        elif cmd.startswith("spamcallto"):
                          dan = text.split(" ")
                          num = int(dan[1])
#                          ret_ = "╔══[ Call Private ]"
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                     if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                for ls in lists:
                                 for var in range(0,num):
                                      group = cl.getGroup(to)
                                      members = [ls]
                                      cl.acquireGroupCallRoute(to)
                                      cl.inviteIntoGroupCall(to, contactIds=members)
#                                 ret_ += "\n╠ @!"
#                                ret_ += "\n╚══[ Total {} Spam call]".format(str(dan[1]))
                                cl.sendMessage(msg.to, "Berhasil Sct ")

                        elif cmd.startswith("เปิดลิ้ง "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「 Sukses Open Qr 」\n• Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "• Nama : {}".format(G.name)
                                ret_ += "\n• Group Qr : {}".format(gQr)
                                ret_ += "\n• Pendingan : {}".format(gPending)
                                ret_ += "\n• Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass

                        elif cmd.startswith("ปิดลิ้ง "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「 Sukses Close Qr 」\n• Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "• Nama : {}".format(G.name)
                                ret_ += "\n• Group Qr : {}".format(gQr)
                                ret_ += "\n• Pendingan : {}".format(gPending)
                                ret_ += "\n• Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass
                                
                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "「✭」 "+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"「✭」 Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("qr on "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    protectqr[G] = True
                                    f=codecs.open('protectqr.json','w','utf-8')
                                    json.dump(protectqr, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「 Protect Qr Diaktifkan 」\n• Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    cl.sendText(msg.to, "Grup itu tidak ada")
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "• Nama grup : {}".format(G.name)
                                ret_ += "\n• Pendingan : {}".format(gPending)
                                ret_ += "\n• Jumlah Member : {}".format(str(len(G.members)))
                                cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except Exception as e:
                                cl.sendMessage(to, str(e))

                        elif cmd == "กลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ กลุ่มที่มีทั้งหมด ]\n║\n"+ma+"║\n╚══[ จำนวน「"+str(len(gid))+"」กลุ่ม ]")

                        elif cmd == "กลุ่ม1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "กลุ่ม2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "กลุ่ม3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
                               
                        elif cmd == "/กลุ่ม4":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kb.getGroupIdsJoined()
                               for i in gid:
                                   G = kb.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kb.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "เปิดลิ้ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "เปิดลิ้งเรียบร้อย...")

                        elif cmd == "ปิดลิ้ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "ปิดลิ้งเรียบร้อย...")

                        elif cmd == "ลิ้ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "กลุ่ม "+str(x.name)+ "\nลิ้งกลุ่ม \nhttp://line.me/R/ti/g/"+gurl)
#===========BOT UPDATE============#
                        elif cmd == "เปลี่ยนรูปกลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendText(msg.to,"ส่งรูป.....")
                                
                        elif cmd == "เปลี่ยนรูป":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARfoto"][mid] = True
                                cl.sendText(msg.to,"ส่งรูป.....")

                        elif cmd == "รูปวิดีโอ":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARvideo"][mid] = True
                                cl.sendText(msg.to,"ส่งวิดีโอ.....")

                        elif cmd.startswith("เปลี่ยนชื่อ "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"คุณได้เปลี่ยนชื่อเป็น " + string + "")
#KICKALL
                        elif "!mai" in msg.text:
                          if msg._from in admin:
                           if msg.toType == 2:
                              print("ok")
                              _name = msg.text.replace("!mai","")
                              gs = k20.getGroup(msg.to)
                              gs = k20.getGroup(msg.to)
                              gs = k20.getGroup(msg.to)
                              targets = []
                              for g in gs.members:
                                 if _name in g.displayName:
                                     targets.append(g.mid)
                              if targets == []:
                                 k20.sendText(msg.to,"Tidak Ditemukan.")
                              else:
                                  for target in targets:
                                   if not target in admin and Bots:
                                      try:
                                          klist=[k20]
                                          kicker=random.choice(klist)
                                          kicker.kickoutFromGroup(msg.to,[target])
                                          print (msg.to,[g.mid])
                                      except Exception as e:
                                          break
                        elif ("Vk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif cmd == "รูป1":
                            if msg._from in admin:
                                Setmain["ARfoto"][Amid] = True
                                ki.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "รูป2":
                            if msg._from in admin:
                                Setmain["ARfoto"][Bmid] = True
                                kk.sendMessage(msg.to,"ส่งรูป.....")
                                
                        elif cmd == "รูป3":
                            if msg._from in admin:
                                Setmain["ARfoto"][Cmid] = True
                                kc.sendMessage(msg.to,"ส่งรูป.....")
                                
                        elif cmd == "รูป4":
                            if msg._from in admin:
                                Setmain["ARfoto"][Dmid] = True
                                kb.sendMessage(msg.to,"ส่งรูป.....")
        
                        elif cmd == "รูป5":
                            if msg._from in admin:
                                Setmain["ARfoto"][Emid] = True
                                kd.sendMessage(msg.to,"ส่งรูป.....")         
                                
                        elif cmd == "รูป6":
                            if msg._from in admin:
                                Setmain["ARfoto"][Fmid] = True
                                ke.sendMessage(msg.to,"ส่งรูป.....")        
                                
                        elif cmd == "รูป7":
                            if msg._from in admin:
                                Setmain["ARfoto"][Gmid] = True
                                kf.sendMessage(msg.to,"ส่งรูป.....")
                                
                        elif cmd == "รูป8":
                            if msg._from in admin:
                                Setmain["ARfoto"][Gmid] = True
                                k8.sendMessage(msg.to,"ส่งรูป.....")

                        elif cmd == "รูป9":
                            if msg._from in admin:
                                Setmain["ARfoto"][Gmid] = True
                                k9.sendMessage(msg.to,"ส่งรูป.....")

                        elif cmd == "รูป10":
                            if msg._from in admin:
                                Setmain["ARfoto"][Gmid] = True
                                k10.sendMessage(msg.to,"ส่งรูป.....")

                        elif cmd == "รูป11":
                            if msg._from in admin:
                                Setmain["ARfoto"][Amid] = True
                                k11.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "รูป12":
                            if msg._from in admin:
                                Setmain["ARfoto"][Bmid] = True
                                k12.sendMessage(msg.to,"ส่งรูป.....")
                                
                        elif cmd == "รูป13":
                            if msg._from in admin:
                                Setmain["ARfoto"][Cmid] = True
                                k13.sendMessage(msg.to,"ส่งรูป.....")
                                
                        elif cmd == "รูป14":
                            if msg._from in admin:
                                Setmain["ARfoto"][Dmid] = True
                                k14.sendMessage(msg.to,"ส่งรูป.....")
        
                        elif cmd == "รูป15":
                            if msg._from in admin:
                                Setmain["ARfoto"][Emid] = True
                                k15.sendMessage(msg.to,"ส่งรูป.....")         
                                
                        elif cmd == "รูป16":
                            if msg._from in admin:
                                Setmain["ARfoto"][Fmid] = True
                                k16.sendMessage(msg.to,"ส่งรูป.....")        
                                
                        elif cmd == "รูป17":
                            if msg._from in admin:
                                Setmain["ARfoto"][Gmid] = True
                                k17.sendMessage(msg.to,"ส่งรูป.....")
                                
                        elif cmd == "รูป18":
                            if msg._from in admin:
                                Setmain["ARfoto"][Gmid] = True
                                k18.sendMessage(msg.to,"ส่งรูป.....")

                        elif cmd == "รูป19":
                            if msg._from in admin:
                                Setmain["ARfoto"][Gmid] = True
                                k19.sendMessage(msg.to,"ส่งรูป.....")

                        elif cmd == "รูป20":
                            if msg._from in admin:
                                Setmain["ARfoto"][Gmid] = True
                                k20.sendMessage(msg.to,"ส่งรูป.....")
                                
                        elif cmd == "รูป21":
                            if msg._from in admin:
                                Setmain["ARfoto"][Jmid] = True
                                kj.sendMessage(msg.to,"ส่งรูป.....")         
                                
                        elif cmd == "รูป22":
                            if msg._from in admin:
                                Setmain["ARfoto"][Zmid] = True
                                sw.sendMessage(msg.to,"ส่งรูป.....")      
                         
                        elif cmd.startswith("/ชื่อ1 "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("/ชื่อ2 "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("/ชื่อ3 "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("/ชื่อ4 "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendMessage(msg.to,"Nama diganti jadi " + string + "")    
   
                        elif cmd.startswith("/ชื่อ5: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kd.getProfile()
                                profile.displayName = string
                                kd.updateProfile(profile)
                                kd.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("/ชื่อ6 "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                ke.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("/ชื่อ7 "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kf.getProfile()
                                profile.displayName = string
                                kf.updateProfile(profile)
                                kf.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("/ชื่อ8 "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kj.getProfile()
                                profile.displayName = string
                                kj.updateProfile(profile)
                                kj.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("/ชื่อ9 "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")       

                        elif cmd == "บอท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendContact(to, mid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Fmid)
                               cl.sendContact(to, Gmid)
                               cl.sendContact(to, mid8)
                               cl.sendContact(to, mid9)
                               cl.sendContact(to, mid10)
                               cl.sendContact(to, mid11)
                               cl.sendContact(to, mid12)
                               cl.sendContact(to, mid13)
                               cl.sendContact(to, mid14)
                               cl.sendContact(to, mid15)
                               cl.sendContact(to, mid16)
                               cl.sendContact(to, mid17)
                               cl.sendContact(to, mid18)
                               cl.sendContact(to, mid19)
                               cl.sendContact(to, mid20)
                               cl.sendContact(to, Jmid)
                               cl.sendContact(to, Zmid)
                               
                        elif cmd == "reinvite":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                k8.leaveGroup(msg.to)
                                k9.leaveGroup(msg.to)
                                k10.leaveGroup(msg.to)
                                k11.leaveGroup(msg.to)
                                k12.leaveGroup(msg.to)
                                k13.leaveGroup(msg.to)
                                k14.leaveGroup(msg.to)
                                k15.leaveGroup(msg.to)
                                k16.leaveGroup(msg.to)
                                k17.leaveGroup(msg.to)
                                k18.leaveGroup(msg.to)
                                k19.leaveGroup(msg.to)
                                k20.leaveGroup(msg.to)
                                kj.leaveGroup(msg.to)
                                sw.leaveGroup(msg.to)
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                ki.updateGroup(G)
 
                        elif ("Vk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                        elif cmd == "reinvitebot":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                kj.leaveGroup(msg.to)
                                sw.leaveGroup(msg.to)
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k10.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k11.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k12.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k13.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k14.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k15.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k16.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k17.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k18.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k19.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k20.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                ki.updateGroup(G)

                        elif cmd == "ดึงคิก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,mid8,mid9,mid10,mid11,mid12,mid13,mid14,mid15,mid16,mid17,mid18,mid19,mid20]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                    kd.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                    kf.acceptGroupInvitation(msg.to)
                                    k8.acceptGroupInvitation(msg.to)
                                    k9.acceptGroupInvitation(msg.to)
                                    k10.acceptGroupInvitation(msg.to)
                                    k11.acceptGroupInvitation(msg.to)
                                    k12.acceptGroupInvitation(msg.to)
                                    k13.acceptGroupInvitation(msg.to)
                                    k14.acceptGroupInvitation(msg.to)
                                    k15.acceptGroupInvitation(msg.to)
                                    k16.acceptGroupInvitation(msg.to)
                                    k17.acceptGroupInvitation(msg.to)
                                    k18.acceptGroupInvitation(msg.to)
                                    k19.acceptGroupInvitation(msg.to)
                                    k20.acceptGroupInvitation(msg.to)
                                    cl.sendMessage(msg.to,"Grup "+str(ginfo.name)+"Aman Dari JS")
                                except:
                                    pass

                        elif cmd == "ck":
                            if msg._from in admin or msg._from in owner:
                               try:cl.inviteIntoGroup(to, ["uc66e45201d1612eb4ce7b3a86bac4685"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["uc66e45201d1612eb4ce7b3a86bac4685"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               cl.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:ki.inviteIntoGroup(to, ["uff4bd67e5bc6ab62760b1ff78d89dfe4"]);has = "OK"
                               except:has = "NOT"
                               try:ki.kickoutFromGroup(to, ["uff4bd67e5bc6ab62760b1ff78d89dfe4"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               ki.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:kk.inviteIntoGroup(to, ["u5db69e110e5c7a468584632c6472bb66"]);has = "OK"
                               except:has = "NOT"
                               try:kk.kickoutFromGroup(to, ["u5db69e110e5c7a468584632c6472bb66"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               kk.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:kc.inviteIntoGroup(to, ["u7fed37def4d8e3bcef59b1e8af11da3a"]);has = "OK"
                               except:has = "NOT"
                               try:kc.kickoutFromGroup(to, ["u7fed37def4d8e3bcef59b1e8af11da3a"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low  0%"
                               kc.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:kb.inviteIntoGroup(to, ["u21f2166935c999fe450ce5ea5aa42652"]);has = "OK"
                               except:has = "NOT"
                               try:kb.kickoutFromGroup(to, ["u21f2166935c999fe450ce5ea5aa42652"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               kb.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                              
                               try:kd.inviteIntoGroup(to, ["u2739569d28dfd03972f92bc4508d5b95"]);has = "OK"
                               except:has = "NOT"
                               try:kd.kickoutFromGroup(to, ["u2739569d28dfd03972f92bc4508d5b95"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               kd.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:ke.inviteIntoGroup(to, ["ue093b1293a087794a6750a77b5ec3990"]);has = "OK"
                               except:has = "NOT"
                               try:ke.kickoutFromGroup(to, ["ue093b1293a087794a6750a77b5ec3990"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               ke.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:kf.inviteIntoGroup(to, ["u6756e5a6ec421fbe85b3173d2c32a16a"]);has = "OK"
                               except:has = "NOT"
                               try:kf.kickoutFromGroup(to, ["u6756e5a6ec421fbe85b3173d2c32a16a"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               kf.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:k8.inviteIntoGroup(to, ["ua747585a5201be67956b55bcfe662466"]);has = "OK"
                               except:has = "NOT"
                               try:k8.kickoutFromGroup(to, ["ua747585a5201be67956b55bcfe662466"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k8.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:k9.inviteIntoGroup(to, ["u252bef6cbe92d5682068c6b07a3659db"]);has = "OK"
                               except:has = "NOT"
                               try:k9.kickoutFromGroup(to, ["u252bef6cbe92d5682068c6b07a3659db"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low  0%"
                               k9.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:k10.inviteIntoGroup(to, ["u971c92c69915f75f6d427d580b8ee7a2"]);has = "OK"
                               except:has = "NOT"
                               try:k10.kickoutFromGroup(to, ["u971c92c69915f75f6d427d580b8ee7a2"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k10.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                              
                               try:k11.inviteIntoGroup(to, ["u4783b96f646f7ee4f77912aaf2fc16c8"]);has = "OK"
                               except:has = "NOT"
                               try:k11.kickoutFromGroup(to, ["u4783b96f646f7ee4f77912aaf2fc16c8"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k11.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:k12.inviteIntoGroup(to, ["u9a7763fdf967b345d935c7e06b632ad7"]);has = "OK"
                               except:has = "NOT"
                               try:k12.kickoutFromGroup(to, ["u9a7763fdf967b345d935c7e06b632ad7"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k12.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:k13.inviteIntoGroup(to, ["u26d534ff9575a209224834af584ddc5a"]);has = "OK"
                               except:has = "NOT"
                               try:k13.kickoutFromGroup(to, ["u26d534ff9575a209224834af584ddc5a"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k13.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:k14.inviteIntoGroup(to, ["u601169a39deea005cb054f6df3a1be01"]);has = "OK"
                               except:has = "NOT"
                               try:k14.kickoutFromGroup(to, ["u601169a39deea005cb054f6df3a1be01"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k14.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:k15.inviteIntoGroup(to, ["u608398e513e31d10a748f7976c06ca6e"]);has = "OK"
                               except:has = "NOT"
                               try:k15.kickoutFromGroup(to, ["u608398e513e31d10a748f7976c06ca6e"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low  0%"
                               k15.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:k16.inviteIntoGroup(to, ["u0cb657723b765e0294eaaee08be417ae"]);has = "OK"
                               except:has = "NOT"
                               try:k16.kickoutFromGroup(to, ["u0cb657723b765e0294eaaee08be417ae"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k16.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                              
                               try:k17.inviteIntoGroup(to, ["uda15719071a4e30a0ed3b1fce2f695ab"]);has = "OK"
                               except:has = "NOT"
                               try:k17.kickoutFromGroup(to, ["uda15719071a4e30a0ed3b1fce2f695ab"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k17.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:k18.inviteIntoGroup(to, ["u36b501abe0dff8c6767724ed32c0a140"]);has = "OK" 
                               except:has = "NOT"
                               try:k18.kickoutFromGroup(to, ["u36b501abe0dff8c6767724ed32c0a140"]);has1 = "OK"
                               except:has1 = "NOT" 
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%" 
                               k18.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:k19.inviteIntoGroup(to, ["u77d0f412a5d3d8f75baf86a9170a7b83"]);has = "OK" 
                               except:has = "NOT"
                               try:k19.kickoutFromGroup(to, ["u77d0f412a5d3d8f75baf86a9170a7b83"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k19.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))  
                               try:k20.inviteIntoGroup(to, ["u12876a2278a9b14d042c632d15ee0480"]);has = "OK"  
                               except:has = "NOT"                     
                               try:k20.kickoutFromGroup(to, ["u12876a2278a9b14d042c632d15ee0480"]);has1 = "OK"
                               except:has1 = "NOT"                     
                               if has == "OK":sil = "🔋██ full 100%"                     
                               else:sil = "🔌█▒ Low 0%"                     
                               if has1 == "OK":sil1 = "🔋██ full 100%"                     
                               else:sil1 = "🔌█▒ Low 0%"
                               k20.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))

                        elif cmd == "ผีมา":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kj.sendMessage(msg.to, "Ghost masuk "+str(G.name))
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                sw.sendMessage(msg.to, "Ghost masuk "+str(G.name))
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "ผีออก":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kj.sendMessage(msg.to, "Ghost dipaksah Out "+str(G.name))
                                kj.leaveGroup(msg.to)
                                sw.sendMessage(msg.to, "Ghost dipaksah Out "+str(G.name))
                                sw.leaveGroup(msg.to)

                        elif cmd == "b" or cmd == "pasukan":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(msg.to,responsename1)
                                kk.sendMessage(msg.to,responsename2)
                                kc.sendMessage(msg.to,responsename3)
                                kb.sendMessage(msg.to,responsename4)
                                kd.sendMessage(msg.to,responsename5)
                                ke.sendMessage(msg.to,responsename6)
                                kf.sendMessage(msg.to,responsename7)
                                k8.sendMessage(msg.to,responsename8)
                                k9.sendMessage(msg.to,responsename9)
                                k10.sendMessage(msg.to,responsename10)
                                k12.sendMessage(msg.to,responsename12)
                                k13.sendMessage(msg.to,responsename13)
                                k14.sendMessage(msg.to,responsename14)
                                k15.sendMessage(msg.to,responsename15)
                                k16.sendMessage(msg.to,responsename16)
                                k17.sendMessage(msg.to,responsename17)
                                k18.sendMessage(msg.to,responsename18)
                                k19.sendMessage(msg.to,responsename19)
                                k20.sendMessage(msg.to,responsename20)
       
                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif ("ติดดำ " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"ติดดำเรียบร้อย\n\n")
                                       except:
                                           pass

                        elif ("ล้างดำ " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"ล้างดำเรียบร้อย\n\n")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "cekban" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"✒ Rey Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"✒ Rey Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))
#===========BOT UPDATE============#
                        elif cmd == "แทค" or text.lower() == '/แทค':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"「 Daftar User Bot 」\n\n"+ma+"\nTotal「%s」List Bots" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    a = a + 1
                                    end = '\n'
                                    mb += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    a = a + 1
                                    end = '\n'
                                    mc += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"「 Daftar Admin 」\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」Pengguna Selfbot" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendText(msg.to, "Bye bye fams "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd == "rtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "「 Respontime 」\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               sendMention(msg.to, sender, "「 Selfbot Speed 」\n• User ", "")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "speedbot" or cmd == "spb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               sendMention(msg.to, sender, "「 Selfbot Speed 」\n• User ", "")
                               elapsed_time = time.time() - start
                               ki.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kk.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kc.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kb.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kd.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               ke.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kf.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kj.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               sw.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                                
                        elif cmd == "เปิดอ่าน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['RAreadPoint'][msg.to] = msg_id
                                 Setmain['RAreadMember'][msg.to] = {}
                                 cl.sendText(msg.to, "「 Status Lurking 」\nBerhasil diaktifkan, selanjutnya ketik lurkers\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'))
                            
                        elif cmd == "ปิดอ่าน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['RAreadPoint'][msg.to]
                                 del Setmain['RAreadMember'][msg.to]
                                 cl.sendText(msg.to, "「 Status Lurking 」\nBerhasil dimatikan\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'))
                            
                        elif cmd == "อ่าน":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            if msg.to in Setmain['RAreadPoint']:
                                if Setmain['RAreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['RAreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  「 Daftar Member 」    \n\n 「 Total {} Sider 」\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['RAreadPoint'][msg.to]
                                        del Setmain['RAreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['RAreadPoint'][msg.to] = msg.id
                                    Setmain['RAreadMember'][msg.to] = {}
                                else:
                                    cl.sendText(msg.to, "User kosong...")
                            else:
                                cl.sendText(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "「 Status Sider 」\nBerhasil diaktifkan\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'))
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "「 Status Sider 」\nBerhasil dimatikan\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'))
                              else:
                                  cl.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
                        elif cmd.startswith("get-audio "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " "," ")
                            cond = query.split("|")
                            search = str(cond[0])
                            with requests.session() as web:
                                web.headers["User-Agent"] = "Mozilla/5.0"
                                result = web.get("https://farzain.xyz/api/premium/yt_search.php?apikey=apikey_saintsbot&id={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    if data["respons"] != []:
                                        num = 0
                                        ret_ = "「 Pencarian Audio 」\n"
                                        for res in data["respons"]:
                                            num += 1
                                            ret_ += "\n {}. {}".format(str(num), str(res['title']))
                                        ret_ += "\n\n Total {} Result".format(str(len(data["respons"])))
                                        cl.sendMessage(msg.to, str(ret_))
                                        cl.sendText(to, "Ketik Get-yt {} | angka\nuntuk melihat detail lagu".format(str(search)))
                                if len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["respons"]):
                                        res = data["respons"][num - 1]
                                        with requests.session() as web:
                                            web.headers["User-Agent"] = "Mozilla/5.0"
                                            result = web.get("http://rahandiapi.herokuapp.com/youtubeapi?key=betakey&q=https://www.youtube.com/watch?v={}".format(str(res['video_id'])))
                                            data = result.text
                                            data = json.loads(data)
                                            ret_ = "「 Detail Lagu 」\nTitle : "+data['result']['title']
                                            ret_ += "\nLikes : "+str(data['result']['likes'])
                                            ret_ += "\nDislikes : "+str(data['result']['dislikes'])
                                            ret_ += "\nDuration : "+str(data['result']['duration'])
                                            ret_ += "\nRating : "+str(data['result']['rating'])
                                            ret_ += "\nAuthor : "+str(data['result']['author'])+"\n"
                                            cover = data['result']['thumbnail']
                                            if data["result"]["audiolist"] != []:
                                                for koplok in data["result"]["audiolist"]:
                                                    ret_ += "\nType : "+koplok['extension']
                                                    ret_ += "\nResolusi : "+koplok['resolution']
                                                    ret_ += "\nSize : "+koplok['size']
                                                    ret_ += "\nLink : "+koplok['url']
                                                    if koplok['resolution'] == '50k':
                                                        audio = koplok['url']
                                            cl.sendImageWithURL(msg.to,cover)
                                            cl.sendMessage(msg.to, str(ret_))
                                            cl.sendAudioWithURL(msg.to,audio)
 
                        elif cmd.startswith("get-fs "):
                          if msg._from in admin:
                                sep = msg.text.split(" ")
                                anu = msg.text.replace(sep[0] + " "," ")                
                                with requests.session() as web:
                                    web.headers["user-agent"] = random.choice(settings["userAgent"])
                                    r = web.get("https://farzain.xyz/api/premium/fs.php?apikey=apikey_saintsbot&id={}".format(urllib.parse.quote(anu)))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["status"] == "success":
                                        ret_ = data["url"]
                                        cl.sendImageWithURL(msg.to,ret_)
                                    else:
                                        cl.sendMessage(msg.to, "Error")
                                        
                        elif cmd.startswith("get-post "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            post = msg.text.replace(sep[0] + " ","")
                            with requests.session() as s:
                                s.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = s.get("http://m.jancok.com/klik/{}/".format(urllib.parse.quote(post)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                ret_ = '「 Get Postingan 」\n\n'
                                try:
                                    for title in soup.select("[class~=badge-item-title]"):
                                        ret_ += "• Judul : "+title.get_text()
                                        ret_ += "\n• Link : m.jancok.com"
                                    for link in soup.find_all('img',limit=1):
                                        cl.sendMessage(msg.to, ret_)
                                        cl.sendImageWithURL(msg.to, link.get('src'))
                                except Exception as e:
                                    cl.sendMessage(msg.to, "Post kosong")
                                    print(str(e))
                                    
                        elif cmd.startswith("get-line "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            user = text.replace(sep[0] + " ","")
                            conn = cl.findContactsByUserid(user)
                            try:
                                anu = conn.mid
                                dn = conn.displayName
                                bio = conn.statusMessage
                                sendMention(to, anu, "「 Contact Line ID 」\n• Nama : ", "\n• Nick : "+dn+"\n• Bio : "+bio+"\n• Contact link : http://line.me/ti/p/~"+user)
                                cl.sendContact(to, anu)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("ดึง "):
                          if msg._from in admin:
                               sep = text.split(" ")
                               idnya = text.replace(sep[0] + " ","")
                               conn = cl.findContactsByUserid(idnya)
                               cl.findAndAddContactsByMid(conn.mid)
                               cl.inviteIntoGroup(msg.to,[conn.mid])
                               group = cl.getGroup(msg.to)
                               xname = cl.getContact(conn.mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan = '「 Sukses Diinvite 」\nNama contact '
                               recky = str(xname.displayName)
                               pesan = ''
                               pesan2 = pesan+"@a\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':xname.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan+ zxc + "ke grup " + str(group.name) +""
                               cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd.startswith("ยูทูป "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                params = {"search_query": search}
                                r = requests.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╔══[ ʀᴇsᴜʟᴛ ʏᴏᴜᴛᴜʙᴇ ]"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n╠❂➣{} ]".format(str(data["title"]))
                                    ret_ += "\n╠❂ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴠɪᴅᴇᴏ ]".format(len(datas))
                                cl.sendMessage(to, str(ret_))

                        elif cmd.startswith("tr-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("tr-" + lang + " ","")
                                if lang not in list_language["list_translate"]:
                                    return ririn.sendMessage(to, "Language not found")
                                translator = Translator()
                                hasil = translator.translate(say, dest=lang)
                                A = hasil.text
                                ririn.sendMessage(to, str(A))

                        elif cmd.startswith("listmeme"):
                          if msg._from in admin:
                            proses = text.split(" ")
                            keyword = text.replace(proses[0] + " ","")
                            count = keyword.split("|")
                            search = str(count[0])
                            r = requests.get("http://api.imgflip.com/get_memes")
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                hasil = "「 Daftar Meme Image 」\n"
                                for aa in data["data"]["memes"]:
                                    no += 1
                                    hasil += "\n" + str(no) + ". "+ str(aa["name"])
                                hasil += " "
                                ret_ = "\n\nSelanjutnya ketik:\nListmeme | angka\nGet-meme text1 | text2 | angka"
                                cl.sendText(msg.to,hasil+ret_)
                            if len(count) == 2:
                                try:
                                    num = int(count[1])
                                    gambar = data["data"]["memes"][num - 1]
                                    hasil = "{}".format(str(gambar["name"]))
                                    sendMention(msg.to, msg._from,"「 Meme Image 」\nTunggu ","\nFoto sedang diproses...")
                                    cl.sendText(msg.to,hasil)
                                    cl.sendImageWithURL(msg.to,gambar["url"])
                                except Exception as e:
                                    cl.sendText(msg.to," "+str(e))
                                    
                        elif cmd.startswith("get-meme "):
                          if msg._from in admin:
                            proses = text.split(" ")
                            keyword = text.replace(proses[0]+" ","")
                            query = keyword.split("|")
                            atas = query[0]
                            bawah = query[1]
                            r = requests.get("https://api.imgflip.com/get_memes")
                            data = json.loads(r.text)
                            try:
                                num = int(query[2])
                                namamem = data["data"]["memes"][num - 1]
                                meme = int(namamem["id"])
                                api = pyimgflip.Imgflip(username='andyihsan', password='ihsan848')
                                result = api.caption_image(meme, atas,bawah)
                                sendMention(msg.to, msg._from,"「 Meme Image 」\nTunggu ","\nFoto sedang diproses...")
                                cl.sendImageWithURL(msg.to,result["url"])
                            except Exception as e:
                                cl.sendText(msg.to," "+str(e))


                        elif cmd.startswith("get-gif "):
                          if msg._from in admin:
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            count = urutan.split("|")
                            search = str(count[0])
                            r = requests.get("https://api.tenor.com/v1/search?key=PVS5D2UHR0EV&limit=10&q="+str(search))
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                hasil = "「 Pencarian Gif 」\n"
                                for aa in data["results"]:
                                    no += 1
                                    hasil += "\n" + str(no) + ". " + str(aa["title"])
                                    ret_ = "\n\nSelanjutnya Get-gif {} | angka\nuntuk melihat detail video".format(str(search))
                                cl.sendText(msg.to,hasil+ret_)
                            elif len(count) == 2:
                                try:
                                    num = int(count[1])
                                    b = data["results"][num - 1]
                                    c = str(b["id"])
                                    hasil = "Informasi gif ID "+str(c)
                                    hasil += "\n"
                                    cl.sendText(msg.to,hasil)
                                    dl = str(b["media"][0]["loopedmp4"]["url"])
                                    cl.sendVideoWithURL(msg.to,dl)
                                except Exception as e:
                                    cl.sendText(msg.to," "+str(e))                        
                        
                        elif cmd.startswith("get-xxx "):
                          if msg._from in admin:
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            count = urutan.split("|")
                            search = str(count[0])
                            r = requests.get("https://api.avgle.com/v1/search/{}/1?limit=10".format(str(search)))
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                hasil = "「 Pencarian Video 18+ 」\n"
                                for aa in data["response"]["videos"]:
                                    no += 1
                                    hasil += "\n"+str(no)+". "+str(aa["title"])+"\nDurasi : "+str(aa["duration"])
                                    ret_ = "\n\nSelanjutnya Get-xxx {} | angka\nuntuk melihat detail video".format(str(search))
                                cl.sendText(msg.to,hasil+ret_)
                            elif len(count) == 2:
                                try:
                                    num = int(count[1])
                                    b = data["response"]["videos"][num - 1]
                                    c = str(b["vid"])
                                    d = requests.get("https://api.avgle.com/v1/video/"+str(c))
                                    data1 = json.loads(d.text)
                                    hasil = "Judul "+str(data1["response"]["video"]["title"])
                                    hasil += "\n\nDurasi : "+str(data1["response"]["video"]["duration"])
                                    hasil += "\nKualitas HD : "+str(data1["response"]["video"]["hd"])
                                    hasil += "\nDitonton "+str(data1["response"]["video"]["viewnumber"])
                                    e = requests.get("https://api-ssl.bitly.com/v3/shorten?access_token=c52a3ad85f0eeafbb55e680d0fb926a5c4cab823&longUrl="+str(data1["response"]["video"]["video_url"]))
                                    data2 = json.loads(e.text)
                                    hasil += "\nLink video : "+str(data1["response"]["video"]["video_url"])
                                    hasil += "\nLink embed : "+str(data1["response"]["video"]["embedded_url"])
                                    hasil += "\n\nKalau tidak bisa jangan lupa pakai vpn kesayangan anda"
                                    cl.sendText(msg.to,hasil)
                                    anuanu = str(data1["response"]["video"]["preview_url"])
                                    path = cl.downloadFileURL(anuanu)
                                    cl.sendImage(msg.to,path)
                                    cl.sendVideoWithURL(msg.to, data["data"]["url"])
                                except Exception as e:
                                    cl.sendText(msg.to," "+str(e))

                        elif cmd.startswith("get-sholat "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「 Jadwal Sholat 」\n"
                                         ret_ += "\n「✭」 Lokasi : " + data[0]
                                         ret_ += "\n「✭」 " + data[1]
                                         ret_ += "\n「✭」 " + data[2]
                                         ret_ += "\n「✭」 " + data[3]
                                         ret_ += "\n「✭」 " + data[4]
                                         ret_ += "\n「✭」 " + data[5]
                                         ret_ += "\n\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                         ret_ += "\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                  cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("get-cuaca "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「 Status Cuaca 」\n"
                                    ret_ += "\n「✭」 Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n「✭」 Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n「✭」 Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n「✭」 Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n「✭」 Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("get-lokasi "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「 Info Lokasi 」"
                                    ret_ += "\n「✭」 Location : " + data[0]
                                    ret_ += "\n「✭」 Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("lirik "):
                          if msg._from in admin:
                            data = msg.text.lower().replace("lirik ","")                                
                            artis = data.split('|')
                            artis = artis[1].replace(' ','_')
                            judul = data.split('|')
                            judul = judul[2].replace(' ','_')
                            with requests.session() as s:
                                s.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = s.get("https://www.wowkeren.com/lirik/lagu/{}/{}.html".format(urllib.parse.quote(artis), judul))
                                x = s.get("https://www.wowkeren.com/seleb/{}/lirik.html".format(urllib.parse.quote(artis)))
                                data = BeautifulSoup(r.content, 'html5lib')
                                data1 = BeautifulSoup(x.content, 'html5lib')
                                ret_ = ''
                                try:
                                    yyk = data1.select("[class~=content]")[1].text
                                    yoyok = yyk.replace("		", " ")
                                    ret_ += "  「 Informasi Penyanyi 」"+yoyok
                                    ret = data.find("div", id="JudulHalaman")
                                    ret_ += "Judul lagu : "+ret.get_text()
                                    ret_ += "\n\n  「 Lirik Lagunya 」"+data.select("[class~=GambarUtama]")[1].text
                                    for link in data1.findAll('div', attrs={'class':'item'}):
                                        cl.sendImageWithURL(msg.to, "https://www.wowkeren.com"+link.find('img')['src'])
                                    cl.sendMessage(to, ret_)
                                except:
                                    cl.sendMessage(to, "lirik tidak tersedia")

                        elif cmd.startswith("get-lirik "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   url = "http://rahandiapi.herokuapp.com/lyricapi?key=betakey&q={}".format(urllib.parse.quote(search))
                                   link = web.get(url)
                                   data = link.text
                                   data = json.loads(data)
                                   start = timeit.timeit()
                                   ret_ = "「 Lirik Search 」"
                                   ret_ += "\n「✭」 Judul : {}".format(str(data["title"]))
                                   ret_ += "\n「✭」 Time Taken : {}".format(str(start))
                                   ret_ += "\n\n{}".format(str(data["lyric"]))
                                   cl.sendText(msg.to, str(ret_))

                        elif cmd.startswith("musik "):
                            if msg._from in admin:
                               sep = msg.text.split(" ")
                               query = msg.text.replace(sep[0] + " ","")
                               cond = query.split("-")
                               search = str(cond[0])
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   result = web.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                   data = result.text
                                   data = json.loads(data)
                                   if len(cond) == 1:
                                      num = 0
                                      ret_ = "「 Pencarian Musik 」\n"
                                      for music in data["result"]:
                                          num += 1
                                          ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                      ret_ += "\n\n「 Total {} Pencarian 」".format(str(len(data["result"])))
                                      cl.sendMessage(to, str(ret_))
                                      sendMention(msg.to, msg._from,"","\nJika ingin menggunakan,\nSilahkan gunakan:\n\nMusik penyanyi-angka")
                                   if len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data["result"]):
                                               music = data["result"][num - 1]
                                               with requests.session() as web:
                                                    web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                                    result = web.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                                    data = result.text
                                                    data = json.loads(data)
                                                    if data["result"] != []:
                                                         ret_ = "「 Pencarian Musik 」"
                                                         ret_ += "\n• Judul : {}".format(str(data["result"]["song"]))
                                                         ret_ += "\n• Album : {}".format(str(data["result"]["album"]))
                                                         ret_ += "\n• Ukuran : {}".format(str(data["result"]["size"]))
                                                         ret_ += " \n• Link Musik : {}".format(str(data["result"]["mp3"]))
                                                         ret_ += "\n「 Tunggu Musiknya Keluar 」"
                                                         cl.sendImageWithURL(to, str(data["result"]["img"]))
                                                         cl.sendMessage(to, str(ret_))
                                                         cl.sendAudioWithURL(to, str(data["result"]["mp3"][0]))

                        elif cmd.startswith("kode wilayah"):
                          if msg._from in admin:
                            ret_ = "「 Daftar Kode Wilayah 」\n\n"
                            ret_ += "248 = Alternatif - Cibubur\n119 = Ancol - bandara\n238 = Asia afrika - Bandung\n169 = Asia afrika - Hang lekir"
                            ret_ += "\n276 = Asia afrika - Sudirman\n295 = Bandengan - kota\n294 = Bandengan - Selatan\n255 = Boulevard Barat raya"
                            ret_ += "\n102 = Buncit raya\n272 = Bundaran - HI\n93 = Cideng barat\n289 = Cikini raya\n242 = Ciledug raya - Cipulir"
                            ret_ += "\n175 = Ciloto - Puncak\n142 = Daan mogot - Grogol\n143 = Daan mogot - Pesing\n338 = Dewi sartika - Cawang"
                            ret_ += "\n124 = DI Panjaitan - By pass\n123 = DI Panjaitan - Cawang\n13 = Dr Satrio - Casablanca\n105 = Dr Satrio - Karet"
                            ret_ += "\n245 = Dukuh atas - MRT Jakarta\n334 = Fachrudin raya\n252 = Fatmawati - Blok A\n253 = Fatmawati - Cipete raya"
                            ret_ += "\n203 = Flyover Daan mogot\n336 = Flyover Jati baru\n172 = Flyover Senen - Kramat\n77 = Gunung sahari"
                            ret_ += "\n137 = Hasyim Ashari\n273 = Jalan MH Thamrin\n327 = Jalan RS Fatmawati\n292 = Jl. Otista 3\n333 = Jl. Panjang - Kebon jeruk"
                            ret_ += "\n226 = JORR - Bintaro\n227 = JORR - Fatmawati\n173 = Kramat raya - Senen\n117 = Kyai Caringin - Cideng\n126 = Letjen Suprapto - Senen"
                            ret_ += "\n204 = Mangga besar\n319 = Margaguna raya\n326 = Margonda raya\n310 = Mas Mansyur - Karet\n309 = Mas Mansyur - Tn. Abang"
                            ret_ += "\n64 = Matraman\n140 = Matraman - Salemba\n284 = Metro Pdk. Indah\n191 = MT Haryono - Pancoran\n160 = Pancoran barat"
                            ret_ += "\n331 = Pejompongan - Slipi\n332 = Pejompongan - Sudirman\n312 = Perempatan pramuka\n171 = Permata hijau - Panjang\n99 = Petojo Harmoni"
                            ret_ += "\n223 = Pramuka - Matraman\n222 = Pramuka raya\n314 = Pramuka raya - jl. Tambak\n313 = Pramuka - Salemba raya\n130 = Puncak raya KM84"
                            ret_ += "\n318 = Radio dalam raya\n328 = RS Fatmawati - TB\n274 = Senayan city\n132 = Slipi - Palmerah\n133 = Slipi - Tomang"
                            ret_ += "\n162 = S Parman - Grogol\n324 = Sudirman - Blok M\n18 = Sudirman - Dukuh atas\n325 = Sudirman - Semanggi\n112 = Sudirman - Setiabudi"
                            ret_ += "\n246 = Sudirman - Thamrin\n320 = Sultan agung - Sudirman\n100 = Suryo pranoto\n220 = Tanjung duren\n301 = Tol kebon jeruk"
                            ret_ += "\n41 = Tomang/Simpang\n159 = Tugu Pancoran\n145 = Warung jati - Pejaten\n205 = Yos Sudarso - Cawang\n206 = Yos Sudarso - Tj. Priuk"
                            ret_ += "\n\nUntuk melihat cctv,\nKetik lihat (kode wilayah)"                            
                            cl.sendMessage(to, ret_)

                        elif cmd.startswith("lihat "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            cct = msg.text.replace(sep[0] + " ","")
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
                                r = s.get("http://lewatmana.com/cam/{}/bundaran-hi/".format(urllib.parse.quote(cct)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                try:
                                    ret_ = "「 Informasi CCTV 」\nDaerah "
                                    ret_ += soup.select("[class~=cam-viewer-title]")[0].text
                                    ret_ += "\nCctv update per 5 menit"
                                    vid = soup.find('source')['src']
                                    ret = "Untuk melihat wilayah lainnya, Ketik kode wilayah"
                                    cl.sendMessage(to, ret_)
                                    cl.sendVideoWithURL(to, vid)
                                    cl.sendMessage(to, ret)
                                except:
                                    cl.sendMessage(to, "Data cctv tidak ditemukan!")

                        elif cmd.startswith("get-image "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    start = timeit.timeit()
                                    items = data["result"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendText(msg.to,"「 Google Image 」\nType : Search Image\nTime taken : %seconds" % (start))
                                    cl.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("get-apk "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " ","")
                            cond = query.split("|")
                            search = str(cond[0])
                            with requests.session() as s:
                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                r = s.get("https://apkpure.com/id/search?q={}".format(str(search)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                data = soup.findAll('dl', attrs={'class':'search-dl'})
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "「 Pencarian Aplikasi 」\n"
                                    for apk in data:
                                        num += 1
                                        link = "https://apkpure.com"+apk.find('a')['href']
                                        title = apk.find('a')['title']
                                        ret_ += "\n {}. {}".format(str(num), str(title))
                                    ret_ += "\n\n Total {} Result".format(str(len(data)))
                                    ret = "Selanjutnya ketik:\nGet-apk {} | angka".format(str(search))
                                    cl.sendMessage(to, str(ret_))
                                    cl.sendMessage(to, str(ret))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data):
                                        apk = data[num - 1]
                                        with requests.session() as s:
                                            s.headers['user-agent'] = random.choice(settings["userAgent"])
                                            r = s.get("https://apkpure.com{}/download?from=details".format(str(apk.find('a')['href'])))
                                            soup = BeautifulSoup(r.content, 'html5lib')
                                            data = soup.findAll('div', attrs={'class':'fast-download-box'})
                                            for down in data:
                                                load = down.select("a[href*=https://download.apkpure.com/]")[0]
                                                file = load['href']
                                                ret_ = "File info :\n"+down.find('span', attrs={'class':'file'}).text
                                                with requests.session() as web:
                                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                                    r = web.get("https://api-ssl.bitly.com/v3/shorten?access_token=497e74afd44780116ed281ea35c7317285694bf1&longUrl={}".format(urllib.parse.quote(file)))
                                                    data = r.text
                                                    data = json.loads(data)
                                                    ret_ += "\nLink Download :\n"+data["data"]["url"]
                                                cl.sendMessage(to, str(ret_))

                        elif cmd.startswith("get-anime "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            anime = msg.text.replace(sep[0] + " ","%20")                
                            with requests.session() as web:
                                web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                            r = web.get("https://kitsu.io/api/edge/anime?filter[text]={}".format(urllib.parse.quote(anime)))
                            data = r.text
                            data = json.loads(data)
                            ret_ = ''
                            if data["data"] != []:
                                for a in data["data"]:
                                    if a["attributes"]["subtype"] == "TV":
                                        sin = a["attributes"]["synopsis"]
                                        translator = Translator()
                                        hasil = translator.translate(sin, dest='id')
                                        sinop = hasil.text
                                        ret_ += '「 Anime {} 」'.format(str(a["attributes"]["canonicalTitle"]))
                                        ret_ += '\n• Rilis : '+str(a["attributes"]["startDate"])
                                        ret_ += '\n• Rating : '+str(a["attributes"]["ratingRank"])
                                        ret_ += '\n• Type : '+str(a["attributes"]["subtype"])
                                        ret_ += '\n• Sinopsis :\n'+str(sinop)
                                        ret_ += '\n\n'
                                        cl.sendImageWithURL(msg.to, str(a["attributes"]["posterImage"]["small"]))
                            cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("get-zodiak "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            query = text.replace(sep[0] + " ","")
                            r = requests.post("https://aztro.herokuapp.com/?sign={}&day=today".format(urllib.parse.quote(query)))
                            data = r.text
                            data = json.loads(data)
                            data1 = data["description"]
                            data2 = data["color"]
                            translator = Translator()
                            hasil = translator.translate(data1, dest='id')
                            hasil1 = translator.translate(data2, dest='id')
                            A = hasil.text
                            B = hasil1.text
                            ret_ = "「 Ramalan zodiak {} hari ini 」\n".format(str(query))
                            ret_ += str(A)
                            ret_ += "\n======================\n• Tanggal : " +str(data["current_date"])
                            ret_ += "\n• Rasi bintang : "+query
                            ret_ += " ("+str(data["date_range"]+")")
                            ret_ += "\n• Pasangan Zodiak : " +str(data["compatibility"])
                            ret_ += "\n• Angka keberuntungan : " +str(data["lucky_number"])
                            ret_ += "\n• Waktu keberuntungan : " +str(data["lucky_time"])
                            ret_ += "\n• Warna kesukaan : " +str(B)
                            cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("get-bintang "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            url = msg.text.replace(sep[0] + " ","")    
                            with requests.session() as s:
                                s.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = s.get("https://www.vemale.com/zodiak/{}".format(urllib.parse.quote(url)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                ret_ = ""
                                for a in soup.select('div.vml-zodiak-detail'):
                                    ret_ += a.h1.string
                                    ret_ += "\n"+ a.h4.string
                                    ret_ += " : "+ a.span.string +""
                                for b in soup.select('div.col-center'):
                                    ret_ += "\nTanggal : "+ b.string
                                for d in soup.select('div.number-zodiak'):
                                    ret_ += "\nAngka keberuntungan : "+ d.string
                                for c in soup.select('div.paragraph-left'):
                                    ta = c.text
                                    tab = ta.replace("    ", "")
                                    tabs = tab.replace(".", ".\n")
                                    ret_ += "\n"+ tabs
                                    #print (ret_)
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("get-telpon "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            nomor = text.replace(sep[0] + " ","")
                            r = requests.get("http://apisora2.herokuapp.com/prank/call/?no={}".format(urllib.parse.quote(nomor)))
                            data = r.text
                            data = json.loads(data)
                            ret_ = "「 Prangked Telpon 」"
                            ret_ += "\n• Status : {}".format(str(data["status"]))
                            ret_ += "\n• Tujuan "+str(data["result"])
                            cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("get-sms "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            nomor = text.replace(sep[0] + " ","")
                            r = requests.get("http://apisora2.herokuapp.com/prank/sms/?no={}".format(urllib.parse.quote(nomor)))
                            data = r.text
                            data = json.loads(data)
                            ret_ = "「 Prangked Sms 」"
                            ret_ += "\n• Status : {}".format(str(data["status"]))
                            ret_ += "\n• Tujuan "+str(data["result"])
                            cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("get-mimpi "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            mimpi = msg.text.replace(sep[0] + " ","")  
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0'
                                r = s.get("http://primbon.com/tafsir_mimpi.php?mimpi={}&submit=+Submit+".format(urllib.parse.quote(mimpi)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                for anu in soup.find_all('i'):
                                    ret_ = anu.get_text()
                                    cl.sendMessage(msg.to,ret_)

                        elif text.lower() == 'top kaskus':
                           if msg._from in admin:
                               r = requests.get("https://api.bayyu.net/kaskus-hotthread/?apikey=c28c944199384f191335f1f8924414fa839350d&page=2")
                               data=r.text
                               data=json.loads(data)                                                                                                      
                               if data["hot_threads"] != []:
                                   no = 0
                                   hasil = "「 Kaskus Search 」\n"
                                   for news in data["hot_threads"]:
                                        no += 1                  
                                        hasil += "\n" + str(no) + ". Judul : " + str(news["title"]) + "\n • Deskripsi : " + str(news["detail"]) + "\n• Link: " + str(news["link"]) + "\n"
                                        hasil += "\n"
                                   cl.sendText(msg.to, str(hasil))

                        elif cmd.startswith("get-video "):
                          if msg._from in admin:
                                sep = msg.text.split(" ")
                                search = msg.text.replace(sep[0] + " ","")
                                with requests.session() as web:
                                      web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                      url = web.get("http://rahandiapi.herokuapp.com/youtubeapi/search?key=betakey&q={}".format(urllib.parse.quote(search)))
                                      data = url.text
                                      data = json.loads(data)
                                      if data["result"] != []:
                                          video = random.choice(data["result"]["videolist"])
                                          vid = video["url"]
                                          start = timeit.timeit()
                                          ret = "「 Informasi Video 」\n"
                                          ret += "• Judul : {}".format(str(data["result"]["title"]))
                                          ret += "\n• Author : {}".format(str(data["result"]["author"]))
                                          ret += "\n• Durasi : {}".format(str(data["result"]["duration"]))
                                          ret += "\n• Like nya : {}".format(str(data["result"]["likes"]))
                                          ret += "\n• Rating : {}".format(str(data["result"]["rating"]))
                                          ret += "\n• TimeTaken : {}".format(str(start))
                                          ret += "\n• Deskripsi : {}\n「 Waiting Encoding 」".format(str(data["result"]["description"]))
                                          cl.sendText(msg.to, str(ret))
                                          cl.sendVideoWithURL(msg.to, str(vid))

                        elif cmd.startswith("get-mp3 "):
                          if msg._from in admin:
                                sep = msg.text.split(" ")
                                search = msg.text.replace(sep[0] + " ","")
                                with requests.session() as web:
                                      web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                      url = web.get("http://rahandiapi.herokuapp.com/youtubeapi/search?key=betakey&q={}".format(urllib.parse.quote(search)))
                                      data = url.text
                                      data = json.loads(data)
                                      if data["result"] != []:
                                          audio = random.choice(data["result"]["audiolist"])
                                          aud = audio["url"]
                                          start = timeit.timeit()
                                          ret = "「 Informasi Mp3 」\n"
                                          ret += "• Judul : {}".format(str(data["result"]["title"]))
                                          ret += "\n• Author : {}".format(str(data["result"]["author"]))
                                          ret += "\n• Durasi : {}".format(str(data["result"]["duration"]))
                                          ret += "\n• Like nya : {}".format(str(data["result"]["likes"]))
                                          ret += "\n• Rating : {}".format(str(data["result"]["rating"]))
                                          ret += "\n• TimeTaken : {}".format(str(start))
                                          ret += "\n• Deskripsi : {}\n「 Waiting Encoding 」".format(str(data["result"]["description"]))
                                          cl.sendText(msg.to, str(ret))
                                          cl.sendAudioWithURL(msg.to, str(aud))

                        elif cmd.startswith("get-instagram "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['graphql']['user']['full_name'])
                                bioIG = str(data['graphql']['user']['biography'])
                                mediaIG = str(data['graphql']['user']['edge_owner_to_timeline_media']['count'])
                                verifIG = str(data['graphql']['user']['is_verified'])
                                usernameIG = str(data['graphql']['user']['username'])
                                followerIG = str(data['graphql']['user']['edge_followed_by']['count'])
                                profileIG = data['graphql']['user']['profile_pic_url_hd']
                                privateIG = str(data['graphql']['user']['is_private'])
                                followIG = str(data['graphql']['user']['edge_follow']['count'])
                                link = "• Link : " + "https://www.instagram.com/" + instagram
                                text = "「 Instagram User 」\n• Name : "+namaIG+"\n• Username : "+usernameIG+"\n• Follower : "+followerIG+"\n• Following : "+followIG+"\n• Total post : "+mediaIG+"\n• Verified : "+verifIG+"\n• Private : "+privateIG+"\n• Biography : "+bioIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("get-date "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"「 Date Info 」\n"+"「✭」 Date Of Birth : "+lahir+"\n「✭」 Age : "+usia+"\n「✭」 Ultah : "+ultah+"\n「✭」 Zodiak : "+zodiak)

                        elif cmd.startswith("spamtag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["RAlimit"] = num
                                cl.sendText(msg.to,"「 Status Spamtag 」\nBerhasil diubah jadi {} kali".format(str(strnum)))

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendText(msg.to,"「 Status Spamcall 」\nBerhasil diubah jadi {} kali".format(str(strnum)))

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["RAlimit"])
                                    if jmlh <= 10000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        cl.sendText(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd.startswith("panggil "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(key1)
                                    if jmlh <= 10000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))

                        elif cmd == "รัวคอล":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                call.acquireGroupCallRoute(to)
                                call.inviteIntoGroupCall(to, contactIds=members)
                                        
                        elif cmd.startswith("รัวคอล "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                proses = text.split(" ")
                                strnum = text.replace(proses[0] + " ","")
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jumlah = int(strnum)
                                cl.sendText(msg.to,"Undangan call grup {} sukses".format(str(strnum)))
                                if jumlah <= 10000:
                                   for x in range(jumlah):
                                   	try:
                                           call.acquireGroupCallRoute(to)
                                           call.inviteIntoGroupCall(to, contactIds=members)
                                   	except Exception as e:
                                          cl.sendText(msg.to,str(e))

                        elif '/ของขวัญ: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('/ของขวัญ: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              cl.sendText(msg.to,"「 Spam Gift 」\nBerhasil spamgift {} kali".format(str(jumlah)))
                              if jumlah <= 10000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      
                        elif '/แสปม: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('/แสปม: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 10000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))

                        elif cmd == "เชคบอท" or cmd == "ชบ":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(msg.to, "อยู่ค้าบ ")
                                kk.sendMessage(msg.to, "อยู่ค้าบ ")
                                kc.sendMessage(msg.to, "อยู่ค้าบ ")
                                kb.sendMessage(msg.to, "อยู่ค้าบ ")
                                kd.sendMessage(msg.to, "อยู่ค้าบ ")
                                ke.sendMessage(msg.to, "อยู่ค้าบ ")
                                kf.sendMessage(msg.to, "อยู่ค้าบ ")
                                k8.sendMessage(msg.to, "อยู่ค้าบ ")
                                k9.sendMessage(msg.to, "อยู่ค้าบ ")
                                k10.sendMessage(msg.to, "อยู่ค้าบ ")
                                k11.sendMessage(msg.to, "อยู่ค้าบ ")
                                k12.sendMessage(msg.to, "อยู่ค้าบ ")
                                k13.sendMessage(msg.to, "อยู่ค้าบ ")
                                k14.sendMessage(msg.to, "อยู่ค้าบ ")
                                k15.sendMessage(msg.to, "อยู่ค้าบ ")
                                k16.sendMessage(msg.to, "อยู่ค้าบ ")
                                k17.sendMessage(msg.to, "อยู่ค้าบ ")
                                k18.sendMessage(msg.to, "อยู่ค้าบ ")
                                k19.sendMessage(msg.to, "อยู่ค้าบ ")
                                k20.sendMessage(msg.to, "อยู่ค้าบ ")
                                

                        elif cmd == "เชิญบอท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                    kd.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                    kf.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                                    
                        elif cmd == "เชิญผี":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Jmid,Zmid])
                                    cl.sendMessage(msg.to,"Grup "+str(ginfo.name)+"Stay di luar bos")
                                except:
                                    pass           

                        elif cmd == "คิกมา":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k10.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k11.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k12.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k13.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k14.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k15.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k16.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k17.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k18.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k19.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k20.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)

                        elif cmd == "คิกออก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                k8.leaveGroup(msg.to)
                                k9.leaveGroup(msg.to)
                                k10.leaveGroup(msg.to)
                                k11.leaveGroup(msg.to)
                                k12.leaveGroup(msg.to)
                                k13.leaveGroup(msg.to)
                                k14.leaveGroup(msg.to)
                                k15.leaveGroup(msg.to)
                                k16.leaveGroup(msg.to)
                                k17.leaveGroup(msg.to)
                                k18.leaveGroup(msg.to)
                                k19.leaveGroup(msg.to)
                                k20.leaveGroup(msg.to)
                                
                        elif cmd == "ออกกลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "Asalamu.alaikum..wr..wb..! Bye bye "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("ออก "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        kb.leaveGroup(i)
                                        cl.sendMessage(to,"Berhasil keluar dari grup " +h)      
 
                        elif cmd == "ผีมา":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "ผีออก":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kj.leaveGroup(msg.to)
                                sw.leaveGroup(msg.to)

                        elif ("ผี2เตะ " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass
                        elif ("ผี1เตะ " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           kj.kickoutFromGroup(msg.to, [target])
                                           kj.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass                  

                        elif ("ตั้งแอดมิน " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"ตั้งเรียบร้อย...")
                                       except:
                                           pass

                        elif ("ตั้งเชล " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"ตั้งเรียบร้อย...")
                                       except:
                                           pass

                        elif ("ตั้งบอท " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"ตั้งเรียบร้อย...")
                                       except:
                                           pass

                        elif ("ลบแอดมิน " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"ลบเรียบร้อย...")
                                       except:
                                           pass

                        elif ("ลบเชล " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"ลบเรียบร้อย...")
                                       except:
                                           pass

                        elif ("ลบบอท " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"ลบเรียบร้อย...")
                                       except:
                                           pass

                        elif cmd == "แอดมินคท" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendMessage(msg.to,"ส่ง คท มา/n/nแอดมินส่งได้คนเดียว")

                        elif cmd == "ลบแอดมินคท" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendMessage(msg.to,"ส่ง คท มา/n/nแอดมินส่งได้คนเดียว")

                        elif cmd == "เชลคท" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendMessage(msg.to,"ส่ง คท มา/n/nแอดมินส่งได้คนเดียว")

                        elif cmd == "ลบเชลคท" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendMessage(msg.to,"ส่ง คท มา/n/nแอดมินส่งได้คนเดียว")

                        elif cmd == "บอทคท" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendMessage(msg.to,"ส่ง คท มา/n/nแอดมินส่งได้คนเดียว")

                        elif cmd == "ลบบอทคท" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendMessage(msg.to,"ส่ง คท มา/n/nแอดมินส่งได้คนเดียว")

                        elif cmd == "ปิดข้อความ" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendMessage(msg.to,"Berhasil di Refresh...")

                        elif cmd == "คทแอดมิน" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "คทเชล" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "คทบอท" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "เปิดคท" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "ปิดคท" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "talkban on" or text.lower() == 'talkban on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["talkban"] = True
                                cl.sendMessage(msg.to,"Talk Ban diaktifkan")

                        elif cmd == "talkban off" or text.lower() == 'talkban off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["talkban"] = False
                                cl.sendMessage(msg.to,"Talk Ban dinonaktifkan")

                        elif cmd == "เชคดำ" or text.lower() == 'bc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Tidak ada blacklist")
                                    ki.sendMessage(msg.to,"Tidak ada blacklist")
                                    kk.sendMessage(msg.to,"Tidak ada blacklist")
                                    kc.sendMessage(msg.to,"Tidak ada blacklist")
                                    kb.sendMessage(msg.to,"Tidak ada blacklist")
                                    kd.sendMessage(msg.to,"Tidak ada blacklist")
                                    ke.sendMessage(msg.to,"Tidak ada blacklist")
                                    kf.sendMessage(msg.to,"Tidak ada blacklist")
                                    kj.sendMessage(msg.to,"Tidak ada blacklist")
                                    sw.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "cb" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"ล้างดำหมดแล้วคัฟเจ้านาย " +mc)

                        elif 'js ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('js ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Anti JS sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Anti JS Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Anti JS Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti JS Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'ผี ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ผี ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Ghost Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Ghost Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
#=========== [ Add Image ] ============#
                        elif cmd.startswith("ตั้งรูป "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in images:
                                wait["Addimage"]["status"] = True
                                wait["Addimage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Silahkan kirim fotonya...") 
                            else:
                                cl.sendText(msg.to, "Foto itu sudah dalam list") 
                                
                        elif cmd.startswith("ลบรูป "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in images:
                                cl.deleteFile(images[str(name.lower())])
                                del images[str(name.lower())]
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Berhasil menghapus {}".format( str(name.lower())))
                            else:
                                cl.sendText(msg.to, "Foto itu tidak ada dalam list") 
                                 
                        elif text.lower() == "รูป":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Image 」\n\n"
                             for image in images:
                                 no += 1
                                 ret_ += str(no) + ". " + image.title() + "\n"
                             ret_ += "\nTotal「{}」Images".format(str(len(images)))
                             cl.sendText(to, ret_)
#=========== [ Add Video ] ============#                               
                        elif cmd.startswith("ตั้งวิดีโอ "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in videos:
                                wait["Addvideo"]["status"] = True
                                wait["Addvideo"]["name"] = str(name.lower())
                                videos[str(name.lower())] = ""
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Silahkan kirim videonya...") 
                            else:
                                cl.sendText(msg.to, "Video itu sudah dalam list") 
                                
                        elif cmd.startswith("ลบวิดีโอ "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in videos:
                                cl.deleteFile(videos[str(name.lower())])
                                del videos[str(name.lower())]
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Berhasil menghapus video {}".format( str(name.lower())))
                            else:
                                cl.sendText(msg.to, "Video itu tidak ada dalam list") 
                                 
                        elif text.lower() == "วิดีโอ":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Video 」\n\n"
                             for video in videos:
                                 no += 1
                                 ret_ += str(no) + ". " + video.title() + "\n"
                             ret_ += "\nTotal「{}」Videos".format(str(len(videos)))
                             cl.sendText(to, ret_)
                             sendMention(msg.to, msg._from,"","\nJika ingin play video nya,\nSilahkan ketik nama - judul\nBisa juga ketik namanya saja")
#=========== [ Add Video ] ============#                               
                        elif cmd.startswith("ตั้งเพลง "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in audios:
                                wait["Addaudio"]["status"] = True
                                wait["Addaudio"]["name"] = str(name.lower())
                                audios[str(name.lower())] = ""
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Silahkan kirim mp3 nya...") 
                            else:
                                cl.sendText(msg.to, "Mp3 itu sudah dalam list") 
                                
                        elif cmd.startswith("ลบเพลง "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in audios:
                                cl.deleteFile(audios[str(name.lower())])
                                del audios[str(name.lower())]
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Berhasil menghapus mp3 {}".format( str(name.lower())))
                            else:
                                cl.sendText(msg.to, "Mp3 itu tidak ada dalam list") 
                                 
                        elif cmd == "เพลง":
                             no = 0
                             ret_ = "「 Daftar Lagu 」\n\n"
                             for audio in audios:
                                 no += 1
                                 ret_ += str(no) + ". " + audio.title() + "\n"
                             ret_ += "\nTotal「{}」Lagu".format(str(len(audios)))
                             cl.sendText(to, ret_)
                             sendMention(msg.to, msg._from,"","\nJika ingin play mp3 nya,\nSilahkan ketik nama - judul\nBisa juga ketik namanya saja")
#=========== [ Add Sticker ] ============#                                            
                        elif cmd.startswith("ตั้งสติกเกอร์ "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in stickers:
                                wait["Addsticker"]["status"] = True
                                wait["Addsticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = ""
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Silahkan kirim stickernya...") 
                            else:
                                cl.sendText(msg.to, "Sticker itu sudah dalam list") 
                                
                        elif cmd.startswith("ลบสติกเกอร์ "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in stickers:
                                del stickers[str(name.lower())]
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                            else:
                                cl.sendText(msg.to, "Sticker itu tidak ada dalam list") 
                                 
                        elif text.lower() == "สติกเกอร์":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Sticker 」\n\n"
                             for sticker in stickers:
                                 no += 1
                                 ret_ += str(no) + ". " + sticker.title() + "\n"
                             ret_ += "\nTotal「{}」Stickers".format(str(len(stickers)))
                             cl.sendText(to, ret_)
                             
                        elif cmd == "promo":
                          if msg._from in admin:
                             cl.sendMessage(msg.to,"──────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅──────\nᴼᴾᴱᴺ ᴼᴿᴰᴱᴿ\n────────┅┅───────\n➣ꜱᴇʟꜰʙᴏᴛ ᴏɴʟʏ\n➣ꜱᴇʟꜰʙᴏᴛ + ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 2 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 3 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 4 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 5 ᴀꜱɪꜱᴛ\n➣ʙᴏᴛᴘʀᴏᴛᴇᴄᴛ 3-11 ʙᴏᴛ ᴀꜱɪꜱᴛ\n➣ɴᴇᴡ ꜱᴄʀɪᴘᴛ\n➣ʜʀɢᴀ ʙɪꜱᴀ ɴᴇɢᴏ\n─────────┅┅─────────\n  ✯❇͜͡❇͜͡C͜͡r͜͡e͜͡a͜͡t͜͡o͜͡r✯͜͡$͜͡ë͜͡I͜͡F͜͡-͜͡฿͜͜͡͡o͜͡t͜͡ ͜͡❇͜͡❇✯\nline.me/ti/p/~mai06555mai\n➣ѕєʟғвот κɪcκєʀ_+_ᴘʀᴏᴛᴇᴄᴛ\n────────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅────────")
                             msg.contentType = 13
                             msg.contentMetadata = {'mid': admin}
                             tanya = msg.text.replace("promo ","")
                             jawab = ("──────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅──────\nᴼᴾᴱᴺ ᴼᴿᴰᴱᴿ\n────────┅┅───────\n➣ꜱᴇʟꜰʙᴏᴛ ᴏɴʟʏ\n➣ꜱᴇʟꜰʙᴏᴛ + ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 2 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 3 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 4 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 5 ᴀꜱɪꜱᴛ\n➣ʙᴏᴛᴘʀᴏᴛᴇᴄᴛ 3-11 ʙᴏᴛ ᴀꜱɪꜱᴛ\n➣ɴᴇᴡ ꜱᴄʀɪᴘᴛ\n➣ʜʀɢᴀ ʙɪꜱᴀ ɴᴇɢᴏ\n─────────┅┅─────────\n  ✯❇͜͡❇͜͡C͜͡r͜͡e͜͡a͜͡t͜͡o͜͡r✯͜͡$͜͡ë͜͡I͜͡F͜͡-͜͡฿͜͜͡͡o͜͡t͜͡ ͜͡❇͜͡❇✯\nline.me/ti/p/~mai06555mai\n➣ѕєʟғвот κɪcκєʀ_+_ᴘʀᴏᴛᴇᴄᴛ\n────────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅────────")
                             jawaban = random.choice(jawab)
                             tts = gTTS(text=jawaban, lang='id')
                             tts.save('tts.mp3')
                             cl.sendAudio(msg.to,'tts.mp3')
                             cl.sendMessage(msg)         
                             cl.sendMessage(msg.to,"Jika Berminat Langsung Hubungi Kami Ya Trima Kasih😊😊")
#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Welcome 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Welcome 」\n" + msgs)

                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Url 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Url 」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect kick 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect kick 」\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Join 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Join 」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Cancel 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Cancel 」\n" + msgs)

                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Invite 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Invite 」\n" + msgs)

                        elif 'Allpro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua sudah diaktifkan"
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua protection diaktifkan"
                                  cl.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    cl.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)

#===========COMMAND ON OFF============#
                        elif cmd == "เปิดรันกลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["SpamInvite"] = True
                                cl.sendMessage(msg.to,"Send Contact to spam grup..")

                        elif cmd == "ปิดรันกลุ่ม":
                          if wait["selfbot"] == False:
                            if msg._from in admin:
                                settings["SpamInvite"] = False
                                cl.sendMessage(msg.to,"Send Contact to send grup Off..")

                        elif cmd == "เปิดยกเลิก" or text.lower() == 'unsend on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = True
                                sendMention(msg.to, sender, "「 Status Unsend 」\nUser ", "\nSilahkan unsend pesannya,\nKetik unsend off jika sudah slesai")

                        elif cmd == "ปิดยกเลิก" or text.lower() == 'unsend off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = False
                                sendMention(msg.to, sender, "「 Status Unsend 」\nUser ", " \nDeteksi unsend dinonaktifkan")

                        elif cmd == "เปิดเชคโพส" or text.lower() == 'timeline on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = True
                                sendMention(msg.to, sender, "「 Status Timeline 」\nUser ", "\nSilahkan kirim postingannya,\nKetik timeline off jika sudah slesai")

                        elif cmd == "ปิดเชคโพส" or text.lower() == 'timeline off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = False
                                sendMention(msg.to, sender, "「 Status Timeline 」\nUser ", " \nDeteksi timeline dinonaktifkan")
                                
                        elif cmd == "เปิดเชิญ" or text.lower() == 'invite on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                sendMention(msg.to, sender, "「 Status Invite 」\nUser ", "\nSilahkan kirim kontaknya,\nKetik invite off jika sudah slesai")

                        elif cmd == "ปิดเชิญ" or text.lower() == 'invite off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                sendMention(msg.to, sender, "「 Status Invite 」\nUser ", " \nInvite via contact dinonaktifkan")
                                
                        elif cmd == "เปิดเตะแทค" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["mentionKick"] = True
                                cl.sendText(msg.to,"「 Status Notag 」\nNotag telah diaktifkan")

                        elif cmd == "ปิดเตะแทค" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["mentionKick"] = False
                                cl.sendText(msg.to,"「 Status Notag 」\nNotag telah dinonaktifkan")

                        elif cmd == "เปิดคท" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                sendMention(msg.to, sender, "「 Status Contact 」\nUser ", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik contact off")

                        elif cmd == "ปิดคท" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendText(msg.to,"「 Status Contact 」\nDeteksi contact dinonaktifkan")

                        elif cmd == "เปิดแทค" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendText(msg.to,"「 Status Respon 」\nAuto respon diaktifkan")

                        elif cmd == "ปิดแทค" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendText(msg.to,"「 Status Respon 」\nAuto respon dinonaktifkan")

                        elif cmd == "เปิดเข้ากลุ่ม" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendText(msg.to,"「 Status Autojoin 」\nAutojoin telah diaktifkan")

                        elif cmd == "ปิดเข้ากลุ่ม" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendText(msg.to,"「 Status Autojoin 」\nAutojoin telah dinonaktifkan")

                        elif cmd == "เปิดคนออก" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendText(msg.to,"「 Status Autoleave 」\nAutoleave telah diaktifkan")

                        elif cmd == "ปิดคนออก" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendText(msg.to,"「 Status Autoleave 」\nAutoleave telah dinonaktifkan")

                        elif cmd == "เปิดบล็อค" or text.lower() == 'autoblock on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                cl.sendText(msg.to,"「 Status Autoleave 」\nAutoleave telah diaktifkan")

                        elif cmd == "ปิดบล็อค" or text.lower() == 'autoblock off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = False
                                cl.sendText(msg.to,"「 Status Autoleave 」\nAutoleave telah dinonaktifkan")

                        elif cmd == "เปิดคนแอด" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendText(msg.to,"「 Status Autoadd 」\nAutoadd telah diaktifkan")

                        elif cmd == "ปิดคนแอด" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendText(msg.to,"「 Status Autoadd 」\nAutoadd telah dinonaktifkan")

                        elif cmd == "เปิดสติกเกอร์" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["stickerOn"] = True
                                sendMention(msg.to, sender, "「 Status Sticker Check 」\n", " [ ON ]\nSilahkan kirim stickernya,\nJika sudah selesai, ketik sticker off")

                        elif cmd == "ปิดสติกเกอร์" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["stickerOn"] = False
                                cl.sendText(msg.to,"「 Status Sticker Check 」\nSticker check dinonaktifkan")

                        elif cmd == "เปิดมุดลิ้ง" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                sendMention(msg.to, sender, "「 มุดลิ้ง 」\nผู้ใช้ ", "\nเปิดมุดลิ้งเรียบร้อย")

                        elif cmd == "ปิดมุดลิ้ง" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                cl.sendText(msg.to,"「 มุดลิ้ง 」\nปิดมุดลิ้งเรียบร้อย")
#===========COMMAND SET============#
                        elif 'ตั้งคนแอด ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งคนแอด ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "「 ตั้งข้อความคนแอด 」\n\n{}".format(str(spl)))

                        elif 'ตั้งคนเข้า ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งคนเข้า ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "「 ตั้งข้อความคนเข้า 」\n\n{}".format(str(spl)))

                        elif 'ตั้งคนออก ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งคนออก ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Leave Msg")
                              else:
                                  wait["leave"] = spl
                                  cl.sendMessage(msg.to, "「 ตั้งข้อความคนออก 」\n\n{}".format(str(spl)))

                        elif 'ตั้งคนแทค ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งคนแทค ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「 ตั้งข้อความคนแทค 」\n\n{}".format(str(spl)))

                        elif 'ตั้งแสปม ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งแสปม ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  cl.sendMessage(msg.to, "「 ตั้งข้อความแสปม 」\n\n{}".format(str(spl)))

                        elif 'ตั้งคนแอบ ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งคนแอบ ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "「 ตั้งข้อความคนแอบ 」\n\n{}".format(str(spl)))

                        elif text.lower() == "ข้อความคนแอด":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 ข้อความคนแอด 」\n\n" + str(wait["message"]))

                        elif text.lower() == "ข้อความคนเข้า":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 ข้อความคนเข้า 」\n\n" + str(wait["welcome"]))

                        elif text.lower() == "ข้อความคนออก":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 ข้อความคนออก 」\n\n" + str(wait["leave"]))

                        elif text.lower() == "ข้อความคนแทค":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 ข้อความคนแทค 」\n\n" + str(wait["Respontag"]))

                        elif text.lower() == "ข้อความแสปม":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 ข้อความแสปม 」\n\n" + str(Setmain["RAmessage1"]))

                        elif text.lower() == "ข้อความคนแอบ":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 ข้อความคนแอบ 」\n\n" + str(wait["mention"]))

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "✔ Join to group : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "✔ Join to group : %s" % str(group.name))

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
