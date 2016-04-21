from virtuoso.virtuoso import ISQLWrapper

isql = ISQLWrapper('33.33.33.13', 'dba', 'dba')
result = isql.execute_cmd("select count(*) from sys_users;")

print result