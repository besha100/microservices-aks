"""A Kubernetes Python Pulumi program"""

from argparse import Namespace
from pulumi_kubernetes.helm.v3 import Chart, ChartOpts, FetchOpts

addons = [
        {
            "name": "istio_base",
            "chart": "base",
            "namespace": "istio-system",
            "url": "https://istio-release.storage.googleapis.com/charts"
        },
        {
            "name": "istio_istiod",
            "chart": "istiod",
            "namespace": "istio-system",
            "url": "https://istio-release.storage.googleapis.com/charts"
        },
        {
            "name": "istio_ingress",
            "chart": "gateway",
            "namespace": "istio-ingress",
            "url": "https://istio-release.storage.googleapis.com/charts"
        },
        {
            "name": "argo_cd",
            "chart": "argo-cd",
            "namespace": "argo-cd",
            "url": "https://argoproj.github.io/argo-helm"
        },
        {
            "name": "argo_rollouts",
            "chart": "argo-rollouts",
            "namespace": "argo-rollouts",
            "url": "https://argoproj.github.io/argo-helm"
        },
        {
            "name": "prometheus",
            "chart": "prometheus",
            "namespace": "prometheus",
            "url": "https://prometheus-community.github.io/helm-charts"
        }
    ]


for app in addons:
    app["name"] = Chart(
        app["chart"],
        ChartOpts(
            chart=app["chart"],
            namespace=app["namespace"],
            fetch_opts=FetchOpts(
                repo=app["url"],
            ),
        ),
    )
