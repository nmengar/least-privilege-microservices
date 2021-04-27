# Reference from https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/
from kubernetes import client, config

def list_pods_for_all_namespaces():
    """
    This will list pods for a given namespace
    """
    try:
        config.load_kube_config()
        v1 = client.CoreV1Api()
        results = v1.list_pod_for_all_namespaces(watch=False)
    except Exception as e:
        print(e)
        exit(1)
    for i in results.items:
        print("%s\t%s\t%s" % (i.status.pod_ip,i.metadata.namespace,i.metadata.name))
    return result