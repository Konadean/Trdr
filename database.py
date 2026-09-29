import sqlite3

class Database:

    def __init__(self, database_name : str):
        self.db_connection = sqlite3.connect(database_name)
        self.cursor = self.db_connection.cursor()

    # Creates a table using the provided name with an auto-indexing primary key
    def create_table(self, table_name : str, columns: dict[str, str]) -> None:
        # Buuld the SQL query
        sql = "CREATE TABLE IF NOT EXISTS " + table_name + "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
        i = 0
        for key, val in columns.items():
            sql += key + " " + val
            if i != len(columns)-1:
                sql += ","
            i += 1
        # Execute the SQL query
        self.cursor.execute(sql)
        return
    
    def delete_table(self, table_name : str) -> None:
        self.cursor.execute("DROP TABLE IF EXISTS " + table_name)
        self.db_connection.commit()
        return

    # Deletes all rows from a specific table
    def reset_table(self, table_name : str) -> None:
        self.cursor.execute("DELETE FROM " + table_name)
        self.cursor.execute("DELETE FROM " + table_name + " WHERE name='id'")
        self.db_connection.commit()
        return
    
    
    # Inserts prvided data into the specified table    
    def insert_row(self, table_name : str, columns : tuple[int], vals : tuple[str]) -> None:
        # Build the SQL query
        sql = "INSERT INTO " + table_name + str(columns) + " VALUES ("
        for i in range(len(columns)):
            sql += "?"
            if i != len(columns)-1:
                sql += ","
        sql += ")"
        # Execute the SQL query
        self.cursor.execute(sql, vals)
        # Save Changes to DB File
        self.db_connection.commit()
        return
    
    # Takes the table name and row index and deletes said row  
    def delete_row(self, table_name : str, id : int) -> None:
        # Build SQL query
        sql = "DELETE FROM " + table_name + " WHERE id = ?"
        self.cursor(sql, (id,))
        # Save Changes to DB File
        self.db_connection.commit()
        return
    
    # Prints all tuples of a specified table
    def print_table(self, table_name : str) -> None:
        # Get the column names
        self.cursor.execute("SELECT * FROM " + table_name + " LIMIT 0")
        column_names = [desc[0] for desc in self.cursor.description]
        num_cols = len(column_names)
        # Load table into cursor
        self.cursor("SELECT * FROM " + table_name)
        # Extract results into local var
        rows = self.cursor.fetchall()
        # Determine the max length entry per column
        max_length_col = [0 for i in range(num_cols)]
        for i in range(len(rows)):
            for j in range(num_cols):
                if len(str(rows[i][j])) > max_length_col[j]:
                    max_length_col[j] = rows[i][j]



        return
    
    def print_formatted_table(self, table_name : str) -> None:
        self.cursor.execute("SELECT * FROM " + table_name)
        column_names = [description[0] for description in self.cursor.description]
        rows = self.cursor.fetchall()
        max_length = [len(col) for col in column_names]
        for row in rows:
            for i in range(len(row)):
                if len(str(row[i])) > max_length[i]:
                    max_length[i] = len(row[i])
        # Print table top border
        print('_'*(1+len(column_names)+sum(max_length)))
        # Print Column Names
        cur_str = ""
        k = ""
        for i in range(len(column_names)):
            cur_str += "|" + column_names[i] + " "*(max_length[i]-len(column_names[i]))
            k += "|" + "-"*(max_length[i])
        cur_str += "|"
        k += "|"
        print(cur_str)
        print(k)

        for i in range(len(rows)):
            curr_row_str = ""
            for j in range(len(column_names)):
                curr_row_str += "|" + str(rows[i][j]) + " "*(max_length[j]-len(str(rows[i][j])))
            curr_row_str += "|"
            print(curr_row_str)

        # Print Table Botton Border
        bot_str = ""
        for i in range(len(max_length)):
            bot_str += "+" + "-"*(max_length[i])
        bot_str += "+"
        print(bot_str)

        return

    def get_row(self, table_name : str, id : int) -> tuple[str, int]:
        sql = "SELECT * FROM users WHERE id = ?"
        self.cursor.execute(sql, (id,))
        row = self.cursor.fetchone()
        return row