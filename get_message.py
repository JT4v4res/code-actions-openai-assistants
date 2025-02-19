from openai import OpenAI
import os
import json


def get_message(client: OpenAI, thread_id: str) -> None:
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

    message_list = messages.data

    message_dicts = [message.to_dict() for message in message_list]

    # format messages to JSON
    print(json.dumps(message_dicts, indent=4))

    # shows the most recent message
    print(messages.data[0].content[0].text.value)


if __name__ == '__main__':
    os.environ['OPENAI_API_KEY'] = "<YOUR_OPENAI_API_KEY>"

    client = OpenAI()

    thread = "<YOUR_THREAD_ID>"

    get_message(client, thread_id=thread)

