# Phoenix-Capstone

    ****** Documented at ease for ease of use :) Happy Learning! ******

# Create Virtual Environment

    python3 -m venv ~/.capstone

# Activate Virtual Environment and Install dependencies

    source ~/.capstone/bin/activate

    pip install flask gunicorn

# Create Flask Application

    from flask import Flask

    def create_app(name: str = 'Hanish Arora'):
    app = Flask(__name__)

        @app.route("/")
        def index():
            return f"Hello World, This is sample application deployed by {name} for Udacity DevOps Capstone! Happy Coding!"

        return app

# Run Application

    # Development Environment

        export FLASK_APP="app:create_app"

        flask run --reload              # With reloading capability without having to re-run app each time after deploying new changes!!!

    # Production Environment

        gunicorn -w 1 --reload -b localhost:5000 "app:create_app(name='Hanish Arora')"

# Add Dependencies

    Add flask/gunicorn dependencies in requirements.txt

    # cat requirements.txt should look like below

        flask
        gunicorn

# Create Dockerfile

    FROM python:3.7.3-stretch

    # Working Directory
    WORKDIR /app

    # Copy source code to working directory
    COPY . app.py /app/

    # Install packages from requirements.txt
    RUN pip install --no-cache-dir 'pip<12' &&\
        pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

    # Expose port 80
    EXPOSE 80

    # Run gunicorn at container launch
    CMD ["gunicorn", "-b", "0.0.0.0:80", "app:create_app(name='Hanish Arora')"]

# Create Makefile

    #Created to Install Dependecies and Lint Dockerfile

    install:
    # This should be run from inside a virtualenv
    	pip install --upgrade pip &&\
        	pip install -r requirements.txt

    lint:
        hadolint Dockerfile
        pylint --disable=R,C,W1203,W1202 app.py

    all: install lint test

# Install Dependencies

    output to install should look like below:

    (.capstone) bash-3.2$ make install
    # This should be run from inside a virtualenv
    pip install --upgrade pip &&\
                    pip install -r requirements.txt
    Requirement already satisfied: pip in /Users/hunny/.capstone/lib/python3.7/site-packages (21.3.1)
    Collecting flask
    Using cached Flask-2.0.2-py3-none-any.whl (95 kB)
    Collecting gunicorn
    Using cached gunicorn-20.1.0-py3-none-any.whl (79 kB)
    Requirement already satisfied: itsdangerous>=2.0 in /Users/hunny/.capstone/lib/python3.7/site-packages (from flask->-r requirements.txt (line 1)) (2.0.1)
    Requirement already satisfied: Jinja2>=3.0 in /Users/hunny/.capstone/lib/python3.7/site-packages (from flask->-r requirements.txt (line 1)) (3.0.3)
    Requirement already satisfied: Werkzeug>=2.0 in /Users/hunny/.capstone/lib/python3.7/site-packages (from flask->-r requirements.txt (line 1)) (2.0.2)
    Requirement already satisfied: click>=7.1.2 in /Users/hunny/.capstone/lib/python3.7/site-packages (from flask->-r requirements.txt (line 1)) (8.0.3)
    Requirement already satisfied: setuptools>=3.0 in /Users/hunny/.capstone/lib/python3.7/site-packages (from gunicorn->-r requirements.txt (line 2)) (40.8.0)
    Requirement already satisfied: importlib-metadata in /Users/hunny/.capstone/lib/python3.7/site-packages (from click>=7.1.2->flask->-r requirements.txt (line 1)) (4.10.0)
    Requirement already satisfied: MarkupSafe>=2.0 in /Users/hunny/.capstone/lib/python3.7/site-packages (from Jinja2>=3.0->flask->-r requirements.txt (line 1)) (2.0.1)
    Requirement already satisfied: zipp>=0.5 in /Users/hunny/.capstone/lib/python3.7/site-packages (from importlib-metadata->click>=7.1.2->flask->-r requirements.txt (line 1)) (3.7.0)
    Requirement already satisfied: typing-extensions>=3.6.4 in /Users/hunny/.capstone/lib/python3.7/site-packages (from importlib-metadata->click>=7.1.2->flask->-r requirements.txt (line 1)) (4.0.1)
    Installing collected packages: gunicorn, flask
    Successfully installed flask-2.0.2 gunicorn-20.1.0

# Lint Dockerfile

    output to lint should look like below:

    (.capstone) bash-3.2$ make lint
    hadolint Dockerfile
    pylint --disable=R,C,W1203,W1202 app.py

    --------------------------------------------------------------------
    Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

