#!/opt/homebrew/bin/python3
# -*- coding:utf-8 -*-
'''
https://foobar.withgoogle.com

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases -- 
Input:
solution.solution(15324)
Output:
    15129,169,25,1

Input:
solution.solution(12)
Output:
    9,1,1,1

==========
Code Hints
==========
Pannels are squares. I think I have to square a number?
the gave an example:
	3x3 leaving 3sq yards then that bexomes 1x1   
	the 12 sq yards becomes: 12 > 9 leaving 3 > 1/1/1
It also mentioned the input being 1 <= input <= 1000000 (inclusive)
'''

def solution(material_area):
	'''
	This is where we handle the reamining material,
	we also use this space to ponder the promotion we will get.
	Commander Lambda is going to love this solution! right?
	'''
	panels = []
	panel_material = material_area
	while 1000000 >= panel_material >= 1:
		panels.append(cut_out(panel_material))
		panel_material = panel_material - cut_out(panel_material)
	return ','.join([str(panel) for panel in panels])

def cut_out(material_remaining):
	'''
	this is where we cutout material, 
	no need to calculate the extra square, 
	we can just *know* when we hit the largest.
	'''
	new_panel = 0
	area_base = -1
	while area_base * 2 + new_panel < material_remaining:
		area_base += 1
		new_panel = area_base ** 2
	return new_panel
