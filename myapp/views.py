from django.shortcuts import redirect, render
from myapp import models

# Create your views here.
def devices(request):
    devices = models.Device.objects.all()  # Assuming you have a Device model
    return render(request, 'devices.html', {'devices': devices})

def toggle_device(request, device_id):
    device = models.Device.objects.get(id=device_id)
    if request.method == "POST":
        device.enabled = not device.enabled
        device.save()
    return redirect('devices')

def test(request):
    devices = models.Device.objects.all()
    return render(request, 'test.html', { 'devices': devices })

def toggle_test(request, device_id):
    device = models.Device.objects.get(id=device_id)
    device.enabled = not device.enabled
    device.save()
    return redirect('test')
