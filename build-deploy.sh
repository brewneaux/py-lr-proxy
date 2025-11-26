#!/bin/bash
set -ex
podman build . -t docker-registry.k8s.brewneaux.me/lrproxy:latest

podman push docker-registry.k8s.brewneaux.me/lrproxy:latest

cd helm/lr-proxy

helm upgrade -i -n lrproxy lrproxy .
