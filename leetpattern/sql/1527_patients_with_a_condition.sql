-- Task: Report patients with Type I diabetes, identified by a condition code
-- beginning with DIAB1 in their space-separated conditions list.
SELECT -- Return all requested details for qualifying patients.
    patient_id, -- Identify the patient.
    patient_name, -- Show the patient's name.
    conditions -- Preserve their full list of conditions.
FROM Patients -- Read patient records.
-- Match DIAB1 only at the beginning of a condition, not inside another code.
WHERE conditions REGEXP '(^| )DIAB1';
