from django.core.management.base import BaseCommand

from users.models import Payment, User


class Command(BaseCommand):

    def handle(self, *args, **options):

        params = dict(email="test@example.com", password="qwerty")
        user, user_status = User.objects.get_or_create(**params)

        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS("Пользователь успешно создан"))

        Payment.objects.create(
            owner=user,
            payment_date="2024-03-20",
            paid_course_id=1,
            paid_lesson=None,
            amount=2000.00,
            type="CASH",
        )

        Payment.objects.create(
            owner=user,
            payment_date="2024-08-06",
            paid_course=None,
            paid_lesson_id=2,
            amount=1500.00,
            type="BANK_TRANSFER",
        )

        self.stdout.write(self.style.SUCCESS("Данные о платежах успешно загружены"))
