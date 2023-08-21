import click
from kube_secrets_list import cli as kube_secrets_cli
from my_cli import cli as my_cli_cli

@click.group()
def k8s_ssl_updater():
    'Group to manage Kubernetes SSL updater related commands'
    pass

k8s_ssl_updater.add_command(kube_secrets_cli, name='kube_secrets')
k8s_ssl_updater.add_command(my_cli_cli, name='my_cli')

if __name__ == '__main__':
    k8s_ssl_updater()
