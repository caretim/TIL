from django.urls import path
from .views import SnippetViewSet


# Blog 목록 보여주기
Snippet_list = SnippetViewSet.as_view({"get": "list", "post": "create"})

# Snippet detail 보여주기 + 수정 + 삭제
Snippet_detail = SnippetViewSet.as_view(
    {"get": "retrieve", "put": "update", "delete": "destroy"}
)

urlpatterns = [
    path("Snippet/", Snippet_list),
    path("Snippet/<int:pk>/", Snippet_detail),
]
