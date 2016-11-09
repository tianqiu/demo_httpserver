#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cgi

form = cgi.FieldStorage()
print "<html><body>"

print "<p>hello,your firstname is " +  (form['firstname'].value) + "</p>"
print "<p>hello,your lastname is " +  (form['lastname'].value) + "</p>"

print "</body></html>"
