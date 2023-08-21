import click
import json
import os
from kubernetes import client, config
from datetime import datetime

@click.group()
def cli():
    'A script to list Kubernetes secrets within a specified namespace'
    pass

def get_namespaces():
    file_path = "namespaces-list.json"
    
    # Check if file exists and is less than 5 minutes old
    if os.path.exists(file_path) and (datetime.now() - datetime.fromtimestamp(os.path.getmtime(file_path))).seconds < 300:
        with open(file_path, 'r') as file:
            return json.load(file)
    
    config.load_kube_config()
    v1 = client.CoreV1Api()
    namespaces = [ns.metadata.name for ns in v1.list_namespace().items]

    # Update the file with the latest namespaces
    with open(file_path, 'w') as file:
        json.dump(namespaces, file)

    return namespaces

@click.command()
@click.option('--namespace', prompt='Select a namespace', type=click.Choice(get_namespaces()), default='default')
def list_secrets(namespace):
    'List the names of all secrets in the selected namespace'
    config.load_kube_config()
    v1 = client.CoreV1Api()
    print(f"Listing secrets in namespace {namespace}:")
    secrets = v1.list_namespaced_secret(namespace=namespace)
    for secret in secrets.items:
        print(secret.metadata.name)

cli.add_command(list_secrets)

if __name__ == '__main__':
    cli()