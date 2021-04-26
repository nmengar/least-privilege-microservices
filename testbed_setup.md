# Tesbed setup
To setup Sockshop application on top of istio and kubernetes in CloudLab, do the following steps-

**Installing Kubernetes on the cluster-**
1. Deploy a 3-node cluster with CentOS 7 installed. Follow (https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/) to add the Kubernetes repository for yum and (https://docs.genesys.com/Documentation/System/8.5.x/DDG/InstallationofDockerEngine(CommunityEdition)onCentOS7) for older version of docker

2. Edit the /etc/hosts file to add the hostnames "master-node", "node-1" and "node-2"

3. Install docker and the 1.19 version of Kubernetes (Kubelet, Kubeadm)- <br />
`yum install kubeadm-1.19.0 kubelet-1.19.0 docker -y`

4. On all the nodes, enable and start kubelet and docker <br />
`systemctl enable kubelet` <br />
`systemctl start kubelet` <br />
`systemctl enable docker` <br />
`systemctl start docker` <br />

5. On all the nodes, turn off swap <br />
`swapoff -a` <br />

6. On the **master node** initialize the kubernetes cluster, <br />
`kubeadm init --apiserver-advertise-address <api-adverstise-ip> --pod-network-cidr=10.244.0.0/16 --kubernetes-version v1.19.0` <br />
Here,
 api-advertise-address --> choose the IP address from the interface which connects the master-node to worker nodes
 pod-network-cidr      --> is chosen based on the container network that is being used (flannel here)
 Once the command finishes executing, copy the kubeadm join command that is displayed

7. Enable the kubectl command for the root user- <br />
`mkdir -p $HOME/.kube` <br />
`cp -i /etc/kubernetes/admin.conf $HOME/.kube/config` <br />
`chown $(id -u):$(id -g) $HOME/.kube/config` <br />

8. Add the container network flannel- <br />
`(when doing kubeadm init use flag --pod-network-cidr=10.244.0.0/16 )` <br />
`export kubever=$(kubectl version | base64 | tr -d ‘\n’)` <br />
`kubectl apply -f https://github.com/coreos/flannel/raw/master/Documentation/kube-flannel.yml` <br />


9. Use the copied command from kubeadm create on the **worker nodes** to join this cluster- <br />
`kubeadm join <api-adverstise-ip>:6443 --token <copied-token>  --discovery-token-ca-cert-hash <copied-hash-...sha256:>` <br />

10. Verify all nodes are connected and ready (this could take 1-2 minutes)- <br />
`kubectl get nodes` <br />

11. Create a namespace sock-shop- <br />
`kubectl create namespace sock-shop` <br />




**Installing Istio-**
This follows the official documentation to install istio.

1. Download Istio- <br />
`curl -L https://istio.io/downloadIstio | sh -` <br />

2. Swicth to Istio directory and export global variables for the shell to use istioctl- <br />
`cd istio-1.8.1` <br />
`export PATH=$PWD/bin:$PATH` <br />

3. Install the demo configuration profile of Istio (if you want different profiles, explore at https://istio.io/latest/docs/setup/additional-setup/config-profiles/ )- <br />
`istioctl install --set profile=demo -y` <br />

4. Enable automatic sidecar injnection for the namespace sock-shop and default- <br />
`kubectl label namespace default istio-injection=enabled` <br />
`kubectl label namespace sock-shop istio-injection=enabled` <br />


**Deploying the sockshop application-**
This mostly follows documentation, but has modified manifest files in a local forked repository

1. Clone the manifest files in the desired folder <br />
`git clone https://github.com/nmengar/microservices-demo.git`

2. Go the the deployment folder <br />
`cd microservices-demo/deploy/kubernetes/`

3. Deploy the application <br />
`kubectl apply -f complete-demo.yml`

4. Check if the deployment work with istio <br />
`istioctl analyze -n sock-shop`


# References <br />
1. Setting up the Kubernetes Cluster - https://www.tecmint.com/install-kubernetes-cluster-on-centos-7/
2. Setting up Istio - https://istio.io/latest/docs/setup/getting-started/
3. Modified manifest files - https://github.com/nmengar/microservices-demo
