from django.shortcuts import render, redirect

from mysite.forms import RegistrationForm


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.
            # post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            # post.save()
            return redirect('post_list')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})
