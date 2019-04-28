import sys
sys.path.append('/home/pankaz-lab-pc3/anaconda/lib/python3.6/site-packages')
import cgi, cgitb
import pandas as pd
import pubchempy as pcp
print("Hello1")
results = pcp.get_compounds('aspirin', 'name')
print(results)

print("Hello2")
