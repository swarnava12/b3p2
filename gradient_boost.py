#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 22:54:15 2018

@author: pankaz-lab-pc3
"""

import pandas as pd
import numpy as np
dataset = pd.read_csv('/home/pankaz-lab-pc3/Desktop/project paper/descriptors.csv')
dataset1 = dataset[['nHetero', 'ATS0dv', 'ATS3dv', 'ATS4dv', 'ATS0d', 'ATS3Z', 'ATS2m', 'ATS3m', 'ATS4m', 'ATS5m', 'ATS0v', 'ATS4v', 'ATS5se', 'ATS0pe', 'ATS2pe', 'ATS4pe', 'ATS6pe', 'ATS0are', 'ATS2are', 'ATS3are', 'ATS7are', 'ATS8are', 'ATS6i', 'ATS7i', 'ATSC0c', 'ATSC0dv', 'ATSC0d', 'ATSC0v', 'ATSC0pe', 'nBondsS', 'nBondsO', 'nBonds', 'Sare', 'TIC1', 'Kier1', 'LabuteASA', 'SlogP_VSA2', 'MPC2', 'MPC3', 'apol', 'SMR', 'ATS6se', 'p_np']]
columns=dataset1.columns
# The labels are in the last column ('Class'). Simply remove it to obtain features columns
