import json
import requests
from datetime import datetime
from config.config import PLATFORM_URL


class ProjectController:

    def __init__(self):
        pass

    def get_all_project_employee(self, id):
        project_employees = requests.get('{}/pathfinder/project_candidate/{}'.format(PLATFORM_URL, id))
        if project_employees.status_code == 200:
            project_data = project_employees.json()
            formatted_projects_data = []
            for project in project_data['results']:
                temp_project = project
                temp_project['employee_id'] = temp_project['candidate_id']
                temp_project['assignment_start_date'] = datetime.strftime(datetime.strptime(temp_project['assignment_start_date'], '%Y-%m-%d'), '%d-%b-%Y')
                temp_project['assignment_end_date'] = datetime.strftime(
                    datetime.strptime(temp_project['assignment_end_date'], '%Y-%m-%d'), '%d-%b-%Y')
                del temp_project['candidate_id']
                formatted_projects_data.append(temp_project)
            project_data['results'] = formatted_projects_data
            return project_data

    def save_a_project_employee(self, data={}):
        data['candidate_id'] = data['employee_id']
        del data['employee_id']
        new_project_employees = requests.post('{}/pathfinder/project_candidate'.format(PLATFORM_URL), data=json.dumps(data), headers={'Content-Type': 'application/json'})
        return (
            new_project_employees.json()  # {"message": "success"}, 201  # generate_token(new_event)
        )

    def update_a_project_employee(self, id, data):
        data['assignment_start_date'] = data['assignment_start_date'].strftime('%Y-%m-%d')
        data['assignment_end_date'] = data['assignment_end_date'].strftime('%Y-%m-%d')
        data['candidate_id'] = data['employee_id']
        del data['employee_id']
        project_employee = requests.put('{}/pathfinder/project_candidate'.format(PLATFORM_URL), json.dumps(data), headers={'Content-Type': 'application/json'})

        if project_employee.status_code == 201:
            return project_employee.json()
        else:
            return False

    def delete_project_employee(self, id, employee_id):
        project_employee = requests.delete('{}/pathfinder/project_candidate/{}/{}'.format(PLATFORM_URL, id, employee_id))
        if project_employee:
            return {"message": "Successfully removed the Project"}, 200
        else:
            return {"message": "No such employee and project association found"}, 400

