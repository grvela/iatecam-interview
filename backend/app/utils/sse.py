from typing import Generator, List
from fastapi import Request, Response
from starlette.responses import StreamingResponse
import asyncio

sse_connections = []

class SSEManager:
    def __init__(self):
        self.event_generators = []

    async def event_generator(self) -> Generator[str, None, None]:
        while True:
            await asyncio.sleep(1)
            if sse_connections:
                for event_data in self.get_event_data():
                    yield f"data: {event_data}\n\n"

    async def sse_endpoint(self) -> Response:
        response = StreamingResponse(self.event_generator(), media_type="text/event-stream")
        sse_connections.append(response)
        return response

    def send_event(self, event_data: str):
        for connection in sse_connections:
            connection.body.write(f"data: {event_data}\n\n".encode("utf-8"))
            connection.body.flush()

    def register_event_data(self, event_data: str):
        self.event_generators.append(event_data)

    def get_event_data(self) -> List[str]:
        return self.event_generators

sse_manager = SSEManager()