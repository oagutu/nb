# NoticeBoard

[![CircleCI](https://circleci.com/gh/oagutu/nb/tree/develop.svg?style=svg)](https://circleci.com/gh/oagutu/nb/tree/develop)

#### Brief Desc:

NoticeBoard is a digital office notice board. 

It's a web API intended to provide a virtual noticeboard for staff within an organisation, 
allowing them to interact with it directly via the web app or indirectly via 3rd party apps.

#### Available endpoints:

| Endpoint   |  url |  method |
|----------|:-------------:|------:|
| Create organization  | `/api/v1/organization/` | POST  |
| Get organization list  | `/api/v1/organization/` |  GET  |
| Get single organization | `/api/v1/organization/<uuid:org_id>` | GET | 
| Update organization | `/api/v1/organization/<uuid:org_id>` | PATCH |
| Delete organization | `/api/v1/organization/<uuid:org_id>` | DELETE |
| Create department | `/api/v1/department/` | POST  |
| Get department list  | `/api/v1/department/` |  GET  |
| Get single department | `/api/v1/department/<uuid:dept_id>` | GET | 
| Update department | `/api/v1/department/<uuid:dept_id>` | PATCH |
| Delete department | `/api/v1/department/<uuid:dept_id>` | DELETE |


#### Technology:
- Python
- Django & Django REST framework
- POSTGRESQL

#### Setup:

- Clone the repo: ```git clone https://github.com/oagutu/nb.git```
- Ensure you have `pipenv` installed if not install using, ```pip install pipenv```
- Create/activate virtual env using ```pipenv shell```
- Install package dependencies: ```pipenv install```
- Create a `.env` file using `env_sample` as a template and fill in your database details.
- Run the project using: `python manage.py runserver`
