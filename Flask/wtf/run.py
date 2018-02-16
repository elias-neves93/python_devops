#from news_app import create_app
#
#app = create_app(config_filename='/server/wtf/settings.py')
#app.run(debug=True, use_reloader=True)

import sys
from app import create_app
config_env_var = sys.argv[1] if len(sys.argv) > 1 else 'FLASK_CONFIG'
app = create_app(config_env_var)
app.run()
