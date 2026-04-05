from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.record import FinancialRecord

def get_summary(db: Session, user_id: int):
    records = db.query(FinancialRecord).filter(FinancialRecord.user_id == user_id).all()
    total_income =sum(r.amount for r in records if r.type == "income")
    total_expense = sum(r.amount for r in records if r.type == "expense")
    net_income = total_income - total_expense
    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": net_income
    }
def get_category_breakdown(db: Session, user_id:int):
    results = db.query(
        FinancialRecord.category,
        FinancialRecord.type,
        func.sum(FinancialRecord.amount).label("total")
    ).filter(
        FinancialRecord.user_id == user_id
    ).group_by(
        FinancialRecord.category,
        FinancialRecord.type
    ).all()
    return [{"category": r.category, "type": r.type, "total": r.total} for r in results]

def get_monthly_summary(db: Session, user_id: int):
    results = db.query(
        func.date_trunc("month", FinancialRecord.date).label("month"),
        FinancialRecord.type,
        func.sum(FinancialRecord.amount).label("total")
    ).filter(
        FinancialRecord.user_id == user_id
    ).group_by(
        "month",
        FinancialRecord.type
    ).all()
    return [{"month": r.month, "type": r.type, "total": r.total} for r in results]