from enum import IntEnum

class StatusE(IntEnum):

    OPEN = 1
    IN_PROGRESS = 2
    CLOSED = 3

def handle_open_status():
    print("Handling open statius")

def handle_in_progress_status():
    print("Handling in progress status")

def handle_closed_status():
    print('Handling closed status')

handlers = {
    StatusE.OPEN.value: handle_open_status,
    StatusE.IN_PROGRESS.value: handle_in_progress_status(),
    StatusE.CLOSED.value: handle_closed_status
}

def handle_status_change(status):
    if status not in handlers:
        raise Exception(f"No handler found for status: {status}")
    handler = handlers[status]
    handler()

handle_status_change(StatusE.OPEN.value)        # Handling open status
handle_status_change(StatusE.IN_PROGRESS.value) # Handling in progress status
handle_status_change(StatusE.CLOSED.value)      # Handling closed status
handle_status_change(4)                         # Will raise the exception