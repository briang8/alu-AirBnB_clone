import uuid
from datetime import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key in kwargs:
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                else:
                    setattr(self, key, kwargs[key])
            self.id = str(uuid.uuid4()) if not hasattr(self, "id") else self.id
            self.created_at = datetime.now() if not hasattr(self, "created_at") else self.created_at
            self.updated_at = datetime.now() if not hasattr(self, "updated_at") else self.updated_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        return {
            **self.__dict__,
            "__class__": self.__class__.__name__,
            "created_at": datetime.isoformat(self.created_at),
            "updated_at": datetime.isoformat(self.updated_at),
        }
