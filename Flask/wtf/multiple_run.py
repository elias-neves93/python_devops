from werkzeug.wsgi import DispatcherMiddleware

from news_app import create_app as create_news_app
from quokka.core import create_app as create_quokka_app
from flask.ext.api import create_app as create_api

app = create_news_app(config_filename='/server/wtf/settings.py')
blog_app = create_quokka_app(config='quokka.mysettings')
api_v1 = create_api(serializers=['xml', 'json'], settings='api_settings_v1')

app.wsgi_app = DispatcherMiddleware(
    app.wsgi_app,  # servido em /
    {
        '/blog': blog_app,
        '/api/v1': api_v1
    }
)

app.run(debug=True, use_reloader=True)
