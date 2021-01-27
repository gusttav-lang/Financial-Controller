from src.dao.project import Project
import pickle


class ProjectDAO:
    """
    Data Access Object Pattern, used to save and open projects
    """
    @staticmethod
    def load_project(path, project=Project()) -> bool:
        try:
            with open(path, "rb") as file:
                obj = pickle.loads(file.read())
                project.replace(obj.copy())
            return True
        except :
            return False

    @staticmethod
    def save_project(path, project=Project()) -> bool:
        try:
            with open(path, 'wb') as file:
                data = pickle.dumps(project)
                file.write(data)
            return True
        except:
            return False