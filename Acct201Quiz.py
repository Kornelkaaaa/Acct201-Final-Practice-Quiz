questions = [

   {
        "question": "What type of cost stays the same in total, regardless of activity level?",
        "options": ["Variable cost", "Fixed cost", "Mixed cost", "Direct cost"],
        "answer": "Fixed cost"
    },
    {
        "question": "Which of the following is a product cost?",
        "options": ["Advertising expense", "Sales commission", "Factory worker wages", "Office rent"],
        "answer": "Factory worker wages"
    },
    {
        "question": "What is the contribution margin if the selling price is $100 and variable cost is $60?",
        "options": ["$40", "$60", "$160", "$100"],
        "answer": "$40"
    },
    {
        "question": "If fixed costs are $30,000 and CM per unit is $10, how many units are needed to break even?",
        "options": ["3,000", "300", "30", "10"],
        "answer": "3,000"
    },
    {
        "question": "If estimated overhead is $100,000 and 5,000 DLH are expected, what is the predetermined overhead rate?",
        "options": ["20", "25", "50", "100"],
        "answer": "20"
    },
    {
        "question": "Which cost should NOT be considered when deciding to outsource a product?",
        "options": ["Avoidable overhead", "Direct labor", "Sunk cost", "Direct materials"],
        "answer": "Sunk cost"
    },
    {
        "question": "If 90% of sales are collected in the month of sale, how much cash is collected from $10,000 sales?",
        "options": ["$9,000", "$1,000", "$10,000", "$0"],
        "answer": "$9,000"
    },
    {
        "question": "What is the final step in a contribution margin income statement?",
        "options": ["Sales", "Operating income", "Fixed costs", "Contribution margin"],
        "answer": "Operating income"
    },
    {
      "question": "Complete the Flexible Budget Performance Report below: Master Budget (100 hours)	--> Sales Revenue	$2,000 | Total Variable Costs	$300 | Total Fixed Costs	$800 /nFlexible Budget (120 hours) ?  /n Total Variable Costs at 120 hours =",
      "options": ["400", "500", "560", "360"],
       "answer": "360"
    },
   {
        "question": "Pasta Disasta, Inc. is preparing its master budget for its first quarter of business. It expects to sell 1,000 pizzas per month. It will purchase enough pizzas so that 100 pizzas are in inventory at all times by purchasing 1,100 pizzas in the first month and 1,000 pizzas in the second and third months. The pizza is expected to cost $3 per pizza. It expects to pay 70% in the month of purchase and the remainder in the following month. Calculate the amount of accounts payable on its budgeted balance at the end of the quarter.",
        "options": ["1000", "900", "800", "700"],
        "answer": "900"
    },
    {
        "question": "Dolittle and Dalley has $4,000 in purchases for January and $5,000 in purchases for February. It expects to pay 70% of its purchases in the month the purchases are made. The remaining amount will be paid in the following month. How much does Dolittle and Dalley include as cash paid for inventory in February?",
        "options": ["5000", "4700", "4500", "4250"],
        "answer": "4700"
    },
    {
        "question": "Pasta Disasta, Inc. is preparing its master budget for its first month of business. It expects to sell 4,000 pizzas per month. It will purchase enough pizzas so that 100 pizzas are in inventory at all times. The pizza is expected to cost $4 per pizza. It expects to pay 70% in the month of purchase and the remainder in the following month. Calculate the amount of budgeted purchases for its first month.",
        "options": ["17,000", "16,500", "16,400", "16,300"],
        "answer": "16,400"
    }
]

score = 0
for i, q in enumerate(questions):
    print(f"\nQuestion {i+1}: {q['question']}")
    for idx, option in enumerate(q['options'], 1):
        print(f"  {idx}. {option}")
    user_input = input("Your answer (type the option number): ")
    try:
        chosen = q['options'][int(user_input) - 1]
        if chosen == q['answer']:
            print("Correct! ✅")
            score += 1
        else:
            print(f"Incorrect ❌ The correct answer is: {q['answer']}")
    except:
        print("Invalid input. Skipping question.")

print(f"\nYour final score: {score}/{len(questions)}")
