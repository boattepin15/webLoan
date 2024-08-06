from django.shortcuts import render, redirect
# from core.models import Profile
from core.forms import auth as auth_form
#from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from core.forms.address import AddressForm
from core.forms.profile import ProfileForm
from core.forms.checkin import CheckinForm
from core.forms.slip import SlipForm
from core.models import Address, Profile, Slip, Checkin






def home(request):
    """"""
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        form = auth_form.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors.as_text().encode('utf-8'))
    else:
        form = auth_form.UserRegisterForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'register.html', context)



@login_required
def profile(request):
    user = request.user
    address, created = Address.objects.get_or_create(user=user)
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        address_form = AddressForm(request.POST, instance=address)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if address_form.is_valid() and profile_form.is_valid():
            address_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        address_form = AddressForm(instance=address)
        profile_form = ProfileForm(instance=profile)

    context = {
        'user': user,
        'address_form': address_form,
        'profile_form': profile_form,
        'profile': profile,
    }
    return render(request, 'profile.html', context)


@login_required
def upload_slip(request):
    if request.method == 'POST':
        form = SlipForm(request.POST, request.FILES)
        if form.is_valid():
            slip = form.save(commit=False)
            slip.user = request.user
            slip.save()
            return redirect('home')  # เปลี่ยนเส้นทางตามที่คุณต้องการหลังจากอัปโหลดสำเร็จ
    else:
        form = SlipForm()

    return render(request, 'upload_slip.html', {'form': form})


@login_required
def slip_approve(request):
    slips = Slip.objects.filter(user=request.user)
    context = {
        'slips': slips,
    }
    return render(request, 'slip_approve.html', context)


@login_required
def checkin(request):
    try:
        checkin_instance = Checkin.objects.get(user=request.user, checkin=True)
    except Checkin.DoesNotExist:
        checkin_instance = None

    if request.method == 'POST':
        form = CheckinForm(request.POST, request.FILES, instance=checkin_instance)
        if form.is_valid():
            checkin = form.save(commit=False)
            checkin.user = request.user
            checkin.save()
            return redirect('home')
    else:
        form = CheckinForm(instance=checkin_instance)
    
    context = {
        'form': form,
        'checkin': checkin_instance
    }

    return render(request, 'checkin.html', context)