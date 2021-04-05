# https://www.programcreek.com/python/example/96328/kubernetes.client.CoreV1Api

from kubernetes import client,config
from os import path
import yaml


def create_service():
    """
    This function will create a new service from the manifest file provided in the
    namespace specified
    """
    config.load_kube_config()
    path = input('Enter path of service manifest:')
    namespace = input('Enter namespace you want to deploy in:')
    with open(path) as f:
        dep = yaml.safe_load(f)
        apps_v1 = client.AppsV1.Api()
        result = apps_v1.create_nampespaced_Service(
            body=dep,
            namespace=namespace
        )
        print('Service created. status=%s' % (result.metadata.name))