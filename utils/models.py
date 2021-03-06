from django.contrib.postgres.fields import JSONField    # NOAQ
from django.db import models

from .xss_filter import XSSHtml


class RichTextField(models.TextField):
    def get_prep_value(self, value):
        with XSSHtml() as parser:
            return parser.clean(value or "")
