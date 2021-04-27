from kubernetes import client,config
from os import path
import time
import yaml
from Pod.list_pods import list_pods_for_all_namespaces
    
def create_deployment(manifest):
    config.load_kube_config()
    apps_v1 = client.AppsV1Api()
    result = apps_v1.create_namespaced_deployment(
        body=manifest,
        namespace=manifest['metadata']['namespace']
    )
    time.sleep(2)
    pods = list_pods_for_all_namespaces()
    for i in pods:
        if i.metadata.namespace == manifest['metadata']['namespace']:
            if manifest['metadata']['app'] in i.metadata.name:
                pod_list.append((i.metadata.name,i.status.pod_ip))
    print('Deployment created. status=%s' % (result.metadata.name))
    print(pod_list)
    return pod_list
    
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