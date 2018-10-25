
SHELL = /bin/bash

build:
	docker build --tag lambda:latest .
	docker run --name lambda -itd lambda:latest /bin/bash
	docker cp lambda:/tmp/package.zip package.zip
	docker stop lambda
	docker rm lambda

shell:
	docker build --tag lambda:latest .
	docker run --name docker --volume $(shell pwd)/:/data --rm -it lambda:latest /bin/bash

test:
	docker build --tag lambda:latest .
	docker run -w /var/task/ --name lambda --env PYTHONPATH=/var/task -itd lambda:latest /bin/bash
	docker exec -it lambda bash -c 'unzip -q /tmp/package.zip -d /var/task/'
	docker exec -it lambda bash -c 'pip3 install boto3 jmespath python-dateutil -t /var/task -U'
	docker exec -it lambda python3 -c 'from pyskel.handler import main; print(main(None, None))'
	docker stop lambda
	docker rm lambda

clean:
	docker stop lambda
	docker rm lambda

deploy:
	sls deploy --stage production
