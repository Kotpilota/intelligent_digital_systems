import logging
# Replace Session by AsyncSession in code
# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.encoders import jsonable_encoder
from app import crud, schemas
from app.db import base  # noqa: F401
from app.core.config import settings
from app.core.security import get_password_hash
import time
from datetime import datetime

logger = logging.getLogger(__name__)




DEFAULT_USERS = [

    {
        "nickname": "Default_employee",
        "firstname": "EMPLOYEE",
        "lastname": "EMPLOYEE",
        "password": "0123456789",
        "email": "test@gmail.com",
        "phone":  "+79153280354",
        "activated": True,
        "role_id": 1,
    },
    {
        "nickname": "Default_admin",
        "firstname": "ADMIN",
        "lastname": "ADMIN",
        "password": "0123456789",
        "email": "djeguede.marc@gmail.com",
        "phone":  "+79013682151",
        "activated": True,
        "role_id": 3,
    },

]

DEFAULT_PROJECTS = [
    {
        "name": "Backend",
        "description": "Python Backend",
        "started_at": "2025-03-15 00:00:00",
        "deadline": "2025-05-15 00:00:00"
    }
]

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


async def init_db(db: AsyncSession) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    # Here is the start of creating continent
    time.sleep(5)

    # Here is the start of creating role #############################################################################
    role_names = ['employee', 'teamlead', 'admin', 'ceo']
    role_result = await crud.role.get_all(db=db)

    if not role_result:
        for role_name in role_names:
            role_in = schemas.RoleCreate(name=role_name)
            role = await crud.role.create(db, obj_in=role_in)
    else:
        logger.warning(
            "Skipping creating role. Roles already exist. "
        )

    # Here is the start of creating task_status #######################################################################
    task_status = ['to_do', 'in_progress', 'done']
    task_status_result = await crud.task_status.get_all(db=db)

    if not task_status_result:
        for tstatus in task_status:
            task_status_in = schemas.Task_StatusCreate(status=tstatus)
            task_status = await crud.task_status.create(db, obj_in=task_status_in)
    else:
        logger.warning(
                "Skipping creating task_status. Task_status already exists. "
            )

    # Here is the start of creating employment_level #######################################################################
    levels = ['junior', 'middle', 'senior']
    employment_level_result = await crud.employment_level.get_all(db=db)

    if not employment_level_result:
        for level in levels:
            employment_level_in = schemas.Employment_LevelCreate(level=level)
            employment_level = await crud.employment_level.create(db, obj_in=employment_level_in)
    else:
        logger.warning(
                "Skipping creating employment_level. Employment_level already exists. "
            )

    # Here is the start of creating employment_type #######################################################################
    types = ['полная', 'частичная', 'удаленная']
    employment_type_result = await crud.employment_type.get_all(db=db)

    if not employment_type_result:
        for type_ in types:
            employment_type_in = schemas.Employment_TypeCreate(type=type_)
            employment_type = await crud.employment_type.create(db, obj_in=employment_type_in)
    else:
        logger.warning(
                "Skipping creating employment_type. Employment_type already exists. "
            )

    # Here is the start of creating project_document_type #######################################################################
    doctypes = ['ТЗ', 'Промежуточные_Отчёты', 'Итоговые_отчёты', 'Изображения']
    pro_doctype_result = await crud.project_document_type.get_all(db=db)

    if not pro_doctype_result:
        for doctype in doctypes:
            pro_doctype_in = schemas.Project_Document_TypeCreate(doctype=doctype)
            pro_doctype = await crud.project_document_type.create(db, obj_in=pro_doctype_in)
    else:
        logger.warning(
                "Skipping creating project_document_type. Project_document_type already exists. "
            )


    # Here is the start of creating skill_type #######################################################################
    skills = ['Hard_Skill', 'Soft_Skill']
    skill_type_result = await crud.skill_type.get_all(db=db)

    if not skill_type_result:
        for skill in skills:
            skill_type_in = schemas.Skill_TypeCreate(type=skill)
            skill_type = await crud.skill_type.create(db, obj_in=skill_type_in)
    else:
        logger.warning(
                "Skipping creating skill_type. Skill_type already exists. "
            )

    time.sleep(1)
    # Here is the start of an example that has to be replaced in your project

    if settings.FIRST_ADMIN:
        # user = await crud.user.get_by_email(db, email=settings.FIRST_ADMIN)
        user = await crud.user.get_all_by_filter(db, email=settings.FIRST_ADMIN)
        if not user:
            for default_user in DEFAULT_USERS:
                user_in = schemas.UserCreate(
                    nickname = default_user["nickname"],
                    firstname = default_user["firstname"],
                    lastname = default_user["lastname"],
                    hashed_password = get_password_hash(default_user["password"]),
                    email = default_user["email"],
                    phone = default_user["phone"],
                    activated = default_user["activated"],
                    role_id = default_user["role_id"],
                )
                user = await crud.user.create(db, obj_in=user_in)  # noqa: F841
        else:
            logger.warning(
                "Skipping creating first admin. User with email "
                f"{settings.FIRST_ADMIN} already exists. "
            )

    else:
        logger.warning(
            "Skipping creating superuser.  FIRST_ADMIN needs to be "
            "provided as an env variable. "
        )
    time.sleep(1)


    # Here is the start of creating project #######################################################################
    project_result = await crud.project.get_all(db=db)

    if not project_result:
        for default_project in DEFAULT_PROJECTS:
            project_in = schemas.ProjectCreate(
                name = default_project['name'],
                description = default_project['description'],
                started_at = datetime.strptime(default_project['started_at'], '%Y-%m-%d %H:%M:%S') ,
                deadline = datetime.strptime(default_project['deadline'], '%Y-%m-%d %H:%M:%S')  
            ) 
            
            project = await crud.project.create(db, obj_in=project_in)  
    else:
        logger.warning(
                "Skipping creating project. Project already exists. "
            )

    time.sleep(1)

    # Here is the start of creating location #######################################################################
    locations = [{'country' : 'Россия', 'city':'Москва'}, {'country':'Россия', 'city':'Санкт-Петербург'} , {'country':'Бенин', 'city':'Котону'} ,
                  {'country':'Франция', 'city':'Париж'} ]
    location_result = await crud.location.get_all(db=db)

    if not location_result:
        for location in locations:
            location_in = schemas.LocationCreate(city=location['city'], country=location['country'])
            location = await crud.location.create(db, obj_in=location_in)
    else:
        logger.warning(
                "Skipping creating location. Location already exists. "
            )

    time.sleep(1)
       


    # Here is the start of creating location #######################################################################
    jobs = [
            {
            'company' : 'Intelligent Digital Systems', 
            'description':'test', 
            'employment_level_id': 1,
            'employment_type_id': 2,
            'location_id': 3,
            'position': 'test',
            'salary': 500000
            },

             {
            'company' : 'LLC Yandex ', 
             'description':'Description', 
             'employment_level_id': 2,
             'employment_type_id': 1,
             'location_id': 4,
             'position': 'test',
             'salary': 200000
             },
             {
            'company' : 'VKontakte', 
            'description':'Младший программист С/C++', 
            'employment_level_id': 1,
            'employment_type_id': 2,
            'location_id': 3,
            'position': 'test',
            'salary': 500000
            },

            {
            'company' : 'SuperJob', 
             'description':'Description', 
             'employment_level_id': 2,
             'employment_type_id': 1,
             'location_id': 4,
             'position': 'test',
             'salary': 200000
             }
            ]
    job_result = await crud.job.get_all(db=db)

    if not job_result:
        for job in jobs:
            job_in = schemas.JobCreate(company=job['company'], 
                                       description=job['description'], 
                                       employment_level_id=job['employment_level_id'], 
                                       employment_type_id=job['employment_type_id'],
                                       location_id=job['location_id'],
                                       position=job['position'],
                                       salary=job['salary'])
            job = await crud.job.create(db, obj_in=job_in)
    else:
        logger.warning(
                "Skipping creating job. Job already exists. "
            )

    time.sleep(1)

    # Here is the end of an example that has to be replaced in your project
