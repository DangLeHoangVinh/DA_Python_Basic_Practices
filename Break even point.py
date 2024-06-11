# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 21:24:29 2024

@author: X1 Carbon Gen 7
"""

import matplotlib.pyplot as plt

#-------------------- Nhập dữ liệu -------------------------------------
Units = float(input('Your units is: '))
SellPrice = float(input('Your selling price per unit is: '))
Variable = float(input('Variable cost per unit is: ' ))
Fixed = float(input('Fixed cost for this year is: ' ))
TargetProfit = float(input('Target Profit for this year is: ' ))

#------------------------------Tính toán ----------------------------
CM_Ratio = SellPrice-Variable  # Contribution Margin Ratio 
CM = Units*SellPrice - Units*Variable # Contribution Margin

print (f'\n\n Your Contribution Margin per unit is:  {CM:.2f}' )
NC = CM - Fixed # Net income
print (f'\n\n Your Net Income per unit is:  {NC:.2f}' )
NumberofUnits = (Fixed + TargetProfit) / CM_Ratio

BEP = Fixed/CM_Ratio # Break-Even Point
BEPS = Fixed/(CM_Ratio/SellPrice) # Break-Even Point in Sales

print (f'\n Your break even point in units is:  {BEP:.2f} ' 
       + f'\n\n Your break even point in total sales dollars is:  {BEPS:.2f}')


# plt.plot([0, 10],[12, 12 + 2], color='red', label='Fixed Costs')   vẽ đường thẳng đi qua 2 điểm: 0,12 và 10, 12 + 2
#plt.plot([0, 12, 16],[12, 12 + 2, 10], color='red', label='Fixed Costs') text đường bẻ gốc,

plt.plot([0, Fixed + 2 * BEP],[Fixed, Fixed], color='red', label='Fixed Costs')   # [x1,x2,x3] [y1,y2,y3 ]

# Fixed Costs
#plt.plot([0, Fixed],[Fixed, Fixed + 2 * BEP], color='red', label='Fixed Costs')
# Total Costs (Fixed + Variable)
plt.plot([0, 2 * BEP],[Fixed, Fixed + Variable * 2 * BEP], color='orange',label='Total Costs (Fixed + Variable)')
# Revenue
plt.plot([0, 2 * BEP],[0, SellPrice * 2 * BEP], color='green',label='Revenue')

# Break-Even Point
plt.plot([BEP]*2,[0, BEPS], color='black', linestyle='--', lw=1 ,marker = 'o', markerfacecolor = 'red', markersize = 6) # [BEP]*2 = [BEP,BEP]
plt.plot([0, BEP],[BEPS]*2, color='black', linestyle='--', lw=1 ,marker = 'o', markerfacecolor = 'red', markersize = 6)

plt.scatter(NumberofUnits, Fixed+BEPS+TargetProfit, c ="blue", linewidths = 2, marker ="*", label='Target Profit: 100.000 (USD)')
#plt.plot([0,NumberofUnits],[Fixed+BEPS+TargetProfit,Fixed+BEPS+TargetProfit],color='black', linestyle='--', lw=1 ,marker = 'o', markerfacecolor = 'red', markersize = 6)
#plt.plot([NumberofUnits,NumberofUnits],[0,Fixed+BEPS+TargetProfit],color='black', linestyle='--', lw=1 ,marker = 'o', markerfacecolor = 'red', markersize = 6)

plt.legend()
plt.title('Break-Even Analysis by Rinez')
plt.ylabel('Sales in Dollars')
plt.xlabel('Units Sold')

plt.ylim(bottom=0)
plt.xlim(left=0)
plt.xlim(right=2*BEP)
plt.show()





