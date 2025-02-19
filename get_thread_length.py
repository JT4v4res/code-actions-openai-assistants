from openai import OpenAI
import os


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


if __name__ == '__main__':
    os.environ['OPENAI_API_KEY'] = "<YOUR_OPENAI_API_KEY>"

    client = OpenAI()

    thread = "<YOUR_THREAD_ID>"

    get_thread_length(client, thread_id=thread)