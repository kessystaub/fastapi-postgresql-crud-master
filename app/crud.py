from sqlalchemy.orm import Session
from models import City, User, Softskill, Hardskill, Formation, Experience, Company, Joboffer, Status, Application, UserSoftskill, UserHardskill, Position, Institution, UserExperience, UserFormation
from schemas import CitySchema
from sqlalchemy.orm import joinedload
import schemas
import models
# city


def get_city(db: Session, skip: int = 0, limit: int = 100):
    return db.query(City).offset(skip).limit(limit).all()


def get_city_by_id(db: Session, city_id: int):
    return db.query(City).filter(City.id == city_id).first()


def get_city_by_name(db: Session, city_name: str):
    return db.query(City).filter(City.name == city_name).first()


def create_city(db: Session, city: CitySchema):
    _city = City(name=city.name, uf=city.uf)
    db.add(_city)
    db.commit()
    db.refresh(_city)
    return _city


def update_city(db: Session, city_id: int, name: str, uf: str):
    _city = get_city_by_id(db=db, city_id=city_id)

    _city.name = name
    _city.uf = uf

    db.commit()
    db.refresh(_city)
    return _city


def remove_city(db: Session, city_id: int):
    _city = get_city_by_id(db=db, city_id=city_id)
    db.delete(_city)
    db.commit()

# user


def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, user_email: str):
    return db.query(User).filter(User.email == user_email).first()


def get_candidaturas_do_usuario(db: Session, user_id: str):
    return db.query(Application, Status, Joboffer)\
        .join(Status, Status.id == Application.status_id)\
        .join(Joboffer, Joboffer.id == Application.joboffer_id)\
        .filter(Application.user_id == user_id).all()


def create_user(db: Session, user: schemas.UserSchema):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: schemas.UserSchema):
    _user = get_user_by_id(db=db, user_id=user_id)

    _user.name = user.name
    _user.password: user.password
    _user.email: user.email
    _user.phone: user.phone
    _user.address: user.address
    _user.address_number: user.address_number
    _user.address_complement: user.address_complement
    _user.address_neighborhood: user.address_neighborhood
    _user.city_id: user.city_id

    db.commit()
    db.refresh(_user)
    return _user


