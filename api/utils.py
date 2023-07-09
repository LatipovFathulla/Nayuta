import os
import glob
from datetime import datetime, timedelta

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph
from reportlab.lib import colors
import re

from api.common import format_number
from api.serializers import CreditSerializer
from bank import settings


def generate_pdf(payments, price, down_payment_percentage, loan_amount, interest_rate, payment_schedule, loan_period,
                 total_payments, overpayment):
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

    output_folder = os.path.join(settings.MEDIA_ROOT, 'pdf')

    # Удаляем файлы в папке media/pdf, которые старше 2 дней
    delete_old_files(output_folder, days=2)

    filename = os.path.join(output_folder, 'results.pdf')

    doc = SimpleDocTemplate(filename, pagesize=letter, title="info prices")

    # Создаем список данных заголовка
    header_data = [
        # [Image('static/nayuta.png', width=2 * inch, height=2 * inch, hAlign='CENTER')],
        [Paragraph('<b>Nayuta.uz</b>', getSampleStyleSheet()['Heading1'])],
        ['Цена', format_number(price)],
        ['Первоначального взнос %', f'{down_payment_percentage}%'],
        ['Сумма кредита', format_number(loan_amount)],
        ['Процентная ставка', re.sub(r'^0,', '', format_number(interest_rate)).lstrip('0.') + '%'],
        # Форматируем процентную ставку
        ['График платежей', get_payment_schedule_label(payment_schedule)],
        ['Срок кредита', str(loan_period)],
        ['Общие выплаты', format_number(total_payments)],
        ['Переплата', format_number(overpayment)],
        # ['Переплата', format_number(get_overpayment)],  # Удалено преобразование в число с плавающей запятой
    ]

    # Создаем таблицу заголовков и задаем стили
    header_table = Table(header_data, colWidths=[150, 150])
    header_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
        ('FONTSIZE', (0, 0), (-1, -1), 12, 'Arial'),
        ('LEADING', (0, 0), (-1, -1), 15),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('ALIGN', (-1, 0), (-1, -1), 'RIGHT'),
        ('ALIGN', (0, 0), (0, -5), 'LEFT'),
    ]))

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
        ('BACKGROUND', (0, 0), (-1, 0), '#5c7ae8'),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Arial'),
        ('FONTSIZE', (0, 0), (-1, 0), 12, 'Arial'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('LEFTPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    # Создаем таблицу данных и применяем стили
    table = Table(data, colWidths=[20, 85, 110, 110, 110, 140])
    table.setStyle(table_style)

    # Добавляем таблицу заголовков и таблицу данных в документ
    elements = [header_table, table]

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


def get_payment_schedule_label(schedule):
    if schedule == 'annuity':
        return 'Аннуитетный'
    elif schedule == 'differentiated':
        return 'Дифференцированный'
    else:
        return ''
