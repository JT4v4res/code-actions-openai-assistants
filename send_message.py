from openai import OpenAI
import os


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


if __name__ == '__main__':
    os.environ['OPENAI_API_KEY'] = "<YOUR_OPENAI_API_KEY>"

    client = OpenAI()

    assistant_id = "<YOUR_ASSISTANT_ID>"

    thread = client.beta.threads.create()

    content = ''

    send_message(client, thread_id=thread.id, assistant_id=assistant_id, content=content)
