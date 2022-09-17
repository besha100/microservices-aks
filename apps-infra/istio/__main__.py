from pulumi_kubernetes.helm.v3 import Chart, ChartOpts, FetchOpts

# creating istio base helm chart
istio_base = Chart(
    "istio-base",
    ChartOpts(
        chart="base",
        namespace="istio-system",
        fetch_opts=FetchOpts(
            repo="https://istio-release.storage.googleapis.com/charts",
        ),
        values={
            "global": {
                "istioNamespace": "istio-system",
            },
        },
    ),
)

# creating istio.baser helm chart
istio_ingress = Chart(
    "istio-ingress",
    ChartOpts(
        chart="gateway",
        namespace="istio-ingress",
        fetch_opts=FetchOpts(
            repo="https://istio-release.storage.googleapis.com/charts",
        ),
    ),
)