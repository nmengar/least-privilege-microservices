from Deployment.Deployment import create_deployment,delete_deployment
from Service import create_service,delete_service
from Namespaces import create_namespace,delete_namespace
from Pod import list_pods
import yaml


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
        self.namespace = ''
        self.spec = dict()
        self.ports = []
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



def parse_manifest(manifest,namespace):
    obj = 1
    return obj

if __name__ == '__main__':
    """
    Currenly this should constantly run until the operation is complete
    TODO: Add mechanism to store and restore state from file
    """
    switcher = {
        0: create_namespace,
        1: delete_namespace,
        2: create_deployment,
        3: delete_deployment,
        4: create_service,
        5: delete_service,
    }
    while True:
        path = input('Enter the path of the manifest file: ')
        multiple_documents = input('Does the file contain multiple manifests(y/n): ')
        try:
            with open(path) as f:
                if multiple_documents == 'n':
                    data = yaml.load(f, Loader=yaml.FullLoader)
                elif multiple_documents == 'y':
                    mdata = yaml.load_all(f, Loader=yaml.FullLoader)
                    data = []
                    for d in mdata:
                        ddict = dict()
                        for k,v in d.items():
                            ddict[k] = v
                        data.append(ddict)
                else:
                    print('Invalid choice for multiple manifests')
                    continue
                print(data)
                continue
        except:
            print('Error in opening/parsing the file')
        
        option = input('\nMenu\n1. Create Namespace\n2. Delete Namespace\n3. Create Deployment\n4. Delete Deployment\n5. Create Service\n6. Delete Service\nEnter option: ')
        if option == 'e':
            exit()
        execution = switcher[int(option) - 1]()
        print(execution)
        
