CREATE_EMPLOYEE= """
INSERT INTO EMPLOYEES(ENAME,
    EPHONE,
    EBIRTH_DATE,
    EGENDER,
    EDESCRIPTION,
    EFILE_PATH,
    PASSWORD)
     VALUES (
    '{ename}',
    '{ephone}',
    '{birth_date}',
    '{gender}',
    '{description}',
    '{file_path}',
    '{password}'
);
"""
UPDATE_EMPLOYEE="""
UPDATE EMPLOYEES
SET 
    ENAME = '{ename}',
    EPHONE = '{ephone}',
    EBIRTH_DATE = '{birth_date}',
    EGENDER = '{gender}',
    EDESCRIPTION = '{description}',
    EFILE_PATH = '{file_path}'
WHERE EID = {eid}; 
"""
READ_EMPLOYEES="""
SELECT 
    e.EID,
    e.ENAME,
    e.EPHONE,
    e.EBIRTH_DATE,
    e.EGENDER,
    e.EDESCRIPTION,
    e.EFILE_PATH,
    e.PASSWORD,
    ARRAY_AGG(DISTINCT h.HNAME) AS HOBBIES,
    ARRAY_AGG(DISTINCT ed.EDUNAME) AS EDUCATIONS
FROM EMPLOYEES e
LEFT JOIN EMPLOYEE_HOBBIES eh ON e.EID = eh.EMPLOYEE_ID
LEFT JOIN HOBBIES h ON eh.HOBBY_ID = h.HID
LEFT JOIN EMPLOYEE_EDUCATIONS ee ON e.EID = ee.EMPLOYEE_ID
LEFT JOIN EDUCATIONS ed ON ee.EDUCATION_ID = ed.EDUID
GROUP BY 
    e.EID, e.ENAME, e.EPHONE, e.EBIRTH_DATE, e.EGENDER, 
    e.EDESCRIPTION, e.EFILE_PATH, e.PASSWORD

"""
READ_EMPLOYEE_BY_ID="""
SELECT 
    e.EID,
    e.ENAME,
    e.EPHONE,
    e.EBIRTH_DATE,
    e.EGENDER,
    e.EDESCRIPTION,
    e.EFILE_PATH,
    e.PASSWORD,
    ARRAY_AGG(DISTINCT h.HNAME) AS HOBBIES,
    ARRAY_AGG(DISTINCT ed.EDUNAME) AS EDUCATIONS
FROM EMPLOYEES e
LEFT JOIN EMPLOYEE_HOBBIES eh ON e.EID = eh.EMPLOYEE_ID
LEFT JOIN HOBBIES h ON eh.HOBBY_ID = h.HID
LEFT JOIN EMPLOYEE_EDUCATIONS ee ON e.EID = ee.EMPLOYEE_ID
LEFT JOIN EDUCATIONS ed ON ee.EDUCATION_ID = ed.EDUID
WHERE e.EID = {eid}
GROUP BY 
    e.EID, e.ENAME, e.EPHONE, e.EBIRTH_DATE, e.EGENDER, 
    e.EDESCRIPTION, e.EFILE_PATH, e.PASSWORD
"""

DELETE_EMPLOYEE_BY_ID="""
DELETE FROM EMPLOYEES WHERE EID = {eid}
"""