def remove_user(db: Session, user_id: int):
    _user = get_user_by_id(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()

# softskill


def get_softskill(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Softskill).offset(skip).limit(limit).all()


def get_softskill_by_id(db: Session, softskill_id: int):
    return db.query(Softskill).filter(Softskill.id == softskill_id).first()


def get_softskill_by_name(db: Session, softskill_name: str):
    return db.query(Softskill).filter(Softskill.name == softskill_name).first()


def create_softskill(db: Session, softskill: schemas.SoftskillSchema):
    db_softskill = models.Softskill(**softskill.dict())
    db.add(db_softskill)
    db.commit()
    db.refresh(db_softskill)
    return db_softskill


def update_softskill(db: Session, softskill_id: int, softskill: schemas.SoftskillSchema):
    _softskill = get_softskill_by_id(db=db, softskill_id=softskill_id)

    _softskill.name = softskill.name

    db.commit()
    db.refresh(_softskill)
    return _softskill


def remove_softskill(db: Session, softskill_id: int):
    _softskill = get_softskill_by_id(db=db, softskill_id=softskill_id)
    db.delete(_softskill)
    db.commit()


# hardskill


def get_hardskill(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Hardskill).offset(skip).limit(limit).all()


def get_hardskill_by_id(db: Session, hardskill_id: int):
    return db.query(Hardskill).filter(Hardskill.id == hardskill_id).first()


def get_hardskill_by_name(db: Session, hardskill_name: str):
    return db.query(Hardskill).filter(Hardskill.name == hardskill_name).first()


def create_hardskill(db: Session, hardskill: schemas.HardskillSchema):
    db_hardskill = models.Hardskill(**hardskill.dict())
    db.add(db_hardskill)
    db.commit()
    db.refresh(db_hardskill)
    return db_hardskill


def update_hardskill(db: Session, hardskill_id: int, hardskill: schemas.HardskillSchema):
    _hardskill = get_hardskill_by_id(db=db, hardskill_id=hardskill_id)

    _hardskill.name = hardskill.name

    db.commit()
    db.refresh(_hardskill)
    return _hardskill


def remove_hardskill(db: Session, hardskill_id: int):
    _hardskill = get_hardskill_by_id(db=db, hardskill_id=hardskill_id)
    db.delete(_hardskill)
    db.commit()


# formation


def get_formation(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Formation).offset(skip).limit(limit).all()


def get_formation_by_id(db: Session, formation_id: int):
    return db.query(Formation).filter(Formation.id == formation_id).first()


def create_formation(db: Session, formation: schemas.FormationSchema):
    db_formation = models.Formation(**formation.dict())
    db.add(db_formation)
    db.commit()
    db.refresh(db_formation)
    return db_formation


def update_formation(db: Session, formation_id: int, formation: schemas.FormationSchema):
    _formation = get_formation_by_id(db=db, formation_id=formation_id)

    _formation.course = formation.course
    _formation.date: formation.date
    _formation.institution_id: formation.institution_id

    db.commit()
    db.refresh(_formation)
    return _formation


def remove_formation(db: Session, formation_id: int):
    _formation = get_formation_by_id(db=db, formation_id=formation_id)
    db.delete(_formation)
    db.commit()


# experience


def get_experience(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Experience).offset(skip).limit(limit).all()


def get_experience_by_id(db: Session, experience_id: int):
    return db.query(Experience).filter(Experience.id == experience_id).first()


def create_experience(db: Session, experience: schemas.ExperienceSchema):
    db_experience = models.Experience(**experience.dict())
    db.add(db_experience)
    db.commit()
    db.refresh(db_experience)
    return db_experience


def update_experience(db: Session, experience_id: int, experience: schemas.ExperienceSchema):
    _experience = get_experience_by_id(db=db, experience_id=experience_id)

    _experience.company = experience.company
    _experience.date: experience.date
    _experience.position_id: experience.position_id

    db.commit()
    db.refresh(_experience)
    return _experience


def remove_experience(db: Session, experience_id: int):
    _experience = get_experience_by_id(db=db, experience_id=experience_id)
    db.delete(_experience)
    db.commit()


# company


def get_company(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Company).offset(skip).limit(limit).all()


def get_company_by_id(db: Session, company_id: int):
    return db.query(Company).filter(Company.id == company_id).first()


def get_company_by_email(db: Session, company_email: str):
    return db.query(Company).filter(Company.email == company_email).first()


def create_company(db: Session, company: schemas.CompanySchema):
    db_company = models.Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def update_company(db: Session, company_id: int, company: schemas.CompanySchema):
    _company = get_company_by_id(db=db, company_id=company_id)

    _company.name = company.name
    _company.description: company.description
    _company.cnpj: company.cnpj
    _company.password: company.password
    _company.email: company.email
    _company.phone_number: company.phone_number
    _company.address: company.address
    _company.address_number: company.address_number
    _company.address_complement: company.address_complement
    _company.address_neighborhood: company.address_neighborhood
    _company.city_id: company.city_id

    db.commit()
    db.refresh(_company)
    return _company


def remove_company(db: Session, company_id: int):
    _company = get_company_by_id(db=db, company_id=company_id)
    db.delete(_company)
    db.commit()

# Joboffer


def get_joboffer(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Joboffer).offset(skip).limit(limit).all()


def get_joboffer_by_id(db: Session, joboffer_id: int):
    return db.query(Joboffer, Company, City, Position)\
        .join(Company, Company.id == Joboffer.company_id)\
        .join(City, City.id == Joboffer.city_id)\
        .join(Position, Position.id == Joboffer.position_id)\
        .filter(Joboffer.id == joboffer_id)\
        .first()


def get_vagas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Joboffer, Company, City, Position)\
        .join(Company, Company.id == Joboffer.company_id)\
        .join(City, City.id == Joboffer.city_id)\
        .join(Position, Position.id == Joboffer.position_id)\
        .offset(skip).limit(limit)\
        .all()


