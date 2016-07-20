from models import *


bp1 = School.create(
    name='BP1'
)

bp2 = School.create(
    name='BP2'
)

miskolc1 = School.create(
    name='Miskolc1'
)

City.create(
    name='Horcsoghalom',
    closest_school=miskolc1
)

City.create(
    name='Karancspuszta',
    closest_school=miskolc1
)

City.create(
    name='Budapest',
    closest_school=bp1
)

Applicant.create(
    name='Lakatos Nintendo',
    city='Karancspuszta',
    email='sukargyerek@gmail.com'
)

Applicant.create(
    name='Kolompar Shakira',
    city='Horcsoghalom',
    email='sukarlejany@gmail.com',
    )

Applicant.create(
    name='Orban Gaspar',
    city='Budapest',
    email='nemkozszereplo@gmail.com',
    )
