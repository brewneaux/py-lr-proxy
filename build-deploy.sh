#!/bin/bash

podman build . -t docker-registry.k8s.brewneaux.me/lrproxy:latest

podman push docker-registry.k8s.brewneaux.me

cd helm/lr-proxy

helm upgrade -i -n lrproxy lrproxy .
