def query_func1(pattern_list=[], *args):
    # def # print(length)
    query_pattern = 'comment_message like  %' + pattern_list[0] + '%'
    if len(pattern_list) > 1:
        for i in range(1, len(pattern_list)):
            query_pattern += ' OR comment_message like  %' + pattern_list[i] + '%'
    return query_pattern


# print query_pattern
lst1 = ['extra', 'twoextra']
sub_query1 = str(query_func1(lst1))

sql1 = "select * from (SELECT company,comment_message, comment_published FROM shuni_database.apps_comment WHERE company='Grameenphone' and comment_published between '2017-07-28T00:00:00' and '2017-07-30T00:00:00' )a WHERE " + sub_query1+" ;"

#print(sql1+'\n\n\n')





def query_func(pattern_list=[], *args):
        cm = 'comment_message LIKE';
        or_cm = ' OR comment_message LIKE';
        q1 = cm + " '% " + pattern_list[0] + " %' ";
        q2 = or_cm + " '" + pattern_list[0] + "' ";
        q3 = or_cm + " '" + pattern_list[0] + " %' ";
        q4 = or_cm + " '% " + pattern_list[0] + "' ";
        q5 = or_cm + " '%" + pattern_list[0] + " %' ";
        q6 = or_cm + " '%" + pattern_list[0] + "' ";
        patter_query = q1 + q2 + q3 + q4 + q5 + q6;
        #print(cm);
        #print(patter_query);
        query_pattern = patter_query
        #print(query_pattern)
        for i in range(1, len(pattern_list)):
            or_q1 = or_cm + " '% " + pattern_list[i] + " %' ";
            or_q2 = or_cm + " '" + pattern_list[i] + "' ";
            or_q3 = or_cm + " '" + pattern_list[i] + " %' ";
            or_q4 = or_cm + " '% " + pattern_list[i] + "' ";
            or_q5 = or_cm + " '%" + pattern_list[i] + " %' ";
            or_q6 = or_cm + " '%" + pattern_list[i] + "' ";
            or_patter_query = or_q1 + or_q2 + or_q3 + or_q4 + or_q5 + or_q6;
            #print(or_patter_query)
            query_pattern += or_patter_query
        return query_pattern

lst = ['4g', '৪জি'];
sub_query = str(query_func(lst))
#print(sub_query)

sql_query = "select * from (SELECT company,comment_message, comment_published FROM apps_comment WHERE company='banglalinkmela' and comment_published between '2017-11-16 00:00:00' and '2017-11-27 23:59:59' )a WHERE " + sub_query+" ;"

print(sql_query)
