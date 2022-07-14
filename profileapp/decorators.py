from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])

        # url에서 현재의 pk에 해당하는 object(현재 profile)의 user가
        # 요청을 보낸 user가 동일한지 확인.
        if not profile.user == request.user:
            return HttpResponseForbidden()

        return func(request, *args, **kwargs)

    return decorated