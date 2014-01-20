import os, json

class MyProjects:
    PROJECTS_FILE = os.path.join(os.path.dirname(__file__), "../data/projects.json")
    
    def __init__(self):
        self._projects = json.load(open(MyProjects.PROJECTS_FILE))['projects']
    
    def get_projects(self):
        return self._projects
