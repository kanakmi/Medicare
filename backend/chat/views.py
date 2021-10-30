from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

# Chat room 

def home(request):
    data = Room.objects.all()
    context = {
        'data': data
    }
    return render(request, 'home.html', context=context)


@login_required
def room(request, room):
    usr = request.user
    if request.method == 'POST':
        rid = request.POST.get('roomid')
        rom = Room.objects.get(id=rid)
        if(usr == rom.author):
            rom.delete()
            return redirect('/chat')
    username = usr.first_name
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


@login_required
def checkview(request):
    room = request.POST['room_name']
    #username = request.POST['username']
    usr = request.user
    username = usr.first_name
    if Room.objects.filter(name=room).exists():
        return redirect('/chat/'+room)
    else:
        new_room = Room.objects.create(name=room)
        new_room.author = usr
        new_room.save()
        return redirect('/chat/'+room)


@login_required
def send(request):
    usr = request.user
    message = request.POST['message']
    #username = request.POST['username']
    username = usr.first_name
    room_id = request.POST['room_id']

    new_message = Message.objects.create(
        value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    temp = messages
    try:
        temp = list(temp.values())
    except:
        return
    try:
        if(str(temp[0]['user'])==str(request.user.email)):
            print("---------------------------------")
            temp = []
        else:
            messages.delete()
    except:
        messages.delete()
    return JsonResponse({"messages": temp})

def tempchat(request):
    return render(request,'homes.html')