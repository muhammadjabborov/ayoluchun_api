from django.db import models
from django.utils.translation import gettext as _

from ..account.models import User
from ..common.models import BaseModel, PaymentType, PaymentStatusType
from ..course.models import Course


class Payment(BaseModel):
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE,
                             related_name='user_payments')
    sum = models.DecimalField(verbose_name=_('Sum'), decimal_places=2, max_digits=10, default=0)
    course = models.ForeignKey(Course, verbose_name=_('Course'), on_delete=models.CASCADE,
                               related_name='course_payments')
    payment_type = models.CharField(verbose_name=_("Sales type"), max_length=25, choices=PaymentType.choices,
                                    default=PaymentType.PAYME)
    payment_status_type = models.CharField(verbose_name=_("Sales type"), max_length=25,
                                           choices=PaymentStatusType.choices, default=PaymentStatusType.WAITING)

    def __str__(self):
        return f"{self.user.first_name} {self.course.title}"

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
