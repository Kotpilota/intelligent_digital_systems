#/*
#  Import your schemas here. Schemas is a data structures, that are used in endpoint for modelling sake
# */

from .exemple import Exemple, ExempleCreate, ExempleUpdate, ExempleInDBBase, ExempleBase


from .user import User, UserCreate, UserUpdate, UserInDBBase, UserBase, UserRegister
from .role import Role, RoleCreate, RoleUpdate, RoleInDBBase
from .auth import AuthPhoneForm
from .session import SessionData

from .assigned_task import Assigned_Task, Assigned_TaskCreate, Assigned_TaskUpdate, Assigned_TaskInDBBase
from .certificate import Certificate, CertificateCreate, CertificateUpdate, CertificateInDBBase
from .employment_level import Employment_Level, Employment_LevelCreate, Employment_LevelUpdate, Employment_LevelInDBBase
from .employment_type import Employment_Type, Employment_TypeCreate, Employment_TypeUpdate, Employment_TypeInDBBase
from .experience import Experience, ExperienceCreate, ExperienceUpdate, ExperienceInDBBase
from .faq import Faq, FaqCreate, FaqUpdate, FaqInDBBase
from .file import File, FileCreate, FileUpdate, FileInDBBase
from .formation import Formation, FormationCreate, FormationUpdate, FormationInDBBase
from .has_skill import Has_Skill, Has_SkillCreate, Has_SkillUpdate, Has_SkillInDBBase
from .job import Job, JobCreate, JobUpdate, JobInDBBase
from .job_application import Job_Application, Job_ApplicationCreate, Job_ApplicationUpdate, Job_ApplicationInDBBase
from .location import Location, LocationCreate, LocationUpdate, LocationInDBBase
from .message import Message, MessageCreate, MessageUpdate, MessageInDBBase
from .participant import Participant, ParticipantCreate, ParticipantUpdate, ParticipantInDBBase
from .project import Project, ProjectCreate, ProjectUpdate, ProjectInDBBase
from .project_document import Project_Document, Project_DocumentCreate, Project_DocumentUpdate, Project_DocumentInDBBase
from .project_document_type import Project_Document_Type, Project_Document_TypeCreate, Project_Document_TypeUpdate, Project_Document_TypeInDBBase
from .skill import Skill, SkillCreate, SkillUpdate, SkillInDBBase
from .skill_type import Skill_Type, Skill_TypeCreate, Skill_TypeUpdate, Skill_TypeInDBBase
from .task import Task, TaskCreate, TaskUpdate, TaskInDBBase
from .task_status import Task_Status, Task_StatusCreate, Task_StatusUpdate, Task_StatusInDBBase
from .mail import Mail, MailCreate, MailUpdate



