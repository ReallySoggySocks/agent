from google.genai import types
from config import available_functions

def call_function(function_call, verbose=False):
    if function_call.name not in available_functions:
        return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call.name,
            response={"error": f"Unknown function: {function_call.name}"},
        )
    ],
)
    elif verbose == True:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")
        