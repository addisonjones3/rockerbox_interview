from rockerbox_pref_parse import parse_prefix_expression

t0 = '1'  # 1
t1 = '* + 2 3 4'  # 20
t2 = '+ 9 * 2 6'  # 21
t3 = '* + 1 + + 2 3 4 + 5 + 6 7'  # 180
t4 = '/ 3 4'  # .75
comb = '1\n' \
       '* + 2 3 4\n' \
       '+ 9 * 2 6\n' \
       '* + 1 + + 2 3 4 + 5 + 6 7p \n' \
       '/ -3 + 4 5\n' \
       '- -1 1'

comb_same_line = '1\n* + 2 3 4\n+ 9 * 2 6\n* + 1 + + 2 3 4 + 5 + 6 7p \n/ -3 4\n- -1 1'

t_div_0 = '+ 1 1\n' \
          '/ 1 0\n' \
          '\n' \
          '* 3 2\n'

t_mult_0 = '* 2 0'

t_multi_space = '/ 2     2\n' \
                '+ 1   +  4   2'

t_all_issues = '1\n' \
               '* + 2 3 4\n' \
               '+ 9 * 2 6\n' \
               '* + 1 + + 2 3 4 + 5 + 6 7p \n' \
               '/ -3 + 4 5\n' \
               '- -1 1\n' \
               '/ 1 0\n' \
               '\n' \
               '+ + 1 1'

t_tab_delim = '+\t1\t2'

# parse_prefix_expression(t0)
# parse_prefix_expression(t1)
# parse_prefix_expression(t2)
# parse_prefix_expression(comb)
# parse_prefix_expression(t0)
# parse_prefix_expression(comb)
parse_prefix_expression(t_multi_space)
parse_prefix_expression(t_tab_delim, token_delimiter='\t')
"""
~3 - 4 hours to research what prefix expressions are (without looking for solutions)
and write the solution.

~1 hour tweaking for command line arguments. I'm not especially experienced
with passing to command line, so that took a little bit of work. 

~2 hours making it more resilient which was likely huge overkill
"""