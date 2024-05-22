from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from core.models import *
from django.utils import timezone

@csrf_exempt
@login_required(login_url="courier/sign-in/")
def available_jobs_api(request):
    jobs =list(Job.objects.filter(status=Job.PROCESSING_STATUS).values())

    return JsonResponse({
        "success": True,
        "jobs": jobs
    })


@csrf_exempt
@login_required(login_url="/courier/sign-in/")
def current_job_update_api(request,id):
    job=Job.objects.filter(id=id,
                           courier=request.user.courier,
                           status__in=[
                               Job.PICKING_STATUS,
                               Job.DELIVERING_STATUS
                           ]
                           ).last()
    if job.status==job.PICKING_STATUS:
        job.pickup_photo=request.FILES['pickup_photo']
        job.pickedup_at=timezone.now()
        job.status=job.DELIVERING_STATUS
        job.save()

    return JsonResponse({
        'success':True
    })