def create_joboffer(db: Session, joboffer: schemas.JobofferSchema):
    db_joboffer = models.Joboffer(**joboffer.dict())
    db.add(db_joboffer)
    db.commit()
    db.refresh(db_joboffer)
    return db_joboffer


def update_joboffer(db: Session, joboffer_id: int, joboffer: schemas.JobofferSchema):
    _joboffer = get_joboffer_by_id(db=db, joboffer_id=joboffer_id)

    _joboffer.code = joboffer.code
    _joboffer.name: joboffer.name
    _joboffer.description: joboffer.description
    _joboffer.city_id: joboffer.city_id
    _joboffer.company_id: joboffer.company_id
    _joboffer.position_id: joboffer.position_id

    db.commit()
    db.refresh(_joboffer)
    return _joboffer


def remove_joboffer(db: Session, joboffer_id: int):
    _joboffer = get_joboffer_by_id(db=db, joboffer_id=joboffer_id)
    db.delete(_joboffer)
    db.commit()

# Application


def get_application(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Application).offset(skip).limit(limit).all()


def get_application_by_id(db: Session, application_id: int):
    return db.query(Application).filter(Application.id == application_id).first()


def get_application_by_user_id(db: Session, user_id: int):
    return db.query(Application).filter(Application.user_id == user_id).all()


def create_application(db: Session, application: schemas.ApplicationSchema):
    db_application = models.Application(**application.dict())
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application


def update_application(db: Session, application_id: int, application: schemas.ApplicationSchema):
    _application = get_application_by_id(db=db, application_id=application_id)

    _application.date = application.date
    _application.status_id = application.status_id
    _application.joboffer_id: application.joboffer_id
    _application.user_id: application.user_id

    db.commit()
    db.refresh(_application)
    return _application


def remove_application(db: Session, application_id: int):
    _application = get_application_by_id(db=db, application_id=application_id)
    db.delete(_application)
    db.commit()

# Status


def get_status(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Status).offset(skip).limit(limit).all()


def get_status_by_id(db: Session, status_id: int):
    return db.query(Status).filter(Status.id == status_id).first()


def create_status(db: Session, status: schemas.StatusSchema):
    db_status = models.Status(**status.dict())
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status


def update_status(db: Session, status_id: int, status: schemas.StatusSchema):
    _status = get_status_by_id(db=db, status_id=status_id)

    _status.status = status.status

    db.commit()
    db.refresh(_status)
    return _status


def remove_status(db: Session, status_id: int):
    _status = get_status_by_id(db=db, status_id=status_id)
    db.delete(_status)
    db.commit()


# UserSoftskill


def get_user_softskill(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserSoftskill).offset(skip).limit(limit).all()


def get_user_softskill_by_id(db: Session, user_softskill_id: int):
    return db.query(UserSoftskill).filter(UserSoftskill.id == user_softskill_id).first()


def get_softskill_by_user_id(db: Session, user_id: int):
    return db.query(UserSoftskill).filter(UserSoftskill.user_id == user_id).all()


def get_user_softskill_by_softskill_id(db: Session, user_id: int, softskill_id: int):
    return db.query(UserSoftskill).filter((UserSoftskill.softskill_id == softskill_id) & (UserSoftskill.user_id == user_id)).first()


def create_user_softskill(db: Session, user_softskill: schemas.UserSoftskillSchema):
    db_user_softskill = models.UserSoftskill(**user_softskill.dict())
    db.add(db_user_softskill)
    db.commit()
    db.refresh(db_user_softskill)
    return db_user_softskill


