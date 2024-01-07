FROM registry.access.redhat.com/ubi9/python-311:1-41 AS base

ENV PIP_INSTALL_COMMAND="pip install"

RUN ${PIP_INSTALL_COMMAND} --upgrade pip setuptools wheel \
    && mkdir ${HOME}/.ssh \
    && touch -m 600 ${HOME}/.ssh/known_hosts \
    && ssh-keyscan github.com >> ${HOME}/.ssh/known_hosts

FROM base AS final

ARG build_branch=main

ENV BUILD_BRANCH=${build_branch}

RUN --mount=type=ssh,required=true  \
    ${PIP_INSTALL_COMMAND} git+ssh://git@github.com/{{ cookiecutter.git_username }}/{{ cookiecutter.git_repo_name }}@${BUILD_BRANCH}

EXPOSE 8080/tcp

ENTRYPOINT ["{{ cookiecutter.git_repo_name }}-cli", "start", "-p", "8080"]
