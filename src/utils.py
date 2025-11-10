from typing import Any, Callable
import time

def calculate_execution_time(callback_fn: Callable) -> tuple[float, Any]:
    start = time.time()
    response = callback_fn()
    return (time.time()-start)*1000, response or None

def get_breakline(type: str) -> str:
    breaklines_dict = {
        "TWO_LINES": "\n\n",
        "NEW_LINE": "\n",
        "NO_BREAK": ""
    }

    return breaklines_dict[type]
