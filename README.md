# Microservice Tutorial

## Server (Python & Java Producer)

Theoretically the producers publish an API which allows web-users to upload images into a directory. In our case the directory is shared between the microservice and the server.

## Image Editor (Consumer)

Via RabbitMQ the microservice gets the path of the user-uploaded image and edits it.

## Examples

<p float="left">
    <img src="/shared-data/mntn.jpg" alt="Mountain Original" width="300"/>
    <img src="/shared-data/mntn_center.jpg" alt="Mountain Edited" width="300"/>
</p>

<p float="left">
    <img src="/shared-data/geko.jpg" alt="Geko Original" width="300"/>
    <img src="/shared-data/geko_center.jpg" alt="Geko Edited" width="300"/>
</p>