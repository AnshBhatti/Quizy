from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from . import quiz
from random import shuffle, choice
from time import time
import datetime
from . import models
# Create your views here.
Test = models.Test


def home(request):
    if request.method == "POST":
        print("UH")
    return render(request, "main/home.html")


def study(request):
    qs = models.Questions.objects.all()
    new = []
    for obj in qs:
        new.append([obj.question, obj.answer])
    return render(request, "main/study.html", {
        "qas": new,
    })


def test(request):
    if request.method == "POST":
        if "name" not in request.POST:
            ans = request.POST
            print(ans)
            res = list(Test.objects.filter(
                name=ans["Name"], timestamp=ans["timestamp"]))
            cor = 0
            mc, mt, fb, tf = [], [], [], []
            for obj in res:
                if obj.qtype == "MC":
                    mc.append([obj.question[3:], ans[obj.question], obj.mc_a])
                    if obj.mc_a.lower() == ans[obj.question].lower():
                        cor += 1
                        mc[-1].append(True)
                    else:
                        mc[-1].append(False)
                elif obj.qtype == "MT":
                    mt.append([obj.question[3:], ans[obj.question], obj.mt_a])
                    if obj.mt_a.lower() == ans[obj.question].lower():
                        cor += 1
                        mt[-1].append(True)
                    else:
                        mt[-1].append(False)
                elif obj.qtype == "FB":
                    fb.append([obj.question[3:], ans[obj.question], obj.fb_a])
                    if obj.fb_a.lower() == ans[obj.question].lower():
                        cor += 1
                        fb[-1].append(True)
                    else:
                        fb[-1].append(False)
                elif obj.qtype == "TF":
                    tf.append([obj.question[3:], ans[obj.question], obj.tf_a])
                    if obj.tf_a.lower()[0] == ans[obj.question].lower():
                        cor += 1
                        tf[-1].append(True)
                    else:
                        tf[-1].append(False)
            print("Grade: "+str(cor/5))
            new = models.Grades(
                timestamp=datetime.datetime.fromtimestamp(float(ans["timestamp"])).strftime('%m/%d/%y %H:%M:%S'), name=ans["Name"], grade=int(100*cor/5))
            new.save()
            return render(request, "main/grade.html", {
                "mc": mc,
                "mt": mt,
                "fb": fb,
                "tf": tf,
                "grade": 100*cor/5,
                "name": ans["Name"],
                "time": datetime.datetime.fromtimestamp(float(ans["timestamp"])).strftime('%m/%d/%y %H:%M:%S')
            })
        questions, answer_key, alloc = quiz.make_quiz(
            MT="MT" in request.POST, MC="MC" in request.POST, TF="TF" in request.POST, FB="FB" in request.POST)
        questions = list(questions.items())
        mt_q, mt_a, mc_q, mc_a, fb_q, fb_a, tf_q, tf_a = [], [], [], {}, [], [], [], []
        i = 0
        n = []
        t = int(time())
        for c in range(alloc[0]):
            mt_q.append(str(i+1)+': '+questions[i][0])
            mt_a.append(answer_key[questions[i][0]])
            i += 1
        for c in range(alloc[1]):
            mc_q.append(str(i+1)+': '+questions[i][0])
            n.append(i)
            mc_a[mc_q[-1]] = questions[i][1]
            new = Test(timestamp=time(
            ), question=mc_q[-1], qtype="MC", name=request.POST["name"], mc_a=answer_key[mc_q[-1][3:]])
            new.save()
            i += 1
        for c in range(alloc[2]):
            fb_q.append(str(i+1)+': '+questions[i][0])
            new = Test(timestamp=time(
            ), question=fb_q[-1], qtype="FB", name=request.POST["name"], fb_a=answer_key[fb_q[-1][3:]])
            new.save()
            i += 1
        for c in range(alloc[3]):
            an = choice(questions[i][1])
            tf_q.append(str(i+1)+': ' +
                        questions[i][0]+' '+an)
            tf_a.append(an)
            new = Test(timestamp=time(), question=tf_q[-1], qtype="TF", name=request.POST["name"], tf_a=str(
                tf_a[-1] == answer_key[questions[i][0]]))
            new.save()
            i += 1
        shuffle(mt_a)
        mta_key = ''
        for q in mt_q:
            for i in range(len(mt_a)):
                if mt_a[i] == answer_key[q[3:]]:
                    mta_key += chr(97+i)
        print(mta_key)
        for c in range(len(mt_a)):
            mt_a[c] = chr(c+97)+'. '+mt_a[c]
        for c in range(alloc[0]):
            new = Test(timestamp=time(
            ), question=mt_q[c], qtype="MT", name=request.POST["name"], mt_a=mta_key[c])
            new.save()
        return render(request, "main/actual_test.html", {
            "name": request.POST["name"],
            "mt": "MT" in request.POST,
            "mc": "MC" in request.POST,
            "tf": "TF" in request.POST,
            "fb": "FB" in request.POST,
            "alloc": alloc,
            "mc_q": mc_q,
            "mca": mc_a,
            "mt_q": mt_q,
            "mt_a": mt_a,
            "fb_q": fb_q,
            "fb_a": fb_a,
            "tf_q": tf_q,
            "length": n,
            "questions": questions,
            "timestamp": t,
        })
    return render(request, "main/test.html")


def grade(request):
    if request.method == "POST":
        print("actual test gets the request")
    return render(request, "main/grade.html",)


def history(request):
    name = ''
    if request.method == "POST":
        name = request.POST["name"]
        objs = list(models.Grades.objects.filter(name=name))
        objs.reverse()
        print(objs)
        return render(request, "main/history.html", {
            "objs": objs,
            "name": name,
        })
    return render(request, "main/history.html", {
        "name": '',
    })
