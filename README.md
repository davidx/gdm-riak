# gdm-riak
Initial test example using google deployment manager to manage a riak cluster.
Based on documentation example.

# Status
This is still a work in progress. 


# Setup

```
gcloud preview dm-v2 deployments create riak-cluster-test --config riak.yaml 
```

# Credits

* Hector Castro for his great work creating the hectcastro/riak docker image.
 https://registry.hub.docker.com/u/hectcastro/riak/

* Google Cloud Docs https://cloud.google.com/deployment-manager/create-advanced-deployment

