# שימוש בתמונת בסיס קלה של פייתון
FROM python:3.9-slim

# הגדרת תיקיית העבודה בתוך הקונטיינר
WORKDIR /app

# העתקת קובץ הדרישות והתקנת הספריות
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# העתקת שאר קבצי הפרויקט לקונטיינר
COPY . .

# יצירת תיקייה עבור המידע (בשביל ה-Volume)
RUN mkdir -p /app/data

# חשיפת פורט 90 (הגדרת השירות כפי שביקשת)
EXPOSE 90

# הפקודה להרצת האפליקציה
CMD ["python", "app.py"]
