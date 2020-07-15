import mongoengine as me
import datetime

me.connect('lesson_9_db')


class Post(me.Document):
    title = me.StringField(required=True)
    body = me.StringField(required=True)
    created = me.DateTimeField(default=datetime.datetime.now)


class User(me.Document):
    first_name = me.StringField(min_length=1, max_length=256, required=True)
    surname = me.StringField(min_length=1, max_length=256)
    interests = me.ListField(me.StringField(min_length=2, max_length=512))
    age = me.IntField()
    post = me.ReferenceField(Post)

    def __str__(self):
        return self.first_name


if __name__ == '__main__':

    ### DATA CREATION ###
    # user = User(first_name='John', surname='Lehnon', interests=['Programming', 'Football'], age=20)
    # user.save()
    # user = User(first_name='Bred', surname='Pitt', interests=['Cinema', 'Theatre', 'Basketball'], age=30)
    # user.save()
    #User.objects.create(first_name='John', surname='Lehnon', interests=['Programming', 'Football'], age=20)
    ###     END       ###

    users = User.objects.filter(age__gt=15)

    #QuerySet

    for user in users:
        print(user.age)

    # print(user.id, user.age, user.surname, user.first_name, user.interests)

    ##CREATING USER WITH POST"""

    post = Post.objects.create(title='news', body='post body')
    user = User.objects.create(
        first_name='Mike',
        surname='Tyson',
        interests=['Basksetball', 'Fighting'],
        age=40,
        post=post
        )

    print(user.age, user.first_name, user.post.title, user.post.body, user.post.created)