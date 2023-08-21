from click_web import create_click_web_app
import my_cli

app = create_click_web_app(my_cli, my_cli.cli)

if __name__ == '__main__':
    app.run()
