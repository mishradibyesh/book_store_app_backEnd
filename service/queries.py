"""
@author: Dibyesh Mishra
@date: 20-01-2022 16:57
"""
from core.connection import DbConnection
from custom_exceptions.custom_exception import DataNotFound


class Functionality:
    """
    class Functionality have methods which helping to manipulate the database  user_details and books table
    in database book_store_app
    """
    connection = DbConnection.establish_connection()
    my_cursor = connection.cursor(dictionary=True)

    def show_table_data(self):
        """
        desc: displaying the user_details table
        return: data_list
        """

        query = "select * from user "
        self.my_cursor.execute(query)
        data_list = [i for i in self.my_cursor]
        if data_list:
            return data_list
        else:
            raise DataNotFound("table  is not present in the database")

    def show_user_data(self, user_id):
        """
        desc: displaying the user_detail
        param: user_id
        return: data_list or error
        """
        query = "select * from user where user_id = %d" % user_id
        self.my_cursor.execute(query)
        data_list = [i for i in self.my_cursor]
        if data_list:
            return data_list
        else:
            raise DataNotFound("this id is not present in the database")

    def get_user_id(self, user_email):
        """
        desc: displaying the user_detail
        param: user_email
        return: data_list or error
        """
        query = "select user_id from user where user_email = '%s'" % user_email
        self.my_cursor.execute(query)
        user_id = [i for i in self.my_cursor]
        if user_id:
            return user_id[0]["user_id"]
        else:
            raise DataNotFound("this email id  is not present in the database")

    def add_user_db(self, user_name, user_password, user_email, mobile):
        """
        desc: adding user details in  the user table
        param : user_id, user_name, user_password, user_email, mobile, is_verified
        return: message string
        """
        query = "insert into user (user_name, user_password, user_email, mobile) values" \
                " ('%s', '%s', '%s', %d)" % (
                     user_name, user_password, user_email, mobile )
        self.my_cursor.execute(query)
        self.connection.commit()
        user_id = self.get_user_id(user_email)
        return user_id

    def verify_user(self, user_id):
        """
        desc: verify user details from the database
        param: user_id
        """
        query = "update user set is_verified = true where user_id = %d" % user_id
        self.my_cursor.execute(query)
        self.connection.commit()

    def update_user(self, user_id, user_name, user_password, user_email, mobile):
        """
        desc: updating user name , password , email and mobile in  the employee_details table
        param: salary, employee_name
        return: updated data or error
        """
        query = "update user set user_name = '%s', user_password='%s', user_email='%s', mobile = %d where user_id = %d"\
                % (user_name, user_password, user_email, mobile,user_id)
        self.my_cursor.execute(query)
        self.connection.commit()
        updated_data = self.show_user_data(user_id)
        return updated_data

    def delete_user(self, user_id):
        """
        desc: deleting user details from the database
        param: user_id
        """
        self.show_user_data(user_id)
        query = "delete from user where user_id = %d" % user_id
        self.my_cursor.execute(query)
        self.connection.commit()

    def login_into_book_store(self, email_id, password):
        """
            desc: query to get a user detail from database
            param: user id
            return: employee detail in dictionary format
        """
        query = f"SELECT * FROM user WHERE user_email = '{email_id}' and user_password = '{password}'"
        self.my_cursor.execute(query)
        user = [i for i in self.my_cursor]
        if user:
            return user
        else:
            raise Exception("Credentials Are incorrect, Please Try again!")

    def show_all_books(self):
        """
        desc: displaying the book details
        return: data_list containing all books details
        """

        query = "select * from books "
        self.my_cursor.execute(query)
        data_list = [i for i in self.my_cursor]
        print(data_list)
        if data_list:
            return data_list
        else:
            raise DataNotFound("table is not present in the database")

    def show_book_data(self, book_id):
        """
        desc: displaying the book_detail
        param: book_id
        return: data_list or error
        """
        query = "select * from books where id = %d" % book_id
        self.my_cursor.execute(query)
        data_list = [i for i in self.my_cursor]
        if data_list:
            return data_list
        else:
            raise DataNotFound("this book id is not present in the database")

    def add_book_to_db(self, id, author, title, image, quantity, price, description):
        """
        desc: adding book details in  the user table
        param : id, author, title, image, quantity, price, description
        return: result
        """
        query = "insert into books (id, author, title, image, quantity, price, description) values" \
                " (%d, '%s', '%s', '%s', %d ,%f,'%s')" % (id, author, title, image, quantity, price, description)
        self.my_cursor.execute(query)
        self.connection.commit()
        result = self.show_book_data(id)
        return result

    def update_book(self,book_id,  id, author, title, image, quantity, price, description):
        """
        desc: updating  id, author, title, image, quantity, price, description in  the books table
        param:  id, author, title, image, quantity, price, description
        return: updated data or error
        """
        query = "update books set id = %d, author = '%s', title='%s', image='%s',quantity=%d, price = %f, " \
                "description = '%s' where id = %d" \
                % (id, author, title, image, quantity, price, description, book_id)
        self.my_cursor.execute(query)
        self.connection.commit()
        updated_data = self.show_book_data(id)
        return updated_data

    def delete_book(self, book_id):
        """
        desc: deleting book details from the database
        param: book_id
        """
        self.show_user_data(book_id)
        query = "delete from books where id = %d" % book_id
        self.my_cursor.execute(query)
        self.connection.commit()

# a = Functionality()
# a.show_all_books()