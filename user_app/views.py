from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from user_app.models import Ownersinfo
from user_app.models import Patientinfo
from decimal import Decimal
from django.utils import timezone


# Create your views here.


def user_index(request):
    return render(request, "user_app/user_index.html")


def user_registration(request):
    if request.method == "POST":
        user_name = request.POST.get("name", "").strip().title()
        user_phone = request.POST.get("phone", "").strip()
        user_password1 = request.POST.get("password1", "").strip()
        user_password2 = request.POST.get("password2", "").strip()

        exist = User.objects.filter(username=user_phone).exists()
        if exist:
            messages.error(request, "User alredy exist")
            return redirect("user_login")

        if user_password1 != user_password2:
            messages.error(request, "Password do not match! try again")
            return redirect("user_registration")

        if not user_phone or not user_password1:
            messages.error(request, "Please fill in all details.")
            return redirect("user_registration")

        user = User.objects.create_user(
            username=user_phone,
            password=user_password1,
            first_name=user_name,
        )
        user.save()
        messages.success(request, "Account created successfully. Please login")

    return render(request, "user_app/user_registration.html")


def user_login(request):
    if request.method == "POST":
        user_phone = request.POST.get("phone", "").strip()
        user_password = request.POST.get("password", "").strip()

        if not user_phone or not user_password:
            messages.error(request, "Please fill in all details.")
            return redirect("user_login")

        exist = User.objects.filter(username=user_phone).exists()
        if not exist:
            messages.error(request, "User does not exist! Please register first.")
            return redirect("user_registration")

        user = authenticate(request, username=user_phone, password=user_password)
        if user is None:
            messages.error(request, "Invalid credentials! Try again.")
            return redirect("user_login")
        login(request, user)
        return redirect("user_profile")  ###

    return render(request, "user_app/user_login.html")


def user_logout(request):
    logout(request)
    return redirect("user_index")


@login_required
def user_profile(request):
    # user = User.objects.get(username=phone)
    user = request.user
    info = Ownersinfo.objects.filter(phone=user.username).first()
    appointment = Patientinfo.objects.filter(phone=user.username)
    context = {"user": user, "info": info, "appointment": appointment}
    return render(request, "user_app/user_profile.html", context)


@login_required
def user_appointment(request):
    user = request.user
    info = Ownersinfo.objects.filter(phone=user.username).first()
    context = {"user": user, "info": info}
    if request.method == "POST":
        # Strings (empty if not provided)
        name = request.POST.get("owner_name", "").strip().title() or None
        phone = request.POST.get("owner_phone", "").strip() or None
        division = request.POST.get("division", "").strip().title() or None
        district = request.POST.get("district", "").strip().title() or None
        upazila = request.POST.get("upazila", "").strip().title() or None
        address = request.POST.get("address", "").strip().title() or None
        tag = request.POST.get("tag", "").strip() or None
        species_type = request.POST.get("species_type", "").strip() or None
        breed = request.POST.get("breed", "").strip().title() or None
        sex = request.POST.get("sex", "").strip().title() or None
        complaint = request.POST.get("complaint", "").strip() or None
        disease_history = request.POST.get("disease_history", "").strip() or None
        treatment_history = request.POST.get("treatment_history", "").strip() or None
        management_history = request.POST.get("management_history", "").strip() or None

        # Decimal/Float Fields
        try:
            body_weight = Decimal(request.POST.get("body_weight", "").strip() or -1)
        except:
            body_weight = -1

        try:
            milk_yield = Decimal(request.POST.get("milk_yield", "").strip() or -1)
        except:
            milk_yield = -1

        # Integer Fields
        try:
            age = int(request.POST.get("age", "").strip() or -1)
        except:
            age = -1

        try:
            parity = int(request.POST.get("parity", "").strip() or -1)
        except:
            parity = -1

        try:
            total_animal = int(request.POST.get("total_animal", "").strip() or -1)
        except:
            total_animal = -1

        try:
            total_sick = int(request.POST.get("total_sick", "").strip() or -1)
        except:
            total_sick = -1

        try:
            total_dead = int(request.POST.get("total_dead", "").strip() or -1)
        except:
            total_dead = -1

        try:
            duration_illness = int(
                request.POST.get("duration_illness", "").strip() or -1
            )
        except:
            duration_illness = -1

        try:
            pregnancy_month = int(request.POST.get("pregnancy_month", "").strip() or -1)
        except:
            pregnancy_month = -1

        # Boolean Fields
        pregnancy_value = request.POST.get("pregnancy", "").strip().lower()
        pregnancy = True if pregnancy_value in ["yes", "true", "1"] else False

        # Date Fields (optional)
        date_of_parturition = (
            request.POST.get("date_of_parturition", "").strip() or None
        )
        date_of_oestrus = request.POST.get("date_of_oestrus", "").strip() or None

        # owner = Ownersinfo(
        #     name=name,
        #     phone=phone,
        #     division=division,
        #     district=district,
        #     upazila=upazila,
        #     address=address,
        # )
        # owner.save()
        # Create or update Owner info
        owner, created = Ownersinfo.objects.get_or_create(phone=phone)

        # Update only if new data provided (to avoid overwriting with empty fields)
        if name:
            owner.name = name
        if division:
            owner.division = division
        if district:
            owner.district = district
        if upazila:
            owner.upazila = upazila
        if address:
            owner.address = address

        owner.save()

        patient = Patientinfo(
            name=name,
            phone=phone,
            tag=tag,
            species=species_type,
            breed=breed,
            weight=body_weight,
            age=age,
            sex=sex,
            pregnancy=pregnancy,
            pregnancy_month=pregnancy_month,
            parity=parity,
            milk_yield=milk_yield,
            date_of_parturition=date_of_parturition,
            date_of_oestrus=date_of_oestrus,
            total_animals=total_animal,
            total_sick_animals=total_sick,
            total_dead_animals=total_dead,
            duration_of_illness=duration_illness,
            complaint=complaint,
            disease_history=disease_history,
            treatment_history=treatment_history,
            management_history=management_history,
        )
        patient.save()
        messages.success(request, "Appointment submitted")
        return redirect("user_profile")  ####

    return render(request, "user_app/user_appointment.html", context)
