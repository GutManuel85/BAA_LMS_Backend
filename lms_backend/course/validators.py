from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import os


def validate_file_size(value):
    filesize = value.size

    if filesize > 1048576:  # 1MB
        raise ValidationError(
            "You can't upload file more than 1 MB. "
            "Here is a tool for compressing images: https://www.img2go.com/compress-image")
    else:
        return value


def validate_pdf_file_size(value):
    filesize = value.size

    if filesize > 2097152:  # 2MB
        raise ValidationError(
            "You can't upload file more than 2 MB. "
            "Here is a tool for compressing pdf: https://pdfstandalone.com/#/compress")
    else:
        return value


def validate_pdf_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # get the file extension
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('Invalid file type. Only PDF files are allowed.'))


