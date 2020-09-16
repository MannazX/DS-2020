#bank.py with solutions by Magnus Sverdrup

def calculate_balance(transactions):
	balance = 0
	for movement in transactions:
		balance += movement
	
	return balance

def calculate_compound(account_balance, rate, years):
	new_balance = account_balance*(1+rate)**years
	
	return new_balance


def filter_withdrawals(transactions):
	withdrawals = []
	for movement in transactions:
		if movement < 0:
			withdrawals.append(movement)
	
	return withdrawals


def risk_analysis(transactions):
	largest_withdraw = transactions[0]
	for movement in transactions:
		if movement < largest_withdraw:
			largest_withdraw = movement

	return largest_withdraw

def join_records(names, transactions):
	records = []
	for idx in range(len(names)):
		records.append((names[idx], transactions[idx]))

	return records


def unique_deposit_names(joined_transactions):
	special_record = []
	for idx in range(len(joined_transactions)):
		if joined_transactions[idx][1] > 0:
			if joined_transactions[idx][0] == joined_transactions[idx][0].lower():
				special_record.append(joined_transactions[idx][0])
	
	return special_record			

def main():
	#calculate balance example
	transactions = [100 , 5000 , -30, -1200]
	balance = calculate_balance(transactions)
	print(balance) #Expected output: 3870

	#calculate compound example
	compound_balance = calculate_compound(500 , 0.05 , 25)
	print(compound_balance) #Expected outuput: 1693.17[...]

	#filter withdrawals example
	withdrawals = filter_withdrawals(transactions)
	print(withdrawals) #Expected outuput: [-30, -1200]

	#risk analysis example 
	transactions = [-5000, 200, 120, -99999] 
	risk = risk_analysis(transactions)
	print(risk)#Expected outuput: -99999

	#join records example
	names = ['Muhammed', 'emma', 'Emma', 'julie']
	joined_transactions = join_records(names, transactions)
	print(joined_transactions)#Expected outuput: [( ’Muhammed’ , −5000), ( ’emma’ , 200), ( ’Emma’ , 120), ( ’ julie ’ , −99999)]

	#unique deposit names example
	unique_names = unique_deposit_names(joined_transactions)
	print(unique_names) #Expected outuput: ['emma']


if __name__ == "__main__":
	# execute only if run as a script
	main()


