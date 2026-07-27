from django.shortcuts import render
from django.http import JsonResponse
from .models import Grievance
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def submit_grievance(request):
    if request.method == 'POST':
        try:
            description = request.POST.get('description')
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            image_file = request.FILES.get('live_image')

            grievance = Grievance.objects.create(
                description=description,
                latitude=latitude,
                longitude=longitude,
                live_image=image_file
            )

            return JsonResponse({'status': 'success', 'id': grievance.id})
        except Exception as error:
            return JsonResponse({'status': 'error', 'message': str(error)}, status=400)

    return JsonResponse({'status': 'error'}, status=405)