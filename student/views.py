from django.shortcuts import render,redirect,get_object_or_404
from staff . models import *
from django.contrib.auth.decorators import login_required
from . forms import *
from . models import *
from django.contrib import messages
from . forms import *
from staff . forms import *



@login_required
def student_dashboard(request):
    total_staff = Staff.objects.count()
    student_profile = Student.objects.get(user=request.user)
    profile_image = student_profile.profile_image.url if student_profile.profile_image else None
    return render(request,'student_templates/student_dashboard.html',{'profile_image': profile_image,'total_staff':total_staff})


def edit_student_details(request,user_id):
    user = request.user
    if request.method == 'POST':
        form = StudentChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            student = Student.objects.get(user=user)
            student.name = user.username
            student.email = user.email
            student.profile_image = user.profile_image
            student.save()
            return redirect('student_dashboard')  
    else:
        form = StudentChangeForm(instance=user)
    return render(request, 'student_templates/edit_student_details.html', {'form': form})



def student_notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'student_templates/student_notifications.html', {'notifications': notifications})


def delete_notification(request, notification_id):
    if request.method == 'POST':
        try:
            notification = Notification.objects.get(pk=notification_id, user=request.user)
            notification.delete()
            messages.success(request, 'Notification deleted successfully.')
        except Notification.DoesNotExist:
            messages.error(request, 'Notification does not exist.')
    return redirect('student_notification')


def student_feedback(request, staff_id):
    staff_member = get_object_or_404(Staff, id=staff_id)

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            student = request.user.student
            Feedback.objects.create(student=student, staff_member=staff_member, message=message)
            messages.success(request, 'Feedback sent successfully.')
            return redirect('student_feedback')  
    else:
        form = FeedbackForm()
    
    return render(request, 'student_templates/student_feedback.html', {'form': form})



def display_questions(request):
    questions = Question.objects.all()
    choices = Choice.objects.all() 
    return render(request, 'student_templates/display_questions.html', {'questions': questions, 'choices': choices})


def evaluate_answers(request):
    if request.method == 'POST':
        score = 0
        total_questions = Question.objects.count()  
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = int(key.split('_')[-1])
                choice_id = int(value)
                choice = Choice.objects.get(pk=choice_id)
                if choice.is_correct:
                    score += 1
        return render(request, 'student_templates/score.html', {'score': score, 'total_questions': total_questions})
    else:
        return render(request, 'error.html', {'message': 'Method not allowed'})    

