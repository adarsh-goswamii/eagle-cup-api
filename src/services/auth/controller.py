from fastapi import Request

class AuthController:
  """Auth Controller"""
  
  @classmethod
  async def login(self, request: Request, payload: str):
    return 'Hello world'
