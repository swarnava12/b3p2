#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:44:04 2018

@author: pankaz-lab-pc3
"""
from rdkit import Chem
from rdkit.Chem import PandasTools
import pandas as pd
import os
from rdkit import RDConfig
from mordred import Calculator, descriptors
import pandas as pd
from flask import Flask, render_template, request
from wtforms import Form, FloatField, validators
#from compute import compute

app = Flask(__name__)

# Model
class InputForm(Form):
    r = FloatField(validators=[validators.InputRequired()])

# View
@app.route('/')
def index1():
    return render_template("BBB/main/index.html")


@app.route('/hw1', methods=['GET', 'POST'])
def form1():
    form = InputForm(request.form)
    
if __name__ == '__main__':
    app.run(debug=True)