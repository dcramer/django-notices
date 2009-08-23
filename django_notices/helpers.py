from django.conf import settings
from constants import *

CURRENT_LEVEL = getattr(settings, 'NOTICE_LEVEL', INFO)

class Notice(object):
    def __init__(self, level, message):
        self.level, self.message = level, message
    
    @property
    def level_label(self):
        """Typically used for CSS class names."""
        return LEVELS.get(self.level, LEVELS[NOTICE])

class NoticeHandler(object):
    def __init__(self, session):
        self.session = session
    
    def __iter__(self):
        """Return each notice and removes it from session."""
        messages = self.session.get('_messages')
        if messages:
            for n in messages:
                if n.level >= CURRENT_LEVEL:
                    yield n
            del self.session['_messages']
    
    def add(self, message, level=NOTICE):
        self.session.setdefault('_messages', []).append(Notice(level, message))
    
    def get(self):
        """Retrieves current notices.
        
        Use ``get_and_clear()`` if you wish to also clear the notices."""
        return self.session.get('_messages', [])
    
    def get_and_clear(self):
        """Retrieves current notices, and clears them from the session."""
        return self.session.pop('_messages', [])

    # Wrapper functions for add
    
    def warn(self, message):
        self.add(message, WARN)
    
    def error(self, message):
        self.add(message, ERROR)
    
    def notice(self, message):
        self.add(message, NOTICE)
    info = notice

    def debug(self, message):
        self.add(message, DEBUG)
    
    def success(self, message):
        self.add(message, SUCCESS)