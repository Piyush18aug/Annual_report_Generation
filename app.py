from flask import Flask, request, send_file, render_template
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

def create_report(trophies, prizes, colors, merits, academic_year, academic_prizes, department):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    c.setFont('Helvetica-Bold', 16)
    c.drawString(200, 800, 'College Achievement Report')

    c.setFont('Helvetica', 12)
    y_position = 750

    c.drawString(50, y_position, f"Department: {department}")
    y_position -= 20

    if trophies:
        c.drawString(50, y_position, "Trophies and Cups Won by College:")
        y_position -= 20
        for award, student in trophies:
            c.drawString(50, y_position, f"- {award} (Student: {student})")
            y_position -= 20

    if prizes:
        c.drawString(50, y_position, "Prizes for Distinction Achieved:")
        y_position -= 20
        for award, student in prizes:
            c.drawString(50, y_position, f"- {award} (Student: {student})")
            y_position -= 20

    if colors:
        c.drawString(50, y_position, "College Colors for Outstanding Performance:")
        y_position -= 20
        for award, student in colors:
            c.drawString(50, y_position, f"- {award} (Student: {student})")
            y_position -= 20

    if merits:
        c.drawString(50, y_position, "Certificates of Merit:")
        y_position -= 20
        for award, student in merits:
            c.drawString(50, y_position, f"- {award} (Student: {student})")
            y_position -= 20

    if academic_year and academic_prizes:
        c.drawString(50, y_position, f"Academic Prizes for the Year {academic_year}:")
        y_position -= 20
        for award, student in academic_prizes:
            c.drawString(50, y_position, f"- {award} (Student: {student})")
            y_position -= 20

    c.save()
    buffer.seek(0)
    return buffer

@app.route('/generate_report', methods=['POST'])
def generate_report():
    try:
        department = request.form.get('department')

        trophies = list(zip(request.form.getlist('trophy_type[]'), request.form.getlist('trophy_student[]')))
        prizes = list(zip(request.form.getlist('prize_type[]'), request.form.getlist('prize_student[]')))
        colors = list(zip(request.form.getlist('color_type[]'), request.form.getlist('color_student[]')))
        merits = list(zip(request.form.getlist('merit_type[]'), request.form.getlist('merit_student[]')))
        academic_year = request.form.get('year')
        academic_prizes = list(zip(request.form.getlist('academic_type[]'), request.form.getlist('academic_student[]')))

        if not department or not academic_year:
            return "Department and academic year are required fields", 400

        pdf_buffer = create_report(trophies, prizes, colors, merits, academic_year, academic_prizes, department)
        
        return send_file(pdf_buffer, as_attachment=True, download_name='college_report.pdf', mimetype='application/pdf')
    
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == "__main__":
    app.run(port=5000, debug=True) 
