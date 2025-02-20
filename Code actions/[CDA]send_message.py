from openai import OpenAI, OpenAIError
import json


def send_message(client: OpenAI, thread_id: str, assistant_id: str, content: str) -> None:
    """
        Send a message to a specified thread and trigger the assistant to respond.

        Args:
            :param client: An instance of the OpenAI client.
            :param thread_id: The ID of the thread where the message will be sent.
            :param assistant_id: The ID of the assistant that will respond to the message.
            :param content: The text content of the message to be sent.

        Returns:
            None

        This function creates a new message in the specified thread with the user's content,
        then triggers the assistant to process and respond to the message by creating and
        polling a run on that thread.
    """
    _ = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=content
    )

    _ = client.beta.threads.runs.create_and_poll(
        thread_id=thread_id,
        assistant_id=assistant_id
    )


def Run(engine):
    assistant_id = engine.params.get('assistant_id')
    openai_api_key = engine.params.get('openai_api_key')
    content = json.loads(engine.body)['content']
    thread_id = engine.params.get('thread_id')

    client = OpenAI(api_key=openai_api_key)

    try:
        engine.log.info(f'Adding message in thread: {thread_id} in assistant: {assistant_id}')

        send_message(client, thread_id=thread_id, assistant_id=assistant_id, content=content)

        engine.result.set(json.dumps({"status": "success"}), status_code=200, content_type="json")

    except OpenAIError as e:
        engine.log.error(f'Error adding message in thread: {thread_id} in assistant: {assistant_id}')
        engine.log.error(e)
        engine.result.set(json.dumps({"status": "error", "error": str(e)}), status_code=500, content_type="json")
