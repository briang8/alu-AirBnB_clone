import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def clear(self):
        self.__objects = {}
        with open(self.__file_path, "w") as f:
            json.dump({}, f)
    
    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        
        classes = {
            'BaseModel': BaseModel,
            'User': User
        }

        try:
            with open(self.__file_path, "r") as f:
                try:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        if value['__class__'] in classes:
                            self.__objects[key] = classes[value['__class__']](**value)
                except:
                    pass
        except FileNotFoundError:
            pass
