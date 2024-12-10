from django.urls import path
from .views import *


urlpatterns = [
    path('', CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),

    path('user_teacher/', TeacherViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_teacher_list'),
    path('user_teacher/<int:pk>/', TeacherViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                       'delete': 'destroy'}), name='user_teacher_detail'),

    path('user_student/', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_student_list'),
    path('user_student/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                       'delete': 'destroy'}), name='user_student_detail'),

    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                        'delete': 'destroy'}), name='category_detail'),

    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson_detail'),

    path('assignment/', AssignmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='assignment_list'),
    path('assignment/<int:pk>/', AssignmentViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                            'delete': 'destroy'}), name='assignment_detail'),

    path('exam/', ExamListAPIView.as_view(), name='exams_list'),
    path('exam/<int:pk>/', ExamDetailAPIView.as_view(), name='exams_detail'),

    path('certificate/',CertificateViewSet.as_view({'get': 'list', 'post': 'create'}), name='certificate_list'),
    path('certificate/<int:pk>/', CertificateViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                            'delete': 'destroy'}), name='certificate_detail'),

    path('review/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='review_detail'),

    path('exam_questions/', QuestionViewSet.as_view({'get': 'list', 'post': 'create'}), name='exam_questions_list'),
    path('exam_questions/<int:pk>/', QuestionViewSet.as_view({'put': 'update',
                                                                   'delete': 'destroy'}), name='exam_questions_detail'),

    path('favorite/', FavoriteViewSet.as_view(), name='favorite'),

    path('cart-list/', CartListAPIView.as_view(), name='cart-list'),

    path('cart_item/create/', CartItemListCreateAPIView.as_view(), name='cart_item_create'),

    path('cart_item/<int:pk>/', CartItemUpdateDeleteApiView.as_view(), name='cart_item_delete'),

]