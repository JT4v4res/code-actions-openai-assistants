from openai import OpenAI
import json


def create_thread(client: OpenAI) -> str:
    thread = client.beta.threads.create()

    return thread.id


def Run(engine):
    openai_api_key = engine.params.get("openai_api_key")


    try:
        client = OpenAI(api_key=openai_api_key)

        thread_id = create_thread(client)

        engine.result.set(json.dumps({"thread_id": thread_id, "status": "success"}, indent=4), status_code=200, content_type="json")
        engine.log.info("File uploaded successfully.")
    except Exception as e:
        engine.log.error(f"Error: {e}")
        engine.result.set(json.dumps({"status": "error", "error": str(e)}, indent=4), status_code=500, content_type="json")