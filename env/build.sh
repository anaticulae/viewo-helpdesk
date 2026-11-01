#!/usr/bin/bash

CURRENT=$(viewo_helpdesk --version)
RELEASE_TAG="${CAELUM_DOCKER_TEST}/caelum_viewo_helpdesk_release:${CURRENT}"

docker build -t $RELEASE_TAG --file Production .
