from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHER', 'OTHER'),
    )


class User(AbstractUser):
    pass


class Teacher(User):
    address = models.CharField(max_length=54)
    gender = models.CharField(max_length=10, choices=GENDER)
    age = models.PositiveIntegerField()
    bio = models.TextField()
    data_birth = models.DateField()
    education = models.CharField(max_length=100)
    work_experience = models.PositiveSmallIntegerField()
    phone_number = PhoneNumberField(null=True, blank=True)
    role = models.CharField(max_length=15, choices=[('teacher', 'teacher')], default='teacher')
    profile_picture = models.ImageField(upload_to='teacher_profile_picture', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Student(User):
    gender = models.CharField(max_length=10, choices=GENDER)
    age = models.PositiveIntegerField()
    phone_number = PhoneNumberField(null=True, blank=True)
    data_birth = models.DateField()
    role = models.CharField(max_length=15, choices=[('student', 'student')], default='student')
    profile_picture = models.ImageField(upload_to='student_profile_picture', null=True, blank=True)
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
    STATUS_CHOICES = (
        ('безплатный', 'безплатный'),
        ('платный', 'безплатный'),

    )
    level = models.CharField(max_length=32, choices=LEVEL_CHOICES, default='начальный')
    course_price = models.PositiveSmallIntegerField()
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='created_by')
    updated_at = models.DateField(auto_now_add=True)
    discount = models.PositiveSmallIntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.course_name

    def get_discount_price(self):
        if self.discount is None:
            return 0
        discount = (self.discount * self.course_price) / 100
        return self.course_price - discount

    def get_avg_rating(self):
        ratings = self.course_review.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0

    def get_count_rating(self):
        ratings = self.course_review.all()
        if ratings.exists():
            return ratings.count()
        return 0


class CourseVideo(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_video')
    course_video = models.FileField(upload_to='course_video/', verbose_name="Видео", null=True, blank=True)
    course_data = models.DateTimeField(auto_now_add=True)


class Lesson(models.Model):
    title = models.CharField(max_length=32, verbose_name='название урока')
    content = models.TextField()
    course_url = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_lesson')
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher')

    def __str__(self):
        return self.title


class LessonVideo(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson_video')
    lesson_video = models.FileField(upload_to='lesson_video/', verbose_name="Видео", null=True, blank=True)
    lesson_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lesson}-videos"


class LessonFile(models.Model):
    file = models.FileField(upload_to='lesson_files/', null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='file')

    def __str__(self):
        return f"{self.lesson}-files"


class Assignment(models.Model):
    title = models.CharField(max_length=32, verbose_name='задание')
    description = models.TextField()
    due_date = models.DateField(verbose_name='срок сдачи')
    course_assignment = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignment_course')
    students = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='assignment_students')

    def __str__(self):
        return self.title


class Exam(models.Model):
    title = models.CharField(max_length=32)
    course_exam = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exam_course')
    questions_exam = models.TextField()
    passing_score = models.PositiveSmallIntegerField(verbose_name='проходной балл', default=0)
    duration = models.DurationField(verbose_name='Время на выполнение')
    exam_data = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    STATUS_LEVEL_CHOICES = (
        ('сложный', 'сложный'),
        ('средний', 'средний'),
        ('легкий', 'легкий'),
    )
    status_level = models.CharField(max_length=32, choices=STATUS_LEVEL_CHOICES, default='средний')


class Certificate(models.Model):
    student_certificate = models.OneToOneField(Student, related_name='student_certificate', on_delete=models.CASCADE)
    course_certificate = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(verbose_name='дата выдачи', auto_now_add=True)
    certificate_url = models.URLField(max_length=200, verbose_name='сертификат', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.student_certificate} - {self.course_certificate}'


class Review(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='user_review')
    course_review = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_review')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Рейтинг", null=True,
                                blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user}-{self.stars}'


class Question(models.Model):
    text = models.CharField(max_length=255)  # Текст вопроса
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.text


class Choice(models.Model):  # Ответ
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)  # Связь с вопросом
    text = models.CharField(max_length=255)  # Текст варианта ответа
    is_correct = models.BooleanField(default=False)  # Флаг правильного ответа

    def __str__(self):
        return self.text


class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)  # Выбранный пользователем ответ
    user = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)  # Результат проверки (правильно/неправильно)

    def __str__(self):
        return f"{self.user} - {self.question.text}: {self.choice.text} ({'Correct' if self.is_correct else 'Wrong'})"


class Favorite(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='favorite_student')
    favorite_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f'{self.user}'

    def get_total_price(self):
        total_price = sum(item.get_total_price() for item in self.items.all())
        return total_price


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_cart')
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.course} - {self.quantity}'

    def get_total_price(self):
        return self.course.price * self.quantity