def update_user_softskill(db: Session, user_softskill_id: int, user_softskill: schemas.UserSoftskillSchema):
    _user_softskill = get_user_softskill_by_id(
        db=db, user_softskill_id=user_softskill_id)

    _user_softskill.user_id = user_softskill.user_id
    _user_softskill.softskill_id = user_softskill.softskill_id

    db.commit()
    db.refresh(_user_softskill)
    return _user_softskill


def remove_user_softskill(db: Session, user_softskill_id: int):
    _user_softskill = get_user_softskill_by_id(
        db=db, user_softskill_id=user_softskill_id)
    db.delete(_user_softskill)
    db.commit()


def remove_user_softskill_by_user(db: Session, user_id: int, softskill_id: int):
    _user_softskill = get_user_softskill_by_softskill_id(
        db=db, user_id=user_id, softskill_id=softskill_id)
    db.delete(_user_softskill)
    db.commit()


# UserFormation


def get_user_formation(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserFormation).offset(skip).limit(limit).all()


def get_user_formation_by_id(db: Session, user_formation_id: int):
    return db.query(UserFormation).filter(UserFormation.id == user_formation_id).first()


def get_user_formation_by_formation_id(db: Session, user_id: int, formation_id: int):
    return db.query(UserFormation).filter((UserFormation.formation_id == formation_id) & (UserFormation.user_id == user_id)).first()


def get_formation_by_user_id(db: Session, user_id: int):
    return db.query(UserFormation).filter(UserFormation.user_id == user_id).all()


def create_user_formation(db: Session, user_formation: schemas.UserFormationSchema):
    db_user_formation = models.UserFormation(**user_formation.dict())
    db.add(db_user_formation)
    db.commit()
    db.refresh(db_user_formation)
    return db_user_formation


def update_user_formation(db: Session, user_formation_id: int, user_formation: schemas.UserFormationSchema):
    _user_formation = get_user_formation_by_id(
        db=db, user_formation_id=user_formation_id)

    _user_formation.user_id = user_formation.user_id
    _user_formation.formation_id = user_formation.formation_id

    db.commit()
    db.refresh(_user_formation)
    return _user_formation


def remove_user_formation(db: Session, user_formation_id: int):
    _user_formation = get_user_formation_by_id(
        db=db, user_formation_id=user_formation_id)
    db.delete(_user_formation)
    db.commit()


def remove_user_formation_by_user(db: Session, user_id: int, formation_id: int):
    _user_formation = get_user_formation_by_formation_id(
        db=db, user_id=user_id, formation_id=formation_id)
    db.delete(_user_formation)
    db.commit()


# UserExperience


def get_user_experience(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserExperience).offset(skip).limit(limit).all()


def get_user_experience_by_id(db: Session, user_experience_id: int):
    return db.query(UserExperience).filter(UserExperience.id == user_experience_id).first()


def get_user_experience_by_experience_id(db: Session, user_id: int, experience_id: int):
    return db.query(UserExperience).filter((UserExperience.experience_id == experience_id) & (UserExperience.user_id == user_id)).first()


def get_experience_by_user_id(db: Session, user_id: int):
    return db.query(UserExperience).filter(UserExperience.user_id == user_id).all()


def create_user_experience(db: Session, user_experience: schemas.UserExperienceSchema):
    db_user_experience = models.UserExperience(**user_experience.dict())
    db.add(db_user_experience)
    db.commit()
    db.refresh(db_user_experience)
    return db_user_experience


def update_user_experience(db: Session, user_experience_id: int, user_experience: schemas.UserExperienceSchema):
    _user_experience = get_user_experience_by_id(
        db=db, user_experience_id=user_experience_id)

    _user_experience.user_id = user_experience.user_id
    _user_experience.experience_id = user_experience.experience_id

    db.commit()
    db.refresh(_user_experience)
    return _user_experience


def remove_user_experience_by_user(db: Session, user_id: int, experience_id: int):
    _user_experience = get_user_experience_by_experience_id(
        db=db, user_id=user_id, experience_id=experience_id)
    db.delete(_user_experience)
    db.commit()


