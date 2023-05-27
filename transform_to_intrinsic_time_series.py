def intrinsic_event_algo(df, column, dc_threshold):

#Set up the extreme references, starting with first available value and having 2 extreme references (a max and a min)until the first DC event
reference_extreme = df.at[0, column]
last_dc_direction = None
dc_event = None
dc_os_events = []
init_min= df.at[0, column]
init_max= df.at[0, column]

for index, row in df.iterrows():
curr_price = row[column]
# Calculate price_change and see if it's greater than or equal to the DC threshold
if last_dc_direction==None:
price_change_min=(curr_price-init_min)/init_min
price_change_max=(curr_price-init_max)/init_max
is_dc = max(abs(price_change_max),abs(price_change_min))>= dc_threshold
if abs(price_change_max)>=dc_threshold:
price_change=price_change_max
elif abs(price_change_min)>=dc_threshold:
price_change=price_change_min
else:
price_change = (curr_price - reference_extreme) / reference_extreme
is_dc = abs(price_change) >= dc_threshold

if is_dc:
direction = 'up' if price_change > 0 else 'down'

# Check if the current direction is different from the last_dc_direction
if direction != last_dc_direction:
reference_extreme = curr_price
dc_event = {"timestamp": row["timestamp"], "mid": curr_price,"bid": row["bid"],"ask": row["ask"], "type": "DC", "direction": direction}
if dc_event is not None:
dc_os_events.append(dc_event)
last_dc_direction = direction
dc_event = None
else:
if last_dc_direction==None and curr_price >init_max:
init_max=curr_price
elif last_dc_direction==None and curr_price <init_min:
init_min=curr_price
if (last_dc_direction=='up'and curr_price>reference_extreme) or (last_dc_direction=='down' and curr_price<reference_extreme):
reference_extreme=curr_price
return pd.DataFrame(dc_os_events)

# Create the intrinsic Time series for a DC threshold of 0.01
dc_threshold = 0.01
event_sequence = intrinsic_event_algo(df, 'mid', dc_threshold)
print(event_sequence)
