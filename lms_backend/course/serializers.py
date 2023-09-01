from rest_framework import serializers

from .models import Category, Course, Lesson, SortingQuiz, UserProfile, CorrectAnswerQuiz, FreeTextQuiz, \
    MultipleChoiceQuiz


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'short_description', 'created_at')


class CourseListSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'short_description', 'get_image', 'categories', 'created_by', 'created_at')


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'short_description', 'long_description', 'get_image', 'created_by',
                  'created_at', )


class SortingQuizSerializer(serializers.ModelSerializer):
    elements = serializers.SerializerMethodField()

    class Meta:
        model = SortingQuiz
        fields = ('title', 'quiz_description', 'elements')

    def get_elements(self, obj):
        elements = []
        for i in range(1, 13):
            element = getattr(obj, f'element{i}', None)
            if element is not None and element != "":
                elements.append(element)
        return elements


class MultipleChoiceQuizSerializer(serializers.ModelSerializer):
    pairs = serializers.SerializerMethodField()

    class Meta:
        model = MultipleChoiceQuiz
        fields = ('title', 'quiz_description', 'pairs')

    def get_pairs(self, obj):
        pairs = []
        for i in range(1, 6):
            answer = getattr(obj, f'answer{i}', None)
            solution = getattr(obj, f'solution{i}', None)
            if answer is not None and answer != "" and solution is not None and solution != "":
                pairs.append({"answer": answer, "solution": solution})
        return pairs


class CorrectAnswerQuizSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = CorrectAnswerQuiz
        fields = ('title', 'quiz_description', 'answers')

    def get_answers(self, obj):
        return [
            {'answer_key': 'correctAnswer', 'answer_value': obj.correctAnswer},
            {'answer_key': 'wrongAnswer1', 'answer_value': obj.wrongAnswer1},
            {'answer_key': 'wrongAnswer2', 'answer_value': obj.wrongAnswer2}
        ]


class FreeTextQuizSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = FreeTextQuiz
        fields = ('title', 'quiz_description', 'answers')

    def get_answers(self, obj):
        answers = []
        for i in range(1, 6):
            answer = getattr(obj, f'correctAnswer{i}', None)
            if answer is not None and answer != "":
                answers.append(answer.lower().strip())
        return answers


class LessonListSerializer(serializers.ModelSerializer):
    sorting_quiz = SortingQuizSerializer(many=False)
    correct_answer_quiz = CorrectAnswerQuizSerializer(many=False)
    free_text_quiz = FreeTextQuizSerializer(many=False)
    multiple_choice_quiz = MultipleChoiceQuizSerializer(many=False)

    class Meta:
        model = Lesson
        fields = ('id', 'order', 'title', 'text_area', 'youtube_video_id', 'sorting_quiz', 'correct_answer_quiz',
                  'free_text_quiz', 'multiple_choice_quiz', 'get_pdf', 'get_image1', 'get_image2', 'get_image3',
                  'status')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'points')


class RankingSerializer(serializers.Serializer):
    username = serializers.CharField()
    points = serializers.IntegerField()
    rank = serializers.IntegerField()

    class Meta:
        fields = ('username', 'points', 'rank')



