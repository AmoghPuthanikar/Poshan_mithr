"""
Admin routes for District CEO dashboard and analytics
"""

from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import json

from app.database import get_db
from app.models import User, Kid, NutritionReport, UserRole
from app.auth import get_current_user_from_cookie

router = APIRouter(prefix="/admin", tags=["admin"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/dashboard", response_class=HTMLResponse)
async def admin_dashboard(request: Request, db: Session = Depends(get_db)):
    """Admin dashboard with aggregated district statistics"""
    current_user = get_current_user_from_cookie(request, db)
    if not current_user or current_user.role != UserRole.ADMIN:
        return RedirectResponse(url="/", status_code=302)

    # Get statistics
    total_kids = db.query(Kid).count()
    total_schools = db.query(User).filter(User.role == UserRole.AUTHORITY).count()

    # Get nutrition status distribution
    from app.models import NutritionStatus

    nutrition_stats = {}
    for status in NutritionStatus:
        count = (
            db.query(NutritionReport).filter(NutritionReport.status == status).count()
        )
        nutrition_stats[status.value] = count

    context = {
        "request": request,
        "current_user": current_user,
        "total_kids": total_kids,
        "total_schools": total_schools,
        "nutrition_stats": json.dumps(nutrition_stats),
    }

    return templates.TemplateResponse("admin_dashboard.html", context)
