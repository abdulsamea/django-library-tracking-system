from celery import shared_task
from .models import Loan
from django.core.mail import send_mail
from django.conf import settings
from datetime import date

@shared_task
def send_loan_notification(loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
        member_email = loan.member.user.email
        book_title = loan.book.title
        send_mail(
            subject='Book Loaned Successfully',
            message=f'Hello {loan.member.user.username},\n\nYou have successfully loaned "{book_title}".\nPlease return it by the due date.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )
    except Loan.DoesNotExist:
        pass


@shared_task
def check_overdue_loans():
    try:
        overdue_loans = Loan.objects.filter(is_returned=False, due_date__lt=date.today())
        for loan in overdue_loans:
            member_email = loan.member.user.email
            member_name = loan.member.user.first_name
            book_title = loan.book.title
            send_mail(
                subject='Reminder for overdue books',
                message=f'Hello {member_name},\n\nYou have loan overdue for the booth: "{book_title}".\nPlease pay the loan for the book.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[member_email],
                fail_silently=False,
            )
    except:
        pass
