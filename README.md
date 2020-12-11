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







