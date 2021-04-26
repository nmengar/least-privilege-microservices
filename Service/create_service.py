# https://www.programcreek.com/python/example/96328/kubernetes.client.CoreV1Api

from kubernetes import client,config
from os import path
import yaml


def create_service(manifest):
    """
    This function will create a new service from the manifest file provided in the
    namespace specified
    """
    config.load_kube_config()
    apps_v1 = client.AppsV1Api()
    result = apps_v1.create_nampespaced_Service(
        body=manifest,
        namespace=manifest['metadata']['namespace']
    )
    print('Service created. status=%s' % (result.metadata.name))