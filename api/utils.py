import os
import glob
from datetime import datetime, timedelta

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

from bank import settings

def format_number(number):
    number_str = f"{number:.2f}"
    integer_part, decimal_part = number_str.split('.')
    formatted_integer_part = ''
    for i, digit in enumerate(reversed(integer_part)):
        formatted_integer_part = digit + formatted_integer_part
        if (i + 1) % 3 == 0 and i != len(integer_part) - 1:
            formatted_integer_part = '.' + formatted_integer_part
    return formatted_integer_part + '.' + decimal_part if decimal_part else formatted_integer_part


def generate_pdf(payments):
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

    output_folder = os.path.join(settings.MEDIA_ROOT, 'pdf')

    # Удаляем файлы в папке media/pdf, которые старше 2 дней
    delete_old_files(output_folder, days=2)

    filename = os.path.join(output_folder, 'results.pdf')

    doc = SimpleDocTemplate(filename, pagesize=letter, title="info prices")

    # Создаем список данных таблицы
    data = [
        ['№', 'Дата платежа', 'Сумма платежа', 'Сумма погашения', 'Сумма процентов', 'Остаток задолженности']
    ]

    for payment in payments:
        payment_number = payment['payment_number']
        payment_date = payment['payment_date']
        payment_amount = format_number(payment['payment_amount'])
        principal_amount = format_number(payment['principal_amount'])
        interest_amount = format_number(payment['interest_amount'])
        remaining_balance = format_number(payment['remaining_balance'])
        if isinstance(payment_date, datetime):
            formatted_date = payment_date.strftime("%Y-%m-%d")
        else:
            formatted_date = datetime.strptime(payment_date, "%Y-%m-%d").strftime("%Y-%m-%d")
        data.append([
            str(payment_number),
            formatted_date,
            payment_amount,
            principal_amount,
            interest_amount,
            remaining_balance
        ])

    # Создаем таблицу и задаем стили
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Arial'),
        ('FONTSIZE', (0, 0), (-1, 0), 12, 'Arial'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    # Создаем таблицу и применяем стили
    table = Table(data, colWidths=[20, 85, 110, 110, 110, 140])
    table.setStyle(table_style)

    # Добавляем таблицу в документ
    elements = [table]

    # Сохраняем документ
    doc.build(elements)

    return filename


def delete_old_files(folder, days):
    now = datetime.now()
    files = glob.glob(os.path.join(folder, '*.pdf'))
    for file in files:
        modified_time = datetime.fromtimestamp(os.path.getmtime(file))
        if (now - modified_time) > timedelta(days=days):
            os.remove(file)
