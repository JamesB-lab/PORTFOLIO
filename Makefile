AWS_ACCOUNT := 714533746634
AWS_REGION := eu-west-2
IMAGE_REGISTRY := ${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com
IMAGE_NAME := portfolio

.PHONY: setup-python-env
setup-python-env:
	python3 -m pip install pipenv
	python3 -m pipenv install

.PHONY: generate-django-secret-key
generate-django-secret-key:
	@python3 generate_secret_key.py

.PHONY: read-private-key
read-private-key:
	@python3 read_private_key.py

.PHONY: upload-config-secret
upload-config-secret:
	aws secretsmanager put-secret-value \
    --secret-id portfolio.prod \
    --secret-string file://config.json

.PHONY: check
check:
	python3 manage.py check --fail-level WARNING

.PHONY: collectstatic
collectstatic:
	python3 manage.py collectstatic --verbosity 2 --no-input

.PHONY: serve-dev
serve-dev:
	python manage.py runserver

.PHONY: serve-prod
serve-prod: check
	gunicorn \
		-b 127.0.0.1:8000 \
		--workers 2 \
		--log-level debug \
		config.wsgi

.PHONY: docker-build
docker-build:
	docker build -t ${IMAGE_NAME}:local .

.PHONY: docker-run
docker-run: docker-build
	docker run \
		-e CONFIG="$$(cat config.json)" \
		--rm \
		-it \
		-p 8000:8000 \
		${IMAGE_NAME}:local

.PHONY: docker-shell
docker-shell: docker-build
	docker run \
		-e CONFIG="$$(cat config.json)" \
		--rm \
		-it \
		--entrypoint=/bin/sh \
		${IMAGE_NAME}:local

.PHONY: docker-push
docker-push: docker-build
	aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${IMAGE_REGISTRY}
	docker tag ${IMAGE_NAME}:local ${IMAGE_REGISTRY}/${IMAGE_NAME}:latest
	docker push ${IMAGE_REGISTRY}/${IMAGE_NAME}:latest
