#flag version

sales=int(input('sales'))

if sales >= 50000.0:
    sales_quota_met = True
else:
    sales_quota_met = False

if sales_quota_met:
    print('You have met your sales quota!')

#daha açık version

sales2=int(input('sales'))

if sales2 >= 50000.0:
    sales_quota_met2 = True
else:
    sales_quota_met2 = False

if sales_quota_met2 == True:
    print('You have met your sales quota!')


