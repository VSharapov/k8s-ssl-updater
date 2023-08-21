import click
from kube_secrets_list import list_secrets
from my_cli import check_file

@click.group()
def cli():
    'Group to manage Kubernetes SSL updater related commands'
    pass

cli.add_command(list_secrets, name='list-secrets')
cli.add_command(check_file, name='check-file')

if __name__ == '__main__':
    cli()
