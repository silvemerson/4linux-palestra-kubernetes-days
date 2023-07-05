# Kubernetes Days - Deploy no Kubernetes com GitLab CI

## whaomi

**Emerson Silva**

Atuo como DevOps Engineer,  possuo experiência em Administração de Sistemas Open Source, Virtualização, Cloud e ferramentas voltadas a práticas DevOps, com ênfase em IaC e CI/CD. 
Atuando há 6 anos na área de Tecnologia da Informação.
Detenho expertise como instrutor de cursos voltados para Containers, Infraestrutura Ágile CI/CD.

- **Certificações**
  - GitLab Associate
  - Scrum Essentials
  - DevOps Essentials
  - AWS Certified Cloud Practitioner

Mais sobre mim: [https://linktr.ee/silvemerson](https://linktr.ee/silvemerson)

# Roteiro da Palestra

- [Pré-requisitos para Live](#pré-requisitos-para-live)
  - [Criando Infra](#criando-infra)
  - [Nginx](#nginx)
  - [SonarQube](#sonarqube)
  - [Gitlab Runner](#gitlab-runner)
  - [GCP Service Account](#gcp-service-account)
- [O que é Kubernetes](#o-que-é-o-kubernetes)
- [O que é o GitLab](#o-que-é-o-gitlab)
- [Continuous Integration e Continuous Delivery/Deployment](#ci-continuous-integration-e-cd-continuous-deliverydeployment)
   - [Continuous Integration](#continuous-integration-integração-contínua)
   - [Continuous Delivery](#continuous-delivery-entrega-contínua)
   - [O que é uma Pipeline](#o-que-é-uma-pipeline)
   - [O que são Teste Unitários](#o-que-são-teste-unitários)
   - [O que é o Gitlab Runner](#o-que-é-o-gitlab-runner)


## Pré-requisitos para Live

### Criando Infra

[Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) 

```git clone https://github.com/silvemerson/infra-gke-terraform.git```

```cd infra-gke-terraform```

```terraform init```

```terraform validate```

```terraform apply```


### Nginx

```helm repo add nginx-stable https://helm.nginx.com/stable```

```kubectl create namespace ingress-nginx```

```helm install nginx-control nginx-stable/nginx-ingress -n ingress-nginx```

```export NGINX_INGRESS_IP=$(kubectl -n ingress-nginx get service nginx-control-nginx-ingress-controller -o json | jq -r '.status.loadBalancer.ingress[].ip')```

```echo $NGINX_INGRESS_IP``` 


### SonarQube

Insira o valor do em IP no arquivo ```sonarqube/sonarqube-values.yaml``` em Ingress. 

exemplo:

```
ingress:
  enabled: true
  # Used to create an Ingress record.
  hosts:
    - name: sonarqube.34-170-148-91.nip.io
      # Different clouds or configurations might need /* as the default path
      path: /

```


```
helm repo add sonarqube https://SonarSource.github.io/helm-chart-sonarqube
helm repo update
kubectl create namespace sonarqube
helm install -n sonarqube sonarqube sonarqube/sonarqube -f sonarqube/sonarqube-values.yaml

```

### Gitlab Runner

```kubectl create namespace runner```

```helm install -n runner gitlab-runner -f runner/gitlab-runner-values.yaml gitlab/gitlab-runner --version 0.41.0```


### GCP Service Account

IAM > Conta de Serviço > Criar conta > concenter permissão > Gerar chave .json


### Variables GitLab


```
DOCKER_HUB_IMAGE: silvemerson/course_catalog

DOCKER_HUB_PASSWORD: dckr_pat_fL9JQ7yYC4LTbJXFUjhkaSS2UjA

DOCKER_HUB_REGISTRY: https://index.docker.io/v1/

DOCKER_HUB_USER: silvemerson

SERVICE_ACCOUNT_KEY: 

```

## O que é o Kubernetes

Kubernetes, também conhecido como K8s, é uma plataforma de código aberto para orquestração de contêineres. Ele foi desenvolvido pelo Google e agora é mantido pela Cloud Native Computing Foundation (CNCF). O Kubernetes facilita a automação, o dimensionamento e a implantação de aplicativos em contêineres.

Um contêiner é uma unidade leve e isolada de software que inclui tudo o que é necessário para executar um aplicativo, como código, dependências e configurações. O Kubernetes fornece um ambiente para gerenciar e executar esses contêineres em escala, oferecendo recursos avançados de orquestração.


## O que é o GitLab

O GitLab é uma plataforma de gerenciamento de código-fonte baseada em Git. Ele oferece recursos de controle de versão distribuído, permitindo que desenvolvedores trabalhem em equipe e colaborem em projetos de software. O GitLab é semelhante ao GitHub em muitos aspectos, mas possui algumas diferenças e vantagens distintas.

O GitLab fornece um ambiente completo para o desenvolvimento de software, que inclui recursos como rastreamento de problemas, integração contínua, entrega contínua e um sistema de registro de contêiner integrado. Ele permite que os desenvolvedores hospedem repositórios de código-fonte, acompanhem as alterações no código, gerenciem problemas e solicitações de fusão, automatizem a compilação e os testes de código, além de implantarem o software resultante.

Uma das principais diferenças entre o GitLab e o GitHub é a disponibilidade de diferentes opções de implantação. O GitLab pode ser executado em nuvem como um serviço hospedado, onde o próprio GitLab gerencia a infraestrutura, ou pode ser instalado em um servidor local ou privado para maior controle e segurança.

Além disso, o GitLab é uma solução de código aberto, o que significa que você pode ter acesso ao código-fonte do GitLab e até mesmo contribuir para o seu desenvolvimento. Isso é especialmente útil para empresas que desejam ter controle total sobre sua infraestrutura de desenvolvimento de software.

No geral, o GitLab é uma plataforma poderosa para colaboração e gerenciamento de projetos de desenvolvimento de software, com uma ampla gama de recursos que ajudam a melhorar a produtividade e a qualidade do trabalho em equipe.

## CI (Continuous Integration) e CD (Continuous Delivery/Deployment)

CI (Continuous Integration) e CD (Continuous Delivery/Deployment) são práticas de desenvolvimento de software que visam automatizar e agilizar o processo de construção, teste e implantação de aplicativos.
### Continuous Integration (Integração Contínua):

A Integração Contínua envolve a integração frequente e automatizada do código-fonte de vários desenvolvedores em um repositório compartilhado. O objetivo é detectar problemas de integração o mais cedo possível, garantindo que o código seja sempre testado e integrado com sucesso. Com a Integração Contínua, os desenvolvedores mesclam seu código com frequência e acionam automaticamente um processo de build e testes para verificar a integridade do sistema. Isso ajuda a identificar e corrigir problemas rapidamente, melhorando a qualidade do software.

### Continuous Delivery (Entrega Contínua):

A Implantação Contínua vai um passo além da Entrega Contínua, automatizando completamente o processo de implantação em produção. Com a Implantação Contínua, todas as etapas de build, testes e implantação são executadas automaticamente, e o software é implantado em produção sem intervenção manual. Essa abordagem permite que as mudanças sejam lançadas com mais rapidez, pois não há a necessidade de intervenção manual em cada implantação.

Em resumo, a Integração Contínua se concentra na integração e teste frequente do código, enquanto a Entrega Contínua visa garantir que o software esteja sempre pronto para implantação em um ambiente de produção. Já a Implantação Contínua automatiza completamente o processo de implantação em produção, permitindo um fluxo contínuo e rápido de mudanças. Essas práticas são fundamentais para a cultura DevOps, promovendo a colaboração entre equipes de desenvolvimento e operações e acelerando a entrega de software de qualidade.


### O que é uma Pipeline

Um pipeline é composto por uma série de estágios, onde cada estágio executa uma tarefa específica no processo de desenvolvimento de software. Esses estágios podem incluir:

Build (Construção): Nesta etapa, o código-fonte é compilado e os artefatos resultantes, como arquivos binários ou pacotes, são gerados. Isso envolve a compilação, empacotamento e organização do código em uma forma executável.

Test (Teste): Esta etapa envolve a execução de testes automatizados para verificar a qualidade e o funcionamento correto do software. Os testes podem incluir testes unitários, testes de integração, testes de aceitação e outros tipos de testes automatizados.

Deploy (Implantação): Nesta fase, o software é implantado em um ambiente de destino, como um ambiente de teste, pré-produção ou produção. Isso pode envolver a configuração de servidores, a instalação de dependências e a implantação dos artefatos gerados nas etapas anteriores.

Release (Liberação): Este estágio envolve a finalização da implantação do software em um ambiente de produção, tornando-o disponível para os usuários finais. Isso pode incluir a atualização de bancos de dados, a configuração de servidores de produção e a configuração de DNS, entre outras tarefas.

Os pipelines são executados de forma automatizada, geralmente usando ferramentas de integração contínua e entrega contínua (CI/CD), como Jenkins, GitLab CI/CD, Travis CI, CircleCI, entre outras. 


## O que são Teste Unitários

Testes unitários são uma prática de teste de software em que partes individuais e isoladas de um programa, chamadas de unidades, são testadas de forma independente. O objetivo dos testes unitários é garantir que cada unidade do código (como uma função, método ou classe) funcione corretamente e produza os resultados esperados.

## O que é o Gitlab Runner

O GitLab Runner é um componente essencial do GitLab CI/CD. É um agente de execução que executa as tarefas de construção, testes e implantação definidas nos arquivos de configuração do GitLab CI/CD. O Runner permite automatizar e executar pipelines de integração contínua e entrega contínua definidos no GitLab.

