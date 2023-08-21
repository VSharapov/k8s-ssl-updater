from click_web import create_click_web_app
from k8s_ssl_updater import k8s_ssl_updater

app = create_click_web_app(k8s_ssl_updater)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
