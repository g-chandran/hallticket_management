from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image
from django.utils import timezone

class StudentProfile(models.Model):
    rollno = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    civil, cse, ece, eee, ei, ibt, it, mech, prod = 'CVL', 'CS', 'EC', 'EE', 'EI', 'IB', 'IT', 'MC', 'PD'
    dept_choice = [(civil, 'CIVIL'),
                    (cse, 'CSE'),
                    (ece, 'ECE'),
                    (eee, 'EEE'),
                    (ei, 'EI'),
                    (ibt, 'IBT'),
                    (it, 'IT'),
                    (mech, 'MECHANICAL'),
                    (prod, 'PRODUCTION')]
    department = models.CharField(
        max_length=10,
        choices=dept_choice,
        default=civil
        )
    dob = models.DateField()
    address = models.TextField()
    mobile = PhoneNumberField()
    email = models.EmailField(null=True)
    one, two, three, four = 'frst', 'sec', 'thrd', 'frth'
    year_choice = [(one, 'FIRST'),
                    (two, 'SECOND'),
                    (three, 'THIRD'),
                    (four, 'FOURTH')]
    year = models.CharField(
        max_length=6,
        choices=year_choice,
        default=one
        )
    image = models.ImageField(default="default.png", upload_to="profile_pics")
    date_added = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.rollno  


    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)

            img.save(self.image.path)


class ExaminerProfile(models.Model):
    staffid = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    mobile = PhoneNumberField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField(default="default.png", upload_to='profile_pics')
    date_added = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name
    

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)

            img.save(self.image.path)



class StudentExam(models.Model):
    rollno = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='student_rollno')
    # name = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='student_name')
    subject = models.CharField(max_length=150)
    date = models.DateField()
    attendance = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.subject
    

    
