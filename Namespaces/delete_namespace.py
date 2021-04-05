from kubernetes import client, config

def delete_namespace():
    """
    This will delete an existing namespace
    """
    namespace = input('Enter the name of the namespace: ')
    v1 = client.CoreV1Api()
    v1.delete_namespace(namespace)