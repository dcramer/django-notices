This is a layer that functions much like the Django ORM does except it works on top of the Sphinx (http://www.sphinxsearch.com) full-text search engine.

Please Note: You will need to create your own sphinx indexes and install sphinx on your server to use this app.

*There will no longer be release packages available. Please use SVN to checkout the latest trunk version, as it should always be stable and current.*

Installation
------------

To install the latest stable version::

	sudo easy_install django-notices

To install the latest development version (updated quite often)::

	git clone git://github.com/dcramer/django-notices.git
	cd django_notices
	sudo python setup.py install

Usage
-----

The easiest way to use django-notices, is simply by adding it to your settings.py::

	INSTALLED_APPS = (
	    '...',
	    'django_notices',
	)
	
	MIDDLEWARE_CLASSES = (
	    'django_notices.middleware.NoticeMiddleware',
	)
	
	TEMPLATE_CONTEXT_PROCESSORS = (
	    'django_notices.context_processors.notices',
	)

Once you've done this you'll now have access to two important pieces of the notice system, the ``notices`` context variable, and ``request.notices``.

The first thing you're going to want to do, is add a handler for ``notices`` within your templates::

	<div id="notices">
		<ul>
			{% for notice in request.notices %}
				<li class="notice notice-{{ notice.level_label }}">{{ notice.message|escape }}</li>
			{% endfor %}
		</ul>
	</div>

What this does, is on each page load, displays each active notice and clears it from the session.

Now once you can display your notices, you'll need to begin adding them. This is also made very ::

	def my_view(request):
		request.notices.warn('This is a warning')

There are several methods available in the built-in handler::

	NoticeHandler.warn
	NoticeHandler.error
	NoticeHandler.info
	NoticeHandler.debug
	NoticeHandler.success

By default, DEBUG level notices are not shown. To change this, you can adjust the ``NOTICE_LEVEL`` setting in your ``settings.py``::

	from django_notices import DEBUG
	NOTICE_LEVEL = DEBUG