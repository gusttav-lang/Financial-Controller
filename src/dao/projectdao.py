from src.dao.project import Project
import pickle


class ProjectDAO:
    """
    Data Access Object Pattern, used to save and open projects
    """
    @staticmethod
    def load_project(path, project) -> bool:
        try:
            with open(path, "rb") as file:
                project_from_file = pickle.loads(file.read())
                project.brokers = project_from_file.brokers
                project.objectives = project_from_file.objectives
                project.assets = project_from_file.assets
                project.liabilities = project_from_file.liabilities
                project.spent_categories = project_from_file.spent_categories
                project.spent_in_month = project_from_file.spent_in_month
                project.standard_spent_limit = project_from_file.standard_spent_limit
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