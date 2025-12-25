from fastapi import FastAPI, UploadFile, HTTPException
import csv, io
from app.db import get_connection
from app.validators import validate_row
from datetime import datetime

app = FastAPI()

@app.post("/upload-grades")
async def upload_grades(file: UploadFile):
    if not file.filename.endswith(".csv"):
        raise HTTPException(400, "Only CSV allowed")

    content = await file.read()
    reader = csv.DictReader(
        io.StringIO(content.decode("utf-8-sig")),
        delimiter=";"
    )

    conn = await get_connection()
    records = 0
    students = set()

    try:
        for row in reader:
            validate_row(row)

            await conn.execute(
                """
                INSERT INTO grades (grade_date, group_number, full_name, grade)
                VALUES ($1, $2, $3, $4)
                """,
                datetime.strptime(row["Дата"], "%d.%m.%Y").date(),
                row["Номер группы"],
                row["ФИО"],
                int(row["Оценка"])
            )

            records += 1
            students.add(row["ФИО"])

    except Exception as e:
        raise HTTPException(400, str(e))
    finally:
        await conn.close()

    return {
        "status": "ok",
        "records_loaded": records,
        "students": len(students)
    }



@app.get("/students/more-than-3-twos")
async def more_than_3_twos():
    conn = await get_connection()
    rows = await conn.fetch(
        """
        SELECT full_name, COUNT(*) AS count_twos
        FROM grades
        WHERE grade = 2
        GROUP BY full_name
        HAVING COUNT(*) > 3
        """
    )
    await conn.close()
    return [dict(row) for row in rows]


@app.get("/students/less-than-5-twos")
async def less_than_5_twos():
    conn = await get_connection()
    rows = await conn.fetch(
        """
        SELECT full_name, COUNT(*) AS count_twos
        FROM grades
        WHERE grade = 2
        GROUP BY full_name
        HAVING COUNT(*) < 5
        """
    )
    await conn.close()
    return [dict(row) for row in rows]
