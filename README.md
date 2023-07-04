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
