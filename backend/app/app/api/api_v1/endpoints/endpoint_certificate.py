from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, List

from app import crud
from app.api import deps
from app.schemas.certificate import Certificate, CertificateCreate, CertificateUpdate
from app.models.user import User

router = APIRouter()

@router.get("/read/{id}", response_model=Certificate)
async def read_certificate(
    id: int,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get a certificate.
    """
    certificate = await crud.certificate.get_by_id(db=db, id=id)
    if not certificate:
        raise HTTPException(status_code=404, detail="certificate not found")
    return certificate

@router.get("/read", response_model=List[Certificate])
async def read_certificates(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get all certificates.
    """
    return await crud.certificate.get_all(db=db)

@router.post("/create", response_model=Certificate)
async def create_certificate(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    certificate_in: CertificateCreate
) -> Any:
    """
    Create a new certificate.
    """
    return await crud.certificate.create(db=db, obj_in=certificate_in)

@router.put("/update/{id}", response_model=Certificate)
async def update_certificate(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int,
    certificate_in: CertificateUpdate
) -> Any:
    """
    Update a certificate.
    """
    certificate = await crud.certificate.get_by_id(db=db, id=id)
    if not certificate:
        raise HTTPException(status_code=404, detail="certificate not found")
    certificate = await crud.certificate.update(db=db, db_obj=certificate, obj_in=certificate_in)
    return certificate

@router.delete("/delete/{id}", response_model=Certificate)
async def delete_certificate(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    id: int
) -> Any:
    """
    Delete a certificate.
    """
    certificate = await crud.certificate.get_by_id(db=db, id=id)
    if not certificate:
        raise HTTPException(status_code=404, detail="certificate not found")
    return await crud.certificate.remove(db=db, id=id)
