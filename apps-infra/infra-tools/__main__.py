from pulumi_kubernetes.helm.v3 import Chart, ChartOpts, FetchOpts

infra_apps = [
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
        }
    ]


for app in infra_apps:
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