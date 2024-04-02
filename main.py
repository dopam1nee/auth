from webapp import create_app
import threading
from webapp.routes import bp

app_list = []

def run_app(app):
    app.run()

app = create_app()
app_list.append(app)
app.register_blueprint(bp)

threads = []
for app in app_list:
    thread = threading.Thread(target=run_app, args=(app,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
    
    