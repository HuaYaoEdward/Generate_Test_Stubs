import unittest


class MyTestCase(unittest.TestCase):
    #def test_something(self):
    #    self.assertEqual(True, False)  # add assertion here

    # Part A:
    # When a user enters login for a new website, the system will create a new file for the new account
    def test_create_new_login(self,website):
        website = Website()
        assert len(website.login) == 0, "the website login info initially is empty"
        return None

    # 1.1 when a user enter the password and username, system will detect them and store in some way
    def test_save_pswd(self,website,pswd):
        website = Website()
        website.save_pswd(pswd)
        assert website.pswd == pswd, "entered pswd is stored in object website correctly"
        return None

    # 1.1 system encrypt the new pswd detected
    def test_encrypt_pswd(self, website, pswd):
        website = Website()
        website.encrypt_pswd(pswd)
        assert website.pswd_encrypted != pswd, "entered pswd is encrypted in some way and not same as original pswd"
        return None

        # 1.2 system double-checks the stored username is without encryption
    def test_save_username(self,website,username):
        website = Website()
        website.save_username(username)
        assert website.username == username, "entered username is stored in object website correctly without encryption"
        return None




    # Part B
    # 2.1 when user visited a website, system automatically check the visit history
    # 2.1 if current website found in the history, system automatically retrieve the save login information
    def test_retrieve_login_username(self, website):
        website = Visited_website()
        website.retrieve_login_username()
        assert website.retreived_username == website.username, "visiting a website visited before generates retrieved " \
                                                               "username same as the username stored before"
        return None

    def test_retrieve_login_pswd(self, website):
        website = Visited_website()
        website.retrieve_login_pswd()
        assert website.retreived_pswd == website.pswd_encrypted, "visiting a website visited before generate retrieved " \
                                                                 "pswd same as the pswd stored before"
        return None
    # 2.2 when a user click the login form, system automatically check if current curser is in the login field
    def test_check_login_form(self,curser,login_form):
        curser = Curser(login_form)
        curser.check_login_form()
        assert curser.login_form == 1, "when login form object is passed in, curser object recognizes it"
        return None
    # 2.2 when current curser is login field, system will decrypt the corresponding pswd saved before
    def test_decrypt_pswd(self,website, curser):
        website = Visited_website()
        website.decrypt_pswd(curser)  # curser.login_form = 1
        assert website.pswd_decrpyted == website.pswd,"when curser is in login form, stored encrpyted password got " \
                                                      "decrypted same as the original password"
        return None

    def insert_login_username(self, website):
        website = Visited_website()
        website.insert_login_username()
        assert website.login_form.username !=0, "when curser is in login form, stored username is inserted."
    def insert_login_password(self, website):
        website = Visited_website()
        website.insert_login_pswd()
        assert website.login_form.pswd !=0, "when curser is in login form, stored pswd is inserted."

    # PART C
    # when user logged in, the user only access theinformation to the corresponding login information
    def test_login_to_system(self,username, pswd):
        login = login_to_system(username, pswd)
        assert login.info == login.login_to_system.info,"when user with username log in, login information " \
                                                        "is corresponding pswd only"
        return None

    # PART D
    # 4.1 when user is granted the access and auto login is triggered, system pop up the choice box to make user
    # confirm or deny auto login access
    def test_request_user_consent(self, user_consented):
        consent = Consent()
        assert len(consent)==0, "the consent popup box should start with 2 options"

        choice = user_consented
        consent.request_user_consent(choice)

        assert consent.choice == 1, "when stored login info retrieve is done internally, a request box pop up" \
                                          "and user can consent or deny auto-filled info"
        return None

    def test_retrieve_user_consent(self):
        consent = Consent()
        consent.retrieve_user_consent()
        assert consent.choice !=0,"when user make a choice in the consent popup box, choice is stored in the system"


if __name__ == '__main__':
    unittest.main()
