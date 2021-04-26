from kubernetes import client,config
from os import path
import yaml


def delete_service():
    """
    This function will delete a service from the manifest file provided in the
    namespace specified
    """
    config.load_kube_config()
    service = input('Enter name of service to be deleted: ')
    namespace = input('Enter namespace of deployment: ')

    apps_v1 = client.AppsV1.Api()
    result = v1.delete_nampespaced_service(
        name=service,
        namespace=namespace,
        body = {}
    )
    print('Service deleted. status=%s' % (result.metadata.name))