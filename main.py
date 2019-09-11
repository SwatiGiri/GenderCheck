#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Importing Dependencies

from flask import Flask, render_template, request, redirect, url_for
import GenDet

# Creating a new web application 


# __name__ means this current file
app= Flask(__name__)

# Represnting the default page


@app.route("/")
# on default page following funtion will be activated
def home():
    return render_template("home.html")


@app.route("/text", methods=["GET","POST"])
def text(comments=[]):
    if request.method =="GET":
        return render_template("home.html",comments=comments)
    comments.append(request.form["Run"])
    comments.append(request.form["Submission Sheet"])
    

# @app.route("/Gendet", methods=["GET","POST"])
# def dynamic_page():
    if request.method =="POST":
        Runfolder = None 
        Samplesubsht = None
        Run = str(request.form["Run"])
        # subsht = str(request.form["LIMS Sample Submission Sheet"])
        subsht = str(request.form["Submission Sheet"])
        result = GenDet.Gendet(Run,subsht)
    return redirect(url_for('text'))
    # return 'OK'
# When python script is run , python assigns the name "__main__" to the script when executed
if __name__=="__main__":
    app.run(host='0.0.0.0', port = 5000, debug=True)
    # app.run(port=5000 , debug = True)

# In[ ]:




