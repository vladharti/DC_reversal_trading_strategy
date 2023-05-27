def dc_reversal_strategy(event_sequence, df):
initial_equity = 1.0 # Initial capital
position = None
pnl = []
equity_curve= initial_equity

for index, event in event_sequence.iterrows():
if event['type'] != 'DC':
continue

event_time = event['timestamp']
price_data = df[df['timestamp'] == event_time].iloc[0]

# Follow the reverse of directional change
if event['direction'] == 'up':
signal = 'sell'
elif event['direction'] == 'down':
signal = 'buy'

if position:
# Calculate the PnL
if position['type'] == 'buy':
pnl.append(price_data['bid'] - position['price'])
elif position['type'] == 'sell':
pnl.append(position['price'] - price_data['ask'])

position = None

# Open a position
if signal == 'buy':
position = {'price': price_data['ask'], 'type': 'buy'}
elif signal == 'sell':
position = {'price': price_data['bid'], 'type': 'sell'}

# Calculate the final PnL and the equity curve
total_pnl = sum(pnl)
equity_curve = [initial_equity + sum(pnl[:i+1]) for i in range(len(pnl))]
equity_curve.insert(0,initial_equity)
return {'pnl': pnl, 'total_pnl': total_pnl, 'equity_curve': equity_curve}

# Execute the strategy
results = dc_reversal_strategy(event_sequence, df)

print("PnL per Trade:", results['pnl'])
print("Total PnL:", results['total_pnl'])
print("Equity Curve:", results['equity_curve'])
