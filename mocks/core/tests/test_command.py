from django.test import TestCase
from unittest.mock import call, patch 
from mocks.core.models import Congressperson
'''
from mocks.core.management.commands import Command


class TestCommand(TestCase):

	@patch('mocks.core.management.commands.congresspeople.os.path.exists')
	@patch('mocks.core.management.commands.congresspeople.open')
	@patch('mocks.core.management.commands.congresspeople.print')
	@patch('mocks.core.management.commands.congresspeople.DictReader')
	@patch(Congressperson.objects, 'create')
	def test_existing_file(self, create, reader, print, open, exists):
		exists.return_value = True
		open = StringIO()
		reader =({1: 'ahoy'})
		command = Command()
		command.handle(source='data.csv')
		self.assertEquals(3, command.count)
		print.assert_has_calls((
			call('Reading dataset...'),
			call('1 congresspeople imported...'),
			call('2 congresspeople imported...'),
			call('3 congresspeople imported...'),
			call(),
			call('Done!')
			))
		self.assertEqual(3, len(create))


	@patch('mocks.core.management.commands.congresspeople.os.path.exists')
	def test_non_existing_files(self, exists):
		exists.return_value = False
		with self.assertRaises(FileNotFoundError):
			Command().handle(source='data.csv')
'''