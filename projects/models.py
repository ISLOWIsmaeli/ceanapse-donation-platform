from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)

    def __str__(self):
        return self.name
    
    @property
    def progress_percentage(self):
        if self.target_amount > 0:
            return (self.total_donations / self.target_amount) * 100
        return 0
    
    @property
    def amount_remaining(self):
        remaining = self.target_amount - self.total_donations
        return max(remaining, 0)