from django.shortcuts import render

from generator.utils import generate_mesh


def home_view(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        mesh_path = generate_mesh(prompt)
        return render(request, "generator/templates/generator/result.html", {"mesh": mesh_path})
    return render(request, "generator/home_view.html")
