def notices(request):
    """Add the ``notices`` variable to the context."""
    return {
        'notices': NoticeHandler(request.session)
    }