# Build Docker Image

    docker build --tag=phoenix .

# Run Container locally in bash

    docker run -it phoenix bash

    nohup flask run &

    curl http://127.0.0.1:5000/ to ensure application is responding.

    Outout should look like below:
        root@ebdb876e883b:/app# curl http://127.0.0.1:5000/
        Hello World, This is sample application deployed by Hanish Arora for Udacity DevOps Capstone! Happy Coding!root@ebdb876e883b:/app#

# Run Container Locally

    bash-3.2$ nohup docker run -p 8000:80 phoenix &

    bash-3.2$ curl http://localhost:8000/
    Hello World, This is sample application deployed by Hanish Arora for Udacity DevOps Capstone! Happy Coding!

# Check if Container is running

    bash-3.2$ docker ps
    CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS        PORTS                  NAMES
    76532a489884   phoenix   "gunicorn -b 0.0.0.0???"   2 seconds ago   Up 1 second   0.0.0.0:8000->80/tcp   lucid_chaplygin

# Stop Container

    docker stop 76532a489884

# Push Repository to Docker Hub

    --> Authenticate & tag

    docker login --username=hanisharora
    docker tag phoenix hanisharora/phoenix

    --> Push image to a docker repository

    docker push hanisharora/phoenix

# Create Kubernetes Cluster Locally

    bash-3.2$ eksctl create cluster --name=phoenix --region=us-west-2 --without-nodegroup --profile phoenix
    2022-01-04 21:56:41 [???]  eksctl version 0.77.0
    2022-01-04 21:56:41 [???]  using region us-west-2
    2022-01-04 21:56:42 [???]  setting availability zones to [us-west-2c us-west-2a us-west-2d]
    2022-01-04 21:56:42 [???]  subnets for us-west-2c - public:192.168.0.0/19 private:192.168.96.0/19
    2022-01-04 21:56:42 [???]  subnets for us-west-2a - public:192.168.32.0/19 private:192.168.128.0/19
    2022-01-04 21:56:42 [???]  subnets for us-west-2d - public:192.168.64.0/19 private:192.168.160.0/19
    2022-01-04 21:56:42 [???]  using Kubernetes version 1.21
    2022-01-04 21:56:42 [???]  creating EKS cluster "phoenix" in "us-west-2" region with
    2022-01-04 21:56:42 [???]  if you encounter any issues, check CloudFormation console or try 'eksctl utils describe-stacks --region=us-west-2 --cluster=phoenix'
    2022-01-04 21:56:42 [???]  CloudWatch logging will not be enabled for cluster "phoenix" in "us-west-2"
    2022-01-04 21:56:42 [???]  you can enable it with 'eksctl utils update-cluster-logging --enable-types={SPECIFY-YOUR-LOG-TYPES-HERE (e.g. all)} --region=us-west-2 --cluster=phoenix'
    2022-01-04 21:56:42 [???]  Kubernetes API endpoint access will use default of {publicAccess=true, privateAccess=false} for cluster "phoenix" in "us-west-2"
    2022-01-04 21:56:42 [???]
    2 sequential tasks: { create cluster control plane "phoenix", wait for control plane to become ready
    }
    2022-01-04 21:56:42 [???]  building cluster stack "eksctl-phoenix-cluster"
    2022-01-04 21:56:45 [???]  deploying stack "eksctl-phoenix-cluster"
    2022-01-04 21:57:15 [???]  waiting for CloudFormation stack "eksctl-phoenix-cluster"
    2022-01-04 21:57:46 [???]  waiting for CloudFormation stack "eksctl-phoenix-cluster"
    2022-01-04 21:58:48 [???]  waiting for CloudFormation stack "eksctl-phoenix-cluster"
    2022-01-04 21:59:50 [???]  waiting for CloudFormation stack "eksctl-phoenix-cluster"
    2022-01-04 22:00:51 [???]  waiting for CloudFormation stack "eksctl-phoenix-cluster"
    2022-01-04 22:01:53 [???]  waiting for CloudFormation stack "eksctl-phoenix-cluster"
    2022-01-04 22:02:54 [???]  waiting for CloudFormation stack "eksctl-phoenix-cluster"
    2022-01-04 22:03:56 [???]  waiting for CloudFormation stack "eksctl-phoenix-cluster"
    2022-01-04 22:04:58 [???]  waiting for CloudFormation stack "eksctl-phoenix-cluster"
    2022-01-04 22:05:59 [???]  waiting for CloudFormation stack "eksctl-phoenix-cluster"
    2022-01-04 22:07:01 [???]  waiting for CloudFormation stack "eksctl-phoenix-cluster"
    2022-01-04 22:08:02 [???]  waiting for CloudFormation stack "eksctl-phoenix-cluster"
    2022-01-04 22:09:04 [???]  waiting for CloudFormation stack "eksctl-phoenix-cluster"
    2022-01-04 22:10:06 [???]  waiting for CloudFormation stack "eksctl-phoenix-cluster"
    2022-01-04 22:11:07 [???]  waiting for CloudFormation stack "eksctl-phoenix-cluster"
    2022-01-04 22:13:15 [???]  waiting for the control plane availability...
    2022-01-04 22:13:15 [???]  saved kubeconfig as "/Users/hunny/.kube/config"
    2022-01-04 22:13:15 [???]  no tasks
    2022-01-04 22:13:15 [???]  all EKS cluster resources for "phoenix" have been created
    2022-01-04 22:13:18 [???]  kubectl command should work with "/Users/hunny/.kube/config", try 'kubectl get nodes'
    2022-01-04 22:13:18 [???]  EKS cluster "phoenix" in "us-west-2" region is ready

