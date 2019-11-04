from rest_framework import serializers, fields
from . import models

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Choice
        fields = ('choice_text', 'votes')

class QuestionSerializer(serializers.ModelSerializer):

    choices = ChoiceSerializer(source='choice_set', many=True)

    class Meta:
        model = models.Question
        fields = ('question_text', 'pub_date', 'choices')