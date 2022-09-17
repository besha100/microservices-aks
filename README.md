<p align="center">
<img src="src/frontend/static/icons/Hipster_HeroLogoCyan.svg" width="300"/>
</p>
Demo: Build, deploy and run a microservices-based online boutique application using Pulumi, Helm, and Istio.


# The Application:

**Online Boutique** is a cloud-native microservices demo application.
Online Boutique consists of a 11-tier microservices application. The application is a
web-based e-commerce app where users can browse items,
add them to the cart, and purchase them.

The Demo Application source code is provided by the Google Cloud team, and I will use it to demonstrate technologies like
Kubernetes and Istio.

## Screenshots

| Home Page                                                                                                         | Checkout Screen                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| [![Screenshot of store homepage](docs/img/online-boutique-frontend-1.png)](docs/img/online-boutique-frontend-1.png) | [![Screenshot of checkout screen](docs/img/online-boutique-frontend-2.png)](docs/img/online-boutique-frontend-2.png) |

## Service Architecture

**Online Boutique** is composed of many microservices written in different
languages that talk to each other over gRPC.

[![Architecture of
microservices](docs/img/architecture-diagram.png)](docs/img/architecture-diagram.png)