from kubernetes import client
import base64
from tempfile import NamedTemporaryFile
import os
import yaml
from os import path


def main():
    try:
        host_url = os.environ["HOST_URL"]
        cacert = os.environ["CACERT"]
        token = os.environ["TOKEN"]

        # Set the configuration
        configuration = client.Configuration()
        with NamedTemporaryFile(delete=False) as cert:
            cert.write(base64.b64decode(cacert))
            configuration.ssl_ca_cert = cert.name
        configuration.host = host_url
        configuration.verify_ssl = True
        configuration.debug = False
        configuration.api_key = {"authorization": "Bearer " + token}
        client.Configuration.set_default(configuration)

        # Prepare all the required properties in order to run the create_namespaced_job method
        # https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/BatchV1Api.md#create_namespaced_job
        v1 = client.BatchV1Api()
        with open(path.join(path.dirname(__file__), "job.yaml")) as f:
            body = yaml.safe_load(f)

        v1.create_namespaced_job(namespace="default", body=body, pretty=True)

        return f'Job created successfully', 200

    except Exception as e:
        return str(e), 500


if __name__ == '__main__':
    main()
