from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from .validators import validate_file_size, validate_pdf_file_extension, validate_pdf_file_size


class Category(models.Model):
    title = models.CharField(max_length=40)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True, max_length=80)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class AbstractStatus:
    DRAFT = 'draft'
    REVIEW = 'review'
    PUBLISHED = 'published'

    CHOICES_STATUS = (  # nested tuples
        (DRAFT, 'Draft'),
        (REVIEW, 'Review'),
        (PUBLISHED, 'Published')
    )

    class Meta:
        abstract = True


class AbstractQuiz(models.Model):

    title = models.CharField(max_length=40, null=False)
    quiz_description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=30, choices=AbstractStatus.CHOICES_STATUS, default=AbstractStatus.DRAFT)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):  # method for representing string of an object
        return self.title


class SortingQuiz(AbstractQuiz):

    element1 = models.TextField(max_length=300, blank=False, null=False)
    element2 = models.TextField(max_length=300, blank=False, null=False)
    element3 = models.TextField(max_length=300, blank=False, null=False)
    element4 = models.TextField(max_length=300, blank=True, null=True)
    element5 = models.TextField(max_length=300, blank=True, null=True)
    element6 = models.TextField(max_length=300, blank=True, null=True)
    element7 = models.TextField(max_length=300, blank=True, null=True)
    element8 = models.TextField(max_length=300, blank=True, null=True)
    element9 = models.TextField(max_length=300, blank=True, null=True)
    element10 = models.TextField(max_length=300, blank=True, null=True)
    element11 = models.TextField(max_length=300, blank=True, null=True)
    element12 = models.TextField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Quiz: Sorting'


class FreeTextQuiz(AbstractQuiz):
    correctAnswer1 = models.TextField(max_length=150, blank=False, null=False)
    correctAnswer2 = models.TextField(max_length=150, blank=True, null=True)
    correctAnswer3 = models.TextField(max_length=150, blank=True, null=True)
    correctAnswer4 = models.TextField(max_length=150, blank=True, null=True)
    correctAnswer5 = models.TextField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Quiz: Free Text'


class CorrectAnswerQuiz(AbstractQuiz):
    correctAnswer = models.TextField(max_length=300, blank=False, null=False)
    wrongAnswer1 = models.TextField(max_length=300, blank=False, null=False)
    wrongAnswer2 = models.TextField(max_length=300, blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Quiz: Correct Answer'


class MultipleChoiceQuiz(AbstractQuiz):
    answer1 = models.TextField(max_length=150, blank=False, null=False)
    solution1 = models.BooleanField(blank=False, null=False)
    answer2 = models.TextField(max_length=150, blank=False, null=False)
    solution2 = models.BooleanField(blank=False, null=False)
    answer3 = models.TextField(max_length=150, blank=False, null=False)
    solution3 = models.BooleanField(blank=False, null=False)
    answer4 = models.TextField(max_length=150, blank=False, null=False)
    solution4 = models.BooleanField(blank=False, null=False)
    answer5 = models.TextField(max_length=150, blank=False, null=False)
    solution5 = models.BooleanField(blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Quiz: Multiple Choice'


class Course(models.Model):
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=40, null=False)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(blank=True, null=True, max_length=80)
    long_description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='courses', blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='uploads/course_images', blank=True, null=True, validators=[validate_file_size])
    created_at = models.DateField(auto_now_add=True)
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['order']

    def __str__(self):  # method for representing string of an object
        return self.title

    def get_image(self):
        if self.image:
            url = settings.WEBSITE_URL + self.image.url
            return url
        return settings.WEBSITE_URL + "/media/static_files/Placeholder.svg"


class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    text_area = models.TextField(blank=True, null=True)
    sorting_quiz = models.ForeignKey(SortingQuiz, blank=True, null=True, on_delete=models.SET_NULL)
    correct_answer_quiz = models.ForeignKey(CorrectAnswerQuiz, blank=True, null=True, on_delete=models.SET_NULL)
    multiple_choice_quiz = models.ForeignKey(MultipleChoiceQuiz, blank=True, null=True, on_delete=models.SET_NULL)
    free_text_quiz = models.ForeignKey(FreeTextQuiz, blank=True, null=True, on_delete=models.SET_NULL)
    youtube_video_id = models.CharField(blank=True, null=True, max_length=20)
    image1 = models.ImageField(upload_to='uploads/lesson_images', blank=True, null=True,
                               validators=[validate_file_size])
    image2 = models.ImageField(upload_to='uploads/lesson_images', blank=True, null=True,
                               validators=[validate_file_size])
    image3 = models.ImageField(upload_to='uploads/lesson_images', blank=True, null=True,
                               validators=[validate_file_size])
    pdf = models.FileField(upload_to='uploads/lesson_pdf', blank=True, null=True,
                           validators=[validate_pdf_file_size, validate_pdf_file_extension])
    status = models.CharField(max_length=30, choices=AbstractStatus.CHOICES_STATUS, default=AbstractStatus.DRAFT)
    created_at = models.DateField(auto_now_add=True)
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['order']

    def __str__(self):  # method for representing string of an object
        return str(self.course) + str(self.title)

    def get_image1(self):
        if self.image1:
            url = settings.WEBSITE_URL + self.image1.url
            return url

    def get_image2(self):
        if self.image2:
            url = settings.WEBSITE_URL + self.image2.url
            return url

    def get_image3(self):
        if self.image3:
            url = settings.WEBSITE_URL + self.image3.url
            return url

    def get_pdf(self):
        if self.pdf:
            url = settings.WEBSITE_URL + self.pdf.url
            return url


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()


post_save.connect(create_user_profile, sender=User)





