from kubernetes import client, config

def create_namespace():
    """
    This will create a new namespace
    """
    namespace = input('Enter the name of the namespace: ')
    v1 = client.CoreV1Api()
    v1.create_namespace(namespace)