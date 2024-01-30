# How to set up Ollama?

_This is a support material for presentation about Ollama. It should not be considered as any kind of documentation._

## What is Ollama?

Ollama (https://ollama.ai/) is a package allowing for quick and easy experiments with open source Large and Small Language Models. It is distributed based on MIT License making it perfect tool for comercial projects. 

The list of models available in Ollama include Llama 2, Mistral, Mixtral, Phi, Orca 2, Llava and many others. The complete list of available models can be found here: https://ollama.ai/library

## How to install Ollama?

At the moment (January 2024) Ollama is available only for macOS and Linux. To use it in Windows it is necessary to install WSL and one of available Linux distributions. Examples refering to WSL given in this repository are tested in Ubuntu 22.04.3 LTS.

Ollama runs also on very limitted hardware, like Raspberry Pi 4 with 8GB of RAM with Raspberry Pi OS. Some examples in this repository refer to such setup.

General instructions for installing Ollama can be found here: https://ollama.ai/download/linux
It runs without problems both in WSL and on Raspberry Pi.

## How to set up Ollama for local usage?

To be able to use Ollama it is necessary to start Ollama server / deamon:
> ollama serve

In different environments it is related to different behaviour: 
- In Raspberry Pi OS Ollama server is set up to start automatically after reboot. It is not necessary to modify its setup or do anything more than rebooting the computer to use it.
- In WSL Ollama server does not start automatically. Moreover, it is necessary to set up 2 environment variables to make it work:
	- OLLAMA_HOST - defining the IP (and alternatively port) for Ollama server 
	- OLLAMA_ORIGINS - defining the set of IPs and URLs from which Ollama server may be called

Example setup for running Ollama locally:
> OLLAMA_HOST=0.0.0.0 
> OLLAMA_ORIGINS=*

To start Ollama server in WSL you can use the shell script *start_ollama.sh* from this repository. 
Make its copy in your home folder, change its attributes to make it runnable:
> chmod 777 start_ollama.sh

and start it in background:

> ./start_ollama.sh &

## How to download a model to Ollama?

Ollama has its own model cache, which is populated automatically when a specific model version is invoked (see below).
Sometimes it is convenient to trigger populating the cache manually, e.g. when you want to download several models
for the future use running a batch. In order to do it, you can use *ollama pull* command with a name 
or a name and a tag of the model you want to use, for instance:
> ollama pull starcoder

For the comlete list of models see: https://ollama.ai/library

Each model listed there has its own tag list, with all available version (in different sizes and for different putposes), 
for instance: https://ollama.ai/library/llama2/tags

## How to use Ollama locally from CLI?

In order to use Ollama locally it is necessary to use *ollama run* command with a name
or a name and a tag of the model you want to use, e.g.: 
> ollama run dolphin-phi:latest

After short time you will be able to write prompts for the selected model in the console. To exit ollama type:
> /bye

## How to set up Ollama to be used with API?

By default Ollama server runs on port 11434. It may be called locally or it can be exposed to a port open 
for calls from other hosts. Example Python code for calling Ollama server locally can be found 
in the file *experiment.py* in this repository. 

For complete documentation of the API see: https://github.com/ollama/ollama/blob/main/docs/api.md

Interesting details:
- It is possible to calculate embeddings from the models used. There is another endpoint in the API for that. For details see: https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings
- It is possible to bind subsequent calls into chat conversation with the model using *context* parameter. It 
is also possible to stream response as a series of JSON objects. For details see: https://github.com/ollama/ollama/blob/main/docs/api.md#parameters

## [optional] How to route trafic to Ollama server from a different port?

Doing experiments with Ollama in December 2023 I was not able to find an easy way to expose the port of Ollama 
server to other hosts to simulate a setup, in which Ollama runs on a separate host or in a container. A quick 
and dirty solution allowing for achieving such setup is to use *nginx* web server (https://nginx.org/en/). 

To install  it in Raspberry Pi OS I used the following command:
> sudo apt install nginx

Next I modified the file */etc/nginx/sites-available/default* - the server section after modification follows:

server {
        listen 80 default_server;
        listen [::]:80 default_server;
        server_name _;

        location / {
                proxy_pass http://127.0.0.1:11434;
                proxy_set_header Host $host;
	}
}
