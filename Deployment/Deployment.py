from kubernetes import client,config
from os import path
import yaml
    
def create_deployment(self):
    config.load_kube_config()
    path = input('Enter path of deployment manifest: ')
    namespace = input('Enter namespace you want to deploy in: ')
    with open(path) as f:
        dep = yaml.safe_load(f)
        apps_v1 = client.AppsV1.Api()
        result = v1.create_nampespaced_deployment(
            body=dep,
            namespace=namespace
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