from flask import Flask, render_template
import random

app = Flask(__name__)

# Real customer data
customers_data = [
    {"id": 1, "name": "John Smith", "credit": 557, "payment": "excellent", "dti": 57, "employment": 8},
    {"id": 2, "name": "Emma Johnson", "credit": 625, "payment": "good", "dti": 18, "employment": 3},
    {"id": 3, "name": "Michael Williams", "credit": 779, "payment": "excellent", "dti": 47, "employment": 13},
    {"id": 4, "name": "Sophia Brown", "credit": 516, "payment": "excellent", "dti": 15, "employment": 6},
    {"id": 5, "name": "William Jones", "credit": 619, "payment": "excellent", "dti": 45, "employment": 6},
    {"id": 6, "name": "Olivia Garcia", "credit": 779, "payment": "poor", "dti": 24, "employment": 14},
    {"id": 7, "name": "James Miller", "credit": 642, "payment": "excellent", "dti": 58, "employment": 5},
    {"id": 8, "name": "Ava Davis", "credit": 716, "payment": "fair", "dti": 27, "employment": 4},
    {"id": 9, "name": "Robert Rodriguez", "credit": 610, "payment": "fair", "dti": 16, "employment": 2},
    {"id": 10, "name": "Isabella Martinez", "credit": 694, "payment": "excellent", "dti": 32, "employment": 11},
    {"id": 11, "name": "David Hernandez", "credit": 635, "payment": "excellent", "dti": 56, "employment": 14},
    {"id": 12, "name": "Mia Lopez", "credit": 774, "payment": "excellent", "dti": 34, "employment": 2},
    {"id": 13, "name": "Richard Gonzalez", "credit": 782, "payment": "fair", "dti": 50, "employment": 19},
    {"id": 14, "name": "Charlotte Wilson", "credit": 685, "payment": "good", "dti": 55, "employment": 2},
    {"id": 15, "name": "Joseph Anderson", "credit": 523, "payment": "good", "dti": 59, "employment": 9},
    {"id": 16, "name": "Amelia Thomas", "credit": 540, "payment": "good", "dti": 16, "employment": 12},
    {"id": 17, "name": "Thomas Taylor", "credit": 642, "payment": "poor", "dti": 50, "employment": 11},
    {"id": 18, "name": "Evelyn Moore", "credit": 583, "payment": "fair", "dti": 32, "employment": 6},
    {"id": 19, "name": "Charles Jackson", "credit": 636, "payment": "excellent", "dti": 48, "employment": 20},
    {"id": 20, "name": "Abigail Martin", "credit": 587, "payment": "good", "dti": 20, "employment": 14},
    {"id": 21, "name": "Christopher Lee", "credit": 708, "payment": "good", "dti": 25, "employment": 5},
    {"id": 22, "name": "Emily Perez", "credit": 538, "payment": "poor", "dti": 58, "employment": 3},
    {"id": 23, "name": "Daniel Thompson", "credit": 693, "payment": "good", "dti": 36, "employment": 7},
    {"id": 24, "name": "Harper White", "credit": 788, "payment": "excellent", "dti": 22, "employment": 15},
    {"id": 25, "name": "Matthew Harris", "credit": 651, "payment": "good", "dti": 31, "employment": 9},
    {"id": 26, "name": "Elizabeth Sanchez", "credit": 602, "payment": "fair", "dti": 42, "employment": 4},
    {"id": 27, "name": "Anthony Clark", "credit": 548, "payment": "poor", "dti": 54, "employment": 2},
    {"id": 28, "name": "Sofia Ramirez", "credit": 761, "payment": "excellent", "dti": 28, "employment": 10},
    {"id": 29, "name": "Donald Lewis", "credit": 658, "payment": "good", "dti": 33, "employment": 8},
    {"id": 30, "name": "Avery Robinson", "credit": 525, "payment": "poor", "dti": 56, "employment": 1},
    {"id": 31, "name": "Mark Walker", "credit": 672, "payment": "good", "dti": 29, "employment": 7},
    {"id": 32, "name": "Ella Young", "credit": 795, "payment": "excellent", "dti": 19, "employment": 16},
    {"id": 33, "name": "Paul Allen", "credit": 681, "payment": "good", "dti": 35, "employment": 6},
    {"id": 34, "name": "Madison King", "credit": 559, "payment": "fair", "dti": 52, "employment": 4},
    {"id": 35, "name": "Steven Wright", "credit": 610, "payment": "good", "dti": 44, "employment": 5},
    {"id": 36, "name": "Scarlett Scott", "credit": 745, "payment": "excellent", "dti": 23, "employment": 12},
    {"id": 37, "name": "Andrew Torres", "credit": 665, "payment": "good", "dti": 34, "employment": 8},
    {"id": 38, "name": "Victoria Nguyen", "credit": 598, "payment": "fair", "dti": 41, "employment": 3},
    {"id": 39, "name": "Kenneth Hill", "credit": 544, "payment": "poor", "dti": 55, "employment": 2},
    {"id": 40, "name": "Aria Flores", "credit": 782, "payment": "excellent", "dti": 18, "employment": 14},
    {"id": 41, "name": "Joshua Green", "credit": 635, "payment": "good", "dti": 38, "employment": 6},
    {"id": 42, "name": "Grace Adams", "credit": 795, "payment": "excellent", "dti": 14, "employment": 18},
    {"id": 43, "name": "Kevin Nelson", "credit": 612, "payment": "fair", "dti": 43, "employment": 5},
    {"id": 44, "name": "Chloe Baker", "credit": 770, "payment": "excellent", "dti": 21, "employment": 13},
    {"id": 45, "name": "Brian Hall", "credit": 688, "payment": "good", "dti": 30, "employment": 9},
    {"id": 46, "name": "Camila Rivera", "credit": 545, "payment": "fair", "dti": 57, "employment": 3},
    {"id": 47, "name": "George Campbell", "credit": 720, "payment": "good", "dti": 27, "employment": 11},
    {"id": 48, "name": "Penelope Mitchell", "credit": 755, "payment": "excellent", "dti": 24, "employment": 15},
    {"id": 49, "name": "Edward Carter", "credit": 660, "payment": "good", "dti": 35, "employment": 7},
    {"id": 50, "name": "Riley Roberts", "credit": 590, "payment": "fair", "dti": 46, "employment": 4},
]

