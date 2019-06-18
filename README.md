# kubernetes-python-example
This repo backs a Medium post which outlines how one could run a kubernetes job using the python client library


##1 Create ServiceAccount and RBAC
`kubectl apply -f ./rbac`

##2 Fetch credentials
We need to fetch credentials to access Kubernetes cluster

Set the `HOST_URL` environmental variable to the result (https://x.x.x.x) from running:

`kubectl cluster-info | grep 'Kubernetes master' | awk '/http/ {print $NF}'`

Set the `CACERT` environmental variable to the result from running:

`kubectl -n default get secrets job-manager-token- xxxx -o jsonpath="{['data']['ca\.crt']}"`

Set the `TOKEN` environmental variable to the result from running:

`kubectl get secrets job-manager-token- xxxx -o jsonpath={.data.token} | base64 -d`
