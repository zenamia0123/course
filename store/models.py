from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    email = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    ROLE_CHOICES = (
        ('клиент', 'клиент'),
        ('преподаватель', 'преподаватель'),
        ('администратор', 'администратор'),
    )
    user_role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='клиент')
    profile_picture = models.ImageField(upload_to='profile')
    bio = models.TextField()


class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.category_name


class Course(models.Model):
    course_name = models.CharField(max_length=32)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    LEVEL_CHOICES = (
        ('начальный', 'начальный'),
        ('средний', 'средний'),
        ('продвинутый', 'продвинутый'),
    )
    level = models.CharField(max_length=32, choices=LEVEL_CHOICES, default='начальный')
    course_price = models.PositiveIntegerField()
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='курсы')
    updated_at = models.DateTimeField(auto_now_add=True)


class Lesson(models.Model):
    title = models.CharField(max_length=32, verbose_name='название урока')
    video_url = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    course_url = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='уроки')


class Assignment(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    due_date = models.DateTimeField(verbose_name='срок сдачи')
    course_assignment = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='задании')
    students = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='задания_студентов')


class Exam(models.Model):
    title = models.CharField(max_length=32)
    course_exam = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='экзамены')
    questions = models.TextField()
    passing_score = models.PositiveSmallIntegerField(verbose_name='проходной балл', default=0)
    duration = models.DateTimeField(verbose_name='продолжительность')


class Certificate(models.Model):
    student_certificate = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='certificates')
    course_certificate = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='curses_certificates')
    issued_at = models.DateTimeField(verbose_name='дата выдачи')
    certificate_url = models.URLField(max_length=200)


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews')
    course_review = models.URLField(max_length=200)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Рейтинг", null=True,
                                blank=True)
    comment = models.TextField()


class ExamQuestions(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='вопросы')
    question_text = models.TextField()
    QUESTION_OPTION_CHOICES = [
        ('a)', 'a)'),
        ('b)', 'b)'),
        ('c)', 'c)'),
        ('d)', 'd)'),
    ]
    question_option = models.CharField(max_length=32, choices=QUESTION_OPTION_CHOICES, default='a)')

    QUESTION_TYPE_CHOICES = [
        ('одиночный выбор', 'одиночный выбор'),
        ('множественный  выбор', 'множественный выбор'),
        ('текстовый ответ', 'текстовый ответ'),
    ]
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES, default='одиночный_выбор')
    correct_answer = models.CharField(max_length=32, verbose_name='Правильный ответ')
    user_answer = models.CharField(max_length=32, choices=QUESTION_OPTION_CHOICES, blank=True, null=True)

    def get_answer_result(self):
        if self.user_answer:
            if self.user_answer == self.correct_answer:
                return 'правильный ответ'
            return 'неправильный ответ'
