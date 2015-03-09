"""Helper methods for working with containers in config."""

import yaml


def GenerateManifest(context):
  """Generates a Container Manifest given a Template context.

  Args:
    context: Template context, which must contain dockerImage and port
        properties, and an optional dockerEnv property.

  Returns:
    A Container Manifest as a YAML string.
  """
  env = ""
  env_list = []
  if "dockerEnv" in context.properties:
    for key, value in context.properties["dockerEnv"].iteritems():
      env_list.append({"name": key, "value": value})
  if env_list:
    env = "env: " + yaml.dump(env_list, default_flow_style=True)

  return """\
version: v1beta2
containers:
  - name: %(name)s
    image: %(dockerImage)s
    ports:
      - name: %(name)s-port
        hostPort: %(port)i
        containerPort: %(port)i
    %(env)s
""" % {"name": context.env["name"],
       "dockerImage": context.properties["dockerImage"],
       "port": context.properties["port"],
       "env": env}

