from kubernetes import client,config
from os import path
import yaml
    
def create_deployment(manifest):
    config.load_kube_config()
    apps_v1 = client.AppsV1Api()
    result = v1.create_nampespaced_deployment(
        body=manifest,
        namespace=manifest['metadata']['namespace']
    )
    print('Deployment created. status=%s' % (result.metadata.name))
    
def delete_deployment(self):
    config.load_kube_config()
    deployment = input('Enter name of deployment to be deleted: ')
    namespace = input('Enter namespace of deployment: ')

    apps_v1 = client.AppsV1.Api()
    result = v1.delete_nampespaced_deployment(
        name=deployment,
        namespace=namespace,
        body = {}
    )
    print('Deployment deleted. status=%s' % (result.metadata.name))