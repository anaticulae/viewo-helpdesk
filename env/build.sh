#!/usr/bin/bash

CURRENT=$(admin_helpdesk --version)
RELEASE_TAG="${CAELUM_DOCKER_TEST}/caelum_admin_helpdesk_release:${CURRENT}"

docker build -t $RELEASE_TAG --file Production .
