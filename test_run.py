import unittest
from utilities import *
import requests


class PistonSecurityTests(unittest.TestCase):

    #
    def test_outgoing_network_connections(self):
        setup_data_copy("test_code/network.py")
        response = requests.post(PISTON_URL, json=data, headers=HEADERS)
        json = response.json()
        self.assertEqual("SIGKILL", json["run"]["signal"])

    def test_max_processes(self):
        pass

    def test_max_files(self):
        setup_data_copy("test_code/files.py")
        response = requests.post(PISTON_URL, json=data, headers=HEADERS)
        json = response.json()
        self.assertEqual("SIGKILL", json["run"]["signal"])

    # Code should timeout after 3 seconds (unless maximum execution time is modified)
    def test_code_execution_timeout(self):
        setup_data_copy("test_code/timeout.py")
        response = requests.post(PISTON_URL + "/api/v2/execute", json=data, headers=HEADERS)
        json = response.json()
        self.assertEqual("SIGKILL", json["run"]["signal"])

    # stdout should be capped at 65536
    def test_max_stdout_size(self):
        setup_data_copy("test_code/stdout.py")
        response = requests.post(PISTON_URL + "/api/v2/execute", json=data, headers=HEADERS)
        json = response.json()
        self.assertEqual("SIGKILL", json["run"]["signal"])
