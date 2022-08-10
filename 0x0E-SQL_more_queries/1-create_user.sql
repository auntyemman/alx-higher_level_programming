--This creates the MySQL server user 'user_0d_1' with priviledges.

CREATE USER user_0d_1 IF NOT EXISTS

GRANT SELECT 

ON *.* 

TO user_0d_1@localhost
IDENTIFIED BY user_0d_1_pwd;
