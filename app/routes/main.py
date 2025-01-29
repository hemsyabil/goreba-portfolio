# app/routes/main.py
from flask import Blueprint, render_template
from flask_login import login_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    name = 'Goreba Portfolio Dashboard'
    
    return render_template(
        'home.html',
        title=name,
        name=name,
        active_page='dashboard'
    )

@main_bp.route('/dashboard')
@login_required  # Add this decorator to protected routes
def dashboard():
    return render_template('dashboard/overview.html')

@main_bp.route('/combined-portfolio')
def combined_portfolio():
    """Combined portfolio view"""
    return render_template('dashboard/combined.html')


