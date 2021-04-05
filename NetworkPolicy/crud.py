from kubernetes import client,config
from os import path
import yaml


def create_network_policy():
    config.load_kube_config()
    path = input('Enter path of network policy manifest:')
    namespace = input('Enter namespace you want to deploy in:')
    with open(path) as f:
        policy = yaml.safe_load(f)
        networking_v1 = client.NetworkingV1Api.Api()
        result = networking_v1.create_nampespaced_network_policy(
            body=policy,
            namespace=namespace
        )
        print('Network Policy created. status=%s' % (result.metadata.name))


def delete_network_policy():
    config.load_kube_config()
    path = input('Enter path of network policy manifest:')
    namespace = input('Enter namespace you want to deploy in:')
    with open(path) as f:
        policy = yaml.safe_load(f)
        networking_v1 = client.NetworkingV1Api.Api()
        result = networking_v1.delete_namespaced_network_policy(
            body=policy,
            namespace=namespace
        )
        print('Network Policy deleted. status=%s' % (result.metadata.name))