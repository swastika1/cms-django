from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Organization(models.Model):
    title = models.CharField(max_length=200)
    slogan = models.CharField(max_length=500)
    logo = models.ImageField(upload_to="organization")
    image = models.ImageField(upload_to="organization", null=True, blank=True)
    address = models.CharField(max_length=500)
    location = models.CharField(max_length=20)
    mission = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    mobile1 = models.CharField(max_length=20, null=True, blank=True)
    mobile2 = models.CharField(max_length=20, null=True, blank=True)
    email1 = models.EmailField()
    email2 = models.EmailField(null=True, blank=True)
    about = models.TextField()
    established = models.DateField()

    def __str__(self):
        return self.title


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(
        auto_now=False, auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        abstract = True


class Receptionist(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    about = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='receptionist/', blank=True, null=True)


class Country(TimeStamp):
    name = models.CharField(max_length=130)
    city = models.CharField(max_length=130)
    about = models.TextField()
    image = models.ImageField(upload_to="countries/",
                              blank=True, null=True)

    def __str__(self):
        return self.name


RELATION = (("Partnered", "Partnered"),
            ("Non partnered", "Non partnered"))

TERM = (("fall", "fall"),
        ("spring", "spring"),
        ("summer", "summer"))


class University(TimeStamp):
    name = models.CharField(max_length=120, blank=True, null=True)
    about = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, blank=True, null=True)
    deadline = models.CharField(max_length=100, null=True, blank=True)
    relation = models.CharField(
        choices=RELATION, default='Partnered', max_length=100, null=True, blank=True)
    requirements = models.TextField(blank=True, null=True)
    contact_person = models.TextField(blank=True, null=True)
    term = models.CharField(choices=TERM, default='fall', null=True,
                            blank=True, max_length=120)
    phone = models.CharField(max_length=10)
    email = models.EmailField(blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    scholarship = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='university/', null=True, blank=True)

    def __str__(self):
        return self.name


class Course(TimeStamp):
    university = models.ManyToManyField(
        University, related_name="university")
    title = models.CharField(max_length=120)
    fee_structure = models.CharField(max_length=120)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


TASK_STATUS = (("Completed", "Completed"),
                (("Verified","Verified")),
                (("Processing","Processing")),
               ("Pending", "Pending"))
TASK_PRIORITY = (("Urgent", "Urgent"),
                 ("Low", "Low"),
                 ("Medium", "Medium"))


