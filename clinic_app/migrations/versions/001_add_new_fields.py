"""initial_full_schema_with_new_fields

Revision ID: merged_20251218
Revises: 
Create Date: 2025-12-18 05:50:00.000000
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'merged_20251218'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Таблица doctor
    op.create_table(
        'doctor',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=150), nullable=False),
        sa.Column('specialty', sa.String(length=100), nullable=True),
        sa.Column('license_number', sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Таблица medicine
    op.create_table(
        'medicine',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False, unique=True),
        sa.Column('usage', sa.Text(), nullable=False),
        sa.Column('action', sa.Text(), nullable=False),
        sa.Column('side_effects', sa.Text(), nullable=False),
        sa.Column('dosage', sa.String(length=100), nullable=True),
        sa.Column('manufacturer', sa.String(length=150), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Таблица patient
    op.create_table(
        'patient',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=150), nullable=False),
        sa.Column('gender', sa.String(length=10), nullable=False),
        sa.Column('birth_date', sa.Date(), nullable=False),
        sa.Column('address', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=True),
        sa.Column('phone', sa.String(length=20), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Таблица appointment
    op.create_table(
        'appointment',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('location', sa.String(length=100), nullable=False),
        sa.Column('symptoms', sa.Text(), nullable=False),
        sa.Column('diagnosis', sa.String(length=150), nullable=False),
        sa.Column('prescription', sa.Text(), nullable=False),
        sa.Column('status', sa.String(length=20), nullable=True),
        sa.Column('follow_up_date', sa.Date(), nullable=True),
        sa.Column('patient_id', sa.Integer(), nullable=False),
        sa.Column('doctor_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['doctor_id'], ['doctor.id']),
        sa.ForeignKeyConstraint(['patient_id'], ['patient.id']),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('appointment')
    op.drop_table('patient')
    op.drop_table('medicine')
    op.drop_table('doctor')
