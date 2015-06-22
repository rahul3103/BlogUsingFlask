from app import db,models
'''
db.session.commit(), which writes the changes atomically. If at any time while working on a session 
there is an error, a call to db.session.rollback() will revert the database to its state before the 
session was started.
'''
'''
#To enter details manualy
u = models.User(nickname='rahul', email='rahul@email.com')
db.session.add(u)
db.session.commit()

v = models.User(nickname='rohit', email='rohit@email.com')
db.session.add(v)
db.session.commit()
'''
'''
# to view the users
users = models.User.query.all()

for u in users:
	print u.id,u.nickname

u = models.User.query.get(1)
print u
'''
'''
#to add the posts
import datetime
u = models.User.query.get(1)
p = models.Post(body='my first post!', timestamp=datetime.datetime.utcnow(), author=u)
db.session.add(p)
db.session.commit()
'''
'''
# get all posts from a user
u = models.User.query.get(1)
posts = u.posts.all()
#print posts

# obtain author of each post
for p in posts:
	print p.id,p.author.nickname,p.body
'''
'''
# a user that has no posts
u = models.User.query.get(2)
print u
print u.posts.all()
'''
'''
# get all users in reverse alphabetical order
print models.User.query.order_by('nickname desc').all()
'''
'''
#deleting all the users
users = models.User.query.all()
for u in users:
	db.session.delete(u)

posts = models.Post.query.all()
for p in posts:
	db.session.delete(p)

db.session.commit()
'''