# Create NodeGroups

    bash-3.2$ eksctl create nodegroup --cluster=phoenix --region=us-west-2 --name=phoenix-ng --node-type=t3.micro --nodes=1 --nodes-min=1 --nodes-max=1 --profile phoenix
    2022-01-04 22:24:50 [???]  eksctl version 0.77.0
    2022-01-04 22:24:50 [???]  using region us-west-2
    2022-01-04 22:24:50 [???]  will use version 1.21 for new nodegroup(s) based on control plane version
    2022-01-04 22:24:57 [???]  nodegroup "phoenix-ng" will use "" [AmazonLinux2/1.21]
    2022-01-04 22:24:59 [???]  1 nodegroup (phoenix-ng) was included (based on the include/exclude rules)
    2022-01-04 22:24:59 [???]  will create a CloudFormation stack for each of 1 managed nodegroups in cluster "phoenix"
    2022-01-04 22:25:00 [???]
    2 sequential tasks: { fix cluster compatibility, 1 task: { 1 task: { create managed nodegroup "phoenix-ng" } }
    }
    2022-01-04 22:25:00 [???]  checking cluster stack for missing resources
    2022-01-04 22:25:01 [???]  cluster stack has all required resources
    2022-01-04 22:25:01 [???]  building managed nodegroup stack "eksctl-phoenix-nodegroup-phoenix-ng"
    2022-01-04 22:25:02 [???]  deploying stack "eksctl-phoenix-nodegroup-phoenix-ng"
    2022-01-04 22:25:02 [???]  waiting for CloudFormation stack "eksctl-phoenix-nodegroup-phoenix-ng"
    2022-01-04 22:25:19 [???]  waiting for CloudFormation stack "eksctl-phoenix-nodegroup-phoenix-ng"
    2022-01-04 22:25:37 [???]  waiting for CloudFormation stack "eksctl-phoenix-nodegroup-phoenix-ng"
    2022-01-04 22:25:59 [???]  waiting for CloudFormation stack "eksctl-phoenix-nodegroup-phoenix-ng"
    2022-01-04 22:26:16 [???]  waiting for CloudFormation stack "eksctl-phoenix-nodegroup-phoenix-ng"
    2022-01-04 22:26:38 [???]  waiting for CloudFormation stack "eksctl-phoenix-nodegroup-phoenix-ng"
    2022-01-04 22:26:59 [???]  waiting for CloudFormation stack "eksctl-phoenix-nodegroup-phoenix-ng"
    2022-01-04 22:27:19 [???]  waiting for CloudFormation stack "eksctl-phoenix-nodegroup-phoenix-ng"
    2022-01-04 22:27:37 [???]  waiting for CloudFormation stack "eksctl-phoenix-nodegroup-phoenix-ng"
    2022-01-04 22:27:55 [???]  waiting for CloudFormation stack "eksctl-phoenix-nodegroup-phoenix-ng"
    2022-01-04 22:28:14 [???]  waiting for CloudFormation stack "eksctl-phoenix-nodegroup-phoenix-ng"
    2022-01-04 22:28:31 [???]  waiting for CloudFormation stack "eksctl-phoenix-nodegroup-phoenix-ng"
    2022-01-04 22:28:32 [???]  no tasks
    2022-01-04 22:28:32 [???]  created 0 nodegroup(s) in cluster "phoenix"
    2022-01-04 22:28:34 [???]  nodegroup "phoenix-ng" has 1 node(s)
    2022-01-04 22:28:34 [???]  node "******************" is ready
    2022-01-04 22:28:34 [???]  waiting for at least 1 node(s) to become ready in "phoenix-ng"
    2022-01-04 22:28:34 [???]  nodegroup "phoenix-ng" has 1 node(s)
    2022-01-04 22:28:34 [???]  node "******************" is ready
    2022-01-04 22:28:34 [???]  created 1 managed nodegroup(s) in cluster "phoenix"
    2022-01-04 22:28:36 [???]  checking security group configuration for all nodegroups
    2022-01-04 22:28:36 [???]  all nodegroups have up-to-date cloudformation templates

