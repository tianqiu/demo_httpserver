#!/usr/bin/python

import cgi
form = cgi.FieldStorage()

print "<html><body>"

print "<p>" +  form['firstname'].value + "</p>"
print "<p>" +  form['lastname'].value + "</p>"

print "</body></html>"
