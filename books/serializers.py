from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import Books


class Book(ModelSerializer):

    class Meta:
        model = Books
        fields = '__all__'

    def validate(self, data):
        # Validate - Method to validate of all fields of a serializer

        title = data.get('title', None)
        author = data.get('author',None)
        if not title.isalpha():
            raise ValidationError(
                {'status': False, 'msg': 'you must enter string only'}
            )

        if Books.objects.filter(title=title,author=author).exists():
            raise ValidationError({"status":False,"msg":"1xil kitob va author bo'lishi mumkin yoq"})


        return data

    def validate_isbn(self, isbn):
        # Validate_field_name - Method to validate of one field of a serializer
        print('printing from serializers.py', len(isbn))
        if len(isbn) <= 15:
            raise ValidationError({"status":False,"msg":"Error"})

        return isbn