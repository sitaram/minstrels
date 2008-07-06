from google.appengine.api import users

print "Content-Type: text/html"
print ""
print "Foo"
print users.get_current_user()
