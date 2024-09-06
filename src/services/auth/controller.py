from fastapi import Request
from db.session import get_db, Base, engine
from schema.user import UserModel

db = get_db()

class AuthController:
  """Auth Controller"""
  
  @classmethod
  async def login(self, request: Request, payload: str):
    try:
      print(engine)
      Base.metadata.create_all(bind=engine)  # This creates the table
      return {"message": "Table created successfully"}
    except Exception as e:
      return {"error": str(e)}
