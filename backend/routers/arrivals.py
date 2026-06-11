from fastapi import APIRouter, Depends, Query
from sqlalchemy import text
from sqlalchemy.orm import Session

from ..database import get_db
from .auth import get_current_user


router = APIRouter()


@router.get("/")
async def get_arrivals(
    year: int = Query(None, description="Filter by year"),
    country: str = Query(None, description="Filter by country"),
    limit: int = Query(100, description="Max records"),
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    """
    Tourist arrivals data
    Optional filters: year, country
    """

    query = """
        SELECT
            year,
            month,
            country_name,
            country_code,
            arrivals,
            purpose,
            entry_point
        FROM tourist_arrivals
        WHERE 1=1
    """

    params = {}

    if year:
        query += " AND year = :year"
        params["year"] = year

    if country:
        query += " AND country_name ILIKE :country"
        params["country"] = f"%{country}%"

    query += " ORDER BY year DESC, month DESC, arrivals DESC"
    query += f" LIMIT {limit}"

    results = db.execute(text(query), params).fetchall()

    total_query = """
        SELECT SUM(arrivals) as total
        FROM tourist_arrivals
        WHERE 1=1
    """
    if year:
        total_query += " AND year = :year"
    if country:
        total_query += " AND country_name ILIKE :country"

    total = db.execute(text(total_query), params).fetchone()

    return {
        "data":           [dict(r._mapping) for r in results],
        "count":          len(results),
        "total_arrivals": int(total.total or 0),
        "filters": {
            "year":    year,
            "country": country,
        }
    }


@router.get("/by-country")
async def get_arrivals_by_country(
    year: int = Query(None),
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    """
    Arrivals grouped by country
    Dashboard pie/bar chart data
    """

    query = """
        SELECT
            country_name,
            country_code,
            SUM(arrivals) as total_arrivals
        FROM tourist_arrivals
        WHERE 1=1
    """

    params = {}
    if year:
        query += " AND year = :year"
        params["year"] = year

    query += """
        GROUP BY country_name, country_code
        ORDER BY total_arrivals DESC
        LIMIT 20
    """

    results = db.execute(text(query), params).fetchall()

    return {
        "data":  [dict(r._mapping) for r in results],
        "year":  year,
        "count": len(results)
    }


@router.get("/by-year")
async def get_arrivals_by_year(
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    """
    Yearly totals — trend chart data
    """

    results = db.execute(text("""
        SELECT
            year,
            SUM(arrivals)              as total_arrivals,
            COUNT(DISTINCT country_name) as source_countries
        FROM tourist_arrivals
        GROUP BY year
        ORDER BY year ASC
    """)).fetchall()

    return {
        "data":  [dict(r._mapping) for r in results],
        "count": len(results)
    }


@router.get("/summary")
async def get_arrivals_summary(
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    """
    Dashboard KPI cards data
    """

    # Latest year
    latest = db.execute(text("""
        SELECT MAX(year) as latest_year
        FROM tourist_arrivals
    """)).fetchone()

    latest_year = latest.latest_year or 2024

    # This year total
    this_year = db.execute(text("""
        SELECT SUM(arrivals) as total
        FROM tourist_arrivals
        WHERE year = :year
    """), {"year": latest_year}).fetchone()

    # Last year total
    last_year = db.execute(text("""
        SELECT SUM(arrivals) as total
        FROM tourist_arrivals
        WHERE year = :year
    """), {"year": latest_year - 1}).fetchone()

    # Top source country
    top_country = db.execute(text("""
        SELECT country_name, SUM(arrivals) as total
        FROM tourist_arrivals
        WHERE year = :year
        GROUP BY country_name
        ORDER BY total DESC
        LIMIT 1
    """), {"year": latest_year}).fetchone()

    # YoY growth calculate
    this_total = int(this_year.total or 0)
    last_total = int(last_year.total or 1)
    growth_pct = round(
        ((this_total - last_total) / last_total) * 100, 2
    )

    return {
        "latest_year":        latest_year,
        "total_arrivals":     this_total,
        "previous_year":      last_total,
        "growth_percent":     growth_pct,
        "top_source_country": top_country.country_name if top_country else None,
    }