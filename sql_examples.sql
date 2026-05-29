-- Average Length of Stay by Diagnosis

SELECT
    Diagnosis,
    AVG(LengthOfStay) AS AverageLOS
FROM Patients
GROUP BY Diagnosis;


-- Readmission Counts

SELECT
    Readmitted,
    COUNT(*) AS PatientCount
FROM Patients
GROUP BY Readmitted;


-- Average Age by Diagnosis

SELECT
    Diagnosis,
    AVG(Age) AS AverageAge
FROM Patients
GROUP BY Diagnosis;