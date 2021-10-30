from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.




def index(request):
    return render(request,'chat/index.html')


@login_required
def room(request,room_name):
    
    context = {
        'room_name':room_name,
        'user_name':request.user.username    
    }

    return render(request,'chat/room.html',context)
