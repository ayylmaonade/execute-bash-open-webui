"""
Title: execute-bash
Description: Allows execution of bash commands with proper status tracking.
Author: Shaun (https://github.com/ayylmaonade)
Date: 14/05/2025
Revision: 0.3
License: GPLv3
"""
from pydantic import BaseModel, Field
import subprocess

class Tools:
    class Valves(BaseModel):
        pass
    
    class UserValves(BaseModel):
        pass
    
    def __init__(self):
        self.valves = self.Valves()
        self.user_valves = self.UserValves()
    
    async def execute_bash(self, command: str, __event_emitter__=None) -> str:
        """
        Executes bash command with status tracking.
        Uses event emitter to show "Executing bash..." → "Executed bash."
        """
        # Show initial status (done=False)
        if __event_emitter__:
            await __event_emitter__({
                "type": "status",
                "data": {"description": "Executing bash...", "done": False}
            })
        
        try:
            result = subprocess.run(
                command,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"
        finally:
            # Show completion status (done=True)
            if __event_emitter__:
                await __event_emitter__({
                    "type": "status",
                    "data": {"description": "Executed bash.", "done": True}
                })
