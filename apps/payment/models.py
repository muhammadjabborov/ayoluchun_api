from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import DecimalField
from django.utils.translation import gettext as _

from ..account.models import User
from ..common.models import BaseModel, PaymentType, PaymentStatusType
from ..course.models import Course


class Payment(BaseModel):
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE, related_name='user_payments')
    sum = models.DecimalField(verbose_name=_('Sum'), decimal_places=2, max_digits=10, default=0)
    course = models.ForeignKey(Course, verbose_name=_('Course'), on_delete=models.CASCADE,
                               related_name='course_payments')
    payment_type = models.CharField(verbose_name=_("Sales type"), max_length=25, choices=PaymentType.choices,
                                    default=PaymentType.PAYME)
    payment_status_type = models.CharField(verbose_name=_("Sales type"), max_length=25,
                                           choices=PaymentStatusType.choices, default=PaymentStatusType.WAITING)

    def __str__(self):
        return f"{self.user.first_name} {self.course.title}"

    def clean(self):
        if self.pk:
            obj = Payment.objects.get(pk=self.pk)
            if obj.payment_type is None:
                raise ValidationError('The payment type can not be None')
            if obj.payment_status_type == PaymentStatusType.FAILED:
                raise ValidationError('You cannot pay')
            if obj.payment_status_type == PaymentStatusType.SUCCESS:
                raise ValidationError('You successfully payed')
            if obj.payment_status_type == PaymentStatusType.WAITING:
                raise ValidationError('Wait a little bit')
            if obj.sum < obj.course.price:
                raise ValidationError('You don not have any money')

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
