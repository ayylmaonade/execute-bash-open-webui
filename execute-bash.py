"""
Title: execute-bash
Description: Allows the execution of _any_ and *all* bash commands and scripts. Use with caution! I strongly recommend you run open-webui in a container if you don't know what you're doing with bash - or even if you do.
Author: Shaun (https://github.com/ayylmaonade)
Repository: https://github.com/ayylmaonade/execute-bash-open-webui
Date: 14/05/2025 (DD/MM/YY)
Revision: 0.1
License: GPLv3
"""

from pydantic import BaseModel, Field
import subprocess


class Tools:
    class Valves(BaseModel):
        pass # Placeholder template for future configuration

    class UserValves(BaseModel):
        pass # Placeholder template for future configuration
    
    # Initialize Tools & assign it to user_valves
    def __init__(self):
        self.valves = self.Valves()
        self.user_valves = self.UserValves()

    def execute_bash(self, command: str) -> str:
        """
        Executes a bash command and returns its output.
        :param command: The bash command to execute.
        :return: Output of the command or an error message.
        """
        try:
            result = subprocess.run(
                command,        # Runs the command specified
                shell=True,     # Execute the command in bash shell
                check=True,     # Calls processError incase cmd fails 
                stdout=subprocess.PIPE, # Grab the std input
                stderr=subprocess.PIPE, 
                text=True, # returns output as text 
            )
            return result.stdout
        except subprocess.CalledProcessError as e:  # error handling
            return f"Error: {e.stderr}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"  # returns error message

