from datetime import datetime

from marshmallow import ValidationError


def validate_date(value):
    try:
        date_of_birth = datetime.strptime(value, "%Y-%m-%d")  # Define the desired format here
        if date_of_birth > datetime.now():
            raise ValidationError("Date of birth can't be in the future.")
        if date_of_birth.year <= 1924:
            raise ValidationError("Date of birth can't be before 1924, hello from underground.")
    except ValueError:
        raise ValidationError("Invalid date format. Use YYYY-MM-DD.")


def validate_expiry_date(value):
    try:
        expiry_of_birth = datetime.strptime(value, "%Y-%m-%d")  # Define the desired format here
        if expiry_of_birth < datetime.now():
            raise ValidationError("Expiry date can't be in the past.")
    except ValueError:
        raise ValidationError("Invalid date format. Use YYYY-MM-DD.")