# Create Kubernetes Cluster with Node Groups

    eksctl create cluster \
    --name phoenix \
    --region us-west-2 \
    --version 1.19 \
    --nodegroup-name phoenix-workers \
    --node-type t2.micro \
    --nodes 2 \
    --nodes-min 1 \
    --nodes-max 2 \
    --profile phoenix

    bash-3.2$ eksctl create cluster --name phoenix --region us-west-2 --version 1.19 --nodegroup-name phoenix-workers --node-type t2.micro --nodes 2 --nodes-min 1 --nodes-max 2 --profile phoenix
    2022-01-05 09:32:06 [???]  eksctl version 0.77.0
    2022-01-05 09:32:06 [???]  using region us-west-2
    2022-01-05 09:32:08 [???]  setting availability zones to [us-west-2b us-west-2a us-west-2c]
    2022-01-05 09:32:08 [???]  subnets for us-west-2b - public:192.168.0.0/19 private:192.168.96.0/19
    2022-01-05 09:32:08 [???]  subnets for us-west-2a - public:192.168.32.0/19 private:192.168.128.0/19
    2022-01-05 09:32:08 [???]  subnets for us-west-2c - public:192.168.64.0/19 private:192.168.160.0/19
    2022-01-05 09:32:08 [???]  nodegroup "phoenix-workers" will use "" [AmazonLinux2/1.19]
    2022-01-05 09:32:08 [???]  using Kubernetes version 1.19
    2022-01-05 09:32:08 [???]  creating EKS cluster "phoenix" in "us-west-2" region with managed nodes
    2022-01-05 09:32:08 [???]  will create 2 separate CloudFormation stacks for cluster itself and the initial managed nodegroup
    2022-01-05 09:32:08 [???]  if you encounter any issues, check CloudFormation console or try 'eksctl utils describe-stacks --region=us-west-2 --cluster=phoenix'
    2022-01-05 09:32:08 [???]  CloudWatch logging will not be enabled for cluster "phoenix" in "us-west-2"
    2022-01-05 09:32:08 [???]  you can enable it with 'eksctl utils update-cluster-logging --enable-types={SPECIFY-YOUR-LOG-TYPES-HERE (e.g. all)} --region=us-west-2 --cluster=phoenix'
    2022-01-05 09:32:08 [???]  Kubernetes API endpoint access will use default of {publicAccess=true, privateAccess=false} for cluster "phoenix" in "us-west-2"
    2022-01-05 09:32:08 [???]
    2 sequential tasks: { create cluster control plane "phoenix",
        2 sequential sub-tasks: {
            wait for control plane to become ready,
            create managed nodegroup "phoenix-workers",
        }
    }
    2022-01-05 09:32:08 [???]  building cluster stack "eksctl-phoenix-cluster"
    2022-01-05 09:32:10 [???]  deploying stack "eksctl-phoenix-cluster"
    2022-01-05 09:32:40 [???]  waiting for CloudFormation stack "eksctl-phoenix-cluster"
    2022-01-05 09:46:38 [???]  building managed nodegroup stack "eksctl-phoenix-nodegroup-phoenix-workers"
    2022-01-05 09:46:40 [???]  deploying stack "eksctl-phoenix-nodegroup-phoenix-workers"
    2022-01-05 09:46:40 [???]  waiting for CloudFormation stack "eksctl-phoenix-nodegroup-phoenix-workers"
    2022-01-05 09:51:03 [???]  waiting for the control plane availability...
    2022-01-05 09:51:04 [???]  saved kubeconfig as "/Users/hunny/.kube/config"
    2022-01-05 09:51:04 [???]  no tasks
    2022-01-05 09:51:04 [???]  all EKS cluster resources for "phoenix" have been created
    2022-01-05 09:51:05 [???]  nodegroup "phoenix-workers" has 2 node(s)
    2022-01-05 09:51:05 [???]  node "**********.us-west-2.compute.internal" is ready
    2022-01-05 09:51:05 [???]  node "**********.us-west-2.compute.internal" is ready
    2022-01-05 09:51:05 [???]  waiting for at least 1 node(s) to become ready in "phoenix-workers"
    2022-01-05 09:51:05 [???]  nodegroup "phoenix-workers" has 2 node(s)
    2022-01-05 09:51:05 [???]  node "**********.us-west-2.compute.internal" is ready
    2022-01-05 09:51:05 [???]  node "**********.us-west-2.compute.internal" is ready
    2022-01-05 09:51:08 [???]  kubectl command should work with "/Users/hunny/.kube/config", try 'kubectl get nodes'
    2022-01-05 09:51:08 [???]  EKS cluster "phoenix" in "us-west-2" region is ready

