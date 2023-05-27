import numpy as np

def optimal(df,min_DC,max_DC,step):
best= None
max_pnl=float("-inf")

for threshold in np.arange(min_DC,max_DC,step):
event_sequence =intrinsic_event_algo(df, 'mid', threshold)
results=dc_reversal_strategy(event_sequence,df)

if results['total_pnl']> max_pnl:
max_pnl=results['total_pnl']
best_threshold = threshold
return best_threshold, max_pnl
min_DC=0.01
max_DC=0.05
step=0.01
optimal_DC,max_pnl=optimal(df,min_DC,max_DC,step)
print("OPTIMAL DC THRESHOLD:",optimal_DC)
print("max pnl",max_pnl)
