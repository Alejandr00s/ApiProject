from UI.UI import user_interface
from API.API import get_database

department_name, record_number = user_interface()

get_database(department_name, record_number)
