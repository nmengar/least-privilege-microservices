from Deployment.Deployment import create_deployment,delete_deployment
from Service import create_service,delete_service
from Namespaces import create_namespace,delete_namespace
from Pod import list_pods
from NetworkPolicy.crud import *
import yaml

namespaces = ['sock-shop']

class Deployment():
    def __init__(self):
        self.namespace = ''
        self.spec = dict()
    
    def add_spec(self,spec):
        self.spec.update(spec)
    
    def assign_namespace(self,namespace):
        self.namespace = namespace


class Service():
    def __init__(self):
        self.metadata = dict()
        self.metadata['namespace'] = ''
        self.metadata['spec'] = dict()
        self.metadata['ports'] = []
        self.metadata['ips'] = []
        self.metadata['deployments'] = []

class NetworkPolicy():
    def __init__(self):
        self.name = ''
        self.namespace = ''
        self.spec = dict()
        self.ips = []
        self.deployments = []
    


class Namespace():
    def __init__(self):
        self.deployments = []
        self.services = []
        self.network_policies = []
    
    def add_deployment(self, deployment):
        self.deployments.append(deployment)
    
    def add_service(self, service):
        self.services.append(service)
    
    def add_network_policy(self, network_policy):
        self.network_policies.append(network_policy)



def parse_manifest(manifest):
    """
    This will parse a manifest file
    """
    if manifest['apiVersion'] != 'apps/v1':
        # Check for API Version Compatibility
        return -1
    
    if manifest['metadata']['namespace'] not in namespaces:
        # No such namespace
        print('No such namespace exists')
        return -1
    
    if manifest['kind'] == 'Deployment':
        # store_state = 
        result = create_deployment(manifest=manifest)
    elif manifest['kind'] == 'Service':
        result = create_service(manifest=manifest)
    elif manifest['kind'] == 'NetworkPolicy':
        result = create_network_policy(manifest=manifest)

    return result

if __name__ == '__main__':
    """
    Currenly this should constantly run until the operation is complete
    TODO: Add mechanism to store and restore state from file/database
    """
    while True:
        path = input('Enter the path of the manifest file: ')
        multiple_documents = input('Does the file contain multiple manifests(y/n): ')
        data = []
        try:
            with open(path) as f:
                if multiple_documents == 'n':
                    data.append(yaml.load(f, Loader=yaml.FullLoader))
                elif multiple_documents == 'y':
                    mdata = yaml.load_all(f, Loader=yaml.FullLoader)
                    for d in mdata:
                        ddict = dict()
                        for k,v in d.items():
                            ddict[k] = v
                        data.append(ddict)
                else:
                    print('Invalid choice for multiple manifests')
                    continue
        except:
            print('Error in opening/parsing the file')
        
        for d in data:
            result = parse_manifest(d)
            if result == -1:
                print('Couldn\'t parse the manifest file')
            else:
                print('Successfully parsed ',d['kind'],' ',d['metadata']['name'])
        # option = input('\nMenu\n1. Create Namespace\n2. Delete Namespace\n3. Create Deployment\n4. Delete Deployment\n5. Create Service\n6. Delete Service\nEnter option: ')
        option = input('Enter e to exit')
        if option == 'e':
            exit()
        # execution = switcher[int(option) - 1]()
        # print(execution)
        
