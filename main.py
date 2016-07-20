from models import *

Applicant.generate_uniqe(Applicant.find_missing_pk())
Applicant.find_school(Applicant.find_missing_city())
