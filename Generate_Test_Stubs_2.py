class PasswordManagement:
    # Part A:
    # When a user enters login for a new website, the system will create a new file for the new account
    def create_new_login(self):
        return None
    # 1.1 when a user enter the password and username, system will detect them and store in some way
    def get_pswd_username(self):
        return
    # 1.1 system encrypt the new pswd detected
    def encrypt_pswd(self):
        return None
    # 1.1 system store the new pswd securely
    def save_pswd(self):
        return None
    # 1.2 system store the new system without encryption
    def save_username(self):
        return None
    # 1.2 system double checks the stored username is without encryption
    def check_plain_username(self):
        return None

    # Part B
    # 2.1 when user visited a website, system automatically check the visit history
    def check_websit_visited(self):
        return None
    # 2.1 if current website found in the history, system automatically retrieve the save login information
    def retrieve_existing_login(self):
        return None
    # 2.2 when a user click the login form, system automatically check if current curser is in the login field
    def check_login_form(self):
        return None
    # 2.2 when current curser is login field, system will decrypt the corresponding pswd saved before
    def decrypt_pswd(self):
        return None

    # PART C
    # 3 when curser is in the login field, system compare the current user information with the
    # author information of the saved pswd to determine the legit access
    def check_saved_user(self):
        return None
    # 3 when current user information matches the author information of the retrieved login, grant auto
    # login access to the current user to continue the auto login process
    def grant_user_access(self):
        return None

    # PART D
    # 4.1 when user is granted the access and auto login is triggered, system pop up the choice boxing of
    # confirm or deny auto login access
    def pop_choice_box(self):
        return None
    # 4.1 when user select the choice from the popup box, system will save the choice.
    def user_choice(self):
        return None
    # 4.1.2 If user choose to deny access from popup box, system will stop the auto login process
    def deny_access(self):
        return None
    # 4.1.2 when access is denied, system stop any further action in this case and back to standing by status
    def bypass_deny(self):
        return None
    # 4.1.3 when user choose to accept access from the popup box, system complete the auto login process
    def cofirm_access(self):
        return None
    # 4.1.3 when system complete the auto login process successfully, system auto save the latest login info
    # for specific website. Username is saved without encryption and pswd is saved with encryption.
    def save_current_login(self):
        return None

