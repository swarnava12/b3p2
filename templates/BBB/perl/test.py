#!/usr/bin/python
import sys
sys.path.append('/home/pankaz-lab-pc3/anaconda/lib/python3.6/site-packages')
import cgi, cgitb
import pandas as pd
import pubchempy as pcp
print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers




print "<TITLE>CGI script output</TITLE>"
print "<H1>This is my first CGI script</H1>"
print "<h1 style=\"color:red\">Hello, world!</h1>"

data_pd = pd.read_csv('descriptors.csv')
#print(data_pd.head(3))
print"<br>"
#print(data_pd.iloc[0,:])
for x in range(1,5):
  print data_pd.iloc[x:]
  print "<br>"
#print(data_pd)
x = 10*9
#print(x)
