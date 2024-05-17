from django.db import models

# Create your models here.
class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='static/assets/pdfs/', blank=True, null=True)

    class Meta:
        abstract = True

class TermsOfService(BaseModel):
    pass

class PrivacyPolicy(BaseModel):
    pass