class Task(TimeStamp):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    status = models.CharField(
        choices=TASK_STATUS, default="Pending", max_length=100)
    priority = models.CharField(
        choices=TASK_PRIORITY, default="Medium", max_length=100)
    due_date = models.DateField(null=True, blank=True)
    assigned_to = models.ManyToManyField(User, related_name="assigned_to")
    assigned_by = models.ForeignKey(
        User, related_name="assigned_by", on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return (self.title)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField()
    qualification = models.CharField(max_length=400, null=True, blank=True)
    experience = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='teacher/',
                              blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


SEATS = (("Available", "Available"),
         ("Full", "Full"))


class LanguageCourse(TimeStamp):
    title = models.CharField(max_length=150, null=True)
    fee = models.PositiveIntegerField(null=True, blank=True)
    schedule = models.TextField(blank=True, null=True)
    seats = models.CharField(choices=SEATS, max_length=150, null=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, related_name='teachers', max_length=150, null=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    books = models.CharField(max_length=130, null=True)

    def __str__(self):
        return self.title


class StudyMaterials(TimeStamp):
    language_course = models.ForeignKey(
        LanguageCourse, on_delete=models.SET_NULL, related_name='language_course', max_length=150, null=True, blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    study_file = models.FileField(
        upload_to='study_file/', blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.language_course, self.study_file)


SOURCE = (("Social Media", "Social Media"),
          ("Television", "Television"),
          ("Radio", "Radio"),
          ("Newspaper", "Newspaper"),
          ("Magazines", "Magazines"),
          ("Friends", "Friends"),
          ("Magazines", "Magazines"),
          ("Pamphlets", "Pamphlets"),
          ("Referral", "Referral"),
          )


class Visitor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    source = models.CharField(choices=SOURCE, max_length=100)
    visited_date = models.DateField(auto_now=True)
    purpose = models.TextField()
    about = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='visitor/',
                              blank=True, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(null=True)
    language_course = models.ForeignKey(
        LanguageCourse, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_to = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='student/',
                              blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


VISA_STATUS = (("Processing", "Processing"),
               ("Lodged", "Lodged"),
               ("Accepted", "Accepted"),
               ("Rejected", "Rejected"))


class Lead(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    course = models.ForeignKey(
        Course, on_delete=models.SET_NULL, null=True, blank=True)
    university = models.ForeignKey(
        University, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    visa_status = models.CharField(
        choices=VISA_STATUS, max_length=50, default="Processing", blank=True, null=True)
    image = models.ImageField(
        upload_to='lead/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Document(TimeStamp):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents')
    lead = models.ForeignKey(
        Lead, on_delete=models.SET_NULL, blank=True, null=True, related_name='lead')

    def __str__(self):
        return str(self.title)


class Consultant(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    image = models.ImageField(upload_to='consultant/',
                              blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    image = models.ImageField(
        upload_to='admin/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


QUALIFICATION = (("Under-Graduate", "Under-Graduate"),
                 ("Graduate", "Graduate"),
                 ("Post-Graduate", "Post-Graduate"))
YEAR = (("2019", "2019"),
        ("2018", "2018"),
        ("2017", "2017"),
        ("2016", "2016"),
        ("2015", "2015"),
        ("2014", "2014"),
        ("2013", "2013"),
        ("2012", "2012"),
        ("2011", "2011"),
        ("2010", "2010"),
        ("2009", "2009"))


class Qualification(TimeStamp):
    level = models.CharField(choices=QUALIFICATION,
                             max_length=100, null=True, blank=True)
    completed_year = models.CharField(
        choices=YEAR, max_length=100, null=True, blank=True)
    student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.level


PAYMENT_METHOD = (("Cash", "Cash"),
                  ("Cheque", "Cheque"))


class Payment(TimeStamp):
    method = models.CharField(
        choices=PAYMENT_METHOD, max_length=20, null=True, blank=True)
    amount = models.PositiveIntegerField(null=True, blank=True)
    particulars = models.CharField(max_length=120, blank=True, null=True)
    date = models.DateTimeField(null=True, blank=True)
    student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, blank=True, null=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.amount, "(" + self.method + ")")


class Feed(TimeStamp):
    post = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.post


class Comment(TimeStamp):
    post = models.ForeignKey(
        Feed, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()

    def __str__(self):
        return self.comment


# class FollowUp(TimeStamp):
#     visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT)
#     summary = models.TextField()
#     by = models.ForeignKey(Staff, on_delete=models.PROTECT)
#     response_through = models.CharField(
#         max_length=200, choices=ENQUIRY_THROUGH)

#     def __str__(self):
#         return self.summary

APPOINTMENT_STATUS = (("Pending", "Pending"),
                      ("Approved", "Approved"),
                      ("Rejected", "Rejected"))


class Appointment(TimeStamp):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    note = models.CharField(max_length=200)
    status = models.CharField(choices=APPOINTMENT_STATUS,
                              max_length=100, null=True, blank=True)
    appointment_date = models.DateTimeField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.subject


class Activity(TimeStamp):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    note = models.TextField()


class Message(TimeStamp):
    sender = models.ForeignKey(
        User, related_name="sender", on_delete=models.PROTECT)
    receiver = models.ForeignKey(
        User, related_name="receiver", on_delete=models.PROTECT)
    msg_content = models.CharField(max_length=250)
    # created_at = # time field
