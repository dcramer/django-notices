from helpers import NoticeHandler

class NoticeMiddleware(object):
    def process_request(self, request):
        request.notices = NoticeHandler(request.session)