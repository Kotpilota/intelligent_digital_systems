from fastapi import APIRouter

from app.api.api_v1.endpoints import auth, endpoint_example
from app.api.api_v1.endpoints import (
    endpoint_user, endpoint_role, endpoint_file, endpoint_faq, endpoint_experience, endpoint_message,
    endpoint_formation, endpoint_certificate, endpoint_job, endpoint_job_application,
    endpoint_task, endpoint_task_status 
    )
from app.api.api_v1.endpoints.admin import (
    endpoint_admin, endpoint_dashboard, endpoint_admin_table_content,
    endpoint_admin_tables, endpoint_registration
    )
from  app.api.api_v1.endpoints.common_part import (
    endpoint_mainpage, endpoint_case_detail, endpoint_case_list,
    endpoint_cv_detail, endpoint_employee_list,
    endpoint_job_postings
    )

from  app.api.api_v1.endpoints.personal_account import (
    endpoint_account, 
    endpoint_chat,
    endpoint_profile, endpoint_assigned_tasks_page
)

from app.api.api_v1.endpoints import (endpoint_assigned_task, endpoint_employment_level, endpoint_employment_type, 
                                      endpoint_has_skill, endpoint_location, endpoint_participant, endpoint_project, 
                                      endpoint_project_document, endpoint_project_document_type, endpoint_skill, 
                                      endpoint_skill_type, endpoint_mail)



api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(endpoint_example.router, prefix="/example", tags=["example"])

api_router.include_router(endpoint_user.router, prefix="/user", tags=["user"])
api_router.include_router(endpoint_role.router, prefix="/role", tags=["role"])
api_router.include_router(endpoint_file.router, prefix="/file", tags=["file"])

api_router.include_router(endpoint_admin.router, prefix="/admin", tags=["admin"])
api_router.include_router(endpoint_mainpage.router, prefix="", tags=["main_page"])



api_router.include_router(endpoint_faq.router, prefix="/faq", tags=["faq"])
api_router.include_router(endpoint_location.router, prefix="/location", tags=["location"])
api_router.include_router(endpoint_employment_level.router, prefix="/employment_level", tags=["employment_level"])
api_router.include_router(endpoint_employment_type.router, prefix="/employment_type", tags=["employment_type"])
api_router.include_router(endpoint_skill_type.router, prefix="/skill_type", tags=["skill_type"])
api_router.include_router(endpoint_skill.router, prefix="/skill", tags=["skill"])
api_router.include_router(endpoint_has_skill.router, prefix="/has_skill", tags=["has_skill"])

api_router.include_router(endpoint_experience.router, prefix="/experience", tags=["experience"])
api_router.include_router(endpoint_message.router, prefix="/message", tags=["message"])
api_router.include_router(endpoint_formation.router, prefix="/formation", tags=["formation"])
api_router.include_router(endpoint_certificate.router, prefix="/certificate", tags=["certificate"])
api_router.include_router(endpoint_job.router, prefix="/job", tags=["job"])
api_router.include_router(endpoint_job_application.router, prefix="/job_application", tags=["job_application"])



api_router.include_router(endpoint_task.router, prefix="/task", tags=["task"])
api_router.include_router(endpoint_task_status.router, prefix="/task_status", tags=["task_status"])
api_router.include_router(endpoint_assigned_task.router, prefix="/assigned_task", tags=["assigned_task"])
api_router.include_router(endpoint_project_document_type.router, prefix="/project_document_type", tags=["project_document_type"])
api_router.include_router(endpoint_project.router, prefix="/project", tags=["project"])
api_router.include_router(endpoint_project_document.router, prefix="/project_document", tags=["project_document"])
api_router.include_router(endpoint_participant.router, prefix="/participant", tags=["participant"])

# admin page
api_router.include_router(endpoint_dashboard.router, prefix="", tags=["dashboard"])
api_router.include_router(endpoint_admin_table_content.router, prefix="", tags=["admin_db_tables"])
api_router.include_router(endpoint_admin_tables.router, prefix="", tags=["admin_tables"])
api_router.include_router(endpoint_registration.router, prefix="", tags=["registration"])

# common_part page
api_router.include_router(endpoint_case_detail.router, prefix="", tags=["case_detail"])
api_router.include_router(endpoint_case_list.router, prefix="", tags=["case_list"])
api_router.include_router(endpoint_cv_detail.router, prefix="", tags=["cv_detail"])
api_router.include_router(endpoint_employee_list.router, prefix="", tags=["employee_list"])
api_router.include_router(endpoint_job_postings.router, prefix="", tags=["job_postings"])

# personal_account page
api_router.include_router(endpoint_account.router, prefix="", tags=["account"])
api_router.include_router(endpoint_assigned_tasks_page.router, prefix="", tags=["assigned_tasks_page"])
api_router.include_router(endpoint_chat.router, prefix="", tags=["chat"])
api_router.include_router(endpoint_profile.router, prefix="", tags=["profile"])


api_router.include_router(endpoint_mail.router, prefix="", tags=["mail"])
