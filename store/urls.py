from django.urls import path
from .views import *


urlpatterns = [
    path('', CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='course_list'),
    path('course/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='course_detail'),

    path('user/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('user/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                       'delete': 'destroy'}), name='user_detail'),

    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                        'delete': 'destroy'}), name='category_detail'),

    path('lesson/', LessonViewSet.as_view({'get': 'list', 'post': 'create'}), name='lesson_list'),
    path('lesson/<int:pk>/', LessonViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='lesson_detail'),

    path('assignment/', AssignmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='assignment_list'),
    path('assignment/<int:pk>/', AssignmentViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                            'delete': 'destroy'}), name='assignment_detail'),

    path('exam/', ExamViewSet.as_view({'get': 'list', 'post': 'create'}), name='exams_list'),
    path('exam/<int:pk>/', ExamViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                'delete': 'destroy'}), name='exams_detail'),

    path('certificate/',CertificateViewSet.as_view({'get': 'list', 'post': 'create'}), name='certificate_list'),
    path('certificate/<int:pk>/', CertificateViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                             'delete': 'destroy'}), name='certificate_detail'),

    path('review/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='review_detail'),

    path('exam_questions/', ExamQuestionsViewSet.as_view({'get': 'list', 'post': 'create'}), name='exam_questions_list'),
    path('exam_questions/<int:pk>/', ExamQuestionsViewSet.as_view({'put': 'update',
                                                                   'delete': 'destroy'}), name='exam_questions_detail'),

]