from django.core.exceptions import ValidationError

def validate_no_hash(value):
    if "#" in value:
        raise ValidationError('"#"은 사용할 수 없어요')

def validate_no_numbers(value):
    for char in value:
        if char.isdigit():
            raise ValidationError('숫자는 사용할 수 없어요')

def validate_score(value):
    if value < 0 or value > 10:
        raise ValidationError("0에서 10사이의 숫자를 입력해주세요")
