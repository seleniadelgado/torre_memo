from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.core import exceptions

import requests
import json

import memos.models

def index(request):
    return render(request, 'index.html')


def connections(request):
    username = request.GET.get('username') 
    connections_response = requests.get('https://torre.bio/api/people/{}/connections?limit=20'.format(username))
    user_response = requests.get('https://bio.torre.co/api/bios/{}'.format(username))
    user = json.loads(user_response.content)
    connections_list = json.loads(connections_response.content)
    user_id = user.get('person')['id']
    connection_memos = { k.connection_id: (k.uuid, k.memo) for k in api_get_memos(request = request, user_id=user_id) }
    data = []
    for connection in connections_list:
        memo_id, memo = connection_memos.get(connection.get('person')['id'], ('', ''))
        data.append({
        'name': connection.get('person')['name'],
        'title': connection.get('person')['professionalHeadline'],
        'memo': memo,
        'memo_id': str(memo_id)
        })
    context = {
    'data': data
    }
    return render(request, 'connections_list.html', context=context)


def api_get_memos(request, user_id):
    if request.method == 'GET':
        memo = memos.models.ConnectionMemos.objects.filter(user_id=user_id)
        return memo


def api_memos(request, connection_id=None, user_id=None, memo_id=None):
    print(memo_id, type(memo_id))
    print(memo_id is None)
    if memo_id is None:
        if request.method == 'POST':
            try:
                # create the memo using the arguments
                #passing in the arguments to make the memo.
                connection_memo = memos.models.ConnectionMemos(connection_id=connection_id, user_id=user_id, memo="")
                # do a full clean of 
                connection_memo.full_clean()
                connection_memo.save()
                # save it and return httpsJSONResponse{}
            except exceptions.ValidationError as e:
                return JsonResponse(
                {
                'object': 'error',
                'message': 'Memo could not be created. {}'.format(e)
                })
                return JsonResponse({}, status=200)
    if request.method == 'POST':
        #update the memo
        memo = request.POST.get('memo')
        memo_note = memos.models.ConnectionMemos.objects.get(uuid=str(memo_id))
        return JsonResponse({}, status=200)
    return HttpResponseNotAllowed(permitted_methods=('POST',))