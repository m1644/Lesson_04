import yaml
from ssh_checkers import ssh_checkout, upload_files


with open('config.yaml') as f:
    data = yaml.safe_load(f)


class TestPositive:
    def test_step1(self):
        res = []
        upload_files(data.get("ip"), data.get("user"), data.get("passwd"), data.get("local_path"), data.get("remote_path"))
        res.append(ssh_checkout(data.get("ip"), data.get("user"), data.get("passwd"),
                                f"echo '11' | sudo -S dpkg -i {data.get('remote_path')}", "Настраивается пакет"))
        res.append(ssh_checkout(data.get("ip"), data.get("user"), data.get("passwd"),
                                "echo '11' | sudo -S dpkg -s p7zip-full", "Status: install ok installed"))
        assert all(res), "test1 FAIL"
