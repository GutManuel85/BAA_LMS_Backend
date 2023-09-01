from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.admin import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Category, UserProfile
from .serializers import Course, CategoryListSerializer, UserProfileSerializer, RankingSerializer
from .serializers import CourseListSerializer, CourseDetailSerializer, LessonListSerializer


@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_course(request, slug):

    course = Course.objects.get(slug=slug)
    course_serializer = CourseDetailSerializer(course)
    lesson_serializer = LessonListSerializer(course.lessons.all(), many=True)

    data = {
        'course': course_serializer.data,
        'lessons': lesson_serializer.data
    }

    return Response(data)


@api_view(['GET'])
def get_categories(request):
    print("********** request.user ****************")
    print(request.user)
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_ranking_data(request):
    user_profiles = UserProfile.objects.all()
    users = User.objects.all()
    ranking = []
    for profile in user_profiles:
        user = users.get(id=profile.user_id)
        ranking.append({
            'username': user.username,
            'points': profile.points
        })
    ranking = sorted(ranking, key=lambda x: x['points'], reverse=True)
    top_ten_ranking = ranking[:10]
    for i, entry in enumerate(top_ten_ranking):
        entry['rank'] = i + 1
    ranking_serializer = RankingSerializer(top_ten_ranking, many=True)
    print(top_ten_ranking)
    return Response(ranking_serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    actual_user_profile = UserProfile.objects.get(user_id=request.user.id)
    user_profile_serializer = UserProfileSerializer(actual_user_profile)
    return Response(user_profile_serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_courses(request):
    courses = Course.objects.all()
    my_courses = []
    for c in courses:
        if c.created_by == request.user:
            my_courses.append(c)
    serializer = CourseListSerializer(my_courses, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def add_points(request, points_to_add):
    actual_user_profile = UserProfile.objects.get(user_id=request.user.id)
    actual_user_profile.points += points_to_add
    actual_user_profile.save()
    return Response()


