# OpenAI assistants

This repository contains the code for using the OpenAI assistants API
in Python. With the provided code, you can easily interact with the assistants API
and handle all the functionalities it provides, such as **messages**, **assistants** and **threads**.

## Provided codes

The repository is split between the codes used to run locally and the codes used to run
on the code actions of Weni's platform. The codes intended to be used in code actions are marked
with [CDA] in the filename.

The run locally codes are intended to be used in your local environment, and they are the ones
that you need to hardcode API keys and other sensitive information. Also, they're helpful if you 
need to test the API before deploying it to the platform.

## Functionality

The code provides the following functionalities:

1. **Messages**: Send messages to the assistant and receive the response.
2. **Create thread**: Create a new thread with the assistant.
3. **Get thread**: Get the thread information.
4. **Send message to thread**: Send a message to a specific thread.
5. **List messages**: List all the messages in a specific thread.
6. **Store cache data on drive**: Store the cache data on the drive to avoid losing it and to have history of user conversation.

## How to use

To use the code, you need to have an API key from OpenAI. You can get one by signing up on their website and registering a
credit card. After that, you can use the API key to interact with the assistant.

## How to run in code actions

1. Create a new code action in Weni's platform.
2. Copy the code from the [CDA] files and paste it into the code action.
3. Put the correct url params and body params.

Pay attention to the body params, as they are the most important part of the code. They contain the sentitive information
such as API keys and needs to be sent in the url encoded format.

## License

This code is licensed under the MIT license. Feel free to use it in your projects.