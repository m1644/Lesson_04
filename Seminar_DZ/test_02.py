from ssh_checkers import ssh_checkout_negative, ssh_checkout
import yaml


''' Задание 2
Условие:
Переделать все шаги негативных тестов на выполнение по SSH. 
Проверить работу.
'''

with open('config.yaml') as f:
    data = yaml.safe_load(f)


class Testneg:
    def test_nstep1(self, make_folders, make_bad_arx):
        # test neg 1
        assert ssh_checkout_negative(data["ip"], data["user"], data["passwd"], 
                                     "cd {}; 7z e {}.{} -o{} -y".format(data["folder_out"], 
                                                                        make_bad_arx, data["type"], 
                                                                        data["folder_ext"]), "ERROR:"), "test1 FAIL"


    def test_nstep2(self, make_bad_arx):
        # test neg 2
        assert ssh_checkout_negative(data["ip"], data["user"], data["passwd"], 
                                     "cd {}; 7z t {}.{}".format(data["folder_out"], make_bad_arx, data["type"]), 
                                     "ERROR:"), "test2 FAIL"


    def test_nstep3(self):
        res = []
        res.append(ssh_checkout(data["ip"], data["user"], data["passwd"], 
                                "echo '{}' | sudo -S dpkg -r" " {}".format(data["passwd"], data["pkgname"]),
                                "Удаляется"))
        res.append(ssh_checkout(data["ip"], data["user"], data["passwd"], 
                                "echo '{}' | " "sudo -S dpkg -s {}".format(data["passwd"], data["pkgname"]), 
                                "Status: deinstall ok"))
        assert all(res), "test3 FAIL"


# Запуск из консоли: pytest -v test_02.py
