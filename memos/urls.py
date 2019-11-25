import django.urls

import memos.views

urlpatterns = [
    django.urls.path('', memos.views.index, name="index"),
    django.urls.path('api/memos', memos.views.api_memos, name="api_memos"),
    django.urls.path('api/memos/<uuid:memo_id>', memos.views.api_memos, name="save_memo"),
    django.urls.path('connections', memos.views.connections, name="connections"),
]