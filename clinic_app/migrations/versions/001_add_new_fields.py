"""add new fields

Revision ID: 001_add_new_fields
Revises: 
Create Date: 2024-01-15 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '001_add_new_fields'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Добавляем новые поля в app_patient
    op.add_column('app_patient', sa.Column('email', sa.String(100), nullable=True))
    op.add_column('app_patient', sa.Column('phone', sa.String(20), nullable=True))
    op.add_column('app_patient', sa.Column('created_at', sa.DateTime(), nullable=True))
    
    # Добавляем новые поля в app_doctor
    op.add_column('app_doctor', sa.Column('specialty', sa.String(100), nullable=True))
    op.add_column('app_doctor', sa.Column('license_number', sa.String(50), nullable=True))
    
    # Добавляем новые поля в app_medicine
    op.add_column('app_medicine', sa.Column('dosage', sa.String(100), nullable=True))
    op.add_column('app_medicine', sa.Column('manufacturer', sa.String(150), nullable=True))
    
    # Добавляем новые поля в app_appointment
    op.add_column('app_appointment', sa.Column('status', sa.String(20), nullable=True))
    op.add_column('app_appointment', sa.Column('follow_up_date', sa.Date(), nullable=True))
    op.add_column('app_appointment', sa.Column('created_at', sa.DateTime(), nullable=True))
    
    # Устанавливаем дефолтные значения для новых полей
    op.execute("UPDATE app_appointment SET status = 'completed' WHERE status IS NULL")
    op.execute("UPDATE app_patient SET created_at = NOW() WHERE created_at IS NULL")
    op.execute("UPDATE app_appointment SET created_at = NOW() WHERE created_at IS NULL")

def downgrade():
    # Удаляем добавленные поля
    op.drop_column('app_appointment', 'created_at')
    op.drop_column('app_appointment', 'follow_up_date')
    op.drop_column('app_appointment', 'status')
    
    op.drop_column('app_medicine', 'manufacturer')
    op.drop_column('app_medicine', 'dosage')
    
    op.drop_column('app_doctor', 'license_number')
    op.drop_column('app_doctor', 'specialty')
    
    op.drop_column('app_patient', 'created_at')
    op.drop_column('app_patient', 'phone')
    op.drop_column('app_patient', 'email')
