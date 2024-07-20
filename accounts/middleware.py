import datetime
from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now
from .models import UserActivity, PageVisit

class UserActivityMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            UserActivity.objects.update_or_create(
                user=request.user,
                defaults={'last_activity': now()}
            )

        session_key = request.session.session_key or request.session.create()
        path = request.path
        visited_pages = request.session.get('visited_pages', [])

        if path not in visited_pages:
            PageVisit.objects.create(
                user=request.user if request.user.is_authenticated else None,
                session_key=session_key,
                path=path
            )
            visited_pages.append(path)
            request.session['visited_pages'] = visited_pages