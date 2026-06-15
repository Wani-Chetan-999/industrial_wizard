from django.db import models

class UploadedDocument(models.Model):
    CATEGORY_CHOICES = [
        ('SOP', 'Standard Operating Procedure'),
        ('MANUAL', 'Equipment Manual'),
        ('LOG', 'Historical Maintenance Log'),
    ]
    # Files will be collected cleanly under your media folder path
    file = models.FileField(upload_to='industrial_docs/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='SOP')
    upload_date = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.category}] {self.file.name}"