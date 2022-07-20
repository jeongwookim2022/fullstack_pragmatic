from django.http import HttpResponseForbidden

from commentapp.models import Comment


#Commnet의 주인인지 아닌지를 확인하기 위함.

def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])

        # 현재 request를 보내는 user가
        # comment의 주인(writer)인지 아닌지 확인하는 코드
        if not comment.writer == request.user:
            return HttpResponseForbidden()

        return func(request, *args, **kwargs)

    return decorated