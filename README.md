# How to set up Ollama?

_This is a support material for presentation about Ollama. It should not be considered as any kind of documentation._

## What is Ollama?

Ollama (https://ollama.ai/) is a package allowing for quick and easy experiments with open source Large and Small Language Models. It is distributed based on MIT License making it perfect tool for comercial projects. 

The list of models available in Ollama include Llama 2, Mistral, Mixtral, Phi, Orca 2, Llava and many others. The complete list of available models can be found here: https://ollama.ai/library

## How to install Ollama in WSL?

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