def calculate_risk(customer):
    credit_risk = (850 - customer['credit']) / 550 * 40
    payment_map = {'excellent': 10, 'good': 30, 'fair': 60, 'poor': 90}
    payment_risk = payment_map[customer['payment']] * 0.3
    dti_risk = (customer['dti'] / 60) * 20
    emp_risk = max(0, (20 - customer['employment']) / 20) * 10
    
    total_risk = credit_risk + payment_risk + dti_risk + emp_risk
    
    if total_risk < 30:
        category = "Low Risk"
        interest_rate = "8-10%"
    elif total_risk < 60:
        category = "Medium Risk"
        interest_rate = "12-15%"
    else:
        category = "High Risk"
        interest_rate = "18-22%"
    
    return round(total_risk, 1), category, interest_rate

# Process customers
customers = []
for data in customers_data:
    score, category, interest_rate = calculate_risk(data)
    customers.append({
        'id': data['id'],
        'name': data['name'],
        'credit_score': data['credit'],
        'payment_history': data['payment'],
        'debt_to_income': data['dti'],
        'employment_years': data['employment'],
        'risk_score': score,
        'risk_category': category,
        'interest_rate': interest_rate
    })

@app.route('/')
def index():
    low_risk = len([c for c in customers if c['risk_category'] == 'Low Risk'])
    medium_risk = len([c for c in customers if c['risk_category'] == 'Medium Risk'])
    high_risk = len([c for c in customers if c['risk_category'] == 'High Risk'])
    avg_score = sum([c['risk_score'] for c in customers]) / len(customers)
    
    highest_risk = sorted(customers, key=lambda x: x['risk_score'], reverse=True)[:5]
    lowest_risk = sorted(customers, key=lambda x: x['risk_score'])[:5]
    
    return render_template('index.html', 
                         customers=customers,
                         low_risk=low_risk,
                         medium_risk=medium_risk,
                         high_risk=high_risk,
                         avg_score=round(avg_score, 1),
                         highest_risk=highest_risk,
                         lowest_risk=lowest_risk)

@app.route('/customer/<int:customer_id>')
def customer_detail(customer_id):
    customer = next((c for c in customers if c['id'] == customer_id), None)
    if customer:
        return render_template('detail.html', customer=customer)
    return "Customer not found", 404

if __name__ == '__main__':
    print("\n" + "="*50)
    print("RISK CALCULATOR - REAL CUSTOMER NAMES")
    print("="*50)
    print(f"Loaded {len(customers)} customers with real names")
    print("Open: http://127.0.0.1:5000")
    print("="*50 + "\n")
    app.run(debug=True)