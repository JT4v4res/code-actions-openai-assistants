from openai import OpenAI
import traceback
import json


def get_thread_length(client: OpenAI, thread_id: str) -> int:
    """
        Get the number of messages in a specified thread.

        Args:
            :param client: An instance of the OpenAI client.
            :param thread_id: The ID of the thread to retrieve messages from.

        Returns:
            The number of messages in the thread.
    """
    # List messages in the thread
    response = client.beta.threads.messages.list(thread_id=thread_id)

    # Get the number of messages
    return len(response.data)


def Run(engine):
    thread_id = engine.params.get('thread_id')
    openai_api_key = engine.params.get('openai_api_key')

    client = OpenAI(api_key=openai_api_key)

    try:
        thread_length = get_thread_length(client, thread_id=thread_id)
        engine.result.set(json.dumps({"thread_length": thread_length}, indent=4), status_code=200, content_type='json')
    except Exception as e:
        engine.log.error(f"Can't get the length of thread: {e}")
        engine.log.error(traceback.format_exc())
        engine.result.set(json.dumps({"error": str(e)}, indent=4), status_code=500, content_type='json')
