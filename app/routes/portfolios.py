# app/routes/portfolios.py
from flask import Blueprint, render_template
from app.models.portfolio import Portfolio

portfolio_bp = Blueprint('portfolio', __name__, url_prefix='/portfolios')

@portfolio_bp.route('/<int:portfolio_id>')
def view_portfolio(portfolio_id):
    """Display detailed view of a single portfolio"""
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    return render_template('portfolio/view.html', portfolio=portfolio)
