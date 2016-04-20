import logging

class ProjectSettings:
    def __init__(self, project, path):
        self.project = project
        self.path = path
        self.map = "default"
        logging.info(":: loading project")
        logging.info("::   project: %s" % self.project)
        logging.info("::   path: %s" % self.path)

    def get_project(self):
        return self.project

    def get_path(self):
        return self.path
