#% description: Creates an Instance Template running the specified Docker image.
#% parameters:
#% - name: dockerImage
#%   type: string
#%   description: Name of the Docker image to run (e.g., username/mysql).
#%   required: true
#% - name: port
#%   type: int
#%   description: Port to expose on the container as well as on the load
#%     balancer (e.g., 8080).
#%   required: false
#% - name: containerImage
#%   type: string
#%   description: Image of the container to run the container in (for example)
#%     container-vm-v20140826
#%     If omitted, defaults to: container-vm-v20140826
#%   required: false
#% - name: dockerEnv
#%   type: map
#%   description: Map of key-value pairs that will be exported to container
#%     as env variables.
#%   required: false

"""Creates a Container VM with the provided Container manifest."""

from container_helper import GenerateManifest
import yaml


def GenerateConfig(context):
  # Loading the container manifest into a YAML object model so that it will be
  # serialized as a single JSON-like object when converted to string.
  manifest = yaml.load(GenerateManifest(context))

  return """
resources:
  - name: %(name)s-it
    type: compute.v1.instanceTemplate
    properties:
      project: %(project)s
      properties:
        metadata:
          items:
            - key: google-container-manifest
              value: "%(manifest)s"
        machineType: f1-micro
        disks:
        - deviceName: boot
          boot: true
          autoDelete: true
          mode: READ_WRITE
          type: PERSISTENT
          initializeParams:
            sourceImage: https://www.googleapis.com/compute/v1/projects/google-containers/global/images/%(containerImage)s
        networkInterfaces:
          - accessConfigs:
            - name: external-nat
              type: ONE_TO_ONE_NAT
            network: https://www.googleapis.com/compute/v1/projects/%(project)s/global/networks/default
""" % {"name": context.env["name"],
       "project": context.env["project"],
       "containerImage": context.properties["containerImage"],
       "manifest": manifest}