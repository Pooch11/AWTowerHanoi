import unittest
from TowerGame import Disk, Peg, TowerGame
import requests
class TowersAPITestCase(unittest.TestCase):
    def test_newgameAPI(self):
        r = requests.get('http://127.0.0.1:5000/newgame')
        self.assertEqual(r.text, "Started a new game!")

    def test_startAPI(self):
        r = requests.get('http://127.0.0.1:5000/?new')
        self.assertEqual(r.text, "Started a new game!")

    def test_inspectPegAPI(self):
        r = requests.get('http://127.0.0.1:5000/?new')
        r = requests.get('http://127.0.0.1:5000/pegstatus?peg=1')
        contents_1 = {'Peg': {'Disks': {0: {'Disk': {'size': 0}}, 1: {'Disk': {'size': 1}}, 2: {'Disk': {'size': 2}}, 3: {'Disk': {'size': 3}}}, 'Position': 1}}
        self.assertEqual(r.text, str(contents_1))

    def test_inspectGameAPI(self):
        r = requests.get('http://127.0.0.1:5000/?new')
        r = requests.get('http://127.0.0.1:5000/gamestatus')
        self.assertEqual(r.status_code, 200)

    def _test_movePegAPI(self, fromPeg, toPeg):
        r = requests.get('http://127.0.0.1:5000/movepeg?from={0}&to={1}'.format(fromPeg, toPeg))
        print(r.text)

    def test_gamewinAPI(self):
        requests.get('http://127.0.0.1:5000/?new')
        self._test_movePegAPI(1,2)
        self._test_movePegAPI(1,3)
        self._test_movePegAPI(2,3)
        self._test_movePegAPI(1,2)
        self._test_movePegAPI(3,1)
        self._test_movePegAPI(3,2)
        self._test_movePegAPI(1,2)
        self._test_movePegAPI(1,3)
        self._test_movePegAPI(2,1)
        self._test_movePegAPI(2,3)
        self._test_movePegAPI(1,3)
        self._test_movePegAPI(2,1)
        self._test_movePegAPI(3,2)
        self._test_movePegAPI(3,1)
        self._test_movePegAPI(2,3)
        self._test_movePegAPI(1,2)
        self._test_movePegAPI(3,2)
        self._test_movePegAPI(1,3)
        self._test_movePegAPI(2,1)
        self._test_movePegAPI(2,3)
        self._test_movePegAPI(1,3)
        r = requests.get('http://127.0.0.1:5000/gamewin')
        self.assertEqual(r.text, "Game Complete!")

    if __name__ == '__main__':
        unittest.main()