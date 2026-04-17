import random
import csv

print("\n" + "="*80)
print("FINANCE RISK CALCULATOR - 50 CUSTOMER ANALYSIS")
print("="*80)

# Set seed for reproducible results
random.seed(42)

# Create sample data with 50 customers
customers = []
for i in range(1, 51):
    customer = {
        'id': i,
        'name': f'Customer_{i}',
        'credit_score': random.randint(500, 800),
        'payment_history': random.choice(['excellent', 'good', 'fair', 'poor']),
        'debt_to_income': random.randint(10, 60),
        'employment_years': random.randint(0, 20)
    }
    customers.append(customer)

# Risk calculation function
def calculate_risk(customer):
    # Credit score (40% weight)
    credit_score = customer['credit_score']
    credit_risk = (850 - credit_score) / 550 * 40
    
    # Payment history (30% weight)
    payment_map = {'excellent': 10, 'good': 30, 'fair': 60, 'poor': 90}
    payment_risk = payment_map[customer['payment_history']] * 0.3
    
    # DTI (20% weight)
    dti_risk = (customer['debt_to_income'] / 60) * 20
    
    # Employment (10% weight)
    emp_risk = max(0, (20 - customer['employment_years']) / 20) * 10
    
    total_risk = credit_risk + payment_risk + dti_risk + emp_risk
    
    if total_risk < 30:
        category = "LOW RISK"
    elif total_risk < 60:
        category = "MEDIUM RISK"
    else:
        category = "HIGH RISK"
    
    return round(total_risk, 1), category

# Calculate risks for all customers
results = []
for customer in customers:
    score, category = calculate_risk(customer)
    results.append({
        'id': customer['id'],
        'name': customer['name'],
        'credit': customer['credit_score'],
        'payment': customer['payment_history'],
        'dti': customer['debt_to_income'],
        'employment': customer['employment_years'],
        'score': score,
        'category': category
    })

# Display table header
print("\n" + "="*80)
print(f"{'ID':<4} {'Name':<12} {'Credit':<7} {'Payment':<10} {'DTI':<5} {'Emp':<5} {'Score':<6} {'Category'}")
print("-"*80)

# Display first 20 customers (to keep output manageable)
for result in results[:20]:
    print(f"{result['id']:<4} {result['name']:<12} {result['credit']:<7} {result['payment']:<10} {result['dti']:<5} {result['employment']:<5} {result['score']:<6} {result['category']}")

print(f"\n... and {len(results) - 20} more customers")

# Summary statistics
low_risk = len([r for r in results if r['category'] == 'LOW RISK'])
medium_risk = len([r for r in results if r['category'] == 'MEDIUM RISK'])
high_risk = len([r for r in results if r['category'] == 'HIGH RISK'])

print("\n" + "="*80)
print("SUMMARY STATISTICS (All 50 Customers)")
print("="*80)
print(f"Low Risk Customers:     {low_risk} ({low_risk/50*100:.0f}%)")
print(f"Medium Risk Customers:  {medium_risk} ({medium_risk/50*100:.0f}%)")
print(f"High Risk Customers:    {high_risk} ({high_risk/50*100:.0f}%)")
print("="*80)

# Show top 5 highest risk customers
print("\n" + "="*80)
print("TOP 5 HIGHEST RISK CUSTOMERS (Need Immediate Attention)")
print("="*80)
high_risk_customers = sorted(results, key=lambda x: x['score'], reverse=True)[:5]
for customer in high_risk_customers:
    print(f"ID: {customer['id']:2d} | {customer['name']:12} | Score: {customer['score']:5.1f} | {customer['category']}")

# Show bottom 5 lowest risk customers
print("\n" + "="*80)
print("TOP 5 LOWEST RISK CUSTOMERS (Best Candidates)")
print("="*80)
low_risk_customers = sorted(results, key=lambda x: x['score'])[:5]
for customer in low_risk_customers:
    print(f"ID: {customer['id']:2d} | {customer['name']:12} | Score: {customer['score']:5.1f} | {customer['category']}")

print("\n" + "="*80)
print("RISK SCORE DISTRIBUTION CHART")
print("="*80)

# Simple bar chart
total = len(results)
bar_length = 40
low_bar = int((low_risk / total) * bar_length)
med_bar = int((medium_risk / total) * bar_length)
high_bar = int((high_risk / total) * bar_length)

print(f"Low Risk    [{'#' * low_bar:<{bar_length}}] {low_risk} customers ({low_risk/50*100:.0f}%)")
print(f"Medium Risk [{'#' * med_bar:<{bar_length}}] {medium_risk} customers ({medium_risk/50*100:.0f}%)")
print(f"High Risk   [{'#' * high_bar:<{bar_length}}] {high_risk} customers ({high_risk/50*100:.0f}%)")

print("\n" + "="*80)
print("WEIGHTED SCORE FORMULA BREAKDOWN")
print("="*80)
print("Formula: Risk Score = (Credit Score x 40%) + (Payment History x 30%) + (DTI x 20%) + (Employment x 10%)")
print("\nFactor Details:")
print("  1. Credit Score: (850 - actual_score) / 550 * 40")
print("     - Higher credit score = Lower risk")
print("     - Range: 500-800 in our dataset")
print("")
print("  2. Payment History: Mapped values * 0.3")
print("     - Excellent = 10 points")
print("     - Good = 30 points")
print("     - Fair = 60 points")
print("     - Poor = 90 points")
print("")
print("  3. Debt-to-Income (DTI): (DTI% / 60) * 20")
print("     - Lower DTI = Lower risk")
print("     - Range: 10-60% in our dataset")
print("")
print("  4. Employment Years: (20 - years) / 20 * 10")
print("     - More years = Lower risk")
print("     - Range: 0-20 years in our dataset")
print("="*80)

# Save results to CSV file
with open('risk_analysis_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name', 'credit', 'payment', 'dti', 'employment', 'score', 'category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for result in results:
        writer.writerow({
            'id': result['id'],
            'name': result['name'],
            'credit': result['credit'],
            'payment': result['payment'],
            'dti': result['dti'],
            'employment': result['employment'],
            'score': result['score'],
            'category': result['category']
        })

print("\n[SUCCESS] Full results saved to 'risk_analysis_results.csv'")
print("You can open this file in Excel to see all 50 customers")
print("="*80)

input("\nPress Enter to exit...")