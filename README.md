about uploading dependancies for a function to AWS lambda.
https://docs.aws.amazon.com/lambda/latest/dg/python-package.html


#direct upload to Lambda or first S3 -> lambda
#If the deployment package is larger than 50 MB, you must use Amazon S3.
#writing the function in AWS lambda console, then, total size < 3 MB
#better use visual studio code IDE with AWS toolkit extension, but 3 MB is enough actually.
#-----
#Premium path: Video uploads, GIF signature moves (pay per number),
#---- "collaberation (fashion, cause, initiative) and work (workshop + judging)" 
#
#The scope of FREE version is based on the philosophy that every dancer, both
#newbie and OGs websites are well taken care of at a base level.
#-----
#The premium version is aimed at experienced dancers who have things under their
#belt, they are mostly teachers and can also afford to spend some money for their
#portfolio.
#do not go for premature feature addition and optimization becoz it might make the 
#portfolio of a newbie look empty.
#------
#on device (mobile) GIF maker app to save a running server(EC2).


#user's problem, desire, constraints
#don't think of scaling before it is a business. Khan academy did it well.
#don't kill the time thinking of the features which u r not going to release right away
#focus to make the business model work first with limited settings and constraints.
#biography and work: I will think where to put the work section and how. time to #eat something first



#why dance ? 
#the most important thing dance made u realize?


#-----
#sharing data model
#-----

s_student = manytomany() must be provided
s_teacher = manytomany() optional
s_teacher_name = charfield()
s_when = DateField
s_where = CharField
s_appreciation = TextField()
s_photo = ImageField() or keep a photo of her/him
s_video1_talks = FileField()
s_video2_dance = FileField()

s_teacher_feedback
s_student_thanks

likes()
comments()

#------
myhood
#------
"""
A room for someone who teaches and want to engage with their students(_/) and followers (x).
"""
"""teacher create this one."""

class MyHood:
    teacher = one2oneField (User)  #each user has only one hood
    myhood = charfield (name)
    #is_admin = one2onefield (User)

"""student join a hood"""

class Student:
    student = foreignkey (User)
    which_hood = foreignkey (MyHood)

class Post:
   poster = ForeignKey(Student) 
   content = CharField()

class Comments:
    commenter = ForeignKey(Student)
    comment = CharField()

#https://stackoverflow.com/questions/45563194/django-rest-permissions-allow-both-isadmin-and-custom-permission
#DRF permissions
#https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#custom-permissions
#https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#handling-object-permissions
#https://stackoverflow.com/questions/30573135/permissions-on-my-model-for-django
#https://django-permission.readthedocs.io/en/latest/
#https://github.com/django-guardian/django-guardian

https://stackoverflow.com/questions/45862889/attribute-error-user-object-has-no-attribute-is-admin | django - Attribute error: 'User' object has no attribute 'is_admin' - Stack Overflow
https://stackoverflow.com/questions/35557156/how-to-get-or-permissions-instead-of-and-in-rest-framework/35593748 | python - How to get OR permissions instead of AND in REST framework - Stack Overflow
https://stackoverflow.com/questions/30573135/permissions-on-my-model-for-django | python - Permissions on my Model for Django - Stack Overflow
https://docs.djangoproject.com/en/1.8/topics/auth/default/#the-permission-required-decorator | Using the Django authentication system | Django documentation | Django
https://www.django-rest-framework.org/api-guide/permissions/ | Permissions - Django REST framework
https://www.django-rest-framework.org/api-guide/permissions/ | Permissions - Django REST framework
https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#custom-permissions | Customizing authentication in Django | Django documentation | Django
https://django-permission.readthedocs.io/en/latest/ | Welcome to django-permission’s documentation! — django-permission 0.8.8 documentation
https://github.com/django-guardian/django-guardian | GitHub - django-guardian/django-guardian: Per object permissions for Django

https://www.google.com/search?q=DjangoModelPermissions&oq=DjangoModelPermissions&aqs=chrome..69i57j69i60.6119769j0j0&sourceid=chrome&ie=UTF-8 | DjangoModelPermissions - Google Search
https://medium.com/@shannon.ions/your-solution-poisons-the-singleton-djangomodelpermissions-class-which-results-in-view-permissions-11b02f66eb74 | Your solution poisons the singleton djangomodelpermissions class which results in view permissions… | by Shannon I'Ons | Medium
https://stackoverflow.com/questions/46584653/django-rest-framework-use-djangomodelpermissions-on-listapiview#_=_ | python - Django Rest Framework use DjangoModelPermissions on ListAPIView - Stack Overflow
https://github.com/encode/django-rest-framework/blob/master/rest_framework/permissions.py#L91 | django-rest-framework/permissions.py at master · encode/django-rest-framework · GitHub
https://gist.github.com/emilsas/0364e1e756759be6017f19cc8fdb41e8 | DjangoModelPermissions Example
https://nezhar.com/blog/django-rest-framework-permissions-in-depth/ | Django REST Framework Permissions in Depth | nezhar.com
https://gist.github.com/emilsas/0364e1e756759be6017f19cc8fdb41e8 | DjangoModelPermissions Example · GitHub
https://stackoverflow.com/questions/30274591/all-fields-in-modelserializer-django-rest-framework | python - All fields in ModelSerializer django rest framework - Stack Overflow
https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/#selecting-the-fields-to-use | Creating forms from models | Django documentation | Django








