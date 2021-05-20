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
                project.asset_categories = project_from_file.asset_categories
                project.year_predictions_list = project_from_file.year_predictions_list
                project.assets_in_dates_list = project_from_file.assets_in_dates_list
                project.ideal_assets_list = project_from_file.ideal_assets_list
                project.stock_criteria = project_from_file.stock_criteria
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