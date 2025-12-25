CREATE TABLE IF NOT EXISTS grades (
    id SERIAL PRIMARY KEY,
    grade_date DATE NOT NULL,
    group_number VARCHAR(10) NOT NULL,
    full_name TEXT NOT NULL,
    grade INTEGER NOT NULL CHECK (grade BETWEEN 2 AND 5)
);

CREATE INDEX idx_grades_full_name ON grades(full_name);
CREATE INDEX idx_grades_grade ON grades(grade);