# Check Nodes

    bash-3.2$ kubectl get nodes -o wide
    NAME                                           STATUS   ROLES    AGE   VERSION               INTERNAL-IP      EXTERNAL-IP     OS-IMAGE         KERNEL-VERSION                CONTAINER-RUNTIME
    ****************.compute.internal              Ready    <none>   21m   v1.19.15-eks-9c63c4   ************     ************    Amazon Linux 2   ************                  docker://20.10.7
    ****************..compute.internal             Ready    <none>   21m   v1.19.15-eks-9c63c4   ************     ************    Amazon Linux 2   ************                  docker://20.10.7

# Get Cluster ARN Information

    bash-3.2$ Cluster_ARN=`aws cloudformation list-exports --query "Exports[?Name=='eksctl-phoenix-cluster::ARN'].Value" --no-paginate --output text --profile phoenix`
    bash-3.2$ echo $Cluster_ARN
    arn:aws:eks:us-west-2:*************:cluster/phoenix

# Set the current-context in kubeconfig

    bash-3.2$ kubectl config use-context $Cluster_ARN
    Switched to context "arn:aws:eks:us-west-2:**************:cluster/phoenix".

# Configures kubectl to connect to an Amazon EKS cluster - Required if already exists another cluster

    bash-3.2$ aws eks update-kubeconfig --name phoenix --profile phoenix
    Updated context arn:aws:eks:us-west-2:**************:cluster/phoenix in /Users/hunny/.kube/config

# Check Current Set Context

    bash-3.2$ kubectl config current-context
    arn:aws:eks:us-west-2:**************:cluster/phoenix

# Check Pods

    bash-3.2$ kubectl get pods
    No resources found in default namespace.

# Deploy Application

    bash-3.2$ kubectl apply -f deploy.yml
    deployment.apps/phoenix created

    bash-3.2$ kubectl rollout status deployment/phoenix
    deployment "phoenix" successfully rolled out

    bash-3.2$ kubectl apply -f service.yml
    service/phoenix created

# Test Accessibility

    bash-3.2$ kubectl get svc -o wide
    NAME         TYPE           CLUSTER-IP       EXTERNAL-IP                                                              PORT(S)        AGE   SELECTOR
    kubernetes   ClusterIP      *.*.*.*          <none>                                                                   443/TCP        32m   <none>
    phoenix      LoadBalancer   *.*.*.*          **********.us-west-2.elb.amazonaws.com                                   80:32237/TCP   14s   app=phoenix

    bash-3.2$ LoadBalancerHostName=`kubectl get svc phoenix -o jsonpath="{.status.loadBalancer.ingress[*].hostname}"`

    bash-3.2$ echo $LoadBalancerHostName
    **********.us-west-2.elb.amazonaws.com

    bash-3.2$ curl ${LoadBalancerHostName}:80
    Hello World, This is sample application deployed by Hanish Arora for Udacity DevOps Capstone! Happy Coding!





                        ###############################     CIRCLE CI EVERYTHING     ###############################

# Add CirlceCI

    -- Create .circle directory in project root directory

    mkdir .circleci

    -- Create config.yml in .circleci directory

    touch config.yml

    Create CircleCI Project from your Github Repository

# Establish AWS/CI Communication

    -- ADD Below AWS Properties in CIRCLE CI Project Environment Variables

    AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY
    AWS_DEFAULT_REGION

    You can find these at below location

    ~/.aws/credentials

# Establish CI/Docker Communication

    -- ADD Below Credentials in CIRCLE CI Project Environment Variables

    DOCKER_USER
    DOCKER_PASSWORD
