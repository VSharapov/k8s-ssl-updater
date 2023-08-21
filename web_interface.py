from click_web import create_click_web_app
import my_cli
import kube_secrets_list

app = create_click_web_app([my_cli.cli, kube_secrets_list.cli])

if __name__ == '__main__':
    app.run(host='0.0.0.0')
