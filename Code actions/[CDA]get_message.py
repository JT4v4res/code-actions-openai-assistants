from openai import OpenAI
import json
import traceback


def get_message(client: OpenAI, thread_id: str) -> str:
    """
        Retrieve and display messages from a specified thread.

        Args:
            :param client: An instance of the OpenAI client.
            :param thread_id: The ID of the thread to retrieve messages from.

        Returns:
            None

        This function retrieves all messages from the specified thread using the OpenAI API,
        formats them as a JSON string, and prints the result. It also displays the most recent
        message's text content.
    """
    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )

    return messages.data[0].content[0].text.value


def Run(engine):
    openai_api_key = engine.params.get('openai_api_key')
    thread_id = engine.params.get('thread_id')

    client = OpenAI(api_key=openai_api_key)

    try:
        message = get_message(client, thread_id=thread_id)
        engine.result.set(json.dumps({'message': message}, indent=4), status_code=200, content_type='application/json')
    except Exception as e:
        engine.log.error(f"Can't get message: {e}")
        engine.log.error(traceback.format_exc())
        engine.result.set(json.dumps({'error': f"Can't get message: {e}"}, indent=4), status_code=500, content_type='application/json')
