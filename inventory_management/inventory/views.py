from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import pytz
from datetime import datetime
from django.contrib.auth.models import User
from .models import ProjectType, AddUserSubmission

# Create your views here.

def startup_view(request):
    return render(request, 'inventory_management/home.html')

def login_view(request):
    return render(request, 'inventory_management/login.html')

def admin_login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to custom admin dashboard
        else:
            error_message = 'Invalid credentials or not an admin user.'
    return render(request, 'inventory_management/adminLogin.html', {'error_message': error_message})

@login_required
def admin_dashboard_view(request):
    admin_name = request.user.get_full_name() or request.user.username
    # Get current time in Indian/Delhi timezone
    india_tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(india_tz)
    hour = now.hour
    if hour < 12:
        greeting = 'Good morning'
    elif hour < 18:
        greeting = 'Good afternoon'
    else:
        greeting = 'Good evening'
    project_types = ProjectType.objects.all()
    return render(request, 'inventory_management/admin_dashboard.html', {
        'admin_name': admin_name,
        'greeting': greeting,
        'project_types': project_types
    })

@login_required
def add_user_view(request):
    admin_name = request.user.get_full_name() or request.user.username
    # Get current time in Indian/Delhi timezone
    import pytz
    from datetime import datetime
    india_tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(india_tz)
    hour = now.hour
    if hour < 12:
        greeting = 'Good morning'
    elif hour < 18:
        greeting = 'Good afternoon'
    else:
        greeting = 'Good evening'
    project_types = ProjectType.objects.all()

    if request.method == 'POST':
        project_id = request.POST.get('project')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            error_message = "Passwords do not match."
            return render(request, 'inventory_management/admin_dashboard.html', {
                'error_message': error_message,
                'admin_name': admin_name,
                'greeting': greeting,
                'project_types': project_types,
                'show_add_user_modal': True
            })
        # Optionally, handle project_id == 'inventory_analysis' for default
        if project_id == 'inventory_analysis':
            project_type = ProjectType.objects.filter(name__iexact='Inventory Analysis').first()
        else:
            project_type = ProjectType.objects.filter(id=project_id).first()
        user = User.objects.create_user(username=username, password=password)
        if project_type:
            from .models import ProjectAssignment
            ProjectAssignment.objects.create(user=user, project_type=project_type)
        # Save the Add User form submission
        AddUserSubmission.objects.create(project_type=project_type, username=username)
        return redirect('admin_dashboard')
    return redirect('admin_dashboard')

@login_required
def remove_user_view(request):
    admin_name = request.user.get_full_name() or request.user.username
    # Get current time in Indian/Delhi timezone
    import pytz
    from datetime import datetime
    india_tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(india_tz)
    hour = now.hour
    if hour < 12:
        greeting = 'Good morning'
    elif hour < 18:
        greeting = 'Good afternoon'
    else:
        greeting = 'Good evening'

    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            if user.is_superuser:
                error_message = "Cannot remove a superuser."
            else:
                user.delete()
                return redirect('admin_dashboard')
        except User.DoesNotExist:
            error_message = "User does not exist."
        return render(request, 'inventory_management/admin_dashboard.html', {
            'error_message': error_message,
            'admin_name': admin_name,
            'greeting': greeting
        })
    return redirect('admin_dashboard')