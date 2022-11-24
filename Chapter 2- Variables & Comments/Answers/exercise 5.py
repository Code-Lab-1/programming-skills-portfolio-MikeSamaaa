Budget = 50 # 50 // 6 = 8
cost_of_usb = 6
usbs_she_can_buy = Budget // cost_of_usb  # floor division was used
remaining_money = 50 % 6  # the percent symbol returns the remainder of the numbers you divided
print(f"It is possible for her to buy {usbs_she_can_buy} usbs and receive a change of £{remaining_money}")
