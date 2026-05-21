from django.core.validators import RegexValidator


LETTER_SPACE_DASH_VALIDATOR = RegexValidator(r'^[a-zA-ZA-y\s-]*$', 'Seules les lettres, espaces '
                                                                   'et tirets sont autrorisés.')
