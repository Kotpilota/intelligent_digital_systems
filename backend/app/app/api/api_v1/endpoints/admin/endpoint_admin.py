from fastapi import APIRouter
from sqlalchemy import  inspect, text, select, func
from fastapi.encoders import  jsonable_encoder

from app.api import deps
from app.models.user import User

from app.db.session import engine
from app.db.base_class import Base, get_class_by_table_name
from typing import  Dict

router = APIRouter()



@router.get('/database_schema')
async def database_schema() -> Dict:

    options = {}

    async with (engine.connect() as conn):
        table_names = await conn.run_sync(
            lambda sync_conn: inspect(sync_conn).get_table_names()
        )

        for table_name in table_names:
            options[table_name]= await conn.run_sync(
                lambda sync_conn: inspect(sync_conn).get_columns(table_name)
            )

            for dct in options[table_name]:
                dct['type']= dct['type'].python_type.__name__

            # This query sums the sizes (in bytes) of all pages belonging to the table.
            # query = text("SELECT SUM(pgsize) AS total_size FROM dbstat WHERE name = :name;")
            query_count = select(func.count()).select_from( text(table_name) )


            # size_result = await conn.execute(query, {"name": table_name})
            # table_size = size_result.scalar()

            row_count_result = await conn.execute(query_count)
            row_count = row_count_result.scalar()

            if table_name!= 'alembic_version':
                query_last_update = select(func.max(get_class_by_table_name(table_name).updated_at))
                last_update_result = await conn.execute(query_last_update)
                last_update = last_update_result.scalar()
            else:
                last_update = ""


            # options[table_name].insert(0, dict({"size":table_size, "row_count": row_count, "last_update":last_update}) )
            options[table_name].insert(0, dict({ "row_count": row_count, "last_update":last_update}) )


    return jsonable_encoder(options)