def remove_user_experience(db: Session, user_experience_id: int):
    _user_experience = get_user_experience_by_id(
        db=db, user_experience_id=user_experience_id)
    db.delete(_user_experience)
    db.commit()

# UserHardskill


def get_user_hardskill(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserHardskill).offset(skip).limit(limit).all()


def get_user_hardskill_by_id(db: Session, user_hardskill_id: int):
    return db.query(UserHardskill).filter(UserHardskill.id == user_hardskill_id).first()


def get_hardskill_by_user_id(db: Session, user_id: int):
    return db.query(UserHardskill).filter(UserHardskill.user_id == user_id).all()


def get_user_hardskill_by_hardskill_id(db: Session, user_id: int, hardskill_id: int):
    return db.query(UserHardskill).filter((UserHardskill.hardskill_id == hardskill_id) & (UserHardskill.user_id == user_id)).first()


def create_user_hardskill(db: Session, user_hardskill: schemas.UserHardskillSchema):
    db_user_hardskill = models.UserHardskill(**user_hardskill.dict())
    db.add(db_user_hardskill)
    db.commit()
    db.refresh(db_user_hardskill)
    return db_user_hardskill


def update_user_hardskill(db: Session, user_hardskill_id: int, user_hardskill: schemas.UserHardskillSchema):
    _user_hardskill = get_user_hardskill_by_id(
        db=db, user_hardskill_id=user_hardskill_id)

    _user_hardskill.user_id = user_hardskill.user_id
    _user_hardskill.hardskill_id = user_hardskill.hardskill_id

    db.commit()
    db.refresh(_user_hardskill)
    return _user_hardskill


def remove_user_hardskill(db: Session, user_hardskill_id: int):
    _user_hardskill = get_user_hardskill_by_id(
        db=db, user_hardskill_id=user_hardskill_id)
    db.delete(_user_hardskill)
    db.commit()


def remove_user_hardskill_by_user(db: Session, user_id: int, hardskill_id: int):
    _user_hardskill = get_user_hardskill_by_hardskill_id(
        db=db, user_id=user_id, hardskill_id=hardskill_id)
    db.delete(_user_hardskill)
    db.commit()


# Position


def get_position(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Position).offset(skip).limit(limit).all()


def get_position_by_id(db: Session, position_id: int):
    return db.query(Position).filter(Position.id == position_id).first()


def get_position_by_name(db: Session, position_name: str):
    return db.query(Position).filter(Position.name == position_name).first()


def create_position(db: Session, position: schemas.PositionSchema):
    db_position = models.Position(**position.dict())
    db.add(db_position)
    db.commit()
    db.refresh(db_position)
    return db_position


def update_position(db: Session, position_id: int, position: schemas.PositionSchema):
    _position = get_position_by_id(
        db=db, position_id=position_id)

    _position.name = position.name

    db.commit()
    db.refresh(_position)
    return _position


def remove_position(db: Session, position_id: int):
    _position = get_position_by_id(
        db=db, position_id=position_id)
    db.delete(_position)
    db.commit()


# Institution


def get_institution(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Institution).offset(skip).limit(limit).all()


def get_institution_by_id(db: Session, institution_id: int):
    return db.query(Institution).filter(Institution.id == institution_id).first()


def get_institution_by_name(db: Session, institution_name: str):
    return db.query(Institution).filter(Institution.name == institution_name).first()


def create_institution(db: Session, institution: schemas.InstitutionSchema):
    db_institution = models.Institution(**institution.dict())
    db.add(db_institution)
    db.commit()
    db.refresh(db_institution)
    return db_institution


def update_institution(db: Session, institution_id: int, institution: schemas.InstitutionSchema):
    _institution = get_institution_by_id(
        db=db, institution_id=institution_id)

    _institution.name = institution.name

    db.commit()
    db.refresh(_institution)
    return _institution


def remove_institution(db: Session, institution_id: int):
    _institution = get_institution_by_id(
        db=db, institution_id=institution_id)
    db.delete(_institution)
    db.commit()
