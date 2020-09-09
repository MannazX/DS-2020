import math

def calculate_balance(transactions):
	
	#write your function here
	return sum(transactions)

def calculate_compound(account_balance, rate, years):
	#write your function here
	return round(account_balance * (1 + rate) ** years, 2)

def filter_withdrawals(transactions):
	#write your function here
	return list(filter(lambda x: x < 0, transactions))

def risk_analysis(transactions):
	#write your function here
	return min(transactions)

def join_records(names, transactions):
	#write your function here
	return list(zip(names, transactions))

def unique_deposit_names(joined_transactions):
	#write your function here

	# I filter withdrawls as specified.
	# I then unpack(*) and rezip to create pairs of tuples which have (names, names) and (transactions, transactions).
	names = list(zip(*filter(lambda n: n[1] > 0, joined_transactions)))

	# I then use set comprehension because if there's duplicates, they will be removed.
	names_lower = {n.lower() for n in names[0]}

	return list(names_lower)


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
	#Expected output:
	#3870
	#1693.17[...]
	#-99999
	#[( ’Muhammed’ , −5000), ( ’emma’ , 200), ( ’Emma’ , 120), ( ’ julie ’ , −99999)]
	#['emma']

