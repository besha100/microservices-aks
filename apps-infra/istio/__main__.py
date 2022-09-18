import pulumi
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

# creating istiod service helm chart
istio_istiod = Chart(
    "istio-istiod",
    ChartOpts(
        chart="istiod",
        namespace="istio-system",
        fetch_opts=FetchOpts(
            repo="https://istio-release.storage.googleapis.com/charts",
        ),
    ),
    opts=pulumi.ResourceOptions(depends_on=[istio_base])
)

# creating istio ingress helm chart
istio_ingress = Chart(
    "istio-ingress",
    ChartOpts(
        chart="gateway",
        namespace="istio-ingress",
        fetch_opts=FetchOpts(
            repo="https://istio-release.storage.googleapis.com/charts",
        ),
    ),
    opts=pulumi.ResourceOptions(depends_on=[istio_istiod])
)

# creating argocd helm chart
argo_cd = Chart(
    "argo-cd",
    ChartOpts(
        chart="argo-cd",
        namespace="argo-cd",
        fetch_opts=FetchOpts(
            repo="https://argoproj.github.io/argo-helm",
        ),
    ),
)

# creating argocd rollout helm chart
argo_rollouts = Chart(
    "argo-rollouts",
    ChartOpts(
        chart="argo-rollouts",
        namespace="argo-rollouts",
        fetch_opts=FetchOpts(
            repo="https://argoproj.github.io/argo-helm",
        ),
    ),
    opts=pulumi.ResourceOptions(depends_on=[argo_cd])
)

# creating argocd rollout helm chart
prometheus = Chart(
    "prometheus-community",
    ChartOpts(
        chart="prometheus",
        namespace="prometheus",
        fetch_opts=FetchOpts(
            repo="https://prometheus-community.github.io/helm-charts",
        ),
    ),
    opts=pulumi.ResourceOptions(depends_on=[argo_rollouts])
)