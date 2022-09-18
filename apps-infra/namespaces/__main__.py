import pulumi_kubernetes as kubernetes

# Create app-infra K8s namespaces.
istio_namespace = kubernetes.core.v1.Namespace(
    "istio-system",
    metadata={
        "name": "istio-system",
    })

istioingress_namespace = kubernetes.core.v1.Namespace(
    "istio-ingress",
    metadata={
        "name": "istio-ingress",
    })

argocd_namespace = kubernetes.core.v1.Namespace(
    "argo-cd",
    metadata={
        "name": "argo-cd",
    })

apps_namespace = kubernetes.core.v1.Namespace(
    "boutique-apps",
    metadata={
        "name": "boutique-apps",
        "labels": { "istio-injection": "true" }
    })


rollouts_namespace = kubernetes.core.v1.Namespace(
    "argo-rollouts",
    metadata={
        "name": "argo-rollouts",
    })

prometheus_namespace = kubernetes.core.v1.Namespace(
    "prometheus",
    metadata={
        "name": "prometheus",
    })
    