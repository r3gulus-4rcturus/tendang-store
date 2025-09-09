from django.shortcuts import render

def show_main(request):
    context = {
        'nama': 'Muhammad Lanang',
        'kelas': 'PBP A'
    }

    return render(request